def main():
    userName = input("What's your name? ")
    print(hello(userName))


def hello(name="world"):
    return f"Hello, {name}!"


if __name__ == "__main__":
    main()
