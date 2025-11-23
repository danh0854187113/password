import random #tạo biến random
#Nhập số dòng
p = input("nhập số dòng: ")
#Kiểm tra định dạng đầu vào
while p.isdigit()== False:
    p = (input("nhập số:  "))
p = int(p)
# Nhạp độ dài
a=(input("nhập độ dài của mật khẩu: "))
# Kiểm tra định dạng đầu vào
while a.isdigit()== False:
    a = (input( "nhập số đi bố: "))
a=int(a)
#kiểm tra định dạng đầu vào
require_all= input("Nhap cac dieu kien: ")
while a <= 0:
 a= int (input("nhập lại độ dài nhiều hơn 0 kí tự: "))
if require_all == "true":
    while a < 4:
        a=int(input("phải lớn hơn 4: "))
        #tạo mật khẩu
        print("độ dài mật khẩu là:",a)
# tạo cacs biến mật khẩu
letters = ("qwertyuiopasdfghjklzxcvbnm")# chữ
numbers = ("1234567890")#số
symbols = ("!@#$%^&*")#kí tự

# TẠO MẬT KHẨU
password = ""
#kiểm tra định dạng đầu vào
# Tạo mật khẩu theo điều kiện
if require_all == "true":
    for i in range(p):
        for i in range(a):
            if i == 0:
                password+=random.choice(letters.upper())
            elif i == 1:
                password+=random.choice(symbols)
            elif i == 2:
                password+=random.choice(letters)
            elif i == 3:
                password+=random.choice(numbers)
            else:
                password+= random.choice(letters + numbers + symbols + letters.upper())
        password += ' \n'
# Tạo mật khẩu tự do
else:
    for i in range(p):
        for i in range(a):
          password += random.choice( letters + numbers + symbols + letters.upper())
        password+="\n"
print(password)