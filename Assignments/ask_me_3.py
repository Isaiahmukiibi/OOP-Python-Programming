name = input("What is your name?")
print("Hi",name)
is_Jack = False
is_Jackie = False
if is_Jack or is_Jackie :
    print("Hi",name)
elif  not is_Jack or is_Jackie:
    print("Hello friends!!!")
    print("Good bye")
    age = int (input("How old are you? "))
    if age < 18:
        print("You are below age of working")
    elif age > 18  and age < 25:
        print("You are of age to look for a job")
    elif age >= 25 and  age < 30:
        print("You should be having a job already")
    elif age < 30 and  age < 60:
        print("You should think of having a family")
    elif age < 90 and  age >= 60:
        print("You should retire")
    else:
        print("Goodbye",name , age ,"years old","you are an allien in nature" )
