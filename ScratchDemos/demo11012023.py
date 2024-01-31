import html

samples = [
    ["The quick brown fox\njumps over the\nlazy cow"],
    ["The quick brown fox jumps over the lazy cow.\nThe quick brown fox jumps over the lazy cow.\nThe quick brown fox jumps over the lazy cow."],
    ["The\nquick\nbrown\nfox\njumps\nover\nthe\nlazy\ncow."]
]

# region demo 1

# sample = "The quick brown fox\njumps over the<br>lazy cow."

# result = "quick" in sample
# print(result)

# result = '\n' in sample
# print(result)

# result = '<br>' in sample
# print(result)

# endregion 

# region demo 2

# for item in samples:
#     for value in item:
#         # print(value, '\n')
#         if '\n' in value:
#             print("\nNewline found.\n")
#         else:
#             print("\nNewline not found.\n")

# print("\nNOT INDEXED:")
# if '\n' in samples:
#     print("\nNewline found.\n")
# else:
#     print("\nNewline not found.\n")

# print("\nINDEXED:")
# if '\n' in samples[0]:
#     print("\nNewline found.\n")
# else:
#     print("\nNewline not found.\n")

# endregion

# region demo 3

# samples2 = tuple(samples)

# print('\n', samples2, '\n')

# print(samples2[0], '\n')

# print(samples2[0][0], '\n')

# endregion

# region demo 4

# text = samples[0][0]
# print('\n', text, '\n')

# endregion

# region demo 5

print('\n', samples[0][0].isprintable(), '\n')

sample_text = html.escape("Everything that has a beginning<br>has an end")
print('\n', sample_text, '\n')
print(sample_text.isprintable(), '\n')

# endregion




