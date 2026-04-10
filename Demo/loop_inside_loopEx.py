for i in range(1,4):
    for j in range(i):
        print(f"Outer Loop iteration {i}, inner loop ileration {j+1}")

print()
for i in range(4):
    for j in range(i):
        print("*",end = " ")