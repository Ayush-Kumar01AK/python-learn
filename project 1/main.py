'''
1 for snake
-1 for water
0 for gun
'''
import random
for i in range(10):
    print(f"\n----- Round {i+1} -----")

    you = input("Entre your choice(s,w,g): ")
    t = {"s":"snake","w":"water","g":"gun"}

    if you not in t:
        print("entre valid input")
        continue
    
    print("your choice:",t[you])
    
    youdict = {"s":1,"w":-1,"g":0}
    younum = youdict[you]
    
    value = [1, -1, 0]
    computer = random.choice(value)
    
    choice = {1: "Snake", -1: "Water", 0: "Gun"}
    
    print("Computer choice:", choice[computer])

    if(computer == 1 and younum == 1 or computer == -1 and younum == -1 or computer == 0 and younum == 0):
        print("Draw")
    elif(computer==1 and younum==-1):
        print("computer win") 
    elif(computer==1 and younum==0):
        print("you win") 
    elif(computer==-1 and younum==1):
        print("you win") 
    elif(computer==-1 and younum==0):
        print("computer win") 
    elif(computer==0 and younum==1):
        print("computer win") 
    elif(computer==0 and younum==-1):
        print("you win") 
    else:
        print("please entre valid input") 