page = int(input("Write a page number please:"))

def pages():
    
    if page%2 == 0:
        print("This number is in the right side of the page.")
    else:
        print("This number is in the left side of the page.")

pages()
