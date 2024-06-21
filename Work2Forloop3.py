#ChatGPT
# I understand the confusion, but the range function in Python does not include the end value in the sequence it generates. Let's clarify how range works and why it doesn't include the end value:
#
# Understanding range:
# range(start, stop) generates a sequence of numbers starting from start and ending just before stop.
# So, range(0, 5) generates the sequence [0, 1, 2, 3, 4].
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

numOfStudents = len(student_heights)
total = 0
average = 0


for n in range(0, len(student_heights)):
    total += student_heights[n]

average = total / numOfStudents

print(f"Total number of heights{numOfStudents} \n")
print(f"Sum of all the heights {total}")
print(f"Average heights is {average}")