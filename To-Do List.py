tasks=[]

while True:
    print("Welcome to To-Do List!!!")
    print("Menu:")
    print("1. Add a Task")
    print("2. View Task")
    print("3. Delete a Task")
    print("4. Exit")

    ch=int(input("Enter Number from 1-4 for the Menu"))

    if ch==1:
        task1=input("Enter the Task")
        tasks.append(task1)
        print("Task Added Successfully")

    elif ch==2:
        if len(tasks)==0:
            print("No Tasks to Display")
        else:
            print("Your Tasks")
            for i in range(len(tasks)):
                print(i+1,tasks[i])
    
    elif ch==3:
        if len(tasks)==0:
            print("No Tasks to Delete")
        else:
            print("Tasks:")
            for i in range(len(tasks)):
                print(i+1,tasks[i])
            num=input("Enter Task Number to Delete").strip()

            if num.isdigit():
                num=int(num)
                if 1<= num <= len(tasks):
                    rt=tasks.pop(num-1)
                    print("Deleted Task:", rt)
                else:
                    print("Invalid Task Number Entered...")
            else:
                print("Enter a Number")

    elif ch==4:
        break