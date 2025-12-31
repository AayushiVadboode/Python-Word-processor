from tkinter import filedialog, messagebox

recent_files = []   # recent files list


def new_file(text_area):
    text_area.delete(1.0, "end")


def open_file(text_area, recent_menu):
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text_area.delete(1.0, "end")
                text_area.insert("end", file.read())

            # recent files update
            if file_path not in recent_files:
                recent_files.insert(0, file_path)

            update_recent_menu(recent_menu, text_area)

        except Exception as e:
            messagebox.showerror("Error", str(e))


def save_file(text_area):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text_area.get(1.0, "end"))
        except Exception as e:
            messagebox.showerror("Error", str(e))


def open_recent(file_path, text_area):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete(1.0, "end")
            text_area.insert("end", file.read())
    except:
        messagebox.showerror("Error", "File not found")


def update_recent_menu(recent_menu, text_area):
    recent_menu.delete(0, "end")

    for path in recent_files[:5]:   # only last 5
        recent_menu.add_command(
            label=path.split("/")[-1],
            command=lambda p=path: open_recent(p, text_area)
        )
