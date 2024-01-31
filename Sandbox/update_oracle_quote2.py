import os
import re

lines = []
target = "Everything that has a beginning"
file_path = "/workspaces/Demos_and_Practice/Sandbox/oracle_quote.txt"

with open("/workspaces/Demos_and_Practice/Sandbox/oracle_quote.txt", 'r+') as text_to_edit:
    lines = text_to_edit.readlines()

    for index, line in enumerate(lines):
        if line == target:
            line[index] = line[index].replace(line[index], "Everything that has a beginning has an end.")
        break

    
    text_to_edit.writelines(lines)

    print("Done.")