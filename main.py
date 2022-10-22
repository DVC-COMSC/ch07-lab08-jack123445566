numbers = [10, 15, 25, 30, 35]

insval = int(input())

for i in range(len(numbers)):
    if numbers[i] > insval:
        numbers.insert(i, insval)
        break
else:  
    numbers.append(insval)

print(numbers)