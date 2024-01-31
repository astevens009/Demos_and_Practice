import html
from html.parser import HTMLParser

class SampleHTMLParser(HTMLParser):
    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        print("Start tag found: ", tag)

    def handle_endtag(self, tag: str) -> None:
        print("End tag found: ", tag)

    def handle_data(self, data: str) -> None:
        print("Here is some data: ", data)

sample_text = r"Everything that has a beginning<br>has an end"
sample_text2 = "Everything that has a beginning<br>has an end"

# region Simple demos

# html_text = html.escape("Everything that has a beginning<br>has an end")

# print('\n', sample_text, '\n')
# print(html_text, '\n')

# endregion

# region HTML demo 1

# sample_parser = SampleHTMLParser()
# sample_parser.feed(sample_text)
# print()

# esc_text = html.escape(sample_text)
# print('\n', esc_text, '\n')+

# endregion

# region raw text demo

# demo_text = repr(sample_text2)
# print('\n', demo_text, '\n')

test1 = 'This is a\ntest'.isprintable()
print(test1)

# endregion





