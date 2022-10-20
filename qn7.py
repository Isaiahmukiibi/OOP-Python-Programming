birth_year= 2002
default ="Jerom"
def my_function():
    name = input("enter your name: ") #prompting the user to enter name.
    if not name:
        print(default) # the default name(Jerom) is printed incase the user has not provided one.
    Age = 2022-birth_year #Assuming that all people  were born in 2002(current_year - birth_year = Age).
    weight = float(input("enter your weight: "))#prompting the user to enter weight.
    
    #The function  prints out a summary of all the data entered by the user.
    print("Your name is:",name or default)
    print("Your age is:", Age)
    print("Your weight is:",weight)
my_function()
