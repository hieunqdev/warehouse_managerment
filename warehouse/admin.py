from django.contrib import admin
from .models import loai_hang, mat_hang, nhan_vien, dia_diem, kho, phieu_nhap_hang, chi_tiet_phieu_nhap, phieu_xuat_hang, chi_tieu_phieu_xuat

# Register your models here.
class loai_hang_admin(admin.ModelAdmin):
    list_display = ['id', 'ma_loai_hang', 'ten_loai_hang']


class mat_hang_admin(admin.ModelAdmin):
    list_display = ['id', 'ma_mat_hang', 'ma_loai_hang', 'ten_hang', 'trang_thai']

class nhan_vien_admin(admin.ModelAdmin):
    list_display = [field.name for field in nhan_vien._meta.fields if field.name]

class dia_diem_admin(admin.ModelAdmin):
    list_display = [field.name for field in dia_diem._meta.fields if field.name]
        

admin.site.register(loai_hang, loai_hang_admin)
admin.site.register(mat_hang, mat_hang_admin)
admin.site.register(nhan_vien, nhan_vien_admin)
admin.site.register(dia_diem, dia_diem_admin)
admin.site.register(kho)
admin.site.register(phieu_nhap_hang)
admin.site.register(chi_tiet_phieu_nhap)
admin.site.register(phieu_xuat_hang)
admin.site.register(chi_tieu_phieu_xuat)