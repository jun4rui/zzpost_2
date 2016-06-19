from django.db import models


# Create your models here.
from django.utils.timezone import now


class OrderInfo(models.Model):
    verbose_name = '订单信息'
    verbose_name_plural = '订单信息'
    senderName = models.CharField(max_length=25, verbose_name='寄件人名称')  # 寄件人名称
    phoneNumber = models.CharField(max_length=25, verbose_name='联系电话')  # 联系电话
    weixinOpenid = models.CharField(max_length=255, verbose_name='微信OPENID', null=True, blank=True)  # 微信openid，暂时不用
    submitTime = models.DateTimeField(default=now, verbose_name='下单时间')  # 寄件人提交订单时间
    fromAddress = models.CharField(max_length=255, verbose_name='取件地址')  # 寄件人地址
    toAddress = models.CharField(max_length=255, verbose_name='收件地址', blank=True)  # 收件人地址
    status = models.CharField(max_length=25, verbose_name='状态', default='post', blank=True)  # 当前订单状态


'''
    def __str__(self):
        return self.fromaddress

    class Meta:
        ordering = ['-submitTime'] #按照时间降序排列
'''
