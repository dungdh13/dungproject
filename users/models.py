from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dia_chi = models.CharField(max_length=60,blank = True)
    khoa_phong = models.CharField(max_length=40,blank = True)
    Ho_ten = models.CharField(max_length=40, blank = True)
    sdt = models.BigIntegerField(null= True,blank=True)
    MSBN = models.BigIntegerField(null= True,blank=True)
    cd_benh = models.CharField(max_length=120, blank = True)
    lich_hen_kham = models.DateField(blank=True, null=True)
    class Meta:
        verbose_name_plural = "Thông tin cá nhân"
    def __str__(self):
        return f'Thông tin của {self.user.username}'


class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sot = models.BooleanField(default=False)
    nhiet_do = models.FloatField(default=37 ,null=True)
    ho = models.BooleanField(default=False)
    dau_hong = models.BooleanField(default=False)
    met_moi = models.BooleanField(default=False)
    dau_dau = models.BooleanField(default=False)
    ret_run = models.BooleanField(default=False)
    dau_co = models.BooleanField(default=False)
    non = models.BooleanField(default=False)
    buon_non = models.BooleanField(default=False)
    kho_tho = models.BooleanField(default=False)
    tiepxuc_f0 = models.BooleanField(default=False)
    tiepxuc_f1 = models.BooleanField(default=False)
    vung_dich = models.BooleanField(default=False)
    yeutodichte = models.BooleanField(default=False)
    tt_banthan = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Thông tin sức khỏe"


    @property
    def Hoten(self):
        return self.user.profile.Ho_ten

    @property
    def khoa_phong(self):
        return self.user.profile.khoa_phong

    @property
    def sdt(self):
        return self.user.profile.sdt


    def __str__(self):
        return self.Hoten


class Router(models.Model):
    title = models.CharField(max_length= 150,default='Văn bản chỉ đạo',verbose_name="tiêu đề")
    specifications = models.FileField(upload_to='upload',default="",verbose_name="Upload")
    class Meta:
        verbose_name_plural = "Văn bản chỉ đạo"

    def __str__(self):
        return self.title

