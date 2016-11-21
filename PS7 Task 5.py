def count_spaces(userInput):
    spaces = 0
    for char in userInput:
        if char == " ":
            spaces = spaces + 1
    return spaces

def main():
    userInput = input("Please write something:")
    print("The number of spaces is", count_spaces(userInput))

main()
