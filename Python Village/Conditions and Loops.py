#Given: Two positive integers a and b (a<b<10000).
#Return: The sum of all odd integers from a through b, inclusively.
#input: 
#=======================
sum = 0
for i in range(4940, 9670):
    if i % 2 == 1:
        sum += i
print('sum= ',sum)
#output : sum=17276325

#다른방법으로 for문
i = 0
sum = 0
for i in range(4941, 9670,2):
    sum=sum+i
print('sum= ',sum)
#output : sum=17276325

#다른방법 while
i = 4940
sum = 0
while i < 9670:
    i+=1
    if i%2 == 1:
        sum += i
print('sum=',sum)  

#output : sum= 1727632
