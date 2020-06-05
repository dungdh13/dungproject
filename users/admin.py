from django.contrib import admin
from .models import Profile
from .models import Todo, Router
import csv
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.site_header = "Ban Chỉ Đạo-bvk"
admin.site.site_title = "Bvk Admin Portal"
admin.site.index_title = "Welcome to BvK Portal"


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

class Isbat_thuong(admin.SimpleListFilter):
    title = 'bat_thuong'
    parameter_name = 'bat_thuong'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(Q(ho=True) | Q(sot = True)| Q(dau_hong = True)| Q(met_moi = True)| Q(dau_dau = True)| Q(ret_run = True)| Q(dau_co = True)| Q(non = True)| Q(buon_non = True) | Q(kho_tho = True) | Q(nhiet_do__gt=37.6))
        elif value == 'No':
            return queryset.exclude(Q(ho=True) | Q(sot = True)| Q(dau_hong = True)| Q(met_moi = True)| Q(dau_dau = True)| Q(ret_run = True)| Q(dau_co = True)| Q(non = True)| Q(buon_non = True) | Q(kho_tho = True) | Q(nhiet_do__gt=37.6))
        return queryset


class TodoAdmin(admin.ModelAdmin, ExportCsvMixin):
    readonly_fields = ('created',)
    date_hierarchy = 'created'
    list_display = ['user','Hoten','tt_banthan','khoa_phong','sdt','created','bat_thuong']
    list_filter = ('created',Isbat_thuong)
    search_fields = ['user__profile__Ho_ten','user__username','user__profile__khoa_phong']
    actions = ["export_as_csv"]

    def bat_thuong(self, obj):
        bt = obj.ho or obj.sot or obj.dau_hong or obj.met_moi or obj.dau_dau or obj.ret_run or obj.dau_co or obj.non or obj.buon_non or obj.kho_tho or (obj.nhiet_do >37.6)
        return bt


class ProfileAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['user', 'Ho_ten','khoa_phong','sdt']
    search_fields = ['khoa_phong','Ho_ten']
    actions = ["export_as_csv"]

def make_active(modeladmin, news, queryset):
    queryset.update(is_active=True)
make_active.short_description = u"Kích hoạt tài khoản đã chọn"

def make_deactive(modeladmin, news, queryset):
    queryset.update(is_active=False)
make_deactive.short_description = u"Bỏ kích hoạt tài khoản đã chọn"

class UserAdmin(UserAdmin):
    list_display=('username', 'email', 'is_active', 'date_joined', 'is_staff')
    list_filter =('date_joined','is_active')
    actions = [make_active,make_deactive]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Router)

