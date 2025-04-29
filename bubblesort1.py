def bubblesort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
a=[51,12,33,55]
print("before sorting",a)

bubblesort(a)
print("after sorting",a)