print('請輸入密碼，最多3次')

password='a123456'
ans=input('請輸入密碼:')
for i in range(2,0,-1):
    
    if ans == password:
        print('輸入正確!!')
        break
    else:
        ans=input('你還有'+str(i)+'次機會:')
        i-=1

        #第二版