#!/usr/bin/env python

import urllib
import os
import re
import sys

print "Url Downloader"

base_url = sys.argv[1] 
proxies = {'http':'http://172.16.30.20:8080' , 'https':'172.16.30.20:8080'}
urlfile = urllib.urlopen(base_url , proxies = proxies)
words = urlfile.read()
urls =  sorted(set(re.findall(r'[\w\.]+\.480p\.[\w\.]+mkv' , words)))
i = 0
for url in urls:
    print url
for url in urls:
    print 'Downloading Episode :', i+1
    try:
        urllib.urlretrieve(base_url + url , filename = url)
    except IOError:
        print 'Something went wrong!'
    i = i+1
