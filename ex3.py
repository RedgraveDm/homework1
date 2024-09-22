import itertools


numbers = [int(num) for num in input().split(' ')]
n = int(input())

unique_pairs = []
for inx1 in range(len(numbers)):
    for inx2 in range(inx1 + 1, len(numbers)):
        num1, num2 = numbers[inx1], numbers[inx2]
        if num1 + num2 == n:
            pair = (min(num1, num2), max(num1, num2))
            if pair not in unique_pairs:
                unique_pairs.append(pair)

print(unique_pairs)

unique_pairs = []
for pair in itertools.combinations(numbers, 2):
    if sum(pair) == n:
        if pair not in unique_pairs:
            unique_pairs.append(pair)

print(unique_pairs)
