
var express = require('express')
var bodyparser = require('body-parser')
var multer = require('multer')
var fs = require('fs')
var web = express()
var form = multer()
web.use(express.static('public'))
web.use(bodyparser.urlencoded({extended:false}))
web.post('/new',form.array(),function(req,res){
    fs.exists('data',function(isExists){
        if(!isExists){
            fs.mkdirSync('data')
        }
    })
    var data = req.body
    var infostring = JSON.stringify(data)
    fs.appendFile('data/info.txt',infostring+',\n',function(err){
        if (err){
            console.log('写入失败')
            res.send('失败')

        }
        else{
            console.log('写入成功')
            res.send('留言时间：'+data.time+'<br>'+'留言内容:'+data.info)
        }
    })
})
web.listen('8080',function(){
    console.log('程序开启')
})