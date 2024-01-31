import re
import datetime

# print(None == False)
# print(None == True)

# region REGEX DEMO 1

# words = ["up", "down", "left", "right"]
# text = "down"

# target = "do.."

# result = re.search(target, text)

# print(result.group())

# target = "..do"

# result = re.search(target, text)

# print(result.group())

# endregion REGEX DEMO 1

# region DATETIME

# current_date = datetime.datetime.now()

# print(f"Time is: {current_date.strftime('%c %H:%M:%S')}")

# endregion DATETIME

# region SAERCH STRING

# sample_list = [
#     "up", 
#     "down", 
#     "left", 
#     "right"
# ]

# TARGET = "up"

# if TARGET in sample_list:
#     print(f"\'{TARGET}\' found at: {sample_list.index(TARGET)}")
# else:
#     print("Not found")

# endregion SAERCH STRING

# region REGEX DEMO 2

# TARGET = "20.."
# TARGET2 = "-20.."
# TEXT = "COPYRIGHT (c) 2022"
# TEXT2 = "COPYRIGHT (c) 2022-2023"

# search_item = re.compile(TARGET)
# content = search_item.search(TEXT)

# print(f"Result: {content.group()}")

# content_to_replace = content.group()

# TEXT = TEXT.replace(content_to_replace, "2024")
# print(TEXT)

# search_item = re.compile(TARGET2)
# content = search_item.search(TEXT2)

# print(f"Result: {content.group()}")

# content_to_replace = content.group()

# TEXT2 = TEXT2.replace(content_to_replace, "-2024")
# print(TEXT2)
    
# endregion REGEX DEMO 2

# region REGEX DEMO 3

item1 = "COPYRIGHT (c) 2022. All rights reserved."
item2 = "COPYRIGHT (c) 2022-2023. All rights reserved."

search_value1 = r"\d{4}"
search_value2 = r"-\d{4}"

items_list = [item1, item2]

value1 = re.compile(search_value1)
value2 = re.compile(search_value2)

for item in items_list:
    print(f"Searching {item}...")
    val1 = value1.search(item)
    print(f"val1 is {val1}")

    val2 = value2.search(item)
    print(f"val2 is {val2}")

    if val1.group() in item:
        print(f"{val1.group()} found in {item}\n")
    elif val2.group() in item:
        print(f"{val2.group()} found in {item}\n")


# endregion REGEX DEMO 3