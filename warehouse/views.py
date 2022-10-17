from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import loai_hang, mat_hang, nhan_vien, dia_diem, kho

# Create your views here.
# dang nhap, dang xuat
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Đăng nhập thất bại!')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('login')


def home(request):
    if not request.user.is_staff:
        return redirect('login/')

    danh_sach_kho = kho.objects.all()
    answer = 0
    for i in danh_sach_kho:
        answer += 1

    context = {
        'danh_sach_kho': danh_sach_kho,
        'answer': answer
    }
    
    return render(request, 'home.html', context)



# CRUD loai hang
def view_loai_hang(request):
    if not request.user.is_staff:
        return redirect('login/')

    danh_sach_loai_hang = loai_hang.objects.all()
    context = {
        'danh_sach_loai_hang': danh_sach_loai_hang
    }
    return render(request, 'loai_hang.html', context)


def add_loai_hang(request):
    if not request.user.is_staff:
        return redirect('login/')
    
    if request.method == 'POST':
        ma_loai_hang = request.POST['ma_loai_hang']
        ten_loai_hang = request.POST['ten_loai_hang']

        loai_hang.objects.create(ma_loai_hang=ma_loai_hang, ten_loai_hang=ten_loai_hang)
        return redirect('view_loai_hang')

    return render(request, 'add_loai_hang.html')


def delete_loai_hang(request, id):
    if not request.user.is_staff:
        return redirect('login/')

    loai_hang_can_xoa = loai_hang.objects.get(id=id)
    loai_hang_can_xoa.delete()
    return redirect('view_loai_hang')


def update_loai_hang(request, id):
    if not request.user.is_staff:
        return redirect('login/')

    loai_hang_can_cap_nhat = loai_hang.objects.get(id=id)
    context = {
        'loai_hang_can_cap_nhat': loai_hang_can_cap_nhat
    }

    if request.method == 'POST':
        ma_loai_hang = request.POST['ma_loai_hang']
        ten_loai_hang = request.POST['ten_loai_hang']

        loai_hang.objects.filter(pk=id).update(ma_loai_hang=ma_loai_hang, ten_loai_hang=ten_loai_hang)
        return redirect('view_loai_hang')

    
    return render(request, 'update_loai_hang.html', context)


#CRUD mat hang
def view_mat_hang(request):
    if not request.user.is_staff:
        return redirect('login/')

    danh_sach_mat_hang = mat_hang.objects.raw("SELECT id, ma_mat_hang, ten_hang, CASE WHEN (trang_thai='1') THEN 'Còn hàng' ELSE 'Hết hàng' END AS trang_thai FROM mat_hang;")
    context = {
        'danh_sach_mat_hang': danh_sach_mat_hang
    }
    return render(request, 'mat_hang.html', context)


def add_mat_hang(request):
    if not request.user.is_staff:
        return redirect('login/')
    
    danh_sach_loai_hang = loai_hang.objects.all()
    context = {
        'danh_sach_loai_hang': danh_sach_loai_hang
    }
    
    if request.method == 'POST':
        ma_mat_hang = request.POST['ma_mat_hang']
        ma_loai_hang = request.POST['ma_loai_hang']
        ten_hang = request.POST['ten_hang']
        trang_thai = request.POST['trang_thai']

        mat_hang.objects.create(ma_mat_hang=ma_mat_hang, ma_loai_hang_id=ma_loai_hang, ten_hang=ten_hang, trang_thai=trang_thai)
        return redirect('view_mat_hang')

    return render(request, 'add_mat_hang.html', context)


def delete_mat_hang(request, id):
    if not request.user.is_staff:
        return redirect('login/')

    mat_hang_can_xoa = mat_hang.objects.get(id=id)
    mat_hang_can_xoa.delete()
    return redirect('view_mat_hang')


def update_mat_hang(request, id):
    if not request.user.is_staff:
        return redirect('login/')

    mat_hang_can_cap_nhat = mat_hang.objects.get(id=id)
    danh_sach_loai_hang = loai_hang.objects.all()
    context = {
        'mat_hang_can_cap_nhat': mat_hang_can_cap_nhat,
        'danh_sach_loai_hang': danh_sach_loai_hang
    }

    if request.method == 'POST':
        ma_mat_hang = request.POST['ma_mat_hang']
        ma_loai_hang = request.POST['ma_loai_hang']
        ten_hang = request.POST['ten_hang']
        trang_thai = request.POST['trang_thai']

        mat_hang.objects.filter(pk=id).update(ma_mat_hang=ma_mat_hang, ma_loai_hang_id=ma_loai_hang, ten_hang=ten_hang, trang_thai=trang_thai)
        return redirect('view_mat_hang')

    return render(request, 'update_mat_hang.html', context)

# nhan vien
def view_nhan_vien(request):
    if not request.user.is_staff:
        return redirect('login/')

    danh_sach_nhan_vien = nhan_vien.objects.all()
    context = {
        'danh_sach_nhan_vien': danh_sach_nhan_vien
    }
    return render(request, 'nhan_vien.html', context)


def add_nhan_vien(request):
    if not request.user.is_staff:
        return redirect('login/')


    if request.method == 'POST':
        ma_nhan_vien = request.POST['ma_nhan_vien']
        ho_ten = request.POST['ho_ten']
        gioi_tinh = request.POST['gioi_tinh']
        nam_sinh = request.POST['nam_sinh']
        dia_chi = request.POST['dia_chi']
        so_dien_thoai = request.POST['so_dien_thoai']

        nhan_vien.objects.create(ma_nhan_vien=ma_nhan_vien, ho_ten=ho_ten, gioi_tinh=gioi_tinh, nam_sinh=nam_sinh, dia_chi=dia_chi, so_dien_thoai=so_dien_thoai)
        return redirect('view_nhan_vien')

    return render(request, 'add_nhan_vien.html')


def delete_nhan_vien(request, id):
    if not request.user.is_staff:
        return redirect('login/')

    nhan_vien_can_xoa = nhan_vien.objects.get(id=id)
    nhan_vien_can_xoa.delete()
    return redirect('view_nhan_vien')


def update_nhan_vien(request, id):
    if not request.user.is_staff:
        return redirect('login/')

    nhan_vien_can_cap_nhat = nhan_vien.objects.get(id=id)
    context = {
        'nhan_vien_can_cap_nhat': nhan_vien_can_cap_nhat
    }

    if request.method == 'POST':
        ma_nhan_vien = request.POST['ma_nhan_vien']
        ho_ten = request.POST['ho_ten']
        gioi_tinh = request.POST['gioi_tinh']
        nam_sinh = request.POST['nam_sinh']
        dia_chi = request.POST['dia_chi']
        so_dien_thoai = request.POST['so_dien_thoai']

        nhan_vien.objects.filter(pk=id).update(ma_nhan_vien=ma_nhan_vien, ho_ten=ho_ten, gioi_tinh=gioi_tinh, nam_sinh=nam_sinh, dia_chi=dia_chi, so_dien_thoai=so_dien_thoai)
        return redirect('view_nhan_vien')

    return render(request, 'update_nhan_vien.html', context)


# dia diem
def view_dia_diem(request):
    if not request.user.is_staff:
        return redirect('login/')

    danh_sach_dia_diem = dia_diem.objects.all()
    context = {
        'danh_sach_dia_diem': danh_sach_dia_diem
    }

    return render(request, 'dia_diem.html', context)


def add_dia_diem(request):
    if not request.user.is_staff:
        return redirect('login/')
    danh_sach_nhan_vien = nhan_vien.objects.all()
    context = {
        'danh_sach_nhan_vien': danh_sach_nhan_vien
    }

    if request.method == 'POST':
        ma_dia_diem = request.POST['ma_dia_diem']
        ten_dia_diem = request.POST['ten_dia_diem']
        dia_chi_dia_diem = request.POST['dia_chi_dia_diem']
        ma_nhan_vien = request.POST['ma_nhan_vien']

        dia_diem.objects.create(ma_dia_diem=ma_dia_diem, ten_dia_diem=ten_dia_diem, dia_chi_dia_diem=dia_chi_dia_diem, ma_nhan_vien_id=ma_nhan_vien)
        return redirect('view_dia_diem')

    return render(request, 'add_dia_diem.html', context)


def delete_dia_diem(request, id):
    if not request.user.is_staff:
        return redirect('login/')

    dia_diem_can_xoa = dia_diem.objects.get(id=id)
    dia_diem_can_xoa.delete()
    return redirect('view_dia_diem')


def update_dia_diem(request, id):
    if not request.user.is_staff:
        return redirect('login/')

    dia_diem_can_cap_nhat = dia_diem.objects.get(id=id)
    danh_sach_nhan_vien = nhan_vien.objects.all()
    context = {
        'dia_diem_can_cap_nhat': dia_diem_can_cap_nhat,
        'danh_sach_nhan_vien': danh_sach_nhan_vien
    }

    if request.method == 'POST':
        ma_dia_diem = request.POST['ma_dia_diem']
        ten_dia_diem = request.POST['ten_dia_diem']
        dia_chi_dia_diem = request.POST['dia_chi_dia_diem']
        ma_nhan_vien = request.POST['ma_nhan_vien']

        dia_diem.objects.filter(pk=id).update(ma_dia_diem=ma_dia_diem, ten_dia_diem=ten_dia_diem, dia_chi_dia_diem=dia_chi_dia_diem, ma_nhan_vien_id=ma_nhan_vien)
        return redirect('view_dia_diem')

    return render(request, 'update_dia_diem.html', context)


# kho
def view_kho(request):
    if not request.user.is_staff:
        return redirect('login/')

    danh_sach_kho = kho.objects.all()
    context = {
        'danh_sach_kho': danh_sach_kho
    }

    return render(request, 'kho.html', context)


def add_kho(request):
    if not request.user.is_staff:
        return redirect('login/')

    danh_sach_dia_diem = dia_diem.objects.all()
    danh_sach_loai_hang = loai_hang.objects.all()
    danh_sach_nhan_vien = nhan_vien.objects.all()

    context = {
        'danh_sach_dia_diem': danh_sach_dia_diem,
        'danh_sach_loai_hang': danh_sach_loai_hang,
        'danh_sach_nhan_vien': danh_sach_nhan_vien
    }

    if request.method == 'POST':
        ma_kho = request.POST['ma_kho']
        ten_kho = request.POST['ten_kho']
        so_dien_thoai = request.POST['so_dien_thoai']
        ma_dia_diem = request.POST['ma_dia_diem']
        ma_loai_hang = request.POST['ma_loai_hang']
        ma_nhan_vien = request.POST['ma_nhan_vien']

        kho.objects.create(ma_kho=ma_kho, ten_kho=ten_kho, so_dien_thoai=so_dien_thoai, ma_dia_diem_id=ma_dia_diem, ma_loai_hang_id=ma_loai_hang, ma_nhan_vien_id=ma_nhan_vien)
        return redirect('view_kho')

    return render(request, 'add_kho.html', context)


def delete_kho(request, id):
    if not request.user.is_staff:
        return redirect('login/')

    kho_can_xoa = kho.objects.get(id=id)
    kho_can_xoa.delete()
    return redirect('view_kho')

def update_kho(request, id):
    if not request.user.is_staff:
        return redirect('login/')

    kho_can_cap_nhat = kho.objects.get(id=id)
    danh_sach_dia_diem = dia_diem.objects.all()
    danh_sach_loai_hang = loai_hang.objects.all()
    danh_sach_nhan_vien = nhan_vien.objects.all()

    context = {
        'kho_can_cap_nhat': kho_can_cap_nhat,
        'danh_sach_dia_diem':danh_sach_dia_diem,
        'danh_sach_loai_hang': danh_sach_loai_hang,
        'danh_sach_nhan_vien': danh_sach_nhan_vien
    }

    if request.method == 'POST':
        ma_kho = request.POST['ma_kho']
        ten_kho = request.POST['ten_kho']
        so_dien_thoai = request.POST['so_dien_thoai']
        ma_dia_diem = request.POST['ma_dia_diem']
        ma_loai_hang = request.POST['ma_loai_hang']
        ma_nhan_vien = request.POST['ma_nhan_vien']

        kho.objects.filter(pk=id).update(ma_kho=ma_kho, ten_kho=ten_kho, so_dien_thoai=so_dien_thoai, ma_dia_diem_id=ma_dia_diem, ma_loai_hang_id=ma_loai_hang, ma_nhan_vien_id=ma_nhan_vien)
        return redirect('view_kho')

    return render(request, 'update_kho.html', context)


    
