import sys


def check_temp():
    if send < 15:
        return ("so cold!")
    elif send < 30:
        return ("It's good day")
    elif send < 50:
        return ("it's hot...")
    else:
        return ("so hot!")


if __name__ == '__main__':
    send = input("Enter your Temperature: ")
    while send != 'q':
        if send.isnumeric():
            send = int(send)
            print(check_temp(send))
        else:
            print("You must enter number")

        send = input("Enter your Temperature: ")

    sys.exit(0)