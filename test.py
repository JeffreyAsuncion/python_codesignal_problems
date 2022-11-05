
a = [1,2,3,4,5]

for i in range(len(a)-1):
    for j in range(len(a)-1):
        if i != j:
            if a[i]+a[j] = target:
                return i,j
            print(a[i],a[j])