# Note:- with big "List comprehension" we gonna run out of memory and
# with big "Generator Expression" we gonna run out of time.

input_list = [5, 6, 3, 10, 15, 2, 20, 5, 23, 29, 50]

# function checking for value divisible by 2 in the list composition


def div_by_two(value):
    if value % 2 == 0:
        return True
    else:
        return False

# generator expression
xyz = (i for i in input_list if div_by_two(i))

# print out the Generator Expression without iteration
print(xyz)

# iterate through the generator expression
for i in xyz:
    print(i)

# another format to iterate through the Generator expression is as commented below
# [print(i) for i in xyz]

# List Composition
xyz = [i for i in input_list if div_by_two(i)]

# print out the List composition
print(xyz)

# iterate through the List composition
[print(i) for i in xyz]