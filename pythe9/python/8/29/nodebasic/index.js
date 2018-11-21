// 引入express模块 express模块为数据请求基础模块
// 如果发生数据请求 那么一定需要使用这个模块
var express = require('express')
// 创建模块的一个实例化对象
var web = express()
// static 静态
// 让web对象使用工程中的静态资源 public文件夹
web.use(express.static('public'))

// get 表示使用get方法
// 方法后面追加两个参数
// 参数1：请求的接口
// 参数2：回调函数 回调函数里面有两个参数
//   参数1:前端从后端传的值 request
//   参数2：后端往前端传的值  response
web.get('/book', function(req , res){
    res.send('<h1>古今奇书《聊斋志异》</h1>')
})

// 让程序监听8080端口
web.listen('8080',function(){
    console.log('服务器启动.......')
})


// 1:下载64 位。msi安装程序 下一步
// 2：安装以后 node -v  or node --version 查看是否安装成功
// 3：注销 否则跟随node一起安装的npm不会生效
// 4：创建一个文件夹（不要中文及大写）
// 5：在终端打开文件夹路径， 输入命令：npm init
// 6：项目的所有配置信息 都可以回车忽略掉
// 7：配置完成后 会生成一个package.json
// 8：创建一个静态文件夹 例如 public 在里面创建文件 index.html
// 9：在项目文件下创建一个 index.js 里面为服务端代码
//     并下载所有依赖项（例如 node install express)
// 10：启动服务器 命令： 弄得index 查看页面 localhost:端口号
// 11：一旦修改服务端代码 需要先重启服务器
// 12：同一个服务器程序 不能再多个终端启动

// Error: listen EADDRINUSE :::8080
// 端口被占