import ying_hang
while True:
    ying_hang.guang_da()
    xuan_ze=int(input('请输入您选择的业务,请输入序号：'))
    if xuan_ze==1:
        ying_hang.ban_ka()
    elif xuan_ze==2:
        ying_hang.cun_kuang()
    elif xuan_ze==666:
        break
    elif xuan_ze==3:
        ying_hang.qu_kuang()
    elif xuan_ze==4:
        ying_hang.zhu_xiao()
    elif xuan_ze==5:
        ying_hang.cha_xun()
    elif xuan_ze==6:
        ying_hang.cai_quan()
    elif xuan_ze==7:
        ying_hang.cai_shu_zi()
    elif xuan_ze==8:
        ying_hang.xue_hua()
        print('                                                            欢迎下次光临，再见')
        break






