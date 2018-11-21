from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse

from wechatpy import WeChatClient
from wechatpy import parse_message
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException

from . models import MaterialModel

from wechatpy.replies import create_reply
from .utils import do_reply,do_event
# Create your views here.

TOKEN = 'cons'

@csrf_exempt
def handle_wx(request):

    if request.method == 'GET':
        signature = request.GET.get('signature','')
        timestamp = request.GET.get('timestamp','')
        nonce = request.GET.get('nonce','')
        echo_str = request.GET.get('echostr','')


        try:
            check_signature(TOKEN,signature,timestamp,nonce)
        except InvalidSignatureException:
            echo_str = 'error'
        response = HttpResponse(echo_str)
        return response
    else:
        msg = parse_message(request.body)
        # 判断消息类型 文本消息处理
        if msg.type == 'text':
            reply = do_reply(msg)
        elif msg.type == 'event':
            reply = do_event(msg)
        response = HttpResponse(reply.render(),content_type='application/xml')
        return response

def create_menu(request):
    client = WeChatClient('wxeac1aed88d8117f1','24397d8edd0a39d21c169a87f351c916')
    client.menu.create({
        "button": [
            {
                "type": "click",
                "name": "今日歌曲",
                "key": "V1001_TODAY_MUSIC"
            },
            {
                "type": "click",
                "name": "歌手简介",
                "key": "V1001_TODAY_SINGER"
            },
            {
                "name": "菜单",
                "sub_button": [
                    {
                        "type": "click",
                        "name": "关于我",
                        'key':'V1001_ABOUT_ME'
                    },
                    {
                        "type": "view",
                        "name": "视频",
                        "url": "http://v.qq.com/"
                    },
                    {
                        "type": "click",
                        "name": "赞一下我们",
                        "key": "V1001_GOOD"
                    }
                ]
            }
        ]
    })
    return HttpResponse('ok')

def get_menu_info(request):
    client = WeChatClient('wxeac1aed88d8117f1', '24397d8edd0a39d21c169a87f351c916')
    menu_info = client.menu.get_menu_info()
    print(menu_info)
    return HttpResponse("OK")

@csrf_exempt
def add_material(request):
    # 上传临时素材并且存入数据库， 注意上穿的图片名字不能是中文
    media_type = request.POST.get("media_type", "")
    # print(request.FILES.values())
    # for i in request.FILES.values():
    #     print(type(i))
    media_file = request.FILES.get("media_file")
    # print(type(media_file))
    # print(dir(media_file))
    title = request.POST.get("title", "")
    introduction = request.POST.get("introduction", "")

    # 主要是获得access_token
    client = WeChatClient('wxeac1aed88d8117f1', '24397d8edd0a39d21c169a87f351c916')

    from wechatpy.client.api import WeChatMedia
    # 初始化上传临时媒体文件的类
    media = WeChatMedia(client)
    info = media.upload(media_type, media_file)
    # info = client.WeChatMedia.add(media_type, media_file.open(),title,introduction)
    print(info)
    material = MaterialModel()
    material.media_type = media_type
    material.title = title
    material.introduction = introduction
    material.media_id = info['media_id']
    material.save()
    return HttpResponse("OK")