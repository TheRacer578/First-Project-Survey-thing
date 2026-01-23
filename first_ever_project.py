import time
import webbrowser
print ("Hello! Welcome to my first script! its a survey like thing, so enjoy!") 
time.sleep(2.5)
name = input("enter your name: ")
print(f"Hello {name}!")
time.sleep(2)
food = input("what do you like to eat?: ")
time.sleep(1)
print(f"You like {food}?")
time.sleep(1)
print("i like cheeseburgers, they are a masterpiece")
time.sleep(2)
likecomputer = input ("Do you like computers? ").lower()

if likecomputer.startswith ("y"):

     print("Cool! i like computers too, that's why i like programming!")

else:
     print("its alright, you dont have to.")
time.sleep(2)
q1 = input("do you use Linux or Windows? ").lower()

if q1.startswith ("w"):

     print("Ok, i wont judge, i used to use windows until i wanted to learn programming, then i switched over to arch linux.")

if q1.startswith ("m"):

     print("Really, MAC, are you stupid?? windows is better then that bro. stop paying apple $9999999 for a macbook pro, you stupid schmoe get a life, buy a ibm thinkpad or something.")

if q1.startswith("l"):
     print("Did we just become best freinds?!")
time.sleep(2)
drink = input ("What is your favorite drink? ")
print(f"You like {drink}?")
time.sleep(1)
print("Cool! if i had to pick i would pick Pepsi, or Mr. Pibb.")
time.sleep(2)
print("Thanks for doing my survey! This is my first thing of code, so pardon me if it is sloppy lol.")
time.sleep(3)
print("Check out my github (place where the file is saved)")
wanna = input ("Would you like to go to the GitHub page? (yes or no)")

if wanna.startswith ("y"):

     webbrowser.open('https://github.com/TheRacer578/First-Project-Survey-thing')

else:
     print("Okay, Catch you on the flip side!")

time.sleep(5)

