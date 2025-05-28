import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.configure(bg="#2E2E2E")  # Dark background

# Remove window resize option
root.resizable(False, False)

# Create a frame to simulate a rounded box look
frame = tk.Frame(root, bg="#1C1C1C", bd=0, relief='solid')
frame.place(relx=0.5, rely=0.5, anchor='center')

# Create and style the label
label = tk.Label(
    frame,
    font=('Helvetica', 40, 'bold'),
    background='#1C1C1C',
    foreground='#00FFCC',  # Aqua blue
    padx=20,
    pady=20
)
label.pack()

# Function to update time
def update_time():
    current_time = strftime("%I:%M:%S %p\n%m/%d/%Y")
    label.config(text=current_time)
    label.after(1000, update_time)

# Start clock
update_time()

# Start GUI
root.mainloop()
