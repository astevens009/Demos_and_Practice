import datetime
import os
import re
import shutil
import logging

################### VARIABLES ###################
DIR_PATH = r"/workspaces/Demos_and_Practice/Sandbox/Demo_Files"
LOG_PATH = r"/workspaces/Demos_and_Practice/Sandbox/Test_Logs"
BACKUP_DIR = r"/workspaces/Demos_and_Practice/Sandbox"

# Using wildcards...
# TARGET = "20.."
# TARGET2 = "..-20.."

# Using regex patterns
TARGET = r"\d{4}"
TARGET2 = r"-\d{4}"

################### VARIABLES ###################

def generate_test_log():
    
    unique_id = get_current_date(True).strftime("%Y_%m_%d_%H_%M_%S")
    
    log_file = os.path.join(LOG_PATH, f"test_log.log_{unique_id}")
    
    logging.basicConfig(filename=log_file, encoding='utf-8', level=logging.DEBUG)

def get_current_date(full_date = False):
    """
    Generate the date to be used to build a unique id
    """
    current_date = datetime.datetime.now()

    if not full_date:
        current_year = current_date.strftime("%Y")
        return current_year
    else:
        return current_date


def backup_file_to_edit(file_to_edit):
    """
    Back up the file to edit in case there is any corruption of the file 
    while making modifications
    """

    try:
        # Create a path to backup the files
        # TODO: Instead of using hr, min, sec count how many files are already in the directory and add 1 to that count
        backup_sub_dir = get_current_date(True).strftime('%Y_%m_%d_%H_%M_%S')
        backup_path = os.path.join(BACKUP_DIR, rf"Backup/{backup_sub_dir}")

        if not os.path.exists(backup_path):
            os.makedirs(backup_path)

        # Backup the file
        file_name = os.path.basename(file_to_edit)
        # file_name = os.path.basename(file_to_edit).split('.')[0]
        # file_ext = os.path.basename(file_to_edit).split('.')[1]

        # TODO: Figure out how to get the proper locale time
        # unique_id = (get_current_date(True)).strftime("%Y_%m_%d_%H%M%S")
        # backup_file_name = os.path.join(backup_path, f"bak_{file_name}.{file_ext}")
        backup_file_name = os.path.join(backup_path, f"bak_{file_name}")
        
        shutil.copyfile(file_to_edit, backup_file_name)
    except Exception as err:
        # TODO: Log the exception
        print(f"ERROR: Problem attempting to backup file.\n{err}")


def update_copyright_date(files_list):
    """
    Modify the copyright date for all the files
    """

    for data_file in files_list:
        try:
            # Define the file path for the open() function
            file_path = os.path.join(DIR_PATH, data_file)

            # TODO: open the file
            # Find the copyright year to be updated
            search_value1 = re.compile(TARGET)
            search_value2 = re.compile(TARGET2)
            
            with open(file_path, 'r+') as fte:
                contents = fte.readlines()

                # Search the file contents for the target
                for item in contents:
                    value = search_value1.search(item)
                    value2 = search_value2.search(item)
                    if value is not None and value2 is not None:
                        # TODO: display the value
                        val = value.group()
                        val2 = value2.group()
                        if val in item:
                            logging.debug(f"TESTING ONLY:\n\tValue found: {val} in {item}")
                            # print(f"\nTEST: {val} found at {contents.index(val)}.")
                        elif val2 in item:
                            logging.debug(f"TESTING ONLY:\n\tValue found: {val2} in {item}")
                    else:
                        continue

            # TODO: read in the file

            # TODO: find the target

            # TODO: edit the target

            # TODO: write the changes to the file
            pass
        except Exception as err:
            logging.debug(err)
           


if __name__ == '__main__':
    
    generate_test_log()

    # TODO: back up the file in case any of the following steps 
    # corrupt the file; will require the creation of a unique id for each file
    files_list = os.listdir(DIR_PATH)
    for file in files_list:
        file_to_edit = os.path.join(DIR_PATH, file)
        backup_file_to_edit(file_to_edit)

    # TODO: edit the files
    update_copyright_date(files_list)

    # TODO: confirm the changes; if there is any deviation, restore the file from 
    # the backup

    # TODO: Cleanup --> remove backup files

