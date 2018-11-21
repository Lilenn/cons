var express = require('express')
var bodyParser = require('body-parser')
var multer = require('multer')
var fs = require('fs')

var web = express()
var form = multer()

web.use(express.static('public'))
web.use(bodyParser.urlencoded({ extended: false }))

web.post('/text', form.array(), function (req, res) {
    fs.exists('data', function (isExists) {

        if (!isExists) {
            fs.mkdirSync('data')
        }

        var data = req.body
        var infoString = JSON.stringify(data)

        fs.appendFile('data/test.txt', infoString + ',\n', function (err) {
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

web.get('/getInfo',function(req , res){
    fs.exists('data',function(isExists){
        if(isExists)
        {
            fs.readFile('data/test.txt',function(err,data){
                if(err)
                {
                    res.send('读取失败' + err)
                }
                else{
                    res.send(data)
                }
            })
        }
    })
})

web.listen('8080', function () {
        console.log('服务器启动成功.......')
})