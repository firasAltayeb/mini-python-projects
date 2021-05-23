def banner_text(text: str = " ", width: int = 80) -> None:
    """ Print a string centred, with ** either side.

    :param text: The string to print.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the left and right edges.
    :param width: The overall width to print within
        (including the 4 spaces for the ** either side).
    :raises ValueError: if the supplied string is too long to fit.
    """
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


banner_text("*", 50)
banner_text("Always look on the bright side")
banner_text(width=60)
banner_text("When you're feeling in the dumps")
banner_text("*", 10)


