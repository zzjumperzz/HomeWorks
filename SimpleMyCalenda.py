#超级简单的计算器
from tkinter import *
root = Tk()
root.minsize(250,350)

#顶部区域
frame_top = Frame(width = 250,height = 50,bg = 'grey')

res = StringVar()
res.set(0)
show_label = Label(frame_top,textvariable = res,width = 12,height = 1,font = ('楷体',20,'bold'),justify = LEFT,anchor = 'e')
show_label.pack(padx = 10,pady = 10)

frame_top.pack()


#是否按下运算符
isoperate = False

#是否按下等于号
isequal = False

#操作列表
cale = []

#按键功能
def nums(num):
    global cale,isoperate,isequal
    #未按下等号
    if isequal == False:

        #未按下运算符
        if isoperate == False:
            #判断是否已输入，还是为0
            if res.get() == '0':
                res.set('')
                res.set(num)
                cale.append(num)
                print('列表是：',cale)
            else:
                res.set(res.get()+num)
                cale.append(num)
                print('列表是：', cale)

        #已经按下运算符
        else:
            res.set(num)
            cale.append(num)
            isoperate = False
            print('列表是：', cale)

    #按下等号
    else:
        res.set(num)
        cale.append(num)
        isequal = False

#运算功能
def operate(sign):
    global cale,isoperate,isequal
    #判断是否重复输入

    if len(cale) == 0:
        #0也算是一个数字
        cale.append(res.get())
        print('列表是：', cale)
        return '长度为零'

    else:

        if cale[-1] in '+-*/':
            return '重复输入'

        else:
            cale.append(sign)

    isoperate = True
    isequal = False
    print('列表是：', cale)


#等于功能
def toequal():
    global isequal,isoperate
    #如果最后一个字符是运算符，则删除该字符
    calestr = ''.join(cale)
    if calestr[-1] in '+-*/':
        calestr = calestr[0:-1]
    result = eval(calestr)
    res.set(result)
    isequal = True
    isoperate = False

#清空功能
def clearshow():
    global cale
    res.set('0')
    cale = []

#正负功能
def fan():
    global cale
    #0没有正负
    if len(cale) == 0 or res.get() == 0:
        return '0没有正负'
    # 如果已经点击运算符，则正负号功能不可用
    elif cale[-1] in '+-*/':
        return '已经点击运算符，正负号功能不可用'


    else:
        v = res.get()
        length = len(res.get())
        # 在数字前插入负号
        cale.insert((len(cale)-length),'-')
        #print('这是第一个',v)

        #在显示上做切片 删除第一位
        if v[0] == '-':
            res.set(v[1:])
        else:
            res.set('-'+res.get())
        print(cale)



#删除
def dele():
    global cale,isequal

    #显示数字为一位则置为零
    if len(res.get()) == 1 and cale[-1] not in '+-*/':
        res.set('0')
        #切片 删除最后一位
        cale = cale[0:-1]
        print('列表是：', cale)


    # 如果列表中的最后一位是运算符，则做清空操作
    elif cale[-1] in '+-*/':
        clearshow()
        print(cale)

    else:
        showstr = res.get()
        showstr = showstr[0:-1]
        res.set(showstr)
        cale = cale[0:-1]
        print('列表是：', cale)


#按键区域
frame_bord = Frame(width=400,height=350,bg='#cccccc')

button_del = Button(frame_bord,text = '←',width = 5,height =1,command = dele).grid(row = 0,column = 0)
button_clear = Button(frame_bord,text = 'C',width = 5,height =1,command = clearshow).grid(row = 0,column = 1)
button_fan = Button(frame_bord,text = '±',width = 5,height =1,command = fan).grid(row = 0,column = 2)
button_ce = Button(frame_bord,text = 'CE',width = 5,height =1,command = clearshow).grid(row = 0,column = 3)

button_1 = Button(frame_bord,text = '1',width = 5,height =2,command = lambda:nums('1')).grid(row = 1,column = 0)
button_2 = Button(frame_bord,text = '2',width = 5,height =2,command = lambda:nums('2')).grid(row = 1,column = 1)
button_3 = Button(frame_bord,text = '3',width = 5,height =2,command = lambda:nums('3')).grid(row = 1,column = 2)
button_jia = Button(frame_bord,text = '+',width = 5,height =2,command = lambda:operate('+')).grid(row = 1,column = 3)

button_4 = Button(frame_bord,text = '4',width = 5,height =2,command = lambda:nums('4')).grid(row = 2,column = 0)
button_5 = Button(frame_bord,text = '5',width = 5,height =2,command = lambda:nums('5')).grid(row = 2,column = 1)
button_6 = Button(frame_bord,text = '6',width = 5,height =2,command = lambda:nums('6')).grid(row = 2,column = 2)
button_jian = Button(frame_bord,text = '-',width = 5,height =2,command = lambda:operate('-')).grid(row = 2,column = 3)

button_7 = Button(frame_bord,text = '7',width = 5,height =2,command = lambda:nums('7')).grid(row = 3,column = 0)
button_8 = Button(frame_bord,text = '8',width = 5,height =2,command = lambda:nums('8')).grid(row = 3,column = 1)
button_9 = Button(frame_bord,text = '9',width = 5,height =2,command = lambda:nums('9')).grid(row = 3,column = 2)
button_cheng = Button(frame_bord,text = 'x',width = 5,height =2,command = lambda:operate('*')).grid(row = 3,column = 3)

button_0 = Button(frame_bord,text = '0',width = 5,height =2,command = lambda:nums('0')).grid(row = 4,column = 0)
button_dian = Button(frame_bord,text = '.',width = 5,height =2,command = lambda:nums('.')).grid(row = 4,column = 1)
button_deng = Button(frame_bord,text = '=',width = 5,height =2,command = toequal).grid(row = 4,column = 2)
button_chu = Button(frame_bord,text = '/',width = 5,height =2,command = lambda:operate('/')).grid(row = 4,column = 3)


button_auther = Button(frame_bord,text = '查看作者',width = 25,height =2,command = lambda: print('张鹏')).grid(row = 5,column = 0,columnspan=4)

frame_bord.pack(padx = 10,pady = 10)


root.mainloop()