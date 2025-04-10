a,b,구구단=0,0,""
for a in range(2,10):
    구구단=구구단 + ("# %d단 #" %a)
print(구구단)
for a in range(1,10) :
    구구단=""
    for b in range(2,10):
        구구단= 구구단 + str("%2d X %2d= %2d" % (b,a,a*b))
    print(구구단)