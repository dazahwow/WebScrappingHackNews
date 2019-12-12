import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')
subText = soup.select('.subtext')

def sort_stories_by_score(hackerNewsList):
    return sorted(hackerNewsList, key= lambda k:k['votes'], reverse=True)

def create_custom_hacker_news(links, subText):
    hackerNews = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subText[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hackerNews.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_score(hackerNews)

pprint.pprint(create_custom_hacker_news(links, subText))
