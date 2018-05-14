> Simple, Interesting | 简单，有趣

## 效果
抖音经常能刷到很多高质量的视频，特别是我们使用的越多，头条的算法给我们推荐的内容越精准。**那么我们可不可以写一个小型的程序，根据自己设置的特征筛选视频并且自动点赞存入我们的收藏夹中呢？比如漂亮的小姐姐，帅气的小哥哥或者是可爱的喵星人。。。**
<!--more-->


![](https://github.com/jevonszmx/DouYinFaceTech/raw/master/20180418_000727.gif)

## 原理说明

##### 本程序与抖音无关，主要供学习用途

1. 将手机打开抖音的推荐视频界面

2. 用 ADB 工具获取当前手机截图，并用 ADB 将截图 pull 上来

```shell

adb shell screencap -p /sdcard/autojump.png
adb pull /sdcard/autojump.png .

```

3. 将图片进行压缩,并调用[百度人脸识别API](http://ai.baidu.com/tech/face)

4. 获得百度返回的数据进行判断分析

5. 如果满足要求，使用ADB点赞

6. 上滑切换新视频 





## 使用教程


#### 1、获取源码
github地址
```
https://github.com/jevonszmx/DouYinFaceTech
```
git命令
```
git clone https://github.com/jevonszmx/DouYinFaceTech.git
```
#### 2、依赖
```
Python：3.6.1 
ADB下载：http://adbshell.com/downloads
```

mac:

```
brew cask install android-platform-tools 

brew install python

pip3 install Pillow

```


#### 3、准备
```
使用数据线连接手机与电脑，并开启调试模式
启动ADB，保证驱动安装（保证可以连接360手机助手等软件）
Douyin.py中替换token的host链接

```
#### 4、运行
```
手机打开抖音，PC退出手机助手等软件
DouYinFaceTech目录下直接运行Douyin.py
```

#### adb相关

adb获取不同分辨率手机坐标的方法：

adb事件可以使用以下命令查看：

```

adb shell getevent -p

```

其中：0035、0036就是点击事件

那么我们开启：

```

adb shell getevent | grep -e "0035" -e "0036"

```

然后再点击抖音点赞，得到如下的数字：

```

/dev/input/event0: 0003 0035 00000341
/dev/input/event0: 0003 0036 000008ec

```

再把0035和0036后面的位置数据从16进制转化为10进制，就是想要的坐标了。


#### 参考/鸣谢

[Tomxin7](http://blog.tomxin.c)