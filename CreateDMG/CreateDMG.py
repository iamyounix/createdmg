import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def select_file_or_folder():
    # Ask the user if they want to select a file or a folder
    choice = messagebox.askquestion("Select Type", "Do you want to select a file? Click 'No' to select a folder.")
    
    if choice == 'yes':
        # Select a file
        path = filedialog.askopenfilename(title="Select a file")
    else:
        # Select a folder
        path = filedialog.askdirectory(title="Select a folder")
    
    return path

def create_dmg():
    # Open a file/folder dialog to select a file or folder
    source_path = select_file_or_folder()
    if not source_path:
        messagebox.showerror("Error", "No file or folder selected. Exiting.")
        return
    
    # Get the base name of the file or folder
    base_name = os.path.basename(source_path.rstrip(os.sep))
    # Define the output DMG file name (in the same directory as the source)
    output_dmg = f"{os.path.join(os.path.dirname(source_path), base_name)}.dmg"
    
    try:
        # Run the hdiutil command to create the DMG
        subprocess.run([
            "hdiutil", "create",
            "-volname", base_name,
            "-srcfolder", source_path,
            "-ov", "-format", "UDZO",
            output_dmg
        ], check=True)
        
        messagebox.showinfo("Success", f"DMG created: {output_dmg}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to create DMG: {e}")

# Set up the tkinter window
root = tk.Tk()
root.title("DMG Creator")

# Set up the GUI layout
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Select a file or folder to create a DMG:")
label.pack(pady=(0, 10))

button = tk.Button(frame, text="Select File/Folder", command=create_dmg)
button.pack()

# Start the tkinter main loop
root.mainloop()
