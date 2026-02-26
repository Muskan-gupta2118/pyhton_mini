'''OUR QUESTION IS :
we all have played snake, water, and gun game in our childhoood .If you haven't ,google the rule of this game and write a python 
program capabale of playing this game with the user  '''
import random
'''
1 for snake
-1 for water
0 for gun
'''
n=0
youstr={"s":1,"w":-1,"g":0}
youDict={1:"snake",-1:"water",0:"gun"}
computer = random.choice([1,-1,0])
print(f"you choose :{n}  and computer choose:{computer}")
if (computer==n):
    print("match draw")
else:
        if(n==1 and computer==-1):
              print("you win")
        elif(computer==-1 and n==0):
              print("you lost")
        elif(computer==1 and n==-1):
              print("you lost")
        elif(computer==1 and n==0):
              print("you win")
        elif(computer==0 and n==1):
              print("you lost")
        elif(computer==0 and n==-1):
              print("you win")
        else:
              print("somthing went wrong")                  
