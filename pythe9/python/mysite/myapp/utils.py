from  wechatpy import create_reply
from . import apiutils
from wechatpy.replies import ArticlesReply, MusicReply,ImageReply
import requests
import json

from . import hisutils
from .models import MaterialModel

def do_reply(msg):
    if msg.content == '天气':
        # msg.content 就是发送过来消息的内容
        reply = create_reply('今天是晴天',msg)
    elif msg.content == '王者荣耀':
        reply = create_reply('万年青铜垃圾游戏，不玩了',msg)
    elif msg.content == '历史':
        result = hisutils.request1()
        reply = create_reply(result, msg)

    elif msg.content == '星座运势':
        result = hisutils.request2()

        res = result['name']+ ':' + '1.时间：' + result['datetime'] + '2.幸运色:' + result['color'] + '3.注意事项:' + result['summary']
        reply = create_reply(res,msg)
    elif msg.content == '倔强':
        reply = ArticlesReply(message=msg)
        reply.add_article({
            "title": "倔强",
            "description": "倔强",
            'image': '',
            "url": "https://mp.weixin.qq.com/s?__biz=MzU1OTc0NTQ1OQ==&tempkey=OTgwX1VsOXpaamFiaTJnRGtuMFZZRTVRNE5MQ0NMbTg1TmNrU2tRLWRvZWFxQ2ZGd0djSmdtazJoNC1NZXBMZW5Ob2ptOGNZb3d4VUdYNklFaWkwSHc5NWJoaEI2dl81SjZHZDhYdUwtbEVBRWZSN01acC05OVhST3hXem9wN1RFd0VCQWdxaUpjck12SGg3R0RzdWFYZC1ZeU1RYWZnOFEtcHlNRGpZN3d%2Bfg%3D%3D&chksm=7c13d1f94b6458ef3458ddd1e6bd5e31ae8bc410a21751e6ae5284cfbb6f9f0144d3613bac07#rd"
        })
    else:
        aip = apiutils.AiPlat('2109307989', '867FI1Wu8YsT3Gd8')
        data = aip.get_nlp_text_trans(msg.content, 0)
        reply = create_reply(data['data']['trans_text'], msg)
    return reply

# 响应用户的关注和取消关注的事件
def do_event(msg):
    if msg.event == 'subscribe':
        reply = create_reply('欢迎您关注我的公众号：请输入天气查看当前天气！',msg)
    elif msg.event == 'unsubscribe':
        pass
    elif msg.event == "click":
        if msg.key == "V1001_TODAY_MUSIC":
            # 回复音乐信息
            reply = MusicReply(message=msg)
            reply.title = '音乐'
            reply.description = '今日音乐 '
            thumb= MaterialModel.objects.get(id=5)
            reply.thumb_media_id= thumb.media_id
            reply.music_url = "http://www.xiami.com/song/1792541433"
            reply.hq_music_url = "http://www.xiami.com/song/1792541433"

        elif msg.key == "V1001_TODAY_SINGER":
            reply = ArticlesReply(message=msg)
            reply.add_article({
                "title": "阿信",
                "description": "陈信宏（Ashin），昵称阿信，1975年12月6日生于台北市北投区。中国台湾男歌手、词曲创作者，中国台湾摇滚乐团五月天的主唱，创意潮牌STAYREAL总裁。",
                "image": "https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=f8e67f4769061d95694b3f6a1a9d61b4/e4dde71190ef76c6f608fd549a16fdfaae5167f2.jpg",
                'url':'https://mp.weixin.qq.com/s?__biz=MzU1OTc0NTQ1OQ==&tempkey=OTgwX2tBU25rdGFHcjRuU0s2THJZRTVRNE5MQ0NMbTg1TmNrU2tRLWRvZWFxQ2ZGd0djSmdtazJoNC1NZXBKdEdlSmFuLU85ZHRJV2JkUlVHeTRienhCSVdQeGZpQ3BzajdBWUJJWC1zSWhfNlJWekc4ZEd5NGVrV2xkckZMTTUwX0FCdlNKN1BHc21JdldHSG1rZF9UT3g3V1NFQUpKcWFxcmNvLUQ3QVF%2Bfg%3D%3D&chksm=7c13d1c14b6458d7daa04b4a5e2737c2293aa2c678abfc3bad271bf63f11a961067f83183d63#rd'
            })
        elif msg.key == 'V1001_ABOUT_ME':
            reply = ArticlesReply(message=msg)
            reply.add_article({
                "title": "关于我",
                "description": "也没啥说的",
                'image':'http://i.dyt6.cc/0f/4d/04/cf/ea/c8/b2/f6/b2/79/7f/7f/0c/f5/db/0e.jpg',
                "url": "https://mp.weixin.qq.com/s/3u6BlqYLx8r9DiLBXbFU5g"
            })
        else:
            # 回复图片信息
            reply = ArticlesReply(message=msg)
            reply.add_article({
                "title": "阿信",
                "description": "陈信宏（Ashin）",
                "image": "http://img5.imgtn.bdimg.com/it/u=1430011000,1084796449&fm=26&gp=0.jpg",
                "url": "https://baike.baidu.com/item/%E9%99%88%E4%BF%A1%E5%AE%8F/334?fr=aladdin"
            })
            reply.add_article({
                "title": "百度图库",
                "description": "图片",
                'image':'http://img3.imgtn.bdimg.com/it/u=1241905237,194043770&fm=26&gp=0.jpg',
                "url": "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E9%98%BF%E4%BF%A1"
            })
            reply.add_article({
                "title": "百度图库",
                "description": "图片",
                'image':'http://img1.imgtn.bdimg.com/it/u=2285845240,3067239871&fm=26&gp=0.jpg',

            })
    else:
        reply = create_reply('我们不知道这个时间类型是什么',msg)
    return reply

