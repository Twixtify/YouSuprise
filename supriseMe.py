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
        video_set = set()  # Empty set, don't save duplicates, append O(1) speed
        for link in soup.find_all('a', attrs={'href': re.compile("/watch")}):
            href = link.get('href')
            if len(href) <= len('/watch?v=dQw4w9WgXcQ'):  # Remove playlist links
                video_set.add('https://www.youtube.com' + href)
        video_list = list(video_set)  # List, append O(n), i.e linear in speed
        url = url.replace(url, video_list[numpy.random.randint(len(video_list))])
        print("Link ", video, " : " + url)
        video += 1
    webbrowser.open(url)

random_video(100)
