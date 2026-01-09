def get_valid_username():
    while True:
        has_letter =0
        has_digit=0
        has_special=0
        name= input("Enter the username: ").lower().strip()
        for i in name:
            if i.isalpha():
                has_letter+=1
            elif i.isdigit():
                has_digit+=1
            else:
                has_special+=1

        if 5<= len(name) <=12 and has_letter>=1 and has_digit>=1 and has_special==0:
            print("Username accepted")
            return name
        else:
            print("Invalid input")


def get_valid_password():
    while True:
        has_letter=0
        has_digit=0
        has_special=0
        password=input("Enter password: ").strip()
        for p in password:
            if p.isalpha():
                has_letter+=1
            elif p.isdigit():
                has_digit+=1
            else:
                has_special+=1
        
        if len(password)>=8 and has_letter>=1 and has_digit>=1 and has_special>=1:
            print("Password accepted")                                      
            return password
        else:
            print("Invalid input. Try again")


def get_valid_age():
    while True:
        age=input("Enter age: ")

        if not age.isdigit():
            print("Invalid input. Enter a number")
            continue 
        
        if age.isdigit():
            age=int(age)
            if 1<=(age) <=120:
                print("Age accepted")
                return age
            else:
                print("Invalid input. Enter the number between 1-120")

username= get_valid_username()
password= get_valid_password()
age= get_valid_age()

            






        
            
