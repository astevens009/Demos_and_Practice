# from pathlib import Path
import fnmatch
from genericpath import exists
import os
import datetime
import shutil


def set_current_date(file_path):
    # TODO: Open the file for writing
    # target1 = "*COPYRIGHT (c) 20*"
    target1 = "*20*"

    file_lines = {}
    with open(file_path, mode='r') as edit_file:
        items = edit_file.readlines()
        
        # NOTE: Create a dictionary and read back in only the edited lines. This will add complexity in that we have to find a way to only edit the specific line.
        

        for index, line in enumerate(items):
            copyright_match = fnmatch.fnmatch(line, target1)
    
            if copyright_match:
                print("Line found at index: {}".format(index))
                lines_found.append(line)

    if len(lines_found) > 0:
        for ln in lines_found:
            print(ln)
    else:
        print(f"{target1} not found")


def create_backup_location(source_file):
    """
    Backup files to be edited in case reversion is needed
    """
    # TODO: Remember to change the unique generator
    current_date = datetime.datetime.now()
    version = current_date.strftime("%Y_%m_%d_%H%M%S")

    # Get the basename without the extension
    filename = os.path.splitext(os.path.basename(source_file))[0]

    os.makedirs("Backup", exist_ok=True)
    shutil.copyfile(source_file, "Backup\\bak_{}_{}.py".format(filename, version))


def backup_file_to_edit(file_path):
    pass


def change_copyright_year(file_path, current_year, confirm = False):
    """
    Modify a section of the file that matches a given pattern
    """
    target = "COPYRIGHT"

    # TODO: Create a backup before modifying file; have it return its location?
    # TODO: Write a clean up program to delete old files
    filename = os.path.basename(file_path)
    backup_file_to_edit(file_path)
    
    # if not os.path.exists("Backup\\bak_{}".format(filename)):
    if not os.path.exists("Backup"):
        create_backup_location(file_path)

    else:
        # If it does exist, create a new version of the file (i.e. - bak_file_20040125.py, bak_file_20040125_01.py, bak_file_20040125_02.py)
        pass

    
    with open(file_path, mode='r+') as edit_file:
        items = edit_file.readlines()
        replacement_line = "# COPYRIGHT (c) {} \n".format(current_year)

        print("Original content:\n{}\n".format(items))

        for index, line in enumerate(items):
            if target in line:
                old_line = line
                items[index] = line.replace(old_line, replacement_line)

                # Update the file
                # This will overwrite the file with the content of the items list
                edit_file.seek(0)
                edit_file.writelines(items)

    # Confirm that the file was successfully changed
    if confirm:
        # edit_file.seek(0)
        # print("Current content:\n{}\n".format(edit_file.read()))
        display_changed_file(file_path)
        

def display_changed_file(file_path):
    print("Updated date...")

    with open(file_path, mode = 'r') as new_file:
        print("Current content:\n{}\n".format(new_file.read()))


def get_current_year():
    """
    Retrieve the current year to update the file
    """
    # Get the current date
    current_date = datetime.datetime.now()

    # Extract the current year
    current_year = current_date.strftime("%Y")

    return current_year
    

if __name__ == '__main__':

    # File to edit
    file_path = "C:\\Users\\n33963\\OneDrive - NGC\\Training\\Sandbox\\Demo_Files"

    # files_list = os.listdir(file_path)
    # for file in files_list:
    #     print(file)

    # set_current_date(file_path)

    change_copyright_year(file_path, get_current_year(), True)

   