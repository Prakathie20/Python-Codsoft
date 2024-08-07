import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master): # default function
        self.master = master # main widget or window
        self.master.title('Todo App Project by techcodio') # title for the project
        self.master.config(bg='#FFFFFF') # setup a background color
        self.tasks = [] # take all the tasks

        self.task_entry = tk.Entry(master, width=30, bg='white')
        self.task_entry.pack(pady=10) # packing this entry 

        self.add_button = tk.Button(master, text='Add task', command=self.add_task, bg='#4CAF50', fg='White') #
        self.add_button.pack(pady=10) # padding y direction

        self.task_listbox = tk.Listbox(master, width=50, bg='#E0E0E0') 
        self.task_listbox.pack(pady=5)
        self.complete_button = tk.Button(master, text='Mark as completed',command=self.mark_completed, bg='#2196F3', fg='White')
        self.complete_button.pack(pady=5)

        self.remove_button = tk.Button(master, text='Remove task',command=self.remove_task, bg='#F44336', fg='white')
        self.remove_button.pack(pady=5)

    def populate_listbox(self):
        self.task_listbox.delete(0, tk.END) # clearing the content of the listbox
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task) # new add into the populate list box

    def add_task(self):
        task = self.task_entry.get().strip() # getting the task from entry
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.populate_listbox()
        else:
            messagebox.showwarning('Warning', 'Task cannot be empty')
    def mark_completed(self):
        selected_task=self.task_listbox.curselection()
        if selected_task:
            index=selected_task[0]
            self.tasks[index]=f'[completed] {self.tasks[index]}'
            self.populate_listbox()
        else:
            messagebox.showwarning('Warning','Please select a task to mark as completed')
    def remove_task(self):
         selected_task=self.task_listbox.curselection()
         if selected_task:
            index=selected_task[0]
            del self.tasks[index] 
            self.populate_listbox()
         else:
            messagebox.showwarning('Warning','Please select a task to remove') 
def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()

