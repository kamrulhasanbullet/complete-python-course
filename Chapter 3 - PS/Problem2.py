# Write a program to fill in a letter template given below with name and date.

letter = '''
    Dear <|Name|>,
    You are selected!
    <|Date|>
    '''

name = input("Enter the name: ")

print(letter.replace("<|Name|>", name).replace("<|Date|>", "24 May 2025"))