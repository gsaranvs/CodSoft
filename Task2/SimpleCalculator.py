def numinput():
    print("Welcome to Simple Calculator")
    a=int(input("Enter the 1st Number"))
    b=int(input("Enter the 2nd Number"))
    return a,b

def calc(a,b):
    while True:
        print("Menu:")
        print("1. Addition")
        print("2. Subraction")
        print("3. Multiply")
        print("4. Division")
        print("5. Exit")

        ch=int(input("Enter the Number from 1-5 to Access the Menu"))

        if ch==1:
            add=a+b
            print(add)
        
        elif ch==2:
            sub=a-b
            print(sub)

        elif ch==3:
            mul=a*b
            print(mul)

        elif ch==4:
            div=a//b
            print(div)

        elif ch==5:
            break

a,b=numinput()
calc(a,b)