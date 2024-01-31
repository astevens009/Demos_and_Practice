cprt1 = "COPYRIGHT (c) 2022. All rights reserved."
cprt2 = "COPYRIGHT (c) 2022-2023. All rights reserved."

# copyright_list = [cprt1, cprt2]
copyright_list = [
    "# COPYRIGHT (c) 2022. All rights reserved. \n",
    "# COPYRIGHT (c) 2022-2023. All rights reserved.\n"
]




print("Original List:")
for item in copyright_list:
    print(item)

# region TEST DEMO 1
    
# for index, item in enumerate(copyright_list):
#     if "COPYRIGHT (c) 2022. All rights reserved." in item:
#         if copyright_list[index].startswith('#'):
#             copyright_list[index] = copyright_list[index].replace(item, "# COPYRIGHT (c) 2024. All rights reserved.") 
#         else:
#             copyright_list[index] = copyright_list[index].replace(item, "COPYRIGHT (c) 2024. All rights reserved.") 
#     if "COPYRIGHT (c) 2022-2023. All rights reserved." in item:
#         if copyright_list[index].startswith('#'):
#             copyright_list[index] = copyright_list[index].replace(item, "# COPYRIGHT (c) 2022-2024. All rights reserved.")
#         else:
#             copyright_list[index] = copyright_list[index].replace(item, "COPYRIGHT (c) 2022-2024. All rights reserved.")

# endregion TEST DEMO 1

# region TEST DEMO 2

for cr in copyright_list:
    if "COPYRIGHT" in cr:
        print("Found")
    else:
        print("Not found")

# endregion TEST DEMO 2
    
print("\nModified List:")
for item in copyright_list:
    print(item)

