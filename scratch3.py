def format_message(msg_type, message_list):
    # header = " TOP ROW "
    # footer = " BOTTOM ROW "
    header = msg_type.upper()
    footer = msg_type.upper()
    head_banner_row = round((80 - len(header)) / 2)
    foot_banner_row = round((80 - len(footer)) / 2)
    header_banner = "*" * head_banner_row
    footer_banner = "*" * foot_banner_row
    

    # Text
    # line1 = "Welcome To The Matrix"
    # line2 = "Everything that has a beginning has an end"
    print(header_banner, header, header_banner)
    for msg in message_list:
        space_formatter = ('\t'*round((70-len(msg)) - 2))
        # space_formatter = ('\t'*50)
        print('\n* {}\n{} *'.format(msg, space_formatter))
    print(footer_banner, footer, footer_banner)

if __name__ == '__main__':
    msgs = [
        "Wakanda Forever",
        "Long live Wakanda!"
        ]
    
    format_message("WARNING", msgs)