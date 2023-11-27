import tkinter as TK                      
from tkinter import ttk                  
from tkinter import messagebox            
import sqlite3 as sql3                    
  
 
def AddTask():   
    Task_String = Task_Field.get()    
    if len(Task_String) == 0:  
        messagebox.showinfo('Error', 'Field Empty.')  
    else:            
        tasks.append(Task_String)  
        cursor.execute('insert into values (?)', (Task_String ,))  
        ListUpdate()  
        Task_Field.delete(0, 'end')

def ListUpdate():        
    ClearList()  
    for task in tasks:  
        TaskListbox.insert('end', task)

def UpdateTask():
    Task_String = Task_Field.get()
    if len(Task_String) == 0:
        messagebox.showinfo('Error', 'Field Empty , write task.')
    elif len(Task_String) != 0:
        try:
            value = TaskListbox.get(TaskListbox.curselection())
            if value in tasks:
                inx=tasks.index(value)
                tasks[inx]=Task_String
                ListUpdate()
                Task_Field.delete(0, 'end')               
                cursor.execute('update tasks set title = ? where title = ? ', (Task_String, value))
            
        except:
            messagebox.showinfo('Error', 'Not Selected. Cannot Update.')
            
def DeleteTask():  
    try:    
        value = TaskListbox.get(TaskListbox.curselection())  
        if value in tasks:  
            tasks.remove(value)  
            ListUpdate()  
            cursor.execute('delete from tasks where title = ?', (value,))  
    except:  
        messagebox.showinfo('Error', 'Task Not Selected. Cannot Delete.')        
def DelAllTask():  
    message_box = messagebox.askyesno('Delete All Task', 'Are you sure?')  
    if message_box == True:  
        while(len(tasks) != 0):  
            tasks.pop()  
        cursor.execute('delete from tasks')  
        ListUpdate()  
 
def ClearList():  
    TaskListbox.delete(0, 'end')  
  
def close():  
    print(tasks)  
    guiWindow.destroy()  
 
def RetrieveDatabase():  
    while(len(tasks) != 0):    
        tasks.pop()  
      
    for row in cursor.execute('select title from tasks'):  
        tasks.append(row[0])  
  
  
if __name__ == "__main__":    
    guiWindow = TK.Tk()   
    guiWindow.title("My To-Do List Application")  
    guiWindow.geometry("500x450+750+250")   
    guiWindow.resizable(0, 0)   
    guiWindow.configure(bg = "#FAEBD7")   
    connection = sql3.connect('listOfTasks.db')    
    cursor = connection.cursor()  
    cursor.execute('create table if not exists tasks (title text)')    

    tasks = []
    
    Header_Frame = TK.Frame(guiWindow, bg = "#FFFDE7")
    Functions_Frame = TK.Frame(guiWindow, bg = "#FFFDE7")  
    Listbox_Frame = TK.Frame(guiWindow, bg = "#FFFDE7")
   
    Header_Frame.pack(fill = "both")
    Functions_Frame.pack(side = "left", expand = True, fill = "both")  
    Listbox_Frame.pack(side = "right", expand = True, fill = "both")
 
    Header_Label = ttk.Label(  
        Header_Frame,  
        text = "ToDo_List",  
        font = ("Brush Script MT", "20"),  
        background = "#4d004d",  
        foreground = "#e6e6e6",
          
    )
    
    Header_Label.pack(padx = 20, pady = 20)  
  
    Task_Label = ttk.Label(  
        Functions_Frame,  
        text = "Enter Task:",  
        font = ("Consolas", "16", "bold"),  
        background = "#FFFDE7",  
        foreground = "#000000"  
    )  

    Task_Label.place(x = 30, y = 40)  
 
    Task_Field = ttk.Entry(  
        Functions_Frame,  
        font = ("Consolas", "15"),  
        width = 18,  
        background = "#ccffff",  
        foreground = "#A52A2A"  
    )  
  
    Task_Field.place(x = 30, y = 80)  
  
    
    Add_Button = ttk.Button(  
        Functions_Frame,  
        text = " Add ",  
        width = 15,  
        command = AddTask
        
    )
    Update_Button = ttk.Button(  
        Functions_Frame,  
        text = " Update ",  
        width = 15,  
        command = UpdateTask
        
    )
    Del_Button = ttk.Button(  
        Functions_Frame,  
        text = " Delete ",  
        width = 15,  
        command = DeleteTask  
    )  
    Del_All_Button = ttk.Button(  
        Functions_Frame,  
        text = " Delete All ",  
        width = 15,  
        command = DelAllTask  
    )  
    Exit_Button = ttk.Button(  
        Functions_Frame,  
        text = "Exit",  
        width = 15,  
        command = close  
    )  
  
    Add_Button.place(x = 40, y = 120)
    Update_Button.place(x = 40, y = 160)
    Del_Button.place(x = 40, y = 200)  
    Del_All_Button.place(x = 40, y = 240)  
    Exit_Button.place(x = 40, y = 280)  
  
  
    TaskListbox = TK.Listbox(  
        Listbox_Frame, 
        font = ("Consolas", "11", "bold","italic"), 
        width = 24,  
        height = 14,  
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#0d11fc",  
        selectbackground = "#d817e6",  
        selectforeground = "#FFFFFF"  
    )  
 
    TaskListbox.place(x = 10, y = 20)  
 
    RetrieveDatabase()  
    ListUpdate()  
    guiWindow.mainloop()    
    connection.commit()  
    cursor.close()  