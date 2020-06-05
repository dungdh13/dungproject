from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, Todo
from django.forms import ModelForm


class UserLoginForm(AuthenticationForm):

    username= forms.CharField(label="Tên Đăng Nhập")
    password= forms.CharField(max_length=32, widget=forms.PasswordInput,label="Mật khẩu")
    class Meta:
        model = User
        fields =['username', 'password']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Địa chỉ email")
    username= forms.CharField(label="Tên Đăng Nhập")
    password1= forms.CharField(max_length=32, widget=forms.PasswordInput,label="Mật khẩu")
    password2= forms.CharField(max_length=32, widget=forms.PasswordInput,label="Xác nhận mật khẩu")
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields =['email']


class ProfileUpdateForm(forms.ModelForm):
    Ho_ten = forms.CharField(label="Họ và tên:",max_length=30, required=False)
    sdt = forms.IntegerField(label="Số điện thoại", max_value=1000000000000000, required=False)
    khoa_phong = forms.CharField(label="Khoa phòng:",max_length=30, required=False)
    dia_chi = forms.CharField(label="Địa chỉ:",max_length=100,required=False)
    MSBN = forms.IntegerField(label="Mã số bệnh nhân(Phần dành riêng cho bệnh nhân và người nhà bệnh nhân)", max_value = 1000000000000000, required=False)
    cd_benh = forms.CharField(label="Chẩn đoán bệnh(Phần dành riêng cho bệnh nhân và người nhà bệnh nhân)",max_length=150, required=False)
    lich_hen_kham = forms.DateField(label="Lịch hẹn khám(Phần dành riêng cho bệnh nhân và người nhà bệnh nhân)",required=False)
    class Meta:
        model = Profile
        fields =['Ho_ten','sdt','khoa_phong','dia_chi','MSBN','cd_benh','lich_hen_kham']




class TodoForm(ModelForm):
    class Meta:
        model = Todo
        localized_fields = '__all__'
        fields = ['sot', 'nhiet_do','ho', 'kho_tho','dau_hong', 'met_moi','dau_dau','ret_run','dau_co','non','buon_non', 'tiepxuc_f0','tiepxuc_f1','yeutodichte','vung_dich','tt_banthan']