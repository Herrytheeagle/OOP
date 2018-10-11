# # names = {'jeff', 'eagle', 'adeoye', 'heritage', 'oscar', 'parlory'}
# #
# # for name in names:
# #     # print("Hello there, " + name)
# #     # print(''.join(['Hello there, ', name]))
#
# import os
#
# location_of_file = 'C:\\Users\\SAMSUNG\\Desktop\\Nest Web\\Python'
# name_of_file = 'Intermediate Python Programming'
# print(location_of_file + '\\' + name_of_file)
# with open(os.path.join(location_of_file, name_of_file)) as f:
#     print(f.read())

who = 'Gary'
how_many = 12

print(who, 'bought', how_many, 'apples!' )
print('{1} bought {0} apples!'.format(who, how_many))
