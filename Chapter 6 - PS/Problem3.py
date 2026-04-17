"""A spam comment is defined as a text containing following keywords:
"Make a lot of money", "buy now", "subscribe this", "click this".
Write a program to detect these spams."""

spam_keywords1 = "Make a lot of money"
spam_keywords2 = "buy now"
spam_keywords3 = "subscribe this"
spam_keywords4 = "click this"

comment = input("Enter a comment: ")

if (
    (spam_keywords1 in comment)
    or (spam_keywords2 in comment)
    or (spam_keywords3 in comment)
    or (spam_keywords4 in comment)
):
    print("This comment is a spam.")
else:
    print("This comment is not a spam.")

