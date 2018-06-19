# _*_ coding:utf-8 _*_
from email.mime.text import MIMEText
import smtplib
from email.header import Header
from email import encoders
from email.utils import parseaddr,formataddr

def _format_addr(s):
	name,addr=parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))


from_addr='xiao_qiao_love@163.com'
passwd='yzy'
to_addr=['yezeyuan@gzkit.com.cn']
print('From:%s,to:%s' % (from_addr,to_addr))
smtp_server='smtp.163.com'
msg=MIMEText('发邮件给你是想试一下行不行','plain','utf-8')
msg['from'] =_format_addr('yzy学python<%s>' %from_addr)
msg['to'] =_format_addr('yzy公司邮箱<%s>'%to_addr)
msg['Subject'] = Header('自己人发邮件给自己人','utf-8').encode()

server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,passwd)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
