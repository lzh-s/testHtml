import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders

class Email():
    def get_email_obj(email_subject,email_from,to_addr_list):
        """
        :param email_subject:邮件主题
        :param email_from:收件人
        :param to_addr_list: 收件人列表
        :return: 邮件对象
        """
        email_obj = MIMEMultipart()
        email_to = ",".join(to_addr_list)#将收件人地址用“，”连接
        #邮件主题、发件人、收件人
        email_obj["Subject"] = Header(email_subject,"utf-8")
        email_obj["From"] = Header(email_from,"utf-8")
        email_obj["To"] = Header(email_to,"utf-8")
        return email_obj

    def attach_content(email_obj,email_content,content_type="plain",charset="utf-8"):
        """

        :param email_content: 邮件正文内容
        :param content_type: 邮件内容格式
        :param charset: 编码格式，默认为utf-8

        """
        content = MIMEText(email_content,content_type,charset)#创建邮件正文对象
        email_obj.attach(content)

    def attach_part(email_obj,source_path,part_name):
        """

        :param source_path: 附件源文件路径
        :param part_name: 附件名
        :return:
        """
        part = MIMEBase("application","octet-stream")
        part.set_payload(open(source_path,"rb").read())#将附件源文件加载到附件对象
        encoders.encode_base64(part)
        part.add_header("Content-Disposition",'attachment;filename="%s"'%part_name)
        email_obj.attach(part)

    def send_email(email_obj,email_host,host_port,from_addr,pwd,to_addr_list):
        """

        :param email_host: SMTP服务器主机
        :param host_port: SMTP服务器端口号
        :param from_addr: 发件地址
        :param pwd: 发件地址的授权码
        :param to_addr_list: 收件地址
        :return: 发送成功，返回True；发送失败，返回False
        """
        try:

            smtp_obj = smtplib.SMTP_SSL(email_host,host_port) #连接邮件服务器
            smtp_obj.login(from_addr,pwd)
            smtp_obj.sendmail(from_addr,to_addr_list,email_obj.as_string())
            smtp_obj.quit()
            print("发送成功！")
            return True
        except smtplib.SMTPException:
              print("发送失败！")
              return False
