
// 引入express模块 express模块为数据请求基础模块
// 如果发生数据请求 那么一定需要使用这个模块
var express = require('express')

// post请求方式 会将参数放入到请求体当中
// 所以需要引入解析请求体的模块 body-parser
var bodyParser = require('body-parser')

// 创建模块的一个实例化对象
var web = express()

// static 静态
// 让web对象使用工程中的静态资源 public文件夹
web.use(express.static('public'))

// 设置对url进行编码 并且不允许url进行扩展
// 如果设置为false 那么参数只能为数组或者字符串
// 如果设置为true 那么参数为任意类型
web.use(bodyParser.urlencoded({extended:false}))

// 存储注册成功以后的账号密码
var account = ''
var psw = ''

// get 表示使用get方法
// 方法后面追加两个参数
// 参数1：请求的接口
// 参数2：回调函数 回调函数里面有两个参数
//   参数1:前端从后端传的值 request
//   参数2：后端往前端传的值  response
web.get('/regist',function(req , res){
    var password = req.query.psw
    var password2 = req.query.pswa
    var user = req.query.user
    if(user != account && password == password2)
    {
        account = user
        psw = password

        res.send('恭喜注册成功！账号是' + user + '密码是' + password + '请妥善保管')
    }
    else{
        res.send('注册失败，账号已经被注册或者密码不一致')
    }
    console.log(password)
    console.log(password2)
})

web.post('/login',function(req , res){
    name = req.body.user
    password  =req.body.password

    if(name == account && password == psw)
    {
        res.send('恭喜登录成功')
    }
    else{
        res.send('登录失败，请检查账号和密码')
    }
})

// 让程序监听8080端口
web.listen('8080',function(){
    console.log('服务器启动.......')
})