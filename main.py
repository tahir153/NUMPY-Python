# I want to print all even values only.

for i in range(10):
    if i % 2 == 0:
        if i == 6:
            continue
        print(i)
