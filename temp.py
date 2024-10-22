# # to select and delete rows

# import pyautogui as pg
# import time
# import keyboard

# pg.FAILSAFE = True

# time.sleep(3)


# # for i in range(300):
# #     pg.scroll(-142)
# #     time.sleep(0.1)
# #     pg.click()

# #     time.sleep(0.1)

# keyboard.wait("shift")
# for i in range(41):
#     pg.click()
#     time.sleep(0.1)



import os

def change_file_extension(directory, new_extension):
    # Ensure the new extension starts with a dot
    if not new_extension.startswith('.'):
        new_extension = '.' + new_extension
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(directory):
        # Form the full old file path
        old_file = os.path.join(directory, filename)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(old_file):
            # Get the file name without its current extension
            file_base = os.path.splitext(filename)[0]
            # Create the new file name with the new extension
            new_filename = file_base + new_extension
            # Form the full new file path
            new_file = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} -> {new_file}')

# Example usage
directory = r"C:\Users\PushkrajKulkarni\Temperory\moto"  # Replace with your USB path
change_file_extension(directory, 'pdf')  # Replace 'newext' with your desired extension (e.g., 'md')
