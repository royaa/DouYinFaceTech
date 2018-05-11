# encoding:utf-8

import os

from PIL import Image

#图片压缩比例
SIZE_normal = 1.0
SIZE_small = 1.5
SIZE_more_small = 2.0

#adb手机截图
def getDouYinImg():
    #截图
    os.system("adb shell /system/bin/screencap -p /sdcard/DCIM/Camera/screenshot.jpg")
    os.system("adb pull /sdcard/DCIM/Camera/screenshot.jpg face.jpg")
    #压缩图片
    img = Image.open("face.jpg").convert('RGB')
    scale = SIZE_small
    w, h = img.size
    img.thumbnail((int(w / scale), int(h / scale)))
    img.save('face.jpg')

#点小爱心
def click_like():
    os.system("adb shell input tap 641 648")#点击事件，小米2


#下滑新的视频
def switch_video():
    os.system("adb shell input swipe 540 1000 200 200")

