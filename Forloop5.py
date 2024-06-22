# limit = int(input("Enter your limit (0 - 1000) \n"))
# add = 0
#
# if limit < 0 or limit > 100:
#     print("Number is out of range")
# else:
#     for x in range(0, limit+1):
#         if x % 2 == 0:
#             add += x
#
#     print(f"The sum of even numbers from 0 to {limit} is {add}")

# OR

limit = int(input("Enter your limit (0 - 1000) \n"))
add = 0

if limit < 0 or limit > 100:
    print("Number is out of range")
else:
    for x in range(0, limit+1, 2):
        add += x

    print(f"The sum of even numbers from 0 to {limit} is {add}")