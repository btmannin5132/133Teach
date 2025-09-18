"""
Boolean Tables, feel free to uncomment if you want to see them

"""

"""
p = [1,0]
q = [1,0]

print("OR")
for P in p:
    for Q in q:
        print(f"{P} | {Q} = {P|Q}")

print("\nAND")
for P in p:
    for Q in q:
        print(f"{P} & {Q} = {P&Q}")


print("\nXOR")
for P in p:
    for Q in q:
        print(f"{P} ^ {Q} = {P^Q}")

print("\nNOT")
for P in p:
    print(f"~{P} = {1-P}")

print("\nNOR")
for P in p:
    for Q in q:
        print(f"~({P} | {Q}) = {1-(P|Q)}")

print("\nNAND")
for P in p:
    for Q in q:
        print(f"~({P} & {Q}) = {1-(P&Q)}")

print("\nXNOR")
for P in p:
    for Q in q:
        print(f"~({P} ^ {Q}) = {1-(P^Q)}")
"""

x = 5
y = 9

if x==5 and y==9:
    print("AND: x=5 and y=9")

if x==5 or y == 9:
    print("OR: x = 5, or y = 9 (or both can be true)")

if x==5 ^ y == 9:
    print("XOR: either x = 5, or y = 9 but not both are true")

if not(x==5 and y==9):
    print("NAND: x is not 5 or y is not 9") 


if not(x==5 or y==9):
    print("NOR: x is not 5 and y is not 9")

if not(x==5 ^ y==9):
    print("XNOR: Both statements are either both true or both")