import re

def find_target(text, target_pattern = None):
    """
    Use regex tools to extract the year
    """
    # target = re.compile(target_pattern)
    target = re.compile(r'\d{4}-\d{4}')
    old_year = target.search(text)
    # old_year = target.search("Copyright (c) 2022-2023. All rights reserved.")
    
    print(f"TEST: old year is {old_year.group()}.\n")
    
    
def tester():
    # phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = phoneNumRegex.search('My number is 415-555-4242.')
    print('Phone number found: ' + mo.group())
    



if __name__ == '__main__':
    range_year_pattern = "^\\d{4}-\\d{4}$"
    str = "Copyright (c) 2022-2023. All rights reserved."
    
    find_target(str, range_year_pattern)
    # tester()