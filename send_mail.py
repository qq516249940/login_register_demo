import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'login_register_demo.settings'

if __name__ == '__main__':   

    send_mail(
        '来自地球外星人的测试邮件',
        '欢迎访问教程站点，本站专注于Python、Django和机器学习技术的分享！',
        'xxxx@qq.com',
        ['xxxx@qq.com'],
    )