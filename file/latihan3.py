t= int(input("Masukkan tinggi : "))
print ()
for i in range(t):
    for j in range(t,i,-1):
        print(" ",end = "")
    for j in range(2*i+1):
        print("*",end = "")
    print ()
for i in range(t-1,-1,-1):
    for j in range(t,i,-1):
        print(" ",end = "")
    for j in range(2*i+1):
        print("*",end = "")
    print ()
