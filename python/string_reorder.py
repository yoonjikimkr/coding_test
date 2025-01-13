s = "Helpo,_World!"
print(s[::-1]) # !dlroW ,olleH
print(s[::2]) # Hlo ol!
print(s[::-2]) # !lo olH
print(s[::4]) # Hello, World!
print(s[:-1]) # Hello, World
print(s[1:]) # ello, World!
print(s[1:-2]) # ello, Worl
print(s[::-4]) 

# ::는 [start:stop:step]을 의미한다.
# start: 생략되었을 경우 0 (문자열의 첫 번째 위치부터 시작).
# stop: 생략되었을 경우 문자열의 끝까지 (len(s))를 의미.
# step: 2로 설정되어 두 칸씩 건너뛰면서 추출.
# 따라서, [::2]는 문자열의 처음부터 끝까지 두 칸씩 건너뛰는 슬라이싱.
print(s[2:8:3]) #l,o # s[2], s[5], s[8]이 아니라 s[2], s[5]까지. stop=len(s) 앞까지.