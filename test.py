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
        send = int(send)

        print(check_temp(send))

        send = input("Enter your Temperature: ")

    sys.exit(0)