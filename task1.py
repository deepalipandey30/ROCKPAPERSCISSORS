
import random 
import os

print("THE RULES FOR THE TASK ARE AS FOLLOWS: \n"+"User has to choose any one options from the available three options and Based on the winning rules this app decides who will win\n"
                                +"ROCK VERSES PAPER----> PAPER WINS \n"
                                + "ROCK VERSES SCISSORS---->ROCK WINS \n"
                                +"PAPER VERSES SCISSORS----->SCISSORS WINS\n") 


while True: 
    
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n") 
      
    ch = int(input("ENTER YOUR MOVE:  ")) 
  
    while ch> 3 or ch< 1: 
        ch = int(input("PLEASE ENTER VALID INPUT: ")) 
          
  
    if ch == 1: 
        ch_name = 'Rock'
    elif ch == 2: 
        ch_name = 'paper'
    else: 
        ch_name = 'scissor'
          
    
    print("user choice is: " + ch_name) 
    print("\nNow its computer turn.......") 
  
    comp_choice = random.randint(1, 3) 
      
    
    while comp_choice == ch: 
        comp_choice = random.randint(1, 3) 
  
   

    if comp_choice == 1: 
        comp_choice_name = 'Rock'
    elif comp_choice == 2: 
        comp_choice_name = 'paper'
    else: 
        comp_choice_name = 'scissor'
          
    print("COMPUTER CHOICE IS: " + comp_choice_name) 
  
    print(ch_name + " V/s " + comp_choice_name) 
  
    
    if((ch == 1 and comp_choice == 2) or
      (ch == 2 and comp_choice ==1 )): 
        print("paper wins => ", end = "") 
        result = "paper"
          
    elif((ch== 1 and comp_choice == 3) or
        (ch == 3 and comp_choice == 1)): 
        print("Rock wins =>", end = "") 
        result = "Rock"
    else: 
        print("scissor wins =>", end = "") 
        result = "scissor"
  
   
    if result == ch_name: 
        print("OPPONENT CHOICE  "+ch_name+"<== User wins ==>") 
    else: 
        print("COMPUTER CHOICE "+ch_name+"<== Computer wins ==>") 
          
    print("DO YOU WANT TO CONTINUE? (Y/N)") 
    ans = input() 
  
  
    
    if ans == 'n' or ans == 'N': 
        break
    clear = lambda: os.system('cls')
    clear()
      

print("\nThanks for playing") 
