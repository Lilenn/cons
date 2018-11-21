var express = require('express')
var bodyParser = require('body-parser')
var multer = require('multer')
var fs = require('fs')
var web = express()
var form = multer()

web.use(express.static('public'))
web.use(bodyParser.urlencoded({ extended: false }))

web.post('/addNew', form.array(), function (req, res) {
    // 判断是否存在指定文件夹
    // 如果存在 则回调函数值为 true
    // 如果不存在 则回调函数值为 false
    fs.exists('data', function (isExists) {
        if (!isExists) {
            fs.mkdirSync('data')
        }
        // var name = req.body.name
        // var job =req.body.job
        // var code = req.body.code
        // var card = req.body.card
        // var tel = req.body.tel
        // var time = req.body.currentTime
        // var json = {
        //     name:name ,
        //     job:job ,
        //     code:code ,
        //     card:card ,
        //     tel:tel ,
        //     time:time
        // }

        var data = req.body
        var json = {
            data: data,
            des: '新增员工'
        }
        var infoString = JSON.stringify(json)
         
        // 第一种方法:
        // fs.exists('data/info.txt', function (isExists) {
        //     if (isExists) 
        //     {
        //         fs.readFile('data/info.txt', function (err, data) {
        //             infoString = infoString + data
        //         })
        //     }
        // })
        
        // 第二种方式
        // fs.wirteFile('data/info.txt', infoString,{flag:'a'}, function (err)
        
        // 第三种方式
        fs.appendFile('data/info.txt', infoString + ',\n', function (err) {
            if (err) {
                console.log('写入失败')
                res.send('失败')
            }
            else {
                console.log('写入成功')
                res.send('成功')
            }
        })
    })
})

web.get('/getinfo', function (req, res) {
    fs.exists('data', function (isExists) {
        if (isExists) {
            fs.readFile('data/info.txt', function (err, data) {
                if (err) {
                    res.send('读取失败' + err)
                }
                else {
                    res.send(data)
                }
            })
        }
    })
})
web.listen('8080', function () {
    console.log('服务器启动.....')
})

// 1.index页面到 new页面  window.location.href = 'new.html'
// 2.放置input标签  获取input标签  getElementByName()
//   后面不要追加.value  因为按照现在的代码 input输入框没有来得及写入内容 代码就已经加载完毕
// 3.将数据发送到后台 xhr的form请求方式
//   var form = new.formdata()
//   form.append()
// 4.后台接收到数据“追加”到本地文件里面 
//    同时注意拼接成json 格式 所以在后面追加,
// 5.index页面进行数据请求 获取全部数据
// 6.后台接收到请求以后 读取本地文件 
//   将读到的数据全部发送到前台 数据格式为 数据一 ， 数据二。。。
//   数据的类型是字符串
// 7.前端 接受数据 将数据格式改成标准json格式的字符串 
//   然后转化成json JSON.parse 方法
//   再遍历 获取每条数据进行拼接
//   显示到当前界面上      