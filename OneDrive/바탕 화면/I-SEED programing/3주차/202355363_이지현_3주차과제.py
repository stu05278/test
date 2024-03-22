#4
score = int(input("점수를 입력하세요 : "))

if score >=90 :
    print("장학생", end='')
elif score >= 60 :
    print("합격", end='')
else :
    print("불합격", end='')

print("입니다. ^^")
        
#5
num = 5
if num %2==0:
    res ='짝수'
else :
    res ='홀수'
print(res)

num=5
res = '짝수' if num % 2 == 0 else '홀수'
print(res)
#답 : 3번

#6-1
nn = [100,200,300,400,500]
nn[1] = 777
print(nn)
# [100,777,300,400,500]
#6-2
nn = [100,200,300,400,500]
nn[1] =[444,555]
print(nn)
#[100,[444,555],300,400,500]
#6-3
nn = [100,200,300,400,500]
nn[1:4]=[444,555]
print(nn)
#[100,444,555,500]
#6-4
nn = [100,200,300,400,500]
nn[2:]=[]
print(nn)
#[100,200]
#9
hap,i=0,0

for i in range(3333,9999) :
    if i%1234 == 0 :
        hap += i
        continue
    
    if hap > 100000 :
        break

print(hap)

#8
hap= 0
n=1234

while n<=4567:
    if n%444==0 :
        hap += n
    n += 1
        
print(hap)

#14
myData=[[n*m for n in range(1,3)]for m in range(2,4)]
print(myData)
#[[2, 4], [3, 6]]
#5
nn=[100,200,300,400,500]
print(nn[4])
print(nn[-1])
print(nn[-2])
print(nn[1:4])
print(nn[0:1])
print(nn[2:-1])
print(nn[0::2])
print(nn[::-1])
print(nn[::-2])
# 500, 500, 400, [200, 300, 400], [100], [300, 400], [100,300, 500], [500, 400, 300, 200, 100], [500, 300, 100]
