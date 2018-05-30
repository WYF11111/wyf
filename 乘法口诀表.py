for i in range(1,10):
    for a in range(1,i+1):
        x=a*i
        print('%d*%d=%d' % (i,a,x),end='\t')
    print(end='\n')
