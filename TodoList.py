from tkinter import *
from tkinter import messagebox

ToDo_list = []
counter = 1
 
def inputError() :
    if enterTaskField.get() == "" :
        messagebox.showerror("Input Error")
        return 0 
    return 1

def clear_taskNumberField() :
    taskNumberField.delete(0.0, END)
 
def clear_taskField() :
    enterTaskField.delete(0, END)

def submit():
    global counter
    value = inputError()
    if value == 0 :
        return
    content = enterTaskField.get() + "\n"
    ToDo_list.append(content)
    TextArea.insert('end -1 chars', str(counter) + "." + content)
    counter += 1
    clear_taskField()

def delete() :
    global counter
    if len(ToDo_list) == 0 :
        messagebox.showerror("No task")
        return
    number = taskNumberField.get(1.0, END)
    if number == "\n" :
        messagebox.showerror("input error")
        return
     
    else :
        task_no = int(number)
    clear_taskNumberField()
    ToDo_list.pop(task_no - 1)
    counter -= 1
    TextArea.delete(1.0, END)
    for i in range(len(ToDo_list)) :
        TextArea.insert('end -1 chars',str(i + 1) + "." + ToDo_list[i])
     
if __name__ == "__main__" :
 
    window = Tk()
    window.configure(background = "light blue")
    window.title("ToDo List")
    window.geometry("250x300")

    enterTask = Label(window, text = "Enter Task", bg = "light blue")
    enterTaskField = Entry(window)

    Submit = Button(window, text = "Submit", fg = "Black", bg = "blue", command = submit)

    TextArea = Text(window, height = 5, width = 25, font = "arial")

    taskNumber = Label(window, text = "Delete Task Number", bg = "light blue")

    taskNumberField = Text(window, height = 1, width = 2, font = "arial")

    delete = Button(window, text = "Delete", fg = "Black", bg = "blue", command = delete)

    Exit = Button(window, text = "Exit", fg = "Black", bg = "red", command = exit)

    enterTask.grid(row = 0, column = 2)

    enterTaskField.grid(row = 1, column = 2, ipadx = 50)
                        
    Submit.grid(row = 2, column = 2)

    TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)
                        
    taskNumber.grid(row = 4, column = 2, pady = 5)
                        
    taskNumberField.grid(row = 5, column = 2)

    delete.grid(row = 6, column = 2, pady = 5)
                        
    Exit.grid(row = 7, column = 2)

    window.mainloop()