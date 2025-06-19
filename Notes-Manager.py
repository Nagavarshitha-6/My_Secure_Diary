import os
from datetime import datetime
attempts=3
password="varshitha-6"
while(attempts>0):
    print("\n======== welcome to My-Secure-dairy ===========\n")
    entered_password=input("Enter the password : ").lower()
    if(entered_password == password):
        print("Access Granted!")
        while(True):
            print("\n======== Menu ===========\n")
            print("1.Create ")
            print("2.View ")
            print("3.Search ")
            print("4.clear")
            print("5.Delete")
            print("6.Backup")
            print("7.View Backup Notes")
            print("8.Exit ")
            choice=input("\nEnter Your Choice : ")
            if choice == "1" :
                date=datetime.now().strftime("[ %Y-%m-%d %I:%M:%p ]")
                note=input("\nEnter a note : ")
                with open("sample.txt","a") as file:
                    file.write(date+"   ->      "+note + "\n")
                print("successfully noted!")
            elif choice == "2":
                if not os.path.exists("sample.txt"):
                    print("No notes found!")
                    continue
                with open("sample.txt","r") as file:
                    content=file.read()
                if content:
                    print("\nThe content of the file is : ")
                    print(content)
                else:
                    print("The file is Empty!")
            elif choice == "3":
                search=input("\nEnter keyword to Search : ")
                with open("sample.txt","r") as file:
                    contentlist=file.readlines()
                found=False
                for line in contentlist:
                   if search.lower() in line.lower():
                       print("Found",line.strip())
                       found=True
                       break
                if not found:
                    print("Element not found!")
            elif choice == "4":
                with open("sample.txt","w") as file:
                    pass
                print("All notes cleared.")
            elif choice == "5":
                if os.path.exists("sample.txt"):
                    os.remove("sample.txt")
                    print("\nNotes Deleted successfully!")
                else:
                    print("file is not available")
            elif choice == "6":
                if os.path.exists("sample.txt"):
                    with open("sample.txt","r") as file:
                        back=file.read()
                    with open("backup.txt","w") as file:
                        file.write(back)
                    print("backup is Successfull!")
                else:
                    print("The File Does not Exist for Back-up")
            elif choice == "7":
                if os.path.exists("backup.txt"):
                    with open("backup.txt","r") as file:
                        backupcontent=file.read()
                    print("The backup file consists of : \n")
                    print(backupcontent)
                else:
                    print("Backup file is Empty!")
            elif choice == "8":
                print("\nThanks for using Notes Manager!\n")
                break
            else:
                print("Invalid Choice, please enter the choice between 1 to 7.")
    else:
        attempts-=1
        if attempts == 0:
            print("\nAccess Denied!")
            break
        else:
            print(f"\nyou have {attempts} more attempts.\n")
            


    
        
        
