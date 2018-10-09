# coding: utf-8
# Konstantyn Davidenko


class NewDevelop:
    """
    news
    """
    def __init__(self):
        self.title = ''
        self.date = ''
        self.text = ''
        self.sell_mod = 1
        self.seals_mos = 1


def get_all_news():
    news = []
    news_file = 'auto_history.txt'
    with open(news_file, 'r') as s:
        line = s.readline()
        while line:
            date, title, text, smod, selmod = line.split('\t')
            print(date, title, text, smod, selmod)
            n = NewDevelop()
            n.date = date
            n.title = title
            n.text = text
            n.sell_mod = selmod
            n.seals_mos = smod
            news.append(n)
            line = s.readline()
    return news