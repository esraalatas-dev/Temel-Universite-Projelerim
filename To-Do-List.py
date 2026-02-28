to_do_list=[]
def add_task(to_do_list):
    task=input("enter the one task:")
    to_do_list.append(task)
    print("add task successfully.")

def show_task(to_do_list):
    print("to do task list:")
    for task in to_do_list:
        print("-"+task)


def delete_task(to_do_list):
    task=input("enter the task to be deleted:")
    if task in to_do_list:
        to_do_list.remove(task)
        print("delete task successfully.")
    else:
        print("task not found..")

while True:
    print("\n *** MY TO DO LİST APP ***")

    print(" select the action you want to do:\t1.enter task\t"
          "2.show task\t"
          "3.delete task\t"
          "4.exit\n")
    choise=input("enter the choise:")

    if choise=="1":
     add_task(to_do_list)
    elif choise=="2":
     show_task(to_do_list)

    elif choise=="3":
     delete_task(to_do_list)

    elif choise=="4":
        print("exiting the application...")
        break

    else:
     print("invalid operating!!.please try again.")








