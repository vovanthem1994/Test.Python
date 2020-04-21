def main():
    print("Vui lòng nhập ngày tháng năm:")
    print("Nhập ngày: ",end = "" )
    Day = int(input())
    print("Nhập tháng: ",end = "")
    Month = int(input())
    print("Nhập năm: ",end = "")
    Year = int(input())
    print("Bạn đã nhập:", "ngày:",Day,"tháng:", Month,"năm:", Year)
    if checkday(Day,Month,Year) == False:
        print("Nhập sai ngày.")
    else:
    #Gọi hàm tìm ngày hôm trước
        print(" Ngày hôm trướclà:",ngayhomtruoc(Day,Month,Year))
    #Gọi hàm tìm ngày hôm sau
        print(" Ngày hôm sau là:",ngayhomsau(Day,Month,Year))

#checks nhập ngày đúng
def checkday(Day, Month, Year):
    if Year < 0:
        return False
    elif 1 > Month  or Month > 12:
        return False
    elif 1 > Day  or Day > ngaycuathang(Month,Year):
        return False 
    else:
        return True 
# Hàm tìm ngày hôm trước
def ngayhomtruoc(Day, Month, Year):
    if Day - 1 == 0:
        Month = Month - 1
        if Month == 0:
            Day = ngaycuathang(Month, Year)
            Month = 12
            Year = Year -1
            return (Day,Month,Year)
        else:
            return (Day - 1 ,Month,Year)
    else:
        return (Day - 1 ,Month,Year)

#hàm tìm ngày hôm sau
def ngayhomsau(Day, Month, Year):
    if Day + 1 > ngaycuathang(Month, Year):
        Day = 1
        Month = Month + 1
        if Month > 12:
            Month = 1
            Year = Year + 1
            return (Day,Month,Year)
        else:
            return (Day,Month,Year)
    else:
        return (Day + 1 ,Month,Year)

#hàm check ngày của tháng   
def ngaycuathang(Month,Year):
    if Month in [1,3,5,7,8,10,12]:
        Day = 31
    elif Month in [4,6,9,11]:
        Day = 30
    else:
        if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
            Day = 29
        else:
            Day = 28
    return Day 
main()