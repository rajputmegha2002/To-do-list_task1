from tkinter import *
import tkinter .messagebox

root=Tk()
root.geometry("400x300")
root.title("To-do-List")

def add_tasks():
    task=write_task.get()
    taskbox_list.insert(END,task)
    write_task.delete(0, END)

def delete_task():
    try:
        task__del=taskbox_list.curselection()[0]
        taskbox_list.delete(task__del)
    except:
        tkinter.messagebox.showwarning(title="Warning", message="You must select a task")


def submit_task():
    task= []

    for index in taskbox_list.curselection():
        task.insert(index,taskbox_list.get(index))    
    
    print(" You have saved your task")
    for index in task:
        print(index)
   

l1=tkinter.Label(root,text="To-Do-List ",width=100,pady=5,padx=5,bg="green", fg="black",font="Arial 10 bold")
l1.pack()

write_task=Entry(root, width=50)
write_task.pack(padx=5,pady=5)

button=tkinter.Button(root,text="Add Task", fg="black", bg="orange",command=add_tasks,width=40 )
button.pack()
button=tkinter.Button(root,text="Delete Task", fg="black", bg="orange",command=delete_task,width=40 )
button.pack()
button=tkinter.Button(root,text="submit Task", fg="black", bg="orange",command=submit_task,width=40 )
button.pack()

taskbox_list=Listbox(root,height=50,width=50)
taskbox_list.pack(padx=5,pady=5)
















root.mainloop()