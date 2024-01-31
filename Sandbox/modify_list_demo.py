pies_list = [
    "apple",
    "blueberry",
    "pecan",
    "chocolate cream",
    "peach",
    "cheesecake"
]

print("Original List:")
for pie in pies_list:
    print(pie)

# modify the list
# for index, pie in enumerate(pies_list):
#     if pie == "blueberry":
#         pie[index] = "blackberry"
#     break

if "blueberry" in pies_list:
    # pies_list[pies_list.index("blueberry")] = "blackberry"
    idx = pies_list.index("blueberry")
    pies_list[idx] = "blackberry"

print("\nModified List:")
for pie in pies_list:
    print(pie)