def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(text):
    text = str(text)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
# python_food()
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and eggs")

print("first", "second", 3, 4, "spam")
