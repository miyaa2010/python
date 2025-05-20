import random

thungphieu = set()

while True:
    print("-- MENU ------")
    print("Vui lòng lựa chọn chức năng: ")
    print("1 - Thêm một số điện thoại vào thùng phiếu dự thưởng")
    print("2 - Xóa một số điện thoại từ thùng phiếu dự thưởng")
    print("3 - Quay số ngẫu nhiên lấy ra một số điện thoại trúng thưởng")
    print("4 - Kết thúc chương trình")
    print("Thùng phiếu hiện tại:", thungphieu)

    lua_chon = input("Nhập lựa chọn của bạn (1-4): ")

    if lua_chon == "1":
        sdt = input("Nhập số điện thoại: ")
        # Kiểm tra định dạng số điện thoại (chỉ chứa số và độ dài 10-11)
        if sdt.isdigit() and 10 <= len(sdt) <= 11:
            thungphieu.add(sdt)
            print("Số điện thoại đã được thêm vào thùng phiếu.")
        else:
            print("Số điện thoại không hợp lệ. Vui lòng nhập số có 10-11 chữ số.")

    elif lua_chon == "2":
        sdt = input("Nhập số điện thoại: ")
        if sdt in thungphieu:
            thungphieu.remove(sdt)
            print("Số điện thoại đã được xóa khỏi thùng phiếu.")
        else:
            print("Số điện thoại không tồn tại trong thùng phiếu.")

    elif lua_chon == "3":
        if len(thungphieu) == 0:
            print("Thùng phiếu hiện tại rỗng.")
        else:
            sdt_trung_thuong = random.choice(list(thungphieu))
            print("Số điện thoại trúng thưởng là:", sdt_trung_thuong)
            # Xóa số trúng thưởng khỏi thùng phiếu
            thungphieu.discard(sdt_trung_thuong)

    elif lua_chon == "4":
        print("Chương trình kết thúc.")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")
