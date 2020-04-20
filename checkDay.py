def main():
    print("Vui lòng nhập ngày tháng năm:")
    Day = nhapngay()
    Month = nhapthang()
    Year = nhapnam()
    print("Bạn đã nhập:", "ngày",Day,"tháng", Month,"năm", Year)
    # Gọi hàm check ngày có hợp lệ hay không
    #if checkday(int(Day), int(Month), int(Year)) == False:
    if checkday(Day, Month, Year) == False:
        print("Nhập ngày tháng năm không hợp lệ")
    else:
        print("Ngày hôm trước là:",ngayhomtruoc(int(Day), int(Month), int(Year)))
        print("Ngày hôm sau là:",ngayhomsau(int(Day), int(Month), int(Year)))

# Hàm kiểm tra không cho nhập ngày là rỗng or nhiều hơn 2 ký tự 
def nhapngay():
    print("Nhập ngày: ",end = "" )
    Day = input()
    if(Day == "" or len(Day) > 2):
        print("Vui lòng nhập lại")
        nhapngay()
    else:
        return Day

# Hàm kiểm tra không cho nhập tháng là rỗng or nhiều hơn 2 ký tự 
def nhapthang():
    print("Nhập tháng: ",end = "")
    Month = input()
    if(Month == "" or len(Month) > 2):
        print("Vui lòng nhập lại")
        nhapthang()
    else:
        return Month

# Hàm kiểm tra không cho nhập năm là rỗng or nhiều hơn 4 ký tự
def nhapnam():
    print("Nhập năm: ",end = "")
    Year = input()
    if(Year == "" or len(Year) > 4):
        print("Vui lòng nhập lại")
        nhapnam()
    else:
        return Year

# kiểm tra ngày, tháng năm nhập vào có hợp lệ không. Có trả về true
def checkday(Day, Month, Year):
    # checks chuỗi
    if Day.isdigit() and Month.isdigit() and Year.isdigit():
        Y = int(Year)
        M = int(Month)
        D = int(Day)
        if Y < 0:
            return False
        elif 1 > M  or M > 12:
            return False
        elif 1 > D  or D > ngaycuathang(M,Y):
            return False 
        else:
            return True 
    else:
        return False
    
#Hàm trả về số ngày của tháng nhập vào để kiểm tra ngày nhập vào đúng or sai
def ngaycuathang(Month,Year):
    if Month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 12:
        Day = 31
    elif Month == 4 or Month == 6 or Month == 9 or Month == 11:
        Day = 30
    else:
        if namnhuan(Year) == True:
            Day = 29
        else:
            Day = 28
    return Day

# Hàm tìm năm nhuận
def namnhuan(Year):
    if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
        return True
    else:
        return False

# Hàm tìm ngày hôm trước
def ngayhomtruoc(Day, Month, Year):
    Day = Day - 1
    if Day == 0:
        Month = Month - 1
        if Month == 0:
            Month = 12
            Year = Year - 1
        Day = ngaycuathang(Month, Year)
    return ("ngày %s tháng %s năm %s" %(Day, Month, Year))

#Ham tìm ngày hôm sau
def ngayhomsau(Day,Month,Year):
    Day = Day + 1
    if Day > ngaycuathang(Month, Year):
        Day = 1
        Month = Month + 1
        if Month > 12:
            Month = 1
            Year = Year + 1
    return ("ngày %s tháng %s năm %s" %(Day, Month, Year))

# Run
main()