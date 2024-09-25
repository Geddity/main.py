import random

left_stone = random.randint(3,20)
right_stone = []

for i in range(1, left_stone):
    for j in range(i, left_stone):
        if left_stone % (i+j) == 0 and i != j:
            right_stone.append(f'{i}{j}')

result = f'{str(left_stone)} - {"".join(right_stone)}'
print(result)

