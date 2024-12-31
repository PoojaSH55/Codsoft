tasks=[]
while True:
  print("\nSimple to-do list")
  print("1. Add Task")
  print("2. Show tasks ")
  print("3. Exit ")

  choice=input("Enter your Choice")
  if choice == '1':
     task=input("Enter your task ")
     tasks.append(task)
     print("Task added Successfully ")
  elif choice == '2':
     print("Your tasks:\n")
     for task in tasks:
        print(f"-{task}")
  elif choice == '3':
     print("Exiting the Program..Byee!")
     exit()
  else:
    print("Invalid Choice")
