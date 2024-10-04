import pyautogui
import tkinter as tk

# Function to update the label with current mouse coordinates
def update_coordinates():
    x, y = pyautogui.position()  # Get current mouse position
    coord_label.config(text=f"Cursor Position: ({x}, {y})")  # Update label
    root.after(100, update_coordinates)  # Schedule the function to run again after 100ms

# Create the main window
root = tk.Tk()
root.title("Mouse Position Tracker")

# Create a label to display the coordinates
coord_label = tk.Label(root, font=("Helvetica", 16))
coord_label.pack(padx=20, pady=20)

# Start the coordinate updates
update_coordinates()

# Run the application
root.mainloop()
