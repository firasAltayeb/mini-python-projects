def convert(seconds):
    day = seconds // 86400  # number of seconds in day
    # remainder of dividing the left hand by right hand
    seconds = seconds % (24 * 3600)  # 86400
    print(f"seconds {seconds}")
    hour = seconds // 3600
    seconds = seconds % 3600
    print(f"seconds {seconds}")
    minutes = seconds // 60
    seconds = seconds % 60
    print(f"seconds {seconds}")

    print(f"{day}:{hour}:{minutes}:{seconds}")


# Driver program
seconds_to_convert = 86399
convert(seconds_to_convert)
