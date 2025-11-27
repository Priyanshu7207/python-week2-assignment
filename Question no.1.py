numbers = [10, 22, 33, 45, 52, 40, 75]

for num in numbers:
    if num > 50:
        break

    if num % 5 == 0:
        continue

    print(num)
