import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

mail_host = "smtp.qq.com" # 设置服务器
mail_user = "1591488713@qq.com" #用户名
mail_pass = "iutxqcrshxwkbafb" #STMP口令，不是密码

sender = '1591488713@qq.com'
receivers = ["zhangxinyi11111111@163.com"] #接受者的邮箱

#Multipart就是分多个部分
msg=MIMEMultipart()
msg['Subject']="这是个带附件的邮件"
msg['From'] = Header("zhangxinyi", 'utf-8')
msg['To'] = Header("1591488713@qq.com", 'utf-8')

#文字部分
message  = MIMEText('i love computer networks', 'plain', 'utf-8')#记得utf-8
msg.attach(message)
 
#附件部分
#jpg类型
jpgmsg=MIMEApplication(open('1.jpg','rb').read())
jpgmsg.add_header('Content-Disposition','attachment',filename="1.jpg")
msg.attach(jpgmsg)
 
try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host, 25) # 25为SMTP端口号
	smtpObj.login(mail_user, mail_pass)
	smtpObj.sendmail(sender, receivers, msg.as_string())
	print("邮件发送成功")
except smtplib.SMTPException:
	print("Error: 无法发送邮件")

