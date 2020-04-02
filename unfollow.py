from uiautomator import device as d
from uiautomator import Device
from time import sleep
import os,time
import pandas as pd
data=pd.read_excel('MySubscriberList.xlsx')
print (data.shape)

d.infod = Device('375637504c583398')

d.info

d.press.home()
sx, sy, ex, ey= 100 ,150,100,450
d.swipe(sx, sy, ex, ey, steps=5)

instaVal=d(text='Instagram', className='android.widget.TextView')
instaVal.click()


userList=list(data['userList'])

time.sleep(3)
d(className='android.widget.FrameLayout',description='Profile').click()

d(text='Following', className='android.widget.TextView').click()
time.sleep(10)

sx, sy, ex, ey= 560,800,560 ,250
d.swipe(sx, sy, ex, ey, steps=10)

count=0
for k in range(70):
    for i in d(resourceId='com.instagram.android:id/button'):
        toCheck=i.info['contentDescription'].replace('Following ','').replace(' button','')
#         print (toCheck)
        if toCheck in userList:
            print (toCheck, ' NO action')
            pass
        else:
            i.click()
            print (toCheck, ' UNfollowed action')
            count +=1
        time.sleep(3)
    sx, sy, ex, ey= 560,800,560 ,250
    d.swipe(sx, sy, ex, ey, steps=10)
    time.sleep(3)
    if count >55:
        break
        
for i in range(7):
    d.press.back()
    
d.screen('off')