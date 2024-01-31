# NOTE: Third extry indicates whether the value has changed
starships = [
    (0, ["U.S.S. Angelou", False]),
    (1, ["U.S.S. Sisko", False]),
    (2, ["U.S.S. Mansa Musa", False]),
    (3, ["U.S.S. Enterprise", False]),
    (4, ["U.S.S. Yangtzee", False]),
    (5, ["U.S.S. Yamato", False]),
    (6, ["U.S.S. Rio Grande", False]),
    (7, ["U.S.S. Mali", False])
]

if __name__ == '__main__':
    
    # TODO: convert list to dictionary
    ships_dict = dict(starships)
    
    # TODO: print results
    print(f"\n{ships_dict}")