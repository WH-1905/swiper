'''
第三方配置
'''

# 互亿无线短信配置
HY_SMS_URL = 'https://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_SMS_PRAMS = {
    'account':'C12422751',
    'password':'cacc2d709203aedc3f6fdac1fa2584f3',
    'content':'您的验证码是：%s。请不要把验证码泄露给其他人。',
    'mobile':None,
    'format':'json '
}