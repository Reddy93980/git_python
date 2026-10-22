def main():
    name = input("What is your name? ")

    try:
        number = float(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"Hello, {name}!")
    print(f"The square of {number} is {number ** 2}.")


if __name__ == "__main__":
    main()