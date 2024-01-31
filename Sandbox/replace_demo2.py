import fnmatch


def update_copyright_date(text_to_update, pattern_to_match):
    text_match = fnmatch.fnmatch(text_to_update, pattern_to_match)

    if text_match:
        print("Found...")
        old_phrase = text_to_update
        text_to_update = text_to_update.replace(old_phrase, "The rain in Spain falls mainly on the frame.\n")

    return text_to_update

if __name__ == '__main__':

    phrase = "The rain in Spain falls mainly on the plane."
    print("\nOriginal phrase: {}\n".format(phrase))

    text_pattern = '*plan*'

    new_text = update_copyright_date(phrase, text_pattern)

    print("New Phrase: {}".format(new_text))
