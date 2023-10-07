from pytube import YouTube
from sys import argv

# in future try tkinter

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

yd = yt.streams.get_highest_resolution()

yd.download('./Videos')
