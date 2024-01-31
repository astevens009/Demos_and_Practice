# from pathlib import Path
import fnmatch
import os
import datetime


def set_current_date(file_path):
    # TODO: Open the file for writing
    # target1 = "*COPYRIGHT (c) 20*"
    target1 = "*20*"

    lines_found =[]
    with open(file_path, mode='r') as edit_file:
        items = edit_file.readlines()

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


def change_copyright_year(file_path, current_year):
    target1 = "*20*"

    # lines_found =[]
    with open(file_path, mode='r+') as edit_file:
        items = edit_file.readlines()
        replacement_line = "# COPYRIGHT (c) {} \n".format(current_year)

        print("Current lines:\n{}\n".format(items))

        for index, line in enumerate(items):
            if "COPYRIGHT" in line:
                # The following line gets the position in the file NOT in items list
                # replace_pos = edit_file.tell()      # this is the position to start the replacement
                old_line = line
                # line = line.replace(old_line, replacement_line)
                items[index] = line.replace(old_line, replacement_line)
                # edit_file.seek(replace_pos, 0)
                # edit_file.writelines(items[index])

                # Update the file
                # This will overwrite the file with the content of the items list
                edit_file.seek(0)
                edit_file.writelines(items)

        # TEST
        print("Updated date...")
        print("Current lines:\n{}\n".format(items))


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
    file_path = "C:\\Users\\n33963\\OneDrive - NGC\\Training\\Sandbox\\file_to_edit.py"

    # set_current_date(file_path)
    change_copyright_year(file_path, get_current_year())
   