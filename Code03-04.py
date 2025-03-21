진수=int(input("진수결정(16,10,8,2):"))
num= input("값 입력:")
if 진수==16 :
    num1=int(num,16)
if 진수==10 :
    num1=int(num,10)
if 진수==8 :
    num1=int(num,8)
if 진수==2 :
    num1=int(num,2)

print("16진수=>", hex(num1))
print("10진수=>", num1)
print("16진수=>", oct(num1))
print("16진수=>", bin(num1))