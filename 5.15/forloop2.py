import  time

t_start = time.time()
count = 0

while count < 1000000:
    count +=1
    print("次数 ...",time.time() - t_start, count)