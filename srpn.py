#This is your SRPN file. Make your changes here.

#Create stack data structure as basis for RPN Calculator
stack = []  
#Create global variables and lists to be used for different functions
answer = 0
comment_counter = 0
r_counter = 0
r = 1804289383
rlist = [1804289383, 846930886, 1681692777, 1714636915, 1957747793, 424238335, 719885386, 1649760492, 596516649,1189641421, 1025202362, 1350490027, 783368690, 1102520059, 2044897763, 1967513926, 1365180540, 1540383426, 304089172, 1303455736, 35005211, 521595368, 1804289383]

#Checks the length of the stack before appending the number, stack overflow if its too long to add

def add_to_stack(num):
  if len(stack) > 22:
    print("Stack overflow.")
  else:
    stack.append(num)

#Uses temp variable to check saturation before adding the correct number to stack

def add_answer(temp):
  global answer
  if temp > 2147483647:     
        add_to_stack(2147483647)
        answer = 2147483647
  elif temp < -2147483648:       
        add_to_stack(-2147483648)
        answer = -2147483648
  else: 
        add_to_stack(int(temp))
        answer = int(temp)

#Main Function        

def process_command(command_in):

#To ensure we're referencing global variables in this function
   
    global answer  
    global comment_counter 
    global r_counter
    global r
    
    temp = 0         

# Splits multiple input on same line to a list, to be run through function sequentially

    commandlist = command_in.split() 

#Iterates through the command list one at a time

    for command in commandlist: 

      try:
#If the single command only contains integers, simple case of adding to stack
        int(command)
        if int(command) > 2147483647:
          add_to_stack(2147483647)
        elif int(command) < -2147483648:
          add_to_stack(-2147483648)
        else:
          add_to_stack(int(command))     
      except:
#If command contains at least 1 non integer, check functionality of non integers
        new_var = ""
#If you start a comment (odd hash so has remainder), pass. If end comment (even has so no remainder), perform check of other operations after the hash - Therefore ignores everthing between hash
        if command =='#':
          comment_counter += 1
          
        if comment_counter % 2 == 0:  
#Checks non integer items one character at a time. If a number, concatenates in to new_var. If we encounter any other character, we add new_var to stack and clear new_var, and check functioanlity of the character we encountered.        
          for character in command:
            if character.isdigit():
              new_var += character
            else:
              if len(new_var) > 0:
                add_to_stack(int(new_var))
                new_var = ""
#Checking all characters with standard functionality. In general, operators will pop numbers from stack and perform the operation on them, before adding the result back to stack
              if character == '=':
                if len(stack) == 0:
                  print ("Stack empty.")
                else:
                  return answer
              elif character == 'd':
                if len(stack) == 0:
                  print (-2147483648)
                else:
                  for item in stack: 
                    print(item)
              elif character == '+':
                if len(stack) == 0 or len(stack) == 1:
                  print ("Stack underflow.")
                else:
                  num2 = stack.pop()
                  num1 = stack.pop()
                  temp = num1 + num2
                  add_answer(temp)
              elif character == '-':
                if len(stack) == 0 or len(stack) == 1:
                  print ("Stack underflow.")
                else:
                  num2 = stack.pop()
                  num1 = stack.pop()
                  temp = num1 - num2
                  add_answer(temp)
              elif character == '*':
                if len(stack) == 0 or len(stack) == 1:
                  print ("Stack underflow.")
                else:
                  num2 = stack.pop()
                  num1 = stack.pop()
                  temp = num1 * num2
                  add_answer(temp)
              elif character == '/':
                if len(stack) == 0 or len(stack) == 1:
                  print ("Stack underflow.")
                else:
                  num2 = stack.pop()
                  num1 = stack.pop()
                  if num2 == 0:
                    print ("Divide by 0.")
                  else:
                    temp = num1 / num2
                    add_answer(int(temp))
              elif character == '%':
                if len(stack) == 0 or len(stack) == 1:
                  print ("Stack underflow.")
                else:
                  num2 = stack.pop()
                  num1 = stack.pop()
                  temp = num1 % num2
                  add_answer(temp)
              elif character == '^':
                if len(stack) == 0 or len(stack) == 1:
                  print ("Stack underflow.")
                else:
                  num2 = stack.pop()
                  num1 = stack.pop()
                  if num2 < 0:
                    print("Negative power.")
                    add_to_stack(num1)
                    add_to_stack(num2)
                  else:
                    temp = num1 ** num2
                    add_answer(temp)
              elif character == '£':     # £ adds two 0's instead of standard one 0 
                add_to_stack(0)
                add_to_stack(0)
              elif character == '#':
                break
              elif character == 'r':
                add_to_stack(r)
                r_counter += 1
                if r_counter == 22:
                 r_counter = 0
                 r = rlist[r_counter]
                else:
                 r = rlist[r_counter]                
              else:
                add_to_stack(0)           #Treat any other characters as single 0's to be added to stack.
          if len(new_var) > 0:
            add_to_stack(int(new_var))


#This is the entry point for the program.
#Do not edit the below


if __name__ == "__main__": 

  while True:
        try:
            cmd = input()
            pc = process_command(cmd)
            if pc != None:
                print(str(pc))
        except:
            exit()
