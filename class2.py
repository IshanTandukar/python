# for i in range(2,10,3):
#  print(i)

for i in range(1,100):
    count = 0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
         print(i)
        