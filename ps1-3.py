def Pascal_triangle(K):
    l=[] 
    for i in range(K):
        if i==0:
            l.append([1])  
        elif i==1:
            l.append([1,1])
        else:
            y = []  
            for j  in range(i+1):
                if j==0 or j==i:
                    y.append(1)
                else:
                    y.append(l[i-1][j]+l[i-1][j-1])
            l.append(y)
    return l
K=12 
x=Pascal_triangle(K)
for i in range(len(x)):#逐行打印结果
    print(x[i])
