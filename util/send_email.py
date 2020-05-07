import smtplib
from email.mime.text import MIMEText

class SendEmail:

    global send_user
    global email_host
    global password
    email_host = 'smtp.163.com'
    send_user = 'whd3322@163.com'
    password = 'DTMTYVGYBNMQKRGP'

    def send_mail(self,user_list,sub,content=None):
        user = 'wangdoudou'+'<'+send_user+'>'
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        # message['To'] = ';'.join(user_list)
        message['To'] = ';'.join('%s' % id for id in user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

    def send_main(self,pass_list,fail_list,skip_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        skip_num = float(len(skip_list))
        content_num = pass_num+fail_num+skip_num
        # 通过率
        pass_result = "%.2f%%" %(pass_num/content_num*100)
        # 失败率
        fail_result = "%.2f%%" %(fail_num/content_num*100)


        user_list = ['985680615@qq.com']
        sub = "接口自动化测试报告"
        content = "此处共运行接口个数为%s个，通过个数为%s个，失败个数为%s个，跳过个数为%s个，通过率为%s,失败" \
                  "率为%s" %(content_num,pass_num,fail_num,skip_num,pass_result,fail_result)
        self.send_mail(user_list,sub,content)


if __name__ == '__main__':
    sen = SendEmail()
    sen.send_main([1,2,3],[5,6,7,8,9],[0])