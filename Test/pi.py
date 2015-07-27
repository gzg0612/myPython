
def calc_pi(n):
    pi=0
    index=1
    count = 0
    while count < n:
        if count%2 == 0:
            pi += 1/((1+ count * 2)**3)
        if count%2 == 1:
            pi -= 1/((1+ count * 2)**3)
        count += 1
    return "%.6f" % (pi*32)**(1/3)

def payout(dict):
    keylist = dict.keys()
    for each_key in keylist:
        dict[each_key] = int(dict[each_key] * 1.1)
        if dict[each_key] < 90000:
           dict[each_key] += 10000
    newdic={}
    for each_key in keylist:
        if dict[each_key] < 95000:
           newdic[each_key] = dict[each_key]
    print(newdic)

def avlen(str):
    strlist = str.strip().split(' ')
    print(len(strlist))
import random
def dice(N, s):
    sum=0
    count = 0
    while count < N:
        i = random.randint(1, 6)
        j = random.randint(1, 6)
        if (i + j) == s:
            sum += 1
        count += 1
    str = "%d/%d" % (sum, N)
    return str
dic={"judy":48000, "brand":83000, "joe":163000}
print(dice(1000,2))
