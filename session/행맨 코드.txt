def printer_hangman(count):
    if count >= 1:
        head = "(.,.)"
    else:
        head = "     "
    if count >= 2:
        body = "|"
    else:
        body = " "
    if count >= 3:
        left_arm = "/"
    else:
        left_arm = " "
    if count >= 4:
        right_arm = "\\"
    else:
        right_arm = " "
    if count >= 5:
        left_leg = "/"
    else:
        left_leg = " "
    if count >= 6:
        right_leg = "\\"
    else:
        right_leg = " "

    print("----------")
    print("  |     ||")
    print("%s   ||" % head)
    print(" %s%s%s    ||" % (left_arm, body, right_arm))
    print("  %s     ||" % body)
    print(" %s %s    ||" % (left_leg, right_leg))
    print("        ||")
    print("     -----")