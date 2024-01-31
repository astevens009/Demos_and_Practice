
# Try to modify an element in a list by matching a pattern

import re

def modify_list_item(pies_list, item_to_modify, change):
    """
    Modifying an item by passing in the item to change and the change 
    """
    if item_to_modify in pies_list:
        # pies_list[pies_list.index("blueberry")] = "blackberry"
        idx = pies_list.index(item_to_modify)
        pies_list[idx] = change

    return pies_list


def modify_list_by_match(pies_list, item_to_modify, change):
    """
    Modify an item by matching it to the requested change
    """

    # target = "blue*"
    
    for index, pie in enumerate(pies_list):
        p = re.search(item_to_modify, pie)
        if p != None:
            if pie == p.group():
                idx = pies_list.index(pie)
                pies_list[idx] = pies_list[idx].replace(pies_list[idx], change)
                break
        else:
            continue

    return pies_list



if __name__ == '__main__':
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

    # pies_list = modify_list_item(pies_list, "blueberry", "blackberry")
    pies_list = modify_list_by_match(pies_list, "blueberry", "blackberry")

    print("\nModified List:")
    for pie in pies_list:
        print(pie)