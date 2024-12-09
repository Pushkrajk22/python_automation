import pyautogui
import tkinter as tk
import keyboard

# Function to update the label with current mouse coordinates
def update_coordinates():
    x, y = pyautogui.position()  # Get current mouse position
    coord_label.config(text=f"Cursor Position: ({x}, {y})")  # Update label
    root.after(100, update_coordinates)  # Schedule the function to run again after 100ms

# Function to print coordinates when 'r' key is pressed
def on_key_event(e):
    if e.name == 'r' and e.event_type == keyboard.KEY_DOWN:  # Detect the 'r' key press
        x, y = pyautogui.position()  # Get current mouse position
        print(f"pg.click({x}, {y})")

# Create the main window
root = tk.Tk()
root.title("Mouse Position Tracker")

# Create a label to display the coordinates
coord_label = tk.Label(root, font=("Helvetica", 16))
coord_label.pack(padx=20, pady=20)

# Start the coordinate updates
update_coordinates()

# Print a startup message to confirm the program is running
print("Program started! Press the 'r' key to print coordinates.")

# Start listening to keyboard events
keyboard.hook(on_key_event)  # Hook into the keyboard event

# Run the application
root.mainloop()
