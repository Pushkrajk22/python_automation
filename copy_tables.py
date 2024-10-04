import pyautogui
import time

# Delay to give you time to focus on the initial input field
time.sleep(5)

# Run the sequence 75 times
for _ in range(75):
    # Press Tab twice
    pyautogui.press('tab')
    pyautogui.press('tab')
    
    # Select all text (Ctrl+A)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)  # Wait a moment for selection to register
    
    # Copy selected text (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Wait for the text to be copied
    
    # Switch to the other tab/window (Alt+Tab)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)  # Wait for the tab switch to complete
    
    # Press Tab twice in the new tab
    pyautogui.press('tab')
    pyautogui.press('tab')
    
    # Paste the copied text (Ctrl+V)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)  # Wait for the paste to complete
    
    # Switch back to the original tab/window (Alt+Tab)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)  # Wait for the tab switch to complete

    # Optional: Add a small delay between iterations if needed
    time.sleep(0.5)
