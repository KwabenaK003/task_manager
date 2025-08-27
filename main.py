import tkinter as tk
import ui


app = tk.Tk()
app.title("Task Manager")
app.geometry("800x500")


ui.show_all_tasks_frame(app)
app.mainloop()
