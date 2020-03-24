from bs4 import BeautifulSoup
import urllib2
import re
root_url = raw_input("Input novel url (https://wuxiaworld.com/novel/example): ")
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
req = urllib2.Request(root_url, headers=hdr)
website = urllib2.urlopen(req)
html = website.read()
links = re.findall('<a href="/novel/[a-z0-9-/">]{1,}', html)
chapter = 0
for link_slash_novel in links:
    link_slash_novel = link_slash_novel.replace('<a href=','')
    link_slash_novel = link_slash_novel.replace('>','')
    link_slash_novel = link_slash_novel.replace('"','')
    html = urllib2.urlopen(urllib2.Request('https://wuxiaworld.com' + link_slash_novel, headers=hdr))
    soup = BeautifulSoup(html, "html.parser")
    soup2 = soup.find('div', {'class' : 'fr-view'})
    content = soup2.get_text().encode('utf-8')
    filename = "chapter" + str(chapter) + ".txt"
    file = open(filename, 'w+')
    file.write(content)
    file.close()
    chapter = chapter + 1
    print("Writing chapter " + str(chapter) + " to file: " + filename)
