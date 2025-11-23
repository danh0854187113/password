import random  #KHAI BÁO RANDOM 
p = input("nhập số dòng: ") # Tạo biến p để nhập số dòng
while p.isdigit()== False: # Nếu P không phải là định dạng số
    p = (input("nhập số:  ")) # bắt nhập lại
p = int(p)# p phải là số thực
a=(input("nhập độ dài của mật khẩu: "))#tạo biến a để nhập độ dài mk
while a.isdigit()== False:# Nếu a không phải là định dạng số
    a = (input( "nhập số đi bố: "))#bắt nhập lại
a=int(a)# a phải là số thực
require_all= input("Nhap cac dieu kien: ")# nhập điều kiện true or false
while a <= 0:# nếu a <= 0
 a= int (input("nhập lại độ dài nhiều hơn 0 kí tự: "))#bắt nhập lại
if require_all == "true": #nếu tất cả điều kiện đúng 
    while a < 4:#khi a <4
        a=int(input("phải lớn hơn 4: "))#bắt nhập lại
        print("độ dài mật khẩu là:",a)#in độ dài mk ra màn hình
letters = ("qwertyuiopasdfghjklzxcvbnm")#các chữ để random
numbers = ("1234567890")#các số để random
symbols = ("!@#$%^&*")#các kí tự để random
password = ""#biến mk
if require_all == "true":#khi tất cả dk = true
    for i in range(p):#biến i
        for i in range(a):#tạo vòng lặp
            if i == 0:#khi i bằng 0
                password+=random.choice(letters.upper())#vị trí 0 sẽ là chữ hoa
            elif i == 1:#khi i bằng 1
                password+=random.choice(symbols)# vị trí 1 sẽ là kí tự
            elif i == 2:#khi i bằng 2
                password+=random.choice(letters)#vị trí 2 là chữ
            elif i == 3:#khi i bằng 3
                password+=random.choice(numbers)#vị trí 3 là số
            else:
                password+= random.choice(letters + numbers + symbols + letters.upper())
        password += ' \n'#công thức mk
else:
    for i in range(p):#vòng lập i
        for i in range(a):#vòng lăpj
          password += random.choice( letters + numbers + symbols + letters.upper())
        password+="\n"#tạo ra mk
print("Mật khẩu của bạn là: \n",password)#in ra mk
