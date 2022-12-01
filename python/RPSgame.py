import random
u_input= input("enter your choice:")
p_actions= ["rock","paper","scissors"]
c_actions= random.choice(p_actions)

if u_input==c_actions :
    print("computer choice:"+c_actions)
    print("ooops It's a tie")
elif u_input== "rock" and c_actions== p_actions[2] or u_input=="paper" and c_actions==p_actions[0] or u_input== "scissors" and c_actions==p_actions[1]:
    print(c_actions)
    print("congrats you won!")
elif u_input== "rock" and c_actions== p_actions[1] or u_input=="paper" and c_actions==p_actions[2] or u_input== "scissors" and c_actions==p_actions[0]:
    print(c_actions)
    print("better luck next time ")
else :
    print("Invalid choice")    