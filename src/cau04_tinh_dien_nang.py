cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("Dien nang tieu thu: ", dien_nang_kwh, "kwh", ", Kieu: ",type(dien_nang_kwh))
print("Chi phi dien: ", chi_phi, "VND", ",Kieu: ",type(chi_phi))
#Du doan
#dien_nang_kwh = 250 * 90 / 60 / 1000 = 0.375
#Kieu du lieu se la float 
#chi_phi = 0.375 * 3000 = 1125.0
#Kieu du lieu se la float 
so_phut = 60
dien_nang_kwh_moi = cong_suat_w * so_phut / 60 / 1000
chi_phi_moi = dien_nang_kwh_moi * don_gia_kwh
print("Dien nang tieu thu moi: ", dien_nang_kwh_moi, "kwh", ", Kieu: ",type(dien_nang_kwh_moi))
print("Chi phi dien moi: ", chi_phi_moi, "VND", ",Kieu: ",type(chi_phi_moi))