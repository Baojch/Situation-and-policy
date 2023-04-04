# Situation-and-policy
### 1.下载与电脑适配版本的chrome Driver或edge driver
https://registry.npmmirror.com/binary.html?path=chromedriver/   \
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
### 2.添加用户名和密码，并修改起始章节数和课程数
### 3.修改driver路径为你的本机driver地址，chromedriver = "你的driver文件地址"
若为edge则将web = webdriver.Edge(chromedriver)取消注释，
并将web = webdriver.Chrome(chromedriver)注释
### 4.直接在安装了selenium库的python环境下运行代码
\ 
PS:记得先置课

