ele='beauty'
from uiautomator import device as d
from uiautomator import Device
from time import sleep
import os,time

d.infod = Device('375637504c583398')

d.info

d.press.home()
sx, sy, ex, ey= 100 ,150,100,450
d.swipe(sx, sy, ex, ey, steps=5)

instaVal=d(text='Instagram', className='android.widget.TextView')
instaVal.click()

time.sleep(3)
d(className='android.widget.FrameLayout',description='Profile').click()

d(text='Following', className='android.widget.TextView').click()
time.sleep(10)

sx, sy, ex, ey= 560,800,560 ,250
d.swipe(sx, sy, ex, ey, steps=10)

existingUserName=[]
for i in range(100):
    for view in d(resourceId='com.instagram.android:id/follow_list_subtitle'):
        print(view.info['text'])
        existingUserName.append(view.info['text'])
    sx, sy, ex, ey= 560,800,560 ,250
    d.swipe(sx, sy, ex, ey, steps=10)
    time.sleep(3)
    
existingUserName=list(set(existingUserName))
import pandas as pd
dataList=pd.DataFrame(data={'userList':existingUserName})
dataList.to_excel('MySubscriberList.xlsx',index=False)
len(existingUserName)

for i in range(7):
    d.press.back()
    
d.screen('off')