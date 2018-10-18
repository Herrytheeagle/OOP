
site_title = 'websites'


def web_types(title, **kwargs):
    print(title)
    for p_title, post in kwargs.items():
        print(p_title, post)

web_types(site_title,
         web_com = 'commercial website',
         web_org = 'organisational website',
         web_edu = 'educational website',)
