import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x400")
        self.root.config(bg="#f7f7f7")
        
        self.task_list = []
        
        # Title Label
        self.title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 16, "bold"), bg="#f7f7f7", fg="#333")
        self.title_label.pack(pady=10)
        
        # Listbox with a scroll bar
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)
        
        self.listbox = tk.Listbox(self.frame, selectmode=tk.SINGLE, width=30, height=10, font=("Helvetica", 12), bg="#fff", fg="#333", bd=0, highlightthickness=0)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        
        # Buttons frame
        self.button_frame = tk.Frame(root, bg="#f7f7f7")
        self.button_frame.pack(pady=20)
        
        # Add Task Button
        self.add_button = ttk.Button(self.button_frame, text="Add Task", command=self.add_task, width=15)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)
        
        # Update Task Button
        self.update_button = ttk.Button(self.button_frame, text="Update Task", command=self.update_task, width=15)
        self.update_button.grid(row=0, column=1, padx=5, pady=5)
        
        # Delete Task Button
        self.delete_button = ttk.Button(self.button_frame, text="Delete Task", command=self.delete_task, width=15)
        self.delete_button.grid(row=1, column=0, padx=5, pady=5)
        
        # Clear All Button
        self.clear_button = ttk.Button(self.button_frame, text="Clear All", command=self.clear_all_tasks, width=15)
        self.clear_button.grid(row=1, column=1, padx=5, pady=5)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.task_list.append(task)
            self.listbox.insert(tk.END, task)

    def update_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            new_task = simpledialog.askstring("Update Task", "Enter the new task:")
            if new_task:
                self.task_list[selected_task_index[0]] = new_task
                self.listbox.delete(selected_task_index)
                self.listbox.insert(selected_task_index, new_task)
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def delete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            self.listbox.delete(selected_task_index)
            del self.task_list[selected_task_index[0]]
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def clear_all_tasks(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
            self.listbox.delete(0, tk.END)
            self.task_list.clear()

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
