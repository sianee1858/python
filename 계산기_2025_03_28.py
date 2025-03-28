선택,answer,수식,num1,num2=0,0,"",0,0
선택 = int(input('1.입력한 수식 계산, 2.두수사이의 합계:'))

if 선택==1:
    수식=input('***수식을 입력하세요')
    answer= eval(수식)
    print(answer)
elif 선택==2:
    num1=int(input('***첫번째 숫자'))
    num2=int(input('***두번째 숫자'))
    for a in range(num1,num2+1):
        answer=answer+a
    print("%d+...+%d는 %d이다"%(num1,num2,answer))

else:
    print('1 과 2만 입력하세요')