# in , not in ,---------use value ,variable in sequence

# use in (strig ,touple , dic ,list,set)

word='APPLE'

letter = input("Gues letter in word :")

# ======================use ( in )
# if letter in word:
#     print(f"Found {letter} ")
# else:
#     print(f"Not founded {letter}")

# ========== use ( not in )
if letter not in word:
    print(f" not Found {letter} ")
else:
    print(f" founded {letter}")