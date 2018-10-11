# def gen():
#     yield 'oh'
#     yield 'hello'
#     yield 'there'
#
# for i in gen():
#     print(i)

RIGHT_COMBINATOIN = (9, 8, 9)

# found_combo = False
# for r1 in range(10):
#     if found_combo:
#         break
#     for r2 in range(10):
#         if found_combo:
#             break
#         for r3 in range(10):
#             if (r1, r2, r3) == RIGHT_COMBINATOIN:
#                 print('Found the combo: {}'.format((r1, r2, r3)))
#                 found_combo = True
#                 break
#             print(r1, r2, r3)


def combo_gen():
    for r1 in range(10):
        for r2 in range(10):
            for r3 in range(10):
                yield (r1, r2, r3)

for (r1, r2, r3) in combo_gen():
    print(r1, r2, r3)
    if (r1, r2, r3) == RIGHT_COMBINATOIN:
        print('Found the combo: {}'.format((r1, r2, r3)))
        break
    print(r1, r2, r3)
