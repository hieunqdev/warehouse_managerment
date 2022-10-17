from django.urls import path
from .views import login, home, logout, view_loai_hang, add_loai_hang, delete_loai_hang, update_loai_hang, view_mat_hang, add_mat_hang, delete_mat_hang, update_mat_hang, view_nhan_vien, add_nhan_vien, update_nhan_vien, delete_nhan_vien, view_dia_diem, add_dia_diem, delete_dia_diem, update_dia_diem, view_kho, add_kho, delete_kho, update_kho

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('', home, name='home'),

    #loai hang
    path('view_loai_hang/', view_loai_hang, name='view_loai_hang'),
    path('add_loai_hang/', add_loai_hang, name='add_loai_hang'),
    path('delete_loai_hang/<int:id>', delete_loai_hang, name='delete_loai_hang'),
    path('update_loai_hang/<int:id>', update_loai_hang, name='update_loai_hang'),

    #mat hang
    path('view_mat_hang/', view_mat_hang, name='view_mat_hang'),
    path('add_mat_hang/', add_mat_hang, name='add_mat_hang'), 
    path('delete_mat_hang/<int:id>', delete_mat_hang, name='delete_mat_hang'),
    path('update_mat_hang/<int:id>', update_mat_hang, name='update_mat_hang'),

    #nhan vien
    path('view_nhan_vien/', view_nhan_vien, name='view_nhan_vien'),
    path('add_nhan_vien/', add_nhan_vien, name='add_nhan_vien'),
    path('delete_nhan_vien/<int:id>', delete_nhan_vien, name='delete_nhan_vien'),
    path('update_nhan_vien/<int:id>', update_nhan_vien, name='update_nhan_vien'),

    #dia diem
    path('view_dia_diem', view_dia_diem, name='view_dia_diem'),
    path('add_dia_diem/', add_dia_diem, name='add_dia_diem'),
    path('delete_dia_diem/<int:id>', delete_dia_diem, name='delete_dia_diem'),
    path('update_dia_diem/<int:id>', update_dia_diem, name='update_dia_diem'),

    #kho
    path('view_kho/', view_kho, name='view_kho'),
    path('add_kho/', add_kho, name='add_kho'),
    path('delete_kho/<int:id>', delete_kho, name='delete_kho'),
    path('update_kho/<int:id>', update_kho, name='update_kho'),
]