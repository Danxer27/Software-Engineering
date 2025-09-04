import tkinter as tk

root = tk.Tk()
root.title("Software Engineering Window")
root.geometry("200x50")

label_software = tk.Label(root, text="Software Engineering")
label_software.pack(pady=10)

label_software = tk.Label(root, text="This is a second branch to the software engineering repository")
label_software.pack(pady=10)

root.mainloop()