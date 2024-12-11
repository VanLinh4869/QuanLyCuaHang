import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime

# danh sach dữ lieu
danh_sach_nhan_vien = []
drink_list = []
invoice_list = []

danh_sach_nhan_vien.extend([
        {"Mã Nhân Viên": "NV001", "Tên Nhân Viên": "Nguyễn Văn A", "Số Điện Thoại": "0123456789",
         "Số Lượng Bán": 0},
        {"Mã Nhân Viên": "NV002", "Tên Nhân Viên": "Trần Thị B", "Số Điện Thoại": "0987654321",
         "Số Lượng Bán": 0},
        {"Mã Nhân Viên": "NV003", "Tên Nhân Viên": "Lê Quang C", "Số Điện Thoại": "0934123456",
         "Số Lượng Bán": 0}
    ])

drink_list.extend([
        {"Mã Giầy Dép": "GD001", "Tên Giầy Dép": "Giày Nữ ", "Giá Giầy Dép(VNĐ)": "300000","Số Lượng":"1000"},
        {"Mã Giầy Dép": "GD002", "Tên Giầy Dép": "Giày Thể Thao C", "Giá Giầy Dép(VNĐ)": "400000","Số Lượng":"1000"},
        {"Mã Giầy Dép": "GD003", "Tên Giầy Dép": "Giày Nam", "Giá Giầy Dép(VNĐ)": "300000","Số Lượng":"1000"},
        {"Mã Giầy Dép": "GD004", "Tên Giầy Dép": "Giày Quai Hậu ", "Giá Giầy Dép(VNĐ)": "350000","Số Lượng":"1000"},
        {"Mã Giầy Dép": "GD005", "Tên Giầy Dép": "Dép Lê ", "Giá Giầy Dép(VNĐ)": "370000","Số Lượng":"1000"},
        {"Mã Giầy Dép": "GD006", "Tên Giầy Dép": "Đép Quai Kẹp", "Giá Giầy Dép(VNĐ)": "330000","Số Lượng":"1000"},
        {"Mã Giầy Dép": "GD007", "Tên Giầy Dép": "Dép Nam Nữ", "Giá Giầy Dép(VNĐ)": "450000","Số Lượng":"1000"},
    ])

def set_centered_window(width, height):
    # Lấy kích thước màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Tính toán tọa độ để căn giữa
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Đặt kích thước và vị trí cửa sổ
    root.geometry(f"{width}x{height}+{x}+{y}")

# Nhân Viên
def xoa_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Hàm xóa các widget trong frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Hàm chính để quay lại màn hình chính
def quay_lai(HienThi_frame):
    clear_frame(HienThi_frame)
    hien_thi_giao_dien_chinh(HienThi_frame)  # Gọi lại màn hình chính


def hien_thi_giao_dien_chinh(HienThi_frame):
    clear_frame(HienThi_frame)

    # Hiển thị tiêu đề màn hình chính
    tk.Label(HienThi_frame, text="Giao Diện Chính", font=("Arial Black", 20), fg="#ff4500", bg="lightblue", relief="groove",
             bd=9).pack(pady=20)

    # Các nút chuyển đến các màn hình khác
    tk.Button(HienThi_frame, text="Nhân Viên",font=("Arial Black", 20), width=20, height=2, bg="#bfecff",fg="#0000cd",
              command=lambda: hien_thi_nhan_vien(HienThi_frame)).pack(padx=20, pady=10, fill='x')
    tk.Button(HienThi_frame, text="Kho",font=("Arial Black", 20), width=20, height=2, bg="#80d9ff",fg="#0000cd",
              command=lambda: hien_thi_giay_dep(HienThi_frame)).pack(padx=20, pady=10, fill='x')
    tk.Button(HienThi_frame, text="Hoá Đơn",font=("Arial Black", 20), width=20, height=2, bg="#004766",fg="#0000cd",
              command=lambda: hien_thi_hoa_don(HienThi_frame)).pack(padx=20, pady=10, fill='x')
    tk.Button(HienThi_frame, text="Tính Doanh Thu",font=("Arial Black", 20), width=20, height=2, bg="#003247",fg="#0000cd",
              command=lambda: hien_thi_doanh_thu(HienThi_frame)).pack(padx=20, pady=10, fill='x')



# Quản Lý Nhân Viên
def hien_thi_nhan_vien(HienThi_frame):
    xoa_frame(HienThi_frame)
    tk.Label(HienThi_frame, text="Quản Lý Nhân Viên", font=("Arial", 17, "bold"), fg="blue", bg="lightyellow", relief="groove", bd=9).grid(row=0, column=0, columnspan=4, pady=10)

    MaNV = tk.Entry(HienThi_frame)
    TenNV = tk.Entry(HienThi_frame)
    SdtNV = tk.Entry(HienThi_frame)
    TimNV = tk.Entry(HienThi_frame)

    tk.Label(HienThi_frame, text="Mã Nhân Viên:", relief="solid", bd=2,font=("Times New Roman", 13)).grid(row=1, column=0, pady=5)
    MaNV.grid(row=1, column=1, pady=5)

    tk.Label(HienThi_frame, text="Họ Tên Nhân Viên:", relief="solid", bd=2,font=("Times New Roman", 13)).grid(row=2, column=0, pady=5)
    TenNV.grid(row=2, column=1, pady=5)

    tk.Label(HienThi_frame, text="Số Điện Thoại:", relief="solid", bd=2,font=("Times New Roman", 13)).grid(row=3, column=0, pady=5)
    SdtNV.grid(row=3, column=1, pady=5)


    danh_sach_nhan_vien_listbox = tk.Listbox(HienThi_frame, width=150, height=20)
    danh_sach_nhan_vien_listbox.grid(row=6, column=0, columnspan=4, pady=10)

    scrollbar = tk.Scrollbar(HienThi_frame, orient=tk.VERTICAL, command=danh_sach_nhan_vien_listbox.yview)
    scrollbar.grid(row=6, column=4, sticky='ns')  # Đặt Scrollbar bên cạnh Listbox

    danh_sach_nhan_vien_listbox.config(yscrollcommand=scrollbar.set)  # Kết nối Listbox với Scrollbar

    def cap_nhat_danh_sach_nhan_vien(Nhap_Vao=""):
        danh_sach_nhan_vien_listbox.delete(0, tk.END)
        for nhan_vien in danh_sach_nhan_vien:
            thong_tin_nhan_vien = f"Mã NV-: {nhan_vien['Mã Nhân Viên']} | Tên Nhân Viên-: {nhan_vien['Tên Nhân Viên']} | " \
                                  f"SĐT-: {nhan_vien['Số Điện Thoại']} | Số Lượng Bán-: {nhan_vien['Số Lượng Bán']}"
            if Nhap_Vao.lower() in thong_tin_nhan_vien.lower():
                danh_sach_nhan_vien_listbox.insert(tk.END, thong_tin_nhan_vien)

    def them_nhan_vien():
        if not MaNV.get() or not TenNV.get() or not SdtNV.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin nhân viên!")
            return
        danh_sach_nhan_vien.append({
            "Mã Nhân Viên": MaNV.get(),
            "Tên Nhân Viên": TenNV.get(),
            "Số Điện Thoại": SdtNV.get(),
            "Số Lượng Bán": 0})
        cap_nhat_danh_sach_nhan_vien()
        MaNV.delete(0, tk.END)
        TenNV.delete(0, tk.END)
        SdtNV.delete(0, tk.END)

        messagebox.showinfo("Thành Công", "Nhân Viên đã được thêm!")

    def xoa_nhan_vien():
        nv_chon_xoa = danh_sach_nhan_vien_listbox.curselection()
        if nv_chon_xoa:
            nhan_vien_cho_chon = danh_sach_nhan_vien[nv_chon_xoa[0]]
            danh_sach_nhan_vien.remove(nhan_vien_cho_chon)
            cap_nhat_danh_sach_nhan_vien()
            messagebox.showinfo("Thành Công", "Nhân viên đã được xóa!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn nhân viên để xóa!")

    def sua_nhan_vien():
        nv_chon_sua = danh_sach_nhan_vien_listbox.curselection()
        if nv_chon_sua:
            nhan_vien_cho_chon = danh_sach_nhan_vien[nv_chon_sua[0]]
            nhan_vien_cho_chon['Mã Nhân Viên'] = MaNV.get()
            nhan_vien_cho_chon['Tên Nhân Viên'] = TenNV.get()
            nhan_vien_cho_chon['Số Điện Thoại'] = SdtNV.get()

            cap_nhat_danh_sach_nhan_vien()
            messagebox.showinfo("Thành Công", "Nhân viên đã được sửa!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn nhân viên để sửa!")

    def tinh_luong_nhan_vien():
        nv_chon_tl = danh_sach_nhan_vien_listbox.curselection()
        if nv_chon_tl:
            nhan_vien_cho_chon = danh_sach_nhan_vien[nv_chon_tl[0]]
            so_luong_ban = nhan_vien_cho_chon['Số Lượng Bán']
            luongcb = 6000000
            thuong = 0.15 * luongcb if so_luong_ban > 1000 else 0.1 * luongcb if so_luong_ban > 300 else 0.05 * luongcb if so_luong_ban > 100 else 0
            tong_luong = luongcb + thuong
            messagebox.showinfo("Lương Nhân Viên", f"Lương của {nhan_vien_cho_chon['Tên Nhân Viên']} là: {tong_luong:,} VND")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn nhân viên để tính lương!")

    def tim_kiem_nhan_vien():
        # Tạo cửa sổ con để nhập mã nhân viên
        def tim_kiem_popup():
            # Cửa sổ con
            tim_popup = tk.Toplevel(HienThi_frame)
            tim_popup.title("Tìm Kiếm Nhân Viên")

            tk.Label(tim_popup, text="Nhập Mã Nhân Viên để tìm:", font=("Times New Roman", 13)).grid(row=0, column=0, padx=10, pady=5)
            tim_entry = tk.Entry(tim_popup, font=("Times New Roman", 13))
            tim_entry.grid(row=0, column=1, padx=10, pady=5)

            def tim_kiem_nhan_vien_gui():
                ma_nhan_vien = tim_entry.get()
                danh_sach_nhan_vien_khop = [nhan_vien for nhan_vien in danh_sach_nhan_vien if
                                            ma_nhan_vien.lower() in nhan_vien['Mã Nhân Viên'].lower()]
                if not danh_sach_nhan_vien_khop:
                    messagebox.showinfo("Thông Báo", "Mã Nhân Viên không tồn tại!")
                else:
                    danh_sach_nhan_vien_listbox.delete(0, tk.END)
                    for nhan_vien in danh_sach_nhan_vien_khop:
                        thong_tin_nhan_vien = f"Mã NV-: {nhan_vien['Mã Nhân Viên']} | Tên Nhân Viên-: {nhan_vien['Tên Nhân Viên']} | " \
                                              f"SĐT-: {nhan_vien['Số Điện Thoại']} | Số Lượng Bán-: {nhan_vien['Số Lượng Bán']}"
                        danh_sach_nhan_vien_listbox.insert(tk.END, thong_tin_nhan_vien)

            tk.Button(tim_popup, text="Tìm Kiếm", command=tim_kiem_nhan_vien_gui, font=("Times New Roman", 13)).grid(row=1, column=0, columnspan=2, pady=10)

        tim_kiem_popup()


    tk.Button(HienThi_frame, text="Thêm Nhân Viên", command=them_nhan_vien, width=20, height=2, bg="#98a77c",font=("Times New Roman", 13)).grid(row=7, column=0, padx=10, pady=10, sticky="nsew")
    tk.Button(HienThi_frame, text="Xóa Nhân Viên", command=xoa_nhan_vien, width=20, height=2, bg="#98a77c",font=("Times New Roman", 13)).grid(row=7, column=1, padx=10, pady=10, sticky="nsew")
    tk.Button(HienThi_frame, text="Sửa Nhân Viên", command=sua_nhan_vien, width=20, height=2, bg="#98a77c",font=("Times New Roman", 13)).grid(row=7, column=2, padx=10, pady=10, sticky="nsew")
    tk.Button(HienThi_frame, text="Tìm Kiếm", command=tim_kiem_nhan_vien, width=20, height=2, bg="#98a77c",font=("Times New Roman", 13)).grid(row=7, column=3, padx=10, pady=10, sticky="nsew")
    tk.Button(HienThi_frame, text="Tính Lương", command=tinh_luong_nhan_vien, width=20, height=2, bg="#98a77c",font=("Times New Roman", 13)).grid(row=8, column=0, padx=10, pady=10, sticky="nsew")
    tk.Button(HienThi_frame, text="Quay lại", command=lambda: quay_lai(HienThi_frame), width=20, height=2,bg="#e7f5dc",font=("Times New Roman", 13)).grid(row=8, column=1, padx=10, pady=10, sticky="nsew")

    cap_nhat_danh_sach_nhan_vien()


# Giầy Dép
def hien_thi_giay_dep(HienThi_frame):
    xoa_frame(HienThi_frame)
    tk.Label(HienThi_frame, text="Quản Lý Kho", font=("Arial black", 20, "bold"), fg="blue", bg="lightyellow", relief="groove", bd=9).grid(row=0, column=0, columnspan=4, pady=10)

    Magiay = tk.Entry(HienThi_frame)
    TenGiay = tk.Entry(HienThi_frame)
    GiaGiay = tk.Entry(HienThi_frame)
    SoLuong = tk.Entry(HienThi_frame)
    TimMaGiay = tk.Entry(HienThi_frame)

    tk.Label(HienThi_frame, text="Mã Giầy Dép:", relief="solid", bd=2, font=("Times New Roman", 13)).grid(row=1, column=0, pady=5)
    Magiay.grid(row=1, column=1, pady=5)

    tk.Label(HienThi_frame, text="Tên Giầy Dép:", relief="solid", bd=2, font=("Times New Roman", 13)).grid(row=2, column=0, pady=5)
    TenGiay.grid(row=2, column=1, pady=5)

    tk.Label(HienThi_frame, text="Giá Giầy Dép (VNĐ):", relief="solid", bd=2, font=("Times New Roman", 13)).grid(row=3, column=0, pady=5)
    GiaGiay.grid(row=3, column=1, pady=5)

    tk.Label(HienThi_frame, text="Số Lượng:", relief="solid", bd=2, font=("Times New Roman", 13)).grid(row=4, column=0, pady=5)
    SoLuong.grid(row=4, column=1, pady=5)

    danh_sach_giay_Dep = tk.Listbox(HienThi_frame, width=150, height=20)
    danh_sach_giay_Dep.grid(row=6, column=0, columnspan=5, pady=10)

    scrollbar = tk.Scrollbar(HienThi_frame, orient=tk.VERTICAL, command=danh_sach_giay_Dep.yview)
    scrollbar.grid(row=6, column=5, sticky='ns')  # Đặt Scrollbar bên cạnh Listbox

    danh_sach_giay_Dep.config(yscrollcommand=scrollbar.set)  # Kết nối Listbox với Scrollbar

    def cap_nhat_danh_sach_Giay_Dep():
        danh_sach_giay_Dep.delete(0, tk.END)  # Xóa các mục cũ
        for Giay_Dep in drink_list:
            try:
                gia_Giay_Dep = float(Giay_Dep['Giá Giầy Dép(VNĐ)'])
                gia_Giay_Dep = "{:,.0f}".format(gia_Giay_Dep).replace(",", ".")
            except ValueError:
                gia_Giay_Dep = "Không hợp lệ"
            danh_sach_giay_Dep.insert(
                tk.END,
                f"Mã Giầy Dép: {Giay_Dep['Mã Giầy Dép']} | Tên Giầy Dép: {Giay_Dep['Tên Giầy Dép']} | Giá Giầy Dép: {gia_Giay_Dep} VNĐ | Số Lượng: {Giay_Dep['Số Lượng']}"
            )

    def them_Giay_Dep():
        if not Magiay.get() or not TenGiay.get() or not GiaGiay.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin Giầy Dép!")
            return
        try:
            int(GiaGiay.get())  # Kiểm tra giá trị nhập vào là số
        except ValueError:
            messagebox.showerror("Lỗi", "Giá Giầy Dép phải là số!")
            return

        drink_list.append({
            "Mã Giầy Dép": Magiay.get(),
            "Tên Giầy Dép": TenGiay.get(),
            "Giá Giầy Dép(VNĐ)": GiaGiay.get()
        })
        cap_nhat_danh_sach_Giay_Dep()

        Magiay.delete(0, tk.END)
        TenGiay.delete(0, tk.END)
        GiaGiay.delete(0, tk.END)

        messagebox.showinfo("Thành Công", "Giầy Dép Đã Được Thêm!")

    def xoa_Giay_Dep():
        selected_index = danh_sach_giay_Dep.curselection()
        if not selected_index:
            messagebox.showerror("Lỗi", "Vui lòng chọn Giầy Dép để xóa!")
            return
        selected_drink = drink_list[selected_index[0]]
        drink_list.remove(selected_drink)
        cap_nhat_danh_sach_Giay_Dep()
        messagebox.showinfo("Thành Công", "Giầy Dép đã được xóa!")

    def sua_Giay_Dep():
        selected_index = danh_sach_giay_Dep.curselection()
        if selected_index:
            selected_drink = drink_list[selected_index[0]]
            selected_drink['Mã Giầy Dép'] = Magiay.get()
            selected_drink['Tên Giầy Dép'] = TenGiay.get()
            selected_drink['Giá Giầy Dép(VNĐ)'] = GiaGiay.get()
            cap_nhat_danh_sach_Giay_Dep()
            messagebox.showinfo("Thành Công", "Giầy Dép đã được sửa!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn Giầy Dép để sửa!")

    def tim_kiem_Giay_Dep():
        # Tạo cửa sổ con để tìm kiếm
        def tim_kiem_popup():
            tim_popup = tk.Toplevel(HienThi_frame)
            tim_popup.title("Tìm Kiếm Giầy Dép")

            tk.Label(tim_popup, text="Nhập Mã Giầy Dép để Tìm:", font=("Times New Roman", 13)).grid(row=0, column=0, padx=10, pady=5)
            tim_entry = tk.Entry(tim_popup, font=("Times New Roman", 13))
            tim_entry.grid(row=0, column=1, padx=10, pady=5)

            def tim_kiem_nhan_vien_gui():
                ma_giay_dep = tim_entry.get()
                giay_dep_khop = [giay_dep for giay_dep in drink_list if ma_giay_dep.lower() in giay_dep['Mã Giầy Dép'].lower()]
                if not giay_dep_khop:
                    messagebox.showinfo("Thông Báo", "Mã Giầy Dép không tồn tại!")
                else:
                    danh_sach_giay_Dep.delete(0, tk.END)
                    for giay_dep in giay_dep_khop:
                        gia_Giay_Dep = float(giay_dep['Giá Giầy Dép(VNĐ)'])
                        gia_Giay_Dep = "{:,.0f}".format(gia_Giay_Dep).replace(",", ".")
                        danh_sach_giay_Dep.insert(tk.END, f"Mã Giầy Dép: {giay_dep['Mã Giầy Dép']} | Tên Giầy Dép: {giay_dep['Tên Giầy Dép']} | Giá: {gia_Giay_Dep} VNĐ")

            tk.Button(tim_popup, text="Tìm Kiếm", command=tim_kiem_nhan_vien_gui, font=("Times New Roman", 13)).grid(row=1, column=0, columnspan=2, pady=10)

        tim_kiem_popup()

    # Các nút chức năng
    tk.Button(HienThi_frame, text="Thêm Giầy Dép", command=them_Giay_Dep, width=20, height=2, bg="#98a77c", font=("Times New Roman", 13)).grid(row=8, column=0, padx=10, pady=10, sticky="e")
    tk.Button(HienThi_frame, text="Xóa Giầy Dép", command=xoa_Giay_Dep, width=20, height=2, bg="#98a77c", font=("Times New Roman", 13)).grid(row=8, column=1, padx=10, pady=10, sticky="e")
    tk.Button(HienThi_frame, text="Sửa Giầy Dép", command=sua_Giay_Dep, width=20, height=2, bg="#98a77c", font=("Times New Roman", 13)).grid(row=8, column=2, padx=10, pady=10, sticky="e")
    tk.Button(HienThi_frame, text="Tìm Kiếm Giầy Dép", command=tim_kiem_Giay_Dep, width=20, height=2, bg="#98a77c", font=("Times New Roman", 13)).grid(row=8, column=3, padx=10, pady=10, sticky="e")
    tk.Button(HienThi_frame, text="Quay lại", command=lambda: quay_lai(HienThi_frame), width=20, height=2, bg="#e7f5dc", font=("Times New Roman", 13)).grid(row=9, column=0, padx=10, pady=10, sticky="e")

    cap_nhat_danh_sach_Giay_Dep()

# Hoá Đơn
def hien_thi_hoa_don(HienThi_frame):
    clear_frame(HienThi_frame)
    tk.Label(HienThi_frame, text="Quản Lý Hoá Đơn Bán Hàng", font=("Arial", 17, "bold"), fg="blue", bg="lightyellow", relief="groove", bd=9).grid(row=0, column=0, columnspan=4, pady=10)

    ten_khach_hang = tk.Entry(HienThi_frame)
    tk.Label(HienThi_frame, text="Tên Khách Hàng:", relief="solid", bd=2,font=("Times New Roman", 13)).grid(row=1, column=0, pady=5)
    ten_khach_hang.grid(row=1, column=1, pady=5)

    nhan_vien_combobox = ttk.Combobox(HienThi_frame, values=[nv["Mã Nhân Viên"] for nv in danh_sach_nhan_vien])
    tk.Label(HienThi_frame, text="Chọn Nhân Viên:", relief="solid", bd=2,font=("Times New Roman", 13)).grid(row=2, column=0, pady=5)
    nhan_vien_combobox.grid(row=2, column=1, pady=5)

    tk.Label(HienThi_frame, text="Chọn Giầy Dép:", relief="solid", bd=2,font=("Times New Roman", 13)).grid(row=3, column=0, pady=5)
    giay_dep_listbox = tk.Listbox(HienThi_frame, selectmode=tk.MULTIPLE, width=40, height=6)
    giay_dep_listbox.grid(row=3, column=1, pady=5)
    for tu in drink_list:
        giay_dep_listbox.insert(tk.END, tu["Tên Giầy Dép"])

    tk.Label(HienThi_frame, text="Số Lượng (phân cách bằng dấu phẩy):", relief="solid", bd=2,font=("Times New Roman", 13)).grid(row=4, column=0, pady=5)
    so_luong_entry = tk.Entry(HienThi_frame)
    so_luong_entry.grid(row=4, column=1, pady=5)

    ngay_hoa_don = DateEntry(HienThi_frame, date_pattern="yyyy-mm-dd")
    tk.Label(HienThi_frame, text="Ngày Lập Hóa Đơn:", relief="solid",font=("Times New Roman", 13)).grid(row=1, column=2, pady=5)
    ngay_hoa_don.grid(row=2, column=2, pady=5)

    ma_giam_gia = ["GIAM10", "GIAM20", "GIAM30"]
    ma_giam_gia_combobox = ttk.Combobox(HienThi_frame, values=ma_giam_gia)
    ma_giam_gia_combobox.set("Chọn mã giảm giá")
    tk.Label(HienThi_frame, text="Mã Giảm Giá:", relief="solid", bd=2,font=("Times New Roman", 13)).grid(row=5, column=0, pady=5)
    ma_giam_gia_combobox.grid(row=5, column=1, pady=5)

    danh_sach_hoa_don_listbox = tk.Listbox(HienThi_frame, width=150, height=20)
    danh_sach_hoa_don_listbox.grid(row=6, column=0, columnspan=4, pady=10)

    def cap_nhat_danh_sach_hoa_don():
        danh_sach_hoa_don_listbox.delete(0, tk.END)
        for hoa_don in invoice_list:
            chi_tiet = ", ".join(f"{tu['Giầy Dép']} ({tu['Số Lượng B']}x {tu['Giá Giầy Dép(VNĐ)']:,} VNĐ)" for tu in hoa_don['Chi Tiết Giầy Dép'])
            tong_tien_dinh_dang = "{:,.0f}".format(hoa_don['Tổng Tiền']).replace(",", ".")
            danh_sach_hoa_don_listbox.insert(
                tk.END,
                f"Khách Hàng: {hoa_don['Tên Khách Hàng']} | NV: {hoa_don['Nhân Viên']} | "
                f"Giầy Dép : {chi_tiet} | Tổng Tiền : {tong_tien_dinh_dang} VNĐ | Giảm Giá: {hoa_don['Giảm Giá']}% |"
                f"Ngày Lập: {hoa_don['Ngày Lập']}"
            )

    def them_hoa_don():
        khach_hang = ten_khach_hang.get()
        nhan_vien = nhan_vien_combobox.get()
        selected_items = giay_dep_listbox.curselection()
        so_luong_text = so_luong_entry.get()
        ma_giam = ma_giam_gia_combobox.get()
        ngay = ngay_hoa_don.get()

        if khach_hang and nhan_vien and selected_items and so_luong_text:
            try:
                so_luong = list(map(int, so_luong_text.split(',')))
                if len(so_luong) != len(selected_items):
                    messagebox.showerror("Lỗi", "Số lượng không khớp với số hàng được chọn!")
                    return

                chi_tiet_Giay_Dep = []
                tong_tien = 0

                for i, idx in enumerate(selected_items):
                    ten_Giay_Dep = giay_dep_listbox.get(idx)  # Lấy tên Giay_Dep từ Listbox
                    Giay_Dep = next((tu for tu in drink_list if tu['Tên Giầy Dép'] == ten_Giay_Dep), None)
                    if not Giay_Dep:
                        continue
                    sl = so_luong[i]
                    gia = int(Giay_Dep['Giá Giầy Dép(VNĐ)'])
                    tong_tien += sl * gia
                    chi_tiet_Giay_Dep.append({
                        "Giầy Dép": Giay_Dep['Tên Giầy Dép'],
                        "Số Lượng B": sl,
                        "Giá Giầy Dép(VNĐ)": gia
                    })

                    # Cập nhật số lượng của giày dép trong danh sách sau khi bán
                    if int(Giay_Dep['Số Lượng']) >= sl:  # Chuyển 'Số Lượng' thành int
                        Giay_Dep['Số Lượng'] = str(int(Giay_Dep['Số Lượng']) - sl)  # Cập nhật số lượng
                    else:
                        messagebox.showerror("Lỗi", f"Số lượng giày dép {Giay_Dep['Tên Giầy Dép']} không đủ để bán!")
                        return

                # Áp dụng giảm giá nếu có
                giam_gia = int(ma_giam.replace("GIAM", "")) if ma_giam in ma_giam_gia else 0
                tong_tien -= tong_tien * giam_gia / 100

                # Thêm hóa đơn vào danh sách
                invoice_list.append({
                    "Tên Khách Hàng": khach_hang,
                    "Nhân Viên": nhan_vien,
                    "Chi Tiết Giầy Dép": chi_tiet_Giay_Dep,
                    "Tổng Tiền": tong_tien,
                    "Giảm Giá": giam_gia,
                    "Ngày Lập": ngay
                })

                # Cập nhật số lượng bán của nhân viên
                for nv in danh_sach_nhan_vien:
                    if nv['Mã Nhân Viên'] == nhan_vien:
                        nv['Số Lượng Bán'] += sum(so_luong)
                        break

                cap_nhat_danh_sach_hoa_don()
                messagebox.showinfo("Thành Công", "Hóa đơn đã được thêm!")

            except ValueError:
                messagebox.showerror("Lỗi", "Số lượng phải là số!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin hóa đơn!")

    def xoa_hoa_don():
        chi_so_chon = danh_sach_hoa_don_listbox.curselection()
        if chi_so_chon:
            hoa_don_chon = invoice_list[chi_so_chon[0]]
            invoice_list.remove(hoa_don_chon)
            cap_nhat_danh_sach_hoa_don()
            messagebox.showinfo("Thành Công", "Hoá đơn đã được xóa!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn hoá đơn để xóa!")

    def sua_hoa_don():
        chi_so_chon = danh_sach_hoa_don_listbox.curselection()
        if chi_so_chon:
            hoa_don_chon = invoice_list[chi_so_chon[0]]
            hoa_don_chon["Tên Khách Hàng"] = ten_khach_hang.get()
            hoa_don_chon["Nhân Viên"] = nhan_vien_combobox.get()
            cap_nhat_danh_sach_hoa_don()
            messagebox.showinfo("Thành Công", "Hoá đơn đã được sửa!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn hoá đơn để sửa!")

    tk.Button(HienThi_frame, text="Thêm Hoá Đơn", command=them_hoa_don, width=30, height=2, bg="#98a77c",font=("Times New Roman", 13)).grid(row=7, column=0, padx=5, pady=10, sticky="e")
    tk.Button(HienThi_frame, text="Xóa Hoá Đơn", command=xoa_hoa_don, width=30, height=2, bg="#98a77c",font=("Times New Roman", 13)).grid(row=7, column=1, padx=5, pady=10, sticky="e")
    tk.Button(HienThi_frame, text="Sửa Hoá Đơn", command=sua_hoa_don, width=30, height=2, bg="#98a77c",font=("Times New Roman", 13)).grid(row=7, column=2, padx=5, pady=10, sticky="e")
    tk.Button(HienThi_frame, text="Quay lại", command=lambda: quay_lai(HienThi_frame), width=30, height=2,bg="#e7f5dc",font=("Times New Roman", 13)).grid(row=8, column=0, padx=5, pady=10, sticky="e")

    cap_nhat_danh_sach_hoa_don()


# Doanh Thu
def hien_thi_doanh_thu(HienThi_frame):
    clear_frame(HienThi_frame)
    tk.Label(HienThi_frame, text="Tính Doanh Thu", font=("Arial black", 17, "bold"), fg="#ff0000", bg="lightyellow",
             relief="groove", bd=9).grid(row=0, column=0, columnspan=4, pady=10)

    ngay_bat_dau = DateEntry(HienThi_frame, date_pattern="yyyy-mm-dd")
    tk.Label(HienThi_frame, text="Chọn Ngày Bắt Đầu:", relief="solid",font=("Times New Roman", 13)).grid(pady=5)
    ngay_bat_dau.grid(pady=5)

    ngay_ket_thuc = DateEntry(HienThi_frame, date_pattern="yyyy-mm-dd")
    tk.Label(HienThi_frame, text="Chọn Ngày Kết Thúc:", relief="solid",font=("Times New Roman", 13)).grid(pady=5)
    ngay_ket_thuc.grid(pady=5)

    def tinh_doanh_thu():
        # Get date range from user
        start_date = datetime.strptime(ngay_bat_dau.get(), "%Y-%m-%d")
        end_date = datetime.strptime(ngay_ket_thuc.get(), "%Y-%m-%d")

        # Filter invoices by date range
        tong_tien = sum(hoa_don["Tổng Tiền"] for hoa_don in invoice_list if
                        start_date <= datetime.strptime(hoa_don["Ngày Lập"], "%Y-%m-%d") <= end_date)
        messagebox.showinfo("Doanh Thu", f"Tổng Doanh Thu trong khoảng thời gian: {tong_tien:,} VNĐ")

    tk.Button(HienThi_frame, text="Tính Doanh Thu", command=tinh_doanh_thu, width=20, height=2, bg="#ff6347",fg="#00bfff",font=("Arial black", 13)).grid(
        row=6, column=2, padx=5, pady=10)
    tk.Button(HienThi_frame, text="Quay Lại", command=lambda: quay_lai(HienThi_frame), width=20, height=2, bg="#e7f5dc",font=("Times New Roman", 13)).grid(row=7,column=0, padx=5, pady=10, sticky="nsew")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ứng Dụng Quản Lý Giày Dép")
    set_centered_window(1000, 800)

    # Frame chính để chứa các widget
    HienThi_frame = tk.Frame(root)
    HienThi_frame.pack(fill="both", expand=True)

    # Hiển thị màn hình chính khi bắt đầu
    hien_thi_giao_dien_chinh(HienThi_frame)

    # Bắt đầu vòng lặp Tkinter
    root.mainloop()