var express = require('express')
var bodyParser  =require('body-parser')

var web = express()

web.use(express.static('public'))
web.use(bodyParser.urlencoded({extended:false}))

web.get('/getText',function(req , res){

    var name = req.query.name

    var des = req.query.des

    setTimeout(function(){
        res.send('听说有一种' + des + '非常厉害,叫做' + name)
    },2000)
})

web.post('/postTest',function(req , res){
    var start = req.body.start
    var des = req.body.des
    console.log(start)
    console.log(des)

    setTimeout(function(){
        res.send('商品评价成功')
    },2000)
})

web.listen('8080' , function(){
    console.log('服务器启动成功.......')
})

// xhr 数据请求流程
// 1：初始化xhr对象
//    设置请求方法 以及接口 open() xhr.readyStart = 0
//    开始发送数据到后台 send() xhr.readyStart =1
// 2：后端接受前端发送过来的数据
//    req.query.xx  get  
//    req.body.xx   post
// 3：将数据从后台返回给前端
//    xhr.readyStart = 2
//    res.send() 发送数据给前端      
// 4：前端接受后端发送过来的数据
//    接收部分数据时 xhr.readyStart =3
//    接收全部数据时 xhr.readyStart = 4  
