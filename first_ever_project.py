import time
print ("Hello! Welcome to my first script! its a survey like thing, so enjoy!") 
time.sleep(2.5)
name = input("enter your name: ")
print("Hello " + name)
time.sleep(2)
food = input("what do you like to eat?: ")
time.sleep(1)
print(f"You like {food}?")
time.sleep(1)
print("i like cheeseburgers, they are a masterpiece")
time.sleep(2)
arch = input ("Do you know what Linux is? ").lower()
if arch == ('no'): 
    print("Linux is a operating system, with mutiple distrobutions. People say it's hard, but really it is not")
if arch == ('yes'): 
    print("cool, now i dont have to explain it")
time.sleep(2)
q1 = input("do you use Linux or Windows? ").lower()

if q1.startswith ("w"):

     print("Ok, i wont judge, i used to use windows until i wanted to learn programming, then i switched over to arch linux.")

else:
     print("Did we just become best freinds?!")
time.sleep(2)
likecomputer = input ("Do you like computers? ").lower()

if likecomputer.startswith ("y"):

     print("Cool! i like computers too, that is why i like programming!")

else:
     print("It's alright, i get it, you only use a computer to use the internet and play games, and that is just fine :)")
time.sleep(2)
print("Thanks for doing my survey! This is my first thing of code, so pardon me if it is sloppy lol.")
time.sleep(5)