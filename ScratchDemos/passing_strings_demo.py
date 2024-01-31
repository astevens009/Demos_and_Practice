import html

def display_raw_string(text):
    """
    Display the non-printable characters in a passed in string
    """
    raw_string = repr(text)
    print(f"\nThe raw string is:\n{raw_string}\n")

def display_html_string(text):
    """
    Display the non-printable HTML characters
    """

    html_string = html.escape(text)
    print(f"\nThe html string is:\n{html_string}\n")


if __name__ == '__main__':
    sample_text = "\nEverything\nwith a beginning\nhas an end.\n"
    sample_html = "<br>Everything<br>with a beginning<br>has an end.<br>"

    display_raw_string(sample_text)
    display_html_string(sample_html)