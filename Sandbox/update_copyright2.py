import datetime
import os
import sys
import shutil


# region global variables/constants

TARGET1 = "COPYRIGHT (c) 2022. All rights reserved."
    
TARGET2 = "COPYRIGHT (c) 2022-2023. All rights reserved."

# Directory where the files to update will be
DIRECTORY_PATH = r"/workspaces/Demos_and_Practice/Sandbox/Demo_Files"

# endregion String(s) to search for

def get_date_info(full_date_info = False):
    """
    Date information
    """
    current_date = datetime.datetime.now()
    
    if not full_date_info:
        current_year = current_date.strftime("%Y")
        return current_year
    else:
        return current_date

def backup_file(file_to_backup):
    """
    Make a copy of the file to edit in the event 
    the file gets corrupted
    """
    
    # Use the date to create a unique identifier for the backup file
    current_date = get_date_info(True)
    backup_id = current_date.strftime("%Y_%m_%d_%H_%M_%S")    # unique identifier
    
    if not os.path.exists("Backup"):
        os.makedirs("Backup")
    
    file_info = os.path.basename(file_to_backup).split('.')
    
    file_name = file_info[0]
    file_ext = file_info[1]
    
    file_source = os.path.join(DIRECTORY_PATH, file_to_backup)
    
    file_dest = os.path.join(r"Sandbox/Backup", f"bak_{file_name}_{backup_id}.{file_ext}")
    
    shutil.copyfile(file_source, file_dest)

def update_copyright_info():
    """
    Update the copyright information to reflect the current year
    """
    # for file in os.listdir(DIRECTORY_PATH):
    #     # TODO: Backup the file before modifying it
    #     backup_file(file)
    
    try:
        for file in os.listdir(DIRECTORY_PATH):
            # TODO: Backup the file before modifying it
            backup_file(file)
    except Exception as err:
        # Log the error
        print(f"Problem with file or directory:\n{err}")
            
    # TODO: Read in a file
    # TODO: Remember to loop through the files in the directory
    file_path = os.path.join(DIRECTORY_PATH, "file_to-edit1.py")
    with open (file_path, 'w+') as file_to_edit:
        pass
    
    # TODO: find the target string
    
    # TODO: Modify the string
    
    # TODO: Write out the modified file
    pass
    


if __name__ == '__main__':
    
    # Check the OS you're using
    # if sys.platform == "linux":
    #     print("\nYou are currently running on Linux.")
    # else:
    #     print("\nYou are currently running on Windows.")
        
    update_copyright_info()
    
