# from  pytube import YouTube
# link="https://www.youtube.com/watch?v=0I3WXCKfpEQ"
# youtube_1=YouTube(link)
# # print(youtube_1.title)
# # print(youtube_1.thumbnail_url)
# videos=youtube_1.streams.all() #for All format videos
# # only_audio=youtube_1.streams.filter(onlyaudio=True)
# vid=list(enumerate(videos))
# for i in vid:
#     print(i)
# strm=int(input("Enter : "))
# videos[strm].download()
# print("sucessfully downloaded")
# ***** playlist *****
from pytube import  Playlist
py=Playlist("https://www.youtube.com/watch?v=aAxvIIxk6HA&list=PLu1V2YqNWkrJMuf1KKoD_pMUfircaCOtr")
print(f'Downloading : {py.title}')
for video in py.videos:
    video.streams.first().download()