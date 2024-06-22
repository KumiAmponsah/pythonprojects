scores = input().split()
biggest = 0

for x in range(0, len(scores)):
    scores[x] = float(scores[x])

for x in range(0, len(scores)):
    if scores[x] > biggest:
        biggest = scores[x]


print(f"The highest number in the list is {biggest}")
