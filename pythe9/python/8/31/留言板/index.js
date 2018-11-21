var express = require('express')

var bodyParser = require('body-parser')

var web = express();

var fs = require('fs')

web.use(express.static('public'))

web.use(bodyParser.urlencoded({extended:false}))

// 声明一个数组  用来存放所有的留言
var allMessage = [];
//查询本地有没有数据 有的话 取出
fs.exists('data/info.json',function(isExists)
{
    // 如果文件存在 说明肯定有数据
    if(isExists)
    {
        allMessage = JSON.parse('data/info.json')
    }
    // 如果不存在  则创建文件夹
    else 
    {
        fs.mkdirSync('data')
    }
})
web.post('/sendMessage',function(req ,res){

    console.log(req.body);
    
    // string.replace()
    // global 全局替换
    req.body.content = req.body.content.replace(/</g,'&lt;')

    req.body.content = req.body.content.replace(/>/g,'&gt;')
    // allMessage.push()    pop()
    // allMessage.unshift()  shift()
    // allMessage.splice();  slice()


    // allMessage.push('XXXX');
    // allMessage.pop();
    // allMessage.shift()
    allMessage.unshift(req.body);

    fs.writeFile('data/info.json',JSON.stringify(allMessage),function(err){
        if(err)
        {
            res.send('留言失败')
        }
        else 
        {
            res.send('留言成功')
        }
    })
    console.log(allMessage)
})
web.get('/getAllMessage',function(req ,res)
{
    res.send(allMessage);
})
web.listen('8080',function()
{
    console.log('启动')
})

// 1.获取输入框的值 以及当前时间 发送到服务器

// 2.服务器在获取前端传输过来的数据之前
//   先检查本地有没有数据
//   有的话用数组接收
//   没有的话 创建文件夹
// 3.将前端传过来的数据 存储在数组中的第一个位置

// 4.前端发送留言完毕，立即获取所有留言（刷新页面）

// 5.后端将存放所有的数据的数组 发送给前端

// 6.前端拿到数据 遍历显示（为了方式XSS攻击，不识别<>）