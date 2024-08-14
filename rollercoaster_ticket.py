print("welcome to the rollercoaster!")
height=int(input("enter your height in cm!"))
bill=0
if height>=120:
    print("yes you can ride the rollercoaster.")
age=int(input("enter your age."))
if age>=18:
        bill=12
        print("adult ticket is $12.")
elif age<12:
        bill=5
        print("Child ticket is $5.")
else:
        bill=7
        print("Teenager ticket is $7.")
photo=input("Do you want photos?")
if photo=="yes":
        bill+= 3
        print(f'You have to pay ${bill}')
else:
    print("No, you cannot ride the rollercoaster.")