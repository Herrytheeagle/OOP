#
# site_title = 'websites'
#
#
# def web_types(title, **kwargs):
#     print(title)
#     for p_title, post in kwargs.items():
#         print(p_title, post)
#
# web_types(site_title,
#          web_com = 'commercial website',
#          web_org = 'organisational website',
#          web_edu = 'educational website',)

import matplotlib.pyplot as plt


def graph_operation(x, y):
    print('function that graphs {}  and {}'.format(str(x), str(y)))
    plt.plot(x, y)
    plt.show()

x1 = [1, 2, 3]
y1 = [2, 3, 1]

graph_operation(x1, y1)

