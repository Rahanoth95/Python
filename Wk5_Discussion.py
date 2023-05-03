# This program is to evaluate if a number is even or odd.

# creating a True statement is the number is even no matter how high
while True:
    # prompts the user to input any number.
    user_input = int(input("Enter a number: "))
    # Equates weather the number is divisible by two and figuring if even or odd
    if user_input % 2 != 0: print("this number is odd.")
    # Break statement is used during loops execution incase the number is not divisible.
    break
    print("This number is even.")
