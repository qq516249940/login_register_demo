import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'login_register_demo.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自外形人的测试邮件', 'xxx@qq.com', 'xxxx@qq.com'
    text_content = '欢迎访问xxxx网站，这里是外星人的博客和教程站点，专注于Python和Django技术的分享！'
    html_content = '<p>欢迎访问<a href="http://www.baidu.com" target=blank>www.baidu.com</a>，这里是外星人的博客和教程站点，本站专注于Python、Django和机器学习技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()