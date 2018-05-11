# encoding:utf-8
import base64
import json
import urllib
import urllib.request
from urllib import request

import time

from GetDouYinImg import *

def get_token(host):
    header_dict = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36', "Content-Type": "application/json"}
    req = request.Request(url=host,headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    res_json = json.loads(res.decode('utf-8'))
    return res_json["access_token"]



'''
进行post请求
url：请求地址
value：请求体
'''
def get_info_post_json_data(url,value):
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
    req = request.Request(url=url,data=value,headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    return (res.decode('utf-8'))



def getBaiDuFaceTech(imgPath,access_token):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    # 二进制方式打开图片文件
    f = open(imgPath, 'rb')
    # 图片转换为base64
    img = base64.b64encode(f.read())
    params = {"image":img, "image_type":"BASE64","face_field":"age,beauty,expression,faceshape,gender,glasses,landmark,race,quality,facetype,parsing","image":img,"max_face_num":2}
    params = urllib.parse.urlencode(params).encode(encoding='utf-8')
    request_url = request_url + "?access_token=" + access_token
    #调用post请求方法
    face_info = get_info_post_json_data(request_url,params)
    
    #json字符串转对象
    face_json = json.loads(face_info)
    # print(face_json)
    #如果没有发现人像，会返回空
    if face_json['error_code'] > 0:
        face_dict={}
    else:
        #把想要的部分提取存入字典中
        result = face_json['result']['face_list'][0]
        # result = face_list['face_list']
        gender = result['gender']
        age = str(result['age'])
        race = str(result['race'])
        beauty = str(result['beauty'])
        face_dict = {"gender":gender,"age":age,"race":race,"beauty":beauty}
    return face_dict

'''
将获得的数据进行分析
face_dict：人脸识别后的数据
'''
def faceInfoAnalysis(face_dict):
    #如果发现人物继续判断
    if len(face_dict)!=0:
        #如果为女生继续判断
        if face_dict["gender"]=="female":
            print("性别：女")
            print("年龄："+face_dict["age"])
            print("颜值："+face_dict["beauty"])
            #如果颜值在40以上，并且年龄大于18继续
            if(float(face_dict["beauty"])>40 and float(face_dict["age"])>18):
                #点赞
                click_like()
                print("卡哇伊ヽ(✿ﾟ▽ﾟ)ノ 已喜欢❤！！！")
                #点赞后休息一秒，主要为能够看到点击爱心的效果
            else:
                print("再看看(๑•̀ㅂ•́)و✧")
        else:
            print("没有发现小姐姐，下一个")
    else:
        print("没有发现小姐姐，下一个")
    #上滑新视频
    switch_video()
    # 上滑新视频之后给2s等待加载新视频
