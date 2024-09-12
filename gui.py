import tkinter as tk
from tkinter import filedialog, messagebox
from main import main
# Create the main application window
root = tk.Tk()
root.title("GoPro Video Manager")
root.geometry("400x200")

global file_path

# Variables to manage the states of the checkboxes
folder_selected = False
merge_videos_var = tk.BooleanVar()
delete_clips_var = tk.BooleanVar()

# Function to select folder path
def select_folder():
    global folder_selected
    folder_path = filedialog.askdirectory()
    global file_path
    file_path = folder_path
    if folder_path:
        folder_selected = True
        merge_checkbox.config(state=tk.NORMAL)
        run_button.config(state=tk.NORMAL)
    else:
        folder_selected = False
        merge_checkbox.config(state=tk.DISABLED)
        delete_checkbox.config(state=tk.DISABLED)
        run_button.config(state=tk.DISABLED)

# Function to update the state of checkboxes
def toggle_merge():
    if merge_videos_var.get():
        delete_checkbox.config(state=tk.NORMAL)
    else:
        delete_checkbox.config(state=tk.DISABLED)

def run_process():
    if folder_selected:
        merge = merge_videos_var.get()
        delete = delete_clips_var.get()
        messagebox.showinfo("Running")
        main(file_path, merge, delete)
        
    else:
        messagebox.showwarning("Error", "Please select a valid folder!")

# Header label
header_label = tk.Label(root, text="GoPro Video Manager", font=("Arial", 16))
header_label.pack(pady=10)

# Button to select folder
folder_button = tk.Button(root, text="Select Folder", command=select_folder)
folder_button.pack(pady=5)

# Merge videos checkbox (disabled initially)
merge_checkbox = tk.Checkbutton(root, text="Merge videos", variable=merge_videos_var, command=toggle_merge, state=tk.DISABLED)
merge_checkbox.pack(pady=5)

# Delete clips checkbox (disabled initially)
delete_checkbox = tk.Checkbutton(root, text="Delete clips", variable=delete_clips_var, state=tk.DISABLED)
delete_checkbox.pack(pady=5)

# Run button (disabled initially)
run_button = tk.Button(root, text="Run", command=run_process, state=tk.DISABLED)
run_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
