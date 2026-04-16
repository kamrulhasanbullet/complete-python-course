# Can you change the values inside a list which is contained in set S?

s = {8, 7, 12, "Harry", [1, 2]}

# No, you cannot create the set because lists are mutable (unhashable), so it will raise a TypeError: unhashable type: 'list'.
