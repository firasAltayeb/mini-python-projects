def banner_text(text: str = "hey", width: int = 80) -> None:
    screen_width = width
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger then specified "
                         "width {1}".format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


banner_text(text="hello")
banner_text(width=60)
banner_text()


