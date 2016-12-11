print("Table of Powers\n")

for i in range(1,4):
    print(i, end = "\t")
print()
print("____________________\n")

for j in range(1,6):
    for k in range(1,4):
        print(j**k, end = "\t")
    print("\n")
