# Katie Hilliard, Module 10.2 Assignment, 12/12/2024

import tkinter as tk
import tkinter.messagebox as msg

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Title Change
        self.title("Hilliard-ToDo")
        self.geometry("400x500")

        # Custom Menu colors
        self.menu_bar = tk.Menu(self, bg="salmon", fg="white")
        self.config(menu=self.menu_bar)

        # Add Exit Button to program
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg="salmon", fg="green")
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.tasks_canvas = tk.Canvas(self, bg="white")
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas_window = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        self.task_create = tk.Text(self, height=3, bg="white", fg="black")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        self.tasks = [] 
        placeholder = tk.Label(self.tasks_frame, text="--- Add Items Here --- ** Right Click to Delete **",
                               bg="salmon", fg="green", pady=10) # Right Click to delete a task
        placeholder.bind("<Button-3>", self.remove_task)
        placeholder.pack(side=tk.TOP, fill=tk.X)
        self.tasks.append(placeholder)

        self.bind("<Return>", self.add_task)
        self.tasks_frame.bind("<Configure>", self.on_frame_configure)

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()

        if len(task_text) > 0:
            # Alternate between salmon and green backgrounds
            task_position = len(self.tasks)
            if task_position % 2 == 0:
                task_bg = "salmon"
                task_fg = "green"
            else:
                task_bg = "green"
                task_fg = "salmon"

            new_task = tk.Label(self.tasks_frame, text=task_text, bg=task_bg, fg=task_fg, pady=10)
            new_task.bind("<Button-3>", self.remove_task)  # Right-click to delete
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

            self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", f"Delete '{task.cget('text')}'?"):
            self.tasks.remove(task)
            task.destroy()

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
