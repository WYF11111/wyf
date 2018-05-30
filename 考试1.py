list1=[{'北京':{'面积':'1000平','人口':'200w'},'上海':{'面积':'600平','人口':'150w'}}]
for a in list1:
    for b,c in a.items():
       for d,e in c.items():
           print(b,d,e)
