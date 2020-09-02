import urllib.request
import feedparser
import os

flag = 0
url = 'https://opac.icu.ac.jp/opac/newbook_rss/?lang=0&dptidpl=1&jfcd=&sort=&cls=&clskey='

rss = feedparser.parse(url)

latest = rss.entries[0].title

with open('check.txt', mode='r')as f:
    tmp = f.read()
    if tmp != latest:
        flag = 1
        with open('check.txt', mode='w')as g:
            g.write(latest)

if flag:
    os.system("osascript -e 'display notification \"New Books Arrive!\"'")
    os.system('osascript /Users/yu/Documents/icu_library_check/icu_lib_url_open')
    