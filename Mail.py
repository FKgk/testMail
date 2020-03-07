from email.mime.text import MIMEText
import smtplib
import re

class WRONG_EMAIL_Error(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

class Mail(object):
    def __init__(self, user, passwd):
        self.USER = user
        self.PASSWD = passwd

        if self.valid(user):
            self.SERVER = "smtp.{}".format(self.USER.split('@')[-1])
            self.PORT = 465

        self.smtp = self.login(self.USER, self.PASSWD)
    
    def login(self, user, passwd):
        smtp = smtplib.SMTP_SSL(self.SERVER, self.PORT)
        smtp.login(user, passwd)
        
        return smtp
    
    def valid(self, addr):
        pattern = '(^[a-zA-Z-0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
        
        if not re.match(pattern, addr):
            raise WRONG_EMAIL_Error("잘못된 이메일 입니다.")
        return True
    
    def send_mail(self, addrs, subject, content):
        msg = MIMEText(content)
        msg['Subject'] = subject
        
        self.smtp.sendmail(self.USER, addrs, msg.as_string())
        
        return True
    
    def close(self):
        self.smtp.close()