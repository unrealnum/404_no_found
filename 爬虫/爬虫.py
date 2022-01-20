# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:05:08 2022

@author: unreal_num border
"""

import requests
import os
import time


def request_download(IMAGE_URL,i,desk):
    r = requests.get(IMAGE_URL)
    with open(desk+'pic\\'+'img'+str(i)+'.png', 'wb') as f:
        f.write(r.content)
        time.sleep(1)
    f.close()



def pic_match(string):
    llist=[]
    fg1=0
    fg2=0
    for i in range(0,len(string)):
        if string[i]=='s':
            if string[i+1]=='r' and string[i+2]=='c':
                if string[i+4]=='"':
                    fg1=i+5
                    i+=5
                    while 1:
                        if string[i]=='"':
                            break
                        else:
                            i+=1
                    fg2=i
                    llist.append(string[int(fg1):int(fg2)])
    return llist

def text_match(string):
    textlist=[]
    fg1=0
    fg2=0
    for i in range(0,len(string)):
        if string[i]=='t':
            if string[i+1]=='.' and string[i+2]=='_' and string[i+3]=='v':
                i+=6
                fg1=i
                while 1:
                    if string[i]=='"':
                        break
                    else:
                        i+=1
                fg2=i
                textlist.append(string[fg1:fg2])
        elif string[i:i+4]=='this' and string[i+5:i+8]=='._v':
            i+=9
            fg1=9
            while 1:
                if string[i]=='"':
                    break
                else:
                    i+=1
            fg2=i
            textlist.append(string[fg1:fg2])
    return textlist
    
                        
                

desk = os.path.join(os.path.expanduser("~"), 'Desktop') + '\\'
fp=open(desk+'text.txt','w')
os.mkdir(desk+'pic')
f=requests.get('http://212.129.245.115:8080/static/js/app.7149a871ab46e4d1cdd7.js')
string=str(f.text)
textlist=[]
textlist=text_match(string)
piclist=[]
piclist=pic_match(string)
for i in textlist:
    fp.write(i)
    fp.write('\n')

cnt=0
for i in piclist:
    request_download(i,cnt,desk)
    cnt+=1
