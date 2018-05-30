import random
import time
list1=[]
list2=[]
def guang_da():
    print('------------------------------')
    print('欢迎来到光大银行')
    time.sleep(1)
    print('以下是本银行的业务')
    print('1.办理银行卡')
    print('2.办理存款业务')
    print('3.办理取款业务')
    print('4.注销银行卡及个人信息')
    print('5.查看个人信息')
    print('等待时间为您准备了小游戏哦')
    print('6.猜拳小游戏')
    print('7.猜数字小游戏')
    print('8.给你一个surprise')
    print('-------------------------------')
def ban_ka():
    print('请填写您的一些身份信息')
    print('这些信息将会在您使用银行卡时用到')
    print('请出示您的身份证供工作人员查看')
    name=input('请输入您的姓名：')
    card=int(input('请输入您的18位身份证号：'))
    print('感谢您的配合，我们将马上为您办理')
    hao_ma=random.randint(1000000000000000000,9999999999999999999)
    print('办理成功')
    time.sleep(0.5)
    print('您的银行卡号为:%19d' % hao_ma)
    time.sleep(0.5)
    dic={'姓名':name,'身份证号':card,'银行卡号':hao_ma}
    list1.append(dic)
    for i in list1:
        print('姓名：%s' % i['姓名'])
        print('身份证号：%15dxxx' % i['身份证号'])
        print('银行卡号：%15dxxxx' % i['银行卡号'])
    print('感谢您使用光大银行')
    time.sleep(0.3)
    print('请收好您的身份证')
def cun_kuang():
    biao_ji=0
    money=0
    print('请出示您的身份证')
    while True:
        print('返回主界面请输入666')
        haoMa=int(input('请输入您的银行卡号：'))
        if haoMa==666:
            break
        for a in list1:
            if haoMa==a['银行卡号']:
                print('正在为您查询')
                time.sleep(1)
                print('号码输入正确')
                biao_ji=100
                break
        if biao_ji==100:
            money1=float(input('请输入存款金额：'))
            money=money+money1
            print('正在为您充值')
            time.sleep(0.5)
            print('充值成功')
            dic2={'账户余额':money}
            list2.append(dic2)
            for i in list2:
                if money==i['账户余额']:
                    print('您当前的账户余额为:%2f' % i['账户余额'])
                    continue
            ji_xu=input('请问您还要继续充值吗？请输入是或者否:')
            if ji_xu=='是':
                bao_ji=100
                continue
            elif ji_xu=='否':
                biao_ji=102
                break
        else:
            print('正在查询')
            print('输入错误，请重新输入')
            time.sleep(0.5)
        if biao_ji==102:
                break
def qu_kuang():
    biao_ji=0
    while True:
        name1=input('请输入您的姓名：')
        if name1==1:
            break
        card1=int(input('请输入您的身份证：'))
        hao_ma1=int(input('请输入您的银行卡号：'))
        for i in list1:
            if name1==i['姓名'] and card1==i['身份证号'] and hao_ma1==i['银行卡号']:
                print('正在核对')
                time.sleep(0.5)
                print('输入正确')
                time.sleep(0.5)
                biao_ji=10
                break
        if biao_ji==10:
            for a in list2:
                y=a['账户余额']
                qu_qian=float(input('请输入您要取款的金额：'))
                if qu_qian<=y:
                    print('正在办理请等待')
                    print('提款成功')
                    time.sleep(0.5)
                    yu_e=y-qu_qian
                    print('您当前余额为：%f' % yu_e)
                    biao_ji=15
                    break
                else:
                    print('余额不足')
        if biao_ji==15:
            break
def zhu_xiao():
    biao_ji=0
    name2=input('请输入您的姓名：')
    card2=int(input('请输入您的身份证号：'))
    hao_ma2=int(input('请输入您的银行卡号：'))
    for i in list1:
        if name2==i['姓名'] and card2==i['身份证号'] and hao_ma2==i['银行卡号']:
            print('正在核对')
            print('身份验证成功')
            time.sleep(0.5)
            list1.remove(i)
            biao_ji=1
            break
    if biao_ji==1:
        for a in list2:
            print('您当前的余额为：%f' % a['账户余额'])
            print('正在帮您取出，请稍后')
            print('已取出，请收好')
            time.sleep(0.5)
            list2.remove(a)
            print('正在注销用户')
            print('注销成功')
            time.sleep(0.5)
def cha_xun():
    biao_ji=0
    card3=int(input('请输入您的身份证信息'))
    for i in list1:
        if card3==i['身份证号']:
            print('验证成功，正在查询')
            print('查询成功')
            time.sleep(0.5)
            print('姓名：%s' % i['姓名'])
            print('身份证号：%15dxxx' % i['身份证号'])
            print('银行卡号：%15dxxxx' % i['银行卡号'])
            biao_ji=1
            break
    if biao_ji==1:
        for a in list2:
            y=a['账户余额']
            if y>0:
                print('账户余额为%f' % a['账户余额'])
                break
            else:
                print('账户余额为0')
    else:
        print('输入错误')
def cai_quan():
    print('欢迎您进入猜拳小游戏')
    time.sleep(0.5)
    print('退出请输入666，请记住哦')
    while True:
        sui_ji=random.randint(1,3)#(石头剪刀布)
        you=int(input('1为拳头，2为剪刀，3为布。请输入1~3的数字：'))
        if you==666:
            break
        if sui_ji==1:
            print('系统美女出的是“拳头”')
        elif sui_ji==2:
            print('系统美女出的是“剪刀”')
        else:
            print('系统美女出的是“布”')
        if you==1:
            print('你出的是“拳头”')
        elif you==2:
            print('你出的是“剪刀”')
        elif you==3:
            print('你出的是“布”')
        else:
            print('输入错误，请重新输入')
        if (you==1 and sui_ji==2) or (you==2 and sui_ji==3) or (you==3 and sui_ji==1):
            print('恭喜你,你赢了')
        elif (you==1 and sui_ji==1) or (you==2 and sui_ji==2) or (you==3 and sui_ji==3):
            print('平局哦！')
        else:
            print('不好意思你输了呦')
def cai_shu_zi():
    ci_shu=0
    print('请输入1~100的数字，有10次机会哦！')
    sui_ji=random.randint(1,101)
    while ci_shu<10:
        if ci_shu==9:
            print('没机会了哦')
            break
        print(sui_ji)
        you=int(input('请输入：'))
        if you < sui_ji:
            print('猜小了哦')
        elif you > sui_ji:
            print('猜大了哦')
        elif you == sui_ji:
            print('恭喜你猜对了哦！好棒')
            break
        if you==666:
            break
        ci_shu=ci_shu+1
def xue_hua():
    for i in range(1,6):
        a=random.randint(1,150)
        print(' '*a,'✾')
        time.sleep(0.1)
        b=random.randint(1,150)
        print(' '*b,'✿')
        time.sleep(0.1)
        c=random.randint(1,150)
        print(' '*c,'❁')
        time.sleep(0.1)
        d=random.randint(1,150)
        print(' '*d,'❃')
        time.sleep(0.1)
        e=random.randint(1,150)
        print(' '*e,'❋')
        time.sleep(0.1)
        f=random.randint(1,150)
        print(' '*f,'❀')
        time.sleep(0.1)
        g=random.randint(1,150)
        print(' '*g,'⚘')
        time.sleep(0.1)


