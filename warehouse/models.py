from django.db import models

# Create your models here.
class loai_hang(models.Model):
    ma_loai_hang = models.CharField(max_length=50)
    ten_loai_hang = models.CharField(max_length=100)

    class Meta:
        db_table = "loai_hang"

    def __str__(self):
        return self.ten_loai_hang

class mat_hang(models.Model):
    lua_chon_trang_thai = (
        ('1', 'Còn hàng'),
        ('0', 'Hết hàng')
    )
    ma_mat_hang = models.CharField(max_length=50)
    ma_loai_hang = models.ForeignKey(loai_hang, on_delete=models.CASCADE)
    ten_hang = models.CharField(max_length=150)
    trang_thai = models.CharField(max_length=10, choices=lua_chon_trang_thai)

    class Meta:
        db_table = "mat_hang"

    def __str__(self):
        return self.ten_hang


class nhan_vien(models.Model):
    LUA_CHON_GIOI_TINH = (
        ('0', 'Nam'),
        ('1', 'Nữ'),
    )
    ma_nhan_vien = models.CharField(max_length=50)
    ho_ten = models.CharField(max_length=50)
    gioi_tinh = models.CharField(max_length=10, choices=LUA_CHON_GIOI_TINH)
    nam_sinh = models.IntegerField()
    dia_chi = models.TextField()
    so_dien_thoai = models.CharField(max_length=50)

    class Meta:
        db_table = "nhan_vien"

    def __str__(self):
        return self.ho_ten



class dia_diem(models.Model):
    ma_dia_diem = models.CharField(max_length=50)
    ten_dia_diem = models.CharField(max_length=100)
    dia_chi_dia_diem = models.TextField()
    ma_nhan_vien = models.ForeignKey(nhan_vien, on_delete=models.CASCADE)

    class Meta:
        db_table = "dia_diem"

    def __str__(self):
        return self.ten_dia_diem


class kho(models.Model):
    ma_kho = models.CharField(max_length=50)
    ten_kho = models.CharField(max_length=50)
    so_dien_thoai = models.CharField(max_length=50)
    ma_dia_diem = models.ForeignKey(dia_diem, on_delete=models.CASCADE)
    ma_loai_hang = models.ForeignKey(loai_hang, on_delete=models.CASCADE)
    ma_nhan_vien = models.ForeignKey(nhan_vien, on_delete=models.CASCADE)

    class Meta:
        db_table = "kho"


class phieu_nhap_hang(models.Model):
    so_phieu_nhap = models.CharField(max_length=50)
    ngay_lap_phieu_nhap = models.DateField()
    ma_kho = models.ForeignKey(kho, on_delete=models.CASCADE)
    ma_nhan_vien = models.ForeignKey(nhan_vien, on_delete=models.CASCADE)

    class Meta:
        db_table = "phieu_nhap_hang"


class chi_tiet_phieu_nhap(models.Model):
    so_phieu_nhap = models.ForeignKey(phieu_nhap_hang, on_delete=models.CASCADE)
    ma_mat_hang = models.ForeignKey(mat_hang, on_delete=models.CASCADE)
    so_luong_nhap = models.FloatField()

    class Meta:
        db_table = "chi_tiet_phieu_nhap"


class phieu_xuat_hang(models.Model):
    so_phieu_xuat = models.CharField(max_length=50)
    ngay_lap_phieu_xuat = models.DateField()
    ma_kho = models.ForeignKey(kho, on_delete=models.CASCADE)
    ma_nhan_vien = models.ForeignKey(nhan_vien, on_delete=models.CASCADE)

    class Meta:
        db_table = "phieu_xuat_hang"


class chi_tieu_phieu_xuat(models.Model):
    so_phieu_xuat = models.ForeignKey(phieu_xuat_hang, on_delete=models.CASCADE)
    ma_mat_hang = models.ForeignKey(mat_hang, on_delete=models.CASCADE)
    so_luong_xuat = models.FloatField()

    class Meta:
        db_table = "chi_tieu_phieu_xuat"
    