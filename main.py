#tkinter python GUI library 
import tkinter as tk
from tkinter import messagebox
import action

root = tk.Tk()
root.title("My Word Processor")
root.geometry("900x600")

# text area
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both")

# menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=lambda: action.new_file(text_area))
file_menu.add_command(label="Open", command=lambda: action.open_file(text_area, recent_menu))
file_menu.add_separator()

# recent submenu
recent_menu = tk.Menu(file_menu, tearoff=0)
file_menu.add_cascade(label="Recent", menu=recent_menu)

file_menu.add_command(label="Save", command=lambda: action.save_file(text_area))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Cut", command=lambda: root.focus_get().event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: root.focus_get().event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: root.focus_get().event_generate("<<Paste>>"))

# help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

help_menu.add_command(
    label="About",
    command=lambda: messagebox.showinfo(
        "About",
        "Simple Word Processor\nMade with Python & Tkinter"
    )
)

root.mainloop()
