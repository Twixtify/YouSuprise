import re
import numpy
import requests
import webbrowser
from bs4 import BeautifulSoup


def random_video(crawl_length):
    video = 1
    numpy.random.seed()
    url = 'https://www.youtube.com'
    while video <= crawl_length:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        video_set = set()  # Empty set, does not save duplicates and is O(1) fast
        for link in soup.find_all('a', attrs={'href': re.compile("/watch")}):
            href = link.get('href')
            print(url + href)
            if len(href) <= 43:  # Remove playlist links
                video_set.add('https://www.youtube.com' + href)
            if link.string is not None:
                print(link.string)
        video_list = list(video_set)  # List append at O(n), linear of size
        url = url.replace(url, video_list[numpy.random.randint(len(video_list))])
        print("New link: " + url)
        video += 1
    webbrowser.open(url)

random_video(10)
