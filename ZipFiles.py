from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import os
import os.path
import zipfile

root = Tk()
root.minsize(450,350)

#显示标签
res = tkinter.StringVar()
res.set('此处显示已选择的文件')
Label = tkinter.Label(root,textvariable = res,bg = 'blue',fg = 'white')
Label.place(x=37.5, y=100,width =375,height = 30)

#添加文件方法
def push_files():
    global paths
    paths = tkinter.filedialog.askopenfilenames()
    if paths == '':
        tkinter.messagebox.showwarning(message='未选择任何文件！')
    else:
        tkinter.messagebox.showinfo(message='文件添加成功')
        strpath = '\n'.join(paths)
        print(strpath)
        #修改压缩按钮状态
        btn_ys['state'] = 'active'
        res.set(strpath)

#压缩方法
def zip_files():
    global paths
    try:
        #确认传进来的路径不为空
        if paths == '':
            tkinter.messagebox.showwarning(message='未传入压缩文件')
        else :
            #传入压缩路径
            dirpath = tkinter.filedialog.askdirectory(title = '请选择压缩路径')
            print(dirpath)

            #创建压缩对象
            zf = zipfile.ZipFile(dirpath + '/压缩.zip','w')

            #遍历指定文件并压缩
            for each in paths:
                print(each)
                #依次进行压缩
                zf.write(each,os.path.basename(each))

            #完成后关闭文件
            zf.close()
            tkinter.messagebox.showinfo('提示','压缩成功,压缩路径' + dirpath +'/压缩.zip')

    except PermissionError:
        tkinter.messagebox.showwarning(message='请选择压缩路径')

#解压方法
def unzip_files():
    try:
        unpath = tkinter.filedialog.askopenfilename(title = '选择解压文件',filetypes = [('zip file','*.zip')])
        strunpath = ''.join(unpath)
        print(strunpath)
        strunpath = str(strunpath)
        strunpath = strunpath.split('.')

        #判断是否为zip后缀的文件
        if strunpath[-1] == 'zip':
            #选择解压路径
            zippath = tkinter.filedialog.askdirectory(title = '请选择解压路径')

            #创建解压文件路径的对象
            zf = zipfile.ZipFile(unpath,'r')

            #解压文件
            zf.extractall(zippath)

            zf.close()

            tkinter.messagebox.showinfo('提示', '解压成功,解压路径:' + zippath)

        else:
            tkinter.messagebox.showinfo('提示', '请选择要解压的文件')

    except AttributeError :
        tkinter.messagebox.showinfo('提示', '请选择要解压的文件')

#菜单栏方法
def example():
    tkinter.messagebox.showinfo(title='菜单栏',message='这是菜单栏~~')

# 创建总菜单
menubar = Menu(root)
# 创建一个下拉菜单，并且加入文件菜单,设置菜单不能被拉出
filemenu = Menu(menubar,tearoff = False)
# 创建下拉菜单的选项
filemenu.add_command(label = 'Open',command = example)
# 创建下拉菜单的分割线
filemenu.add_separator()
#退出对话框
filemenu.add_command(label = 'Exit',command = root.quit)

# 将文件菜单作为下拉菜单添加到总菜单中，并且将命名为File
menubar.add_cascade(label = 'File',menu = filemenu)

#显示总菜单
root.config(menu = menubar)



#添加文件按钮
btn_add = tkinter.Button(root, text='添加文件', command=push_files)
btn_add.place(x=37.5, y=20, width=100, height=60)

#压缩按钮，默认为置灰状态
btn_ys = tkinter.Button(root,text = '压缩文件',command = zip_files,state = 'disable')
btn_ys.place(x=175, y=20,width =100,height = 60)

#解压按钮
btn_jy = tkinter.Button(root,text = '解压文件',command =unzip_files)
btn_jy.place(x=312.5, y=20,width =100,height = 60)


root.mainloop()