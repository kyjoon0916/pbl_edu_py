#this is a guess the number game.
import random
print("hello! What is your name?")
myName=input()
count =0
number = random.randrange(1,20)
print("Well", myName + ", i am thinking of a number between 1 and 20")
print("take a guess")


while True:
                    
       guess = int(input())
       count +=1
       if guess < number:
              print("your gess is wrong, is too low! try:%d"%count)
       if guess > number:       
              print("your gess is wrong, is too high! try:%d"%count)
       if guess == number:
              print("Good job " + myName + "! you guessed my number! try:%d"%count)
              break
       
            
             

