def hanoi(n,source,help,target):
    if n==1:
        print(source,'->',target)
    else:
        hanoi(n-1,source,target,help)
        hanoi(1,source,help,target)
        hanoi(n-1,help,source,target)

hanoi(4,'a','b','c')