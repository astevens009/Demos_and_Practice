import re


# region Using RegEx

single_year_pattern = "^\\d{4}$"
range_year_pattern = "^\\d{4}-\\d{4}$"

# endregion Using RegEx

def find_pattern(text):
    """
    Using string split()
    """
    
    # NOTE: Remember when searching a file tell() will give you the position in the file. Use that to find the regex pattern and then update the copyright year
    
    # NOTE: May not work since I don't know the length of the line where the target is found
    
    # target_pattern = "Copyright".casefold()
    
    # pos = text.find(target_pattern)
    
    # if pos != -1:       # -1 means the target was not found
    #     # target_line = 
    pass


def find_year_pattern(text):
    """
    Extract the year based on the given pattern
    """
    
    # target_year = re.compile(range_year_pattern)
    target_year = re.compile(r"^\d{4}-\d{4}$")
    old_year = target_year.search(text)
    
    # print("TEST: old year is {}".format(old_year))
    print(f"TEST: old year is {old_year.group()}")
    


if __name__ == '__main__':
    
    # NOTE: year => XXXX 
    # NOTE: or
    # NOTE: year => XXXX-XXXX


    african_proverb1 = \
        """
        Copyright (c) 2020-2023. All rights reserved.

        The best way to eat an elephant 
        in your path
        is to cut him up into little pieces

        """

    african_proverb2 = \
        """
        Copyright (c) 2023
        
        After a foolish deed 
        comes remorse
        """
        
    proverbs_list = [
        african_proverb1,
        african_proverb2
    ]
    
    find_year_pattern(african_proverb1)
    
    # Out of curiosity...
    # print(copyright)
    