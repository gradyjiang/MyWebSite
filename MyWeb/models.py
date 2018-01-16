from django.db import models

# Create your models here.


class PictureTable(models.Model):
    """
    保存图片路径及图片描述
    """
    picDescription = models.CharField(max_length=256)
    picPath = models.CharField(max_length=256)

    def __str__(self):
        return self.picDescription + " " + self.picPath

