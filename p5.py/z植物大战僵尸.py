class zhi_wu:
    def __init__(self,name,shu_xing,xing_wei):
        self.name=name
        self.shu_xing=shu_xing
        self.xing_wei=xing_wei
    def shuo_ming(self):
        print('我是：%s,我的属性是：%s我的行为是: %s' % (self.name,self.shu_xing,self.xing_wei))
    def __str__(self):
        a='我是'+self.name+'我正在'+self.xing_wei
        return a
b=int(input('请输入您要查看的植物：'))
if b==2:
    c=zhi_wu('向日葵','无','放阳光')
    c.shuo_ming()
    print(c)
elif b==3:
    c=zhi_wu('豌豆','颜色、发型、血量','发炮、摇头')
    c.shuo_ming()
    print(c)
elif b==1:
    c=zhi_wu('坚果','血量、类型','阻挡')
    c.shuo_ming()
    print(c)
elif b==4:
    c=zhi_wu('僵尸','颜色、血量、类型、速度','走、跑、跳、吃、死')
    c.shuo_ming()
    print(c)


