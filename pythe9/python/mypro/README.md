#验证模块包含
* User 用户数据表包含 username , password ,email  is_active
* Group 用户组
*Permission 存放用户和组的权限

#一个登陆的视图
*通过用户提交的标案获取用户户名和密码
* 将用户名和密码与数据库中的数据进行匹配
*检查用户是否进入活跃状态
*通过再http请求上附加session，让用户进入登陆状态


#使用消息框架
*django.contrib.message 和 MessageMiddleware 共同构成了消息系统

#sorl-thumbnail
* 这个模块采用两种方法显示缩略图
* 一个是提供了一个心得标签模板{% thumbnail %} 
* 另一个基于ImageField自定义的图片字段

# 使用jQuery发送Ajax请求
* Ajax asynchronous JavaScript and XML
* xml 不是必须采用的格式，还可以时json和html 或者纯文本