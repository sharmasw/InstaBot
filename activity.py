from uiautomator import device as d
from uiautomator import Device
from time import sleep
import os,time,random
from tqdm import tqdm

d.infod = Device('375637504c583398')

print(d.info)

d.press.home()
sx, sy, ex, ey= 100 ,150,100,450
d.swipe(sx, sy, ex, ey, steps=5)

instaVal=d(text='Instagram', className='android.widget.TextView')
instaVal.click()

time.sleep(3)

sx, sy, ex, ey= 560,800,560 ,250
d.swipe(sx, sy, ex, ey, steps=10)

for i in tqdm(range(50)):
    
    if random.randint(10,100)%2==0:
        try:
            pp=d(resourceId='com.instagram.android:id/row_feed_button_like',description='Like')
            pp.click()
        except:
            pass
        time.sleep(3)
    else:
        # time.sleep(2)
        pass
    sx, sy, ex, ey= 560,800,560 ,250
    d.swipe(sx, sy, ex, ey, steps=10)
    
for i in range(7):
    d.press.back()
    
# d.screen('off')