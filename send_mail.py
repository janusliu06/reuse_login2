import os
from django.core.mail import send_mail


# 单独运行本文件
os.environ['DJANGO_SETTINGS_MODULE'] = 'reuse_login.settings'
if __name__ == '__main__':

    for i in range(1):

        send_mail(
            '来自liuyang Django的测试邮件',
            '神TM邮件系统',
            'janusliu06@sina.com',
            ['173330773@qq.com'],
        )