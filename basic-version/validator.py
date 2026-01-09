while True:
    has_letter=0
    has_digit=0
    has_special=0
    name=input("Enter the username: ").strip().lower()

    for i in name:
        if i.isalpha():
            is_letter+=1
        elif i.isdigit():
            is_digit+=1
        else:
            is_special+=1

    if 5<=len(name)<=12 and is_letter>=1 and is_digit>=1 and is_special==0:
        print("Valid username")
        break
    else:
        print("Invalid input")


while True:
    has_letter=0
    has_digit=0
    has_special=0
    password=input("Enter the password: ").strip()

    for p in password:
        if p.isalpha():
            has_letter+=1
        elif p.isdigit():
            has_digit+=1
        else:
            has_special+=1

    if len(password)>=8 and has_letter>=1  and has_digit>=1  and has_special>=1 :
        print("Password accepted")
        break
    else:
        print("Try again. Enter the correct password")



while True:
    age=input("Enter age: ")

    if not age.isdigit():
        print("Invalid input")
        continue
        
    age=int(age)
    if age>=1 and age<=120:
        print("Age accepted")
        break
    else:
        print("Invalid input")


    

               
    

        

