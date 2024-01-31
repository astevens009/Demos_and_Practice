# Python program to replace text in a file

import os
import datetime
import fnmatch
from update_copyright2 import backup_file


def get_current_year():
    """
    Current year to update copyright year in file
    """
    current_date = datetime.datetime.now()
    current_year = current_date.strftime("%Y")

    return current_year


# Directroy of the source file(s)
DIR_PATH = r"/workspaces/Demos_and_Practice/Sandbox/Demo_Files"
CURRENT_YEAR = get_current_year()

# Strings to be modified
# Using wildcard '*'
target1 = "COPYRIGHT (c) 20*"
target2 = "COPYRIGHT (c) 20*-20*"

# file.txt should be replaced with
# the actual text file name
file_path = os.path.join(DIR_PATH, "African_Proverbs.txt")
# TODO: Back up the file before editing
backup_file(file_path)

with open(file_path, "r+") as file_to_edit:
    # each sentence becomes an element in the list lines_list
    lines_list = file_to_edit.readlines()

    # acts as a counter to know the
    # index of the element to be replaced
    # c = 0
    for line in lines_list:
        if fnmatch.fnmatch(line, target1):
            updated_text = f"COPYRIGHT (c) {CURRENT_YEAR}"
            # Replacement carries the value
            # of the text to be replaced
            line = line.replace(line, updated_text)
            break   # No need to read in any other lines

        elif fnmatch.fnmatch(line, target2):
            # TODO: The start of the year range needs to be retrieved
            updated_text = f"COPYRIGHT (c) 2022-{CURRENT_YEAR}"
            # TODO: Store the line
            # TODO: Split line
            # TODO: Find and store the start of the year range (i.e. - 2022)
            # TODO: Replace the end of the year range (i.e. - change 2023 to cureent year)
            # TODO: Join the line (i.e. - rebuild the line with the change)
            line = line.replace(line, updated_text)
            break   # No need to read in any other lines
        
        # c += 1


    # The pre existing text in the file is erased
    # file_to_edit.truncate(0)

    # the modified list is written into
    # the file thereby replacing the old text
    file_to_edit.writelines(lines_list)

    print("Text successfully replaced")
