from django.db import models

# 试用报告中的单个问题
class User(models.Model) :
    # 主键，由trial_sha1以及标题计算而成
    sha1 = models.CharField(max_length=40, primary_key=True)
    # 试用任务的sha1
    name = models.CharField(max_length=40)
    service = models.CharField(max_length=140)
    class Meta:
        unique_together = ('name','service')