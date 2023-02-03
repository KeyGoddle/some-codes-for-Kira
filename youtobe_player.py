import numpy as np
import cv2
import pafy
import vlc
from bs4 import BeautifulSoup
import time
import io,sys,subprocess
#from tkinter import askopenfilename
import tkinter as tk 
from tkinter import ttk 
from tkinter.filedialog import askopenfilename 
import tkinter.messagebox as tkMessageBox 
import tkinter.simpledialog as tkSimpleDialog 
from tkinter.simpledialog import Dialog

from youtube_search import YoutubeSearch
import numpy as np

def searcher(finding):
    res=YoutubeSearch(finding,max_results=1).to_dict()
    a = str(res)
    s=a[a.find('/watch?v'):]
    stri = s[:s.find("'")]
    return ('https://www.youtube.com/'+stri)




global process

#name=askopenfilename(filetype=[("Video Files","*.h24")])
def pafyi(url):
    global best
    video = pafy.new(url)
    best = video.getbest()
    global media
    global a
    

    media = vlc.MediaPlayer(best.url)
    media.play()
    best = video.getbest(preftype="mp4")
    capture = cv2.VideoCapture(best.url)
    while True:
        grabbed, frame = capture.read()
        start_time=time.time()
        
        a =input()
        if a!='':
            print (time.time()-start_time)
            media.set_pause(1)
            time.sleep(4)
        if a=='':
            media.play()
        if a=='close':
            
            media.stop()
            print ('Введите новую песню')
            a=input()
            url=(searcher(a))
            pafyi(url)

global url

url = (searcher('миллион алых роз'))
pafyi(url)




        
        
