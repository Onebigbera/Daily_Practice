#coding:utf-8

import smtplib
from email.mime.text import MIMEText

#设置服务器地址
server = "smtp.163.com"

#帐户名
sender = "13659831387@163.com"

#这个密码不是登陆密码，而是我们申请的授权密码
password = "limeng1"

#发送邮件的内容
message = "您好！感谢联系腾讯云课堂。网易云课堂对课程强调体系性与实用性，课程形式主要为视频和文本PDF格式。我们会为您做账号认证并开通课程上传权限，关于付费课程，云课堂会收取课程收入的10%作为服务费，结算周期是21天。附件是认证所需的信息请填写并回传，认证需要，另请附上身份证电子版。"

#将要发送的内容转换成邮件格式
msg = MIMEText(message)

#添加邮件标题
msg["Subject"] = "腾讯云课堂"

#添加发件人
msg["From"] = sender

# recive_list = """
#     "15527570912@163.com",
#     "13297916476@163.com",
#     "zhouyi9192@163.com",
#     "j741896551@163.com",
#                 """

# sendlist = recive_list.replace("\n","").replace(" ","").split(",")

#收件人
msg["To"] = "j741896551@163.com"

#设置一个服务器
mail_server = smtplib.SMTP(server,25)

#登陆服务器
login = mail_server.login(sender,password)

#发送邮件
send_mail = mail_server.sendmail(sender,
                                        [
                                     "15527570912@163.com",
                                    "13297916476@163.com",
                                    "zhouyi9192@163.com",
                                    "j741896551@163.com",
                                         ],
                                 msg.as_string())

#退出服务器
mail_server.quit()
