print("are you Hungry")
answer = str(input("enter your answer"))
if answer == 'yes':
    print("eat something")
    print("what do you want to eat?")
    an = str(input("enter your answer"))
    if an == "Pizza":
        print("eat Pizza")
elif answer == "i am tired":
    print("then go to sleep")
elif answer == "i am hungry and also tired":
    print("Eat something and then sleep")
elif answer == "no":
    print("Are you thirsty?")
    ans = str(input("enter your answer"))
    if ans == "yes":
        print("Drink some water")

else:
    print("do something")
