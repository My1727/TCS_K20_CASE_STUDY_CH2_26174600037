tong_phut = 135 
cong_suat_w = 250
so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print("So gio: ", so_gio, "gio")
print("So phut con lai: ", so_phut_con_lai, "phut")
su_dung_lau = tong_phut > 60
print("Su dung lau: ", su_dung_lau)
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Du lieu hop le: ", du_lieu_hop_le)
bieu_thuc_1 = 100 + 20 * 3
bieu_thuc_2 = (100 + 20) * 3
# Du đoan: 
# - 100 + 20 * 3 = 100 + 60 = 160 (Nhan truoc, cong sau)
# - (100 + 20) * 3 = 120 * 3 = 360 (Thuc hien trong ngoac truoc)
print("Gia tri bieu thuc 100 + 20 *3 la: ", bieu_thuc_1)
print("Gia tri bieu thuc (100 + 20) * 3 la: ", bieu_thuc_2)