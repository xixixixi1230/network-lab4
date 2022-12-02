import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.qq.com" # 设置服务器
mail_user = "1591488713@qq.com" #用户名
mail_pass = "iutxqcrshxwkbafb" #STMP口令，不是密码
 
sender = '1591488713@qq.com'
receivers = ["zhangxinyi11111111@163.com"] #接受者的邮箱

message  = MIMEText('i love computer networks', 'plain', 'utf-8')#记得utf-8
message['From'] = Header("zhangxinyi", 'utf-8')
message['To'] = Header("1591488713@qq.com", 'utf-8')
 
subject = '邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host, 25) # 25为SMTP端口号
	smtpObj.login(mail_user, mail_pass)
	smtpObj.sendmail(sender, receivers, message.as_string())
	print("邮件发送成功")
except smtplib.SMTPException:
	print("Error: 无法发送邮件")

