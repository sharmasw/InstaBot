import random
from uiautomator import device as d
from uiautomator import Device
from time import sleep
import os,time
liftOfKeywords=['love','instagood','photooftheday','beautiful','happy','picoftheday','selfie','art','nature','fun','style','smile','food']
ele=random.choice(liftOfKeywords)

d.infod = Device('375637504c583398')

d.info

d.press.home()
sx, sy, ex, ey= 100 ,150,100,450
d.swipe(sx, sy, ex, ey, steps=5)

instaVal=d(text='Instagram', className='android.widget.TextView')
instaVal.click()
time.sleep(3)
d(className='android.widget.FrameLayout',description='Search and Explore').click()
kk=d(className='android.widget.EditText',resourceId='com.instagram.android:id/action_bar_search_edit_text')
kk.click()
time.sleep(3)
kk.set_text(ele)
time.sleep(3)
d.press.back()

d(resourceId='com.instagram.android:id/view_switcher_container').click()
d(resourceId='com.instagram.android:id/row_hashtag_textview_tag_name',index='0',className='android.widget.TextView').click()
d(resourceId='com.instagram.android:id/image_button',index='4').click()
d(className='android.widget.ImageView',resourceId='com.instagram.android:id/row_feed_button_like').click()
d(className='android.widget.TextView',text='Follow').click()
time.sleep(3)


for k in range(20):
    time.sleep(5)
    for i in range(3):
        time.sleep(3)
        sx, sy, ex, ey= 560,800,560 ,250
        d.swipe(sx, sy, ex, ey, steps=10)
    try:
        d(className='android.widget.ImageView',resourceId='com.instagram.android:id/row_feed_button_like').click()
        d(className='android.widget.TextView',text='Follow').click()
        print(str(k)+' Click and follow happened')
    except:
        print (str(k)+' Passed')
        pass
    
for i in range(7):
    d.press.back()
    
# d.screen('off')