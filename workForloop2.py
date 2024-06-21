heights = []

number = int(input("Number of heights\n"))

for x in range(number):
    height = int(input(f"Enter height {x+1}\n"))
    heights.append(height)

total = 0
for x in range(number):
    total = total + heights[x]
    print(heights[x])


print(f"Total height is {total}")
