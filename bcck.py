import time
#NHẬP THỜI GIAN CUẢ POMODORO
pomodoro = input("nhập phút của pomodoro ( nếu nhấn enter thì sẽ mặc định là 25phút): ")
if pomodoro.strip()=="":
    pomodoro_time = 25
elif pomodoro.isdigit()== False:
    pomodoro = (input( "vui lòng nhập số (nếu enter mặc định là 25phút) :"))
    if pomodoro.strip()=="":
        pomodoro_time = 25
    else :
       pomodoro_time =int(pomodoro)
else :
    pomodoro_time =int(pomodoro)
print(pomodoro_time)
#NHẬP THỜI GIAN NGHỈ GIẢI LAO
giải_lao =input("nhập thời gian giải lao :")
if giải_lao.strip()=="":
    giải_lao_time = 5
elif giải_lao.isdigit()== False:
    giải_lao = (input( "vui lòng nhập số (nếu enter mặc định là 5phút) :"))
    if giải_lao.strip()=="":
        giải_lao_time = 5
    else :
      giải_lao_time =int(giải_lao)
else :
    giải_lao_time =int(giải_lao)
print(giải_lao_time)
while True:
    seconds = pomodoro_time * 60
    print("\nBắt đầu Pomodoro!")
    while seconds > 0:
        mins = seconds // 60    
        secs = seconds % 60
        print(f"Pomodoro còn: {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("\nPomodoro xong!")
    # Break
    seconds = giải_lao_time * 60
    print("Bắt đầu giải lao!")
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        print(f"Break còn: {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("\nGiải lao xong!")
    # Hỏi tiếp tục
    tiep = input("Nhấn Enter để tiếp tục, gõ q để thoát: ")
    if tiep.lower() == "q":
        print("Thoát chương trình.")
        break