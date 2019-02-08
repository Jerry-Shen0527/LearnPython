
def hanoi(n,source,help,target):
    global step     #python调用全局变量的方法
    if n==1:
        print(step,source,'->',target)
        step=step+1
    else:
        hanoi(n-1,source,target,help)
        hanoi(1,source,help,target)
        hanoi(n-1,help,source,target)

step=1

hanoi(4,'a','b','c')