import os
import re

lines = []
target = "Everything that has a beginning"
file_path = "/workspaces/Demos_and_Practice/Sandbox/oracle_quote.txt"

if os.path.exists(file_path):
    with open("/workspaces/Demos_and_Practice/Sandbox/oracle_quote.txt", 'r+') as text_to_edit:
        lines = text_to_edit.readlines()

        for line in lines:
            if fnmatch.fnmatch(line, target):
                line = line.replace(line, "Everything that has a beginning has an end.")
                break

        text_to_edit.writelines(lines)

        print("Done.")
else:
    print(f"{file_path} does not exist.")
