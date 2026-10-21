ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))  # Sua loi 1: Ep kieu float
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")   # Sua loi 2: Đung ten bien & Sua loi 3: Them ngoac đong )
# LAN CHAY 1:
# src/cau07_chan_doan_loi.py, dong 6, SyntaxError: '(' was never closed
# Nguyen nhan: Ham print() o cuoi bi thieu dau đong ngoac tron ')'
# Cach khac phuc: Them dau ')' vao cuoi cau lenh.
# LAN CHAY 2:
# src/cau07_chan_doan_loi.py, dong 4, TypeError: unsupported operand type(s) for /: 'str' and 'int
# Nguyen nhan: cong_suat_w nhap tu input() co kieu chuoi (str), khong the dung cho phep tinh nhan/chia
# Cach khac phuc: Bo sung float() de ep kieu du lieu sang so thuc
# LAN CHAY 3:
# src/cau07_chan_doan_loi.py, dong 6, NameError: name 'dien_nang' is not defined
# Nguyen nhan: Goi ten dien_nang khong ton tai
# Cach khac phuc: Doi 'dien_nang' thanh 'dien_nang_kwh'
# CAC LOI DA PHAT HIEN
# Loi TypeError: Tai dong 2 cong_suat_w chua chuyen sang float(), gay loi phep tinh o dong 5.
# Loi NameError va SyntaxError tai dong 7 do dung sai ten bien 'dien_nang' va thieu ngoac ')' cuoi print()# Cap nhat phien ban v2
