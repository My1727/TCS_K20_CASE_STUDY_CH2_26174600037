from datetime import datetime
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))
# DU DOAN KET QUA PHEP TRU
# bat_dau:  13 gio 15 phut ngay 14/10/2026
# ket_thuc: 15 gio 05 phut ngay 14/10/2026
# Khoang cach thoi gian: 15:05 - 13:15 = 1 gio 50 phut.
# Ket qua in ra man hinh (print(thoi_luong)): 1:50:00
# Kieu du lieu (type(thoi_luong)): <class 'datetime.timedelta'>
# GIAI THICH SU KHAC NHAU
# 1. datetime: bieu dien mot moc thoi gian cu the (gom nam, thang, ngay, gio, phut, giay)
# 2. str: 
#  -Bieu dien thoi gian duoi dang chuoi ky tu (text) de in ra hoac hien thi
#  -Khong the thuc hien cac phep tinh cong/tru thoi gian tren kieu str
# 3. timedelta: Bieu dien khoang thoi gian (do chenh lech/thoi luong) giua hai moc datetime