sogiolam = float(input("Nhap so gio lam moi tuan:  "))
luong_gio = float(input("Nhap luong tren moi gio lam tieu chuan: "))
giotieuchuan = 44
giovuotchuan = max(0, sogiolam - giotieuchuan)
thuc_linh = giotieuchuan * luong_gio + giovuotchuan * luong_gio *1.5
print(f"So tien thuc linh cua nhan vien:  {thuc_linh}")