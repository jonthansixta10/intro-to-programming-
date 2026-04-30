counter = [1, 20]
while counter[0] <= counter[1]:
    if counter[0] <= 15:
        print(counter[0])
    counter[0] += 1

for number in range(1, 30):
    if number % 2 == 0:
        continue

    print(number)


for number1 in range(1, 30):
    if number1 % 2 == 0:
        pass # this is a placeholder for code that will be added later

    print(number1)



count_down = [10, 1]
while count_down[0] >= count_down[1]:
    if count_down[0] == 5:
        count_down[0] -= 1
        continue
    print(count_down[0])
    count_down[0] -= 1



sum_total = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3, -3333, 11, 12, 13, 14, 15]
total = 0
for number in sum_total:
    if number < 0:
        break
    total += number
print(total)