import urllib3
import urllib.request as urllib3
from urllib.request import urlopen
import os
import sys
import re
import webbrowser
#import vlc
import youtube_dl
from bs4 import BeautifulSoup as soup
import subprocess
from subprocess import Popen, PIPE

print("enter the search term:")
search = input()

parent_dir = '/Users/harshitruwali/Movies/'

print("creating a new directory")
path = os.path.join(parent_dir, search) 
os.mkdir(path)
folder = path
print("created a new directory named ", search)

for the_file in os.listdir(folder):
    os.path.join(folder, the_file)
    try:
        if os.path.isfile(the_file):
            os.unlink(the_file)
    except Exception as e:
        print(e)
            
    myvideo = search
    if myvideo:
        flag = 0
        url = "https://www.youtube.com/results?search_query=" + myvideo.replace(' ', '+') 
        #url = "https://www.youtube.com/user/MrFish235/videos"
        response = urllib3.urlopen(url)
        html = response.read()
        soup1 = soup(html, "lxml")
        url_list = []
        for vid in soup1.findAll(attrs={'class':'yt-uix-tile-link'}):
            if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
                flag = 1
                final_url = 'https://www.youtube.com' + vid['href']
                url_list.append(final_url)
                url = url_list[0]
        ydl_opts = {}
        os.chdir(path)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            subprocess.Popen(path, shell=True)
        if flag == 0:
            print("-----over----")
      



