# Python 作业 14



```java

有的时候，工作中，我们需要存档文件， 会拷贝一个目录里面所有的文件到另外的机器上
如果是特别机密的存档文件，比如合约，财务信息等，我们不希望这些目录中的文件有任何修改。

假如有员工偷偷修改了存档的文件，就会和源文件不一致

我们需要实现一个工具，能够快速检测存档目录中的文件和源文件是否有不同。

方法是，为源目录中的所有文件产生一个校验文件，里面记录了所有文件的校验和（使用MD5算法）

这样存档后，如果有人修改任何一个文件， 
运行工具 检查 就能发现 现有文件的校验和 与源文件中的校验文件里面记录的值 不同

网上有类似的工具：  filecheckmd5.exe 
下载地址：https://github.com/jcyrss/songqin-testdev/raw/master/others/softwares/filecheckmd5.zip

要求大家用Python语言开发类似的工具。


实现难点 如下，大家自己到网上搜索解决方法，锻炼自己查询资料，解决问题的能力，

难点1： 图形界面
大家可以使用Python 内置的图形界面库 tkinter 去实现

难点2： md5校验和的概念  和 生成文件md5校验和的方法 （特别是对大文件的支持）

```




## 参考答案，往下翻
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

```python
from tkinter import Button, Tk, HORIZONTAL,Label,filedialog,messagebox,END

from tkinter.ttk import Notebook,Frame

from tkinter.scrolledtext import ScrolledText

import time,os,threading,hashlib

MD5_VALIDATION_FILE = u'FCMD5-sums.MD5'

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def generate_file_md5( filepath, blocksize=2**20):
    m = hashlib.md5()
    with open( filepath, "rb" ) as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update( buf )
    return m.hexdigest()


class MonApp(Tk):
    def __init__(self):
        super().__init__()
        self.minsize(width=650, height=550)
        center(self)

        self.srcFolderPath = ''
        self.targetFolderPath = ''
        self.title(u'md5校验器')

        self.tabMgr = Notebook(self)
        
        self.tab1Initial()
        self.tab2Initial()





    def tab1Initial(self):

        tab1 = Frame(self.tabMgr)
        self.tabMgr.add(tab1, text=u' 创建校验码 ')
        self.tabMgr.pack(expand=1, fill="both")

        # tab1.rowconfigure(1, minsize=100)
        # tab1.columnconfigure(0,minsize=100)

        Button(tab1, text=u'选择源文件夹', command=self.selectSrcFolder).grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        self.txtSrcFolder = Label(tab1, text= " ")
        self.txtSrcFolder.grid(row=1, column=0, columnspan=3, )



        self.btnCreating = Button(tab1, text='Go!', command=self.createMD5)
        self.btnCreating.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

        self.txtCreating = ScrolledText(tab1)
        self.txtCreating.grid(row=3, column=0, rowspan=2,columnspan=2, padx=20, pady=10)
        # self.txtCreating['state']= 'disabled'



    def tab2Initial(self):

        tab2 = Frame(self.tabMgr)
        self.tabMgr.add(tab2, text=u' 进行校验 ')
        self.tabMgr.pack(expand=1, fill="both")
        

        Button(tab2, text=u'选择目标文件', command=self.selectTargetFolder).grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        self.txtTargetFile = Label(tab2, text= " ")
        self.txtTargetFile.grid(row=1, column=0, columnspan=3, )



        self.btnValidating = Button(tab2, text=u'校验!', command=self.validateMD5)
        self.btnValidating.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

        self.txtValidating = ScrolledText(tab2)
        self.txtValidating.grid(row=3, column=0, rowspan=2,columnspan=2, padx=20, pady=10)
        
    def selectSrcFolder(self):
        self.srcFolderPath = os.path.abspath(filedialog.askdirectory())
        self.txtSrcFolder['text'] = self.srcFolderPath
        # self.targetFolderPath = filedialog.askdirectory()
        # self.txtTargetFile['text'] = self.targetfilePath

    def selectTargetFolder(self):
        self.targetFilePath = os.path.abspath(filedialog.askopenfilename(defaultextension='.MD5',
                  filetypes=[('MD5 file','*.MD5'),('All files','*.*')]))
        self.targetFolderPath =  os.path.dirname(self.targetFilePath)
        self.txtTargetFile['text'] = self.targetFilePath



    def _getAllFiles(self,directory):
        fileList = []
        for path, dirs, files in os.walk(os.path.abspath(directory)):

            #   去掉 System Volume Information 卷信息文件
            if 'System Volume Information' in path:
                continue


            for filename in files:
                # 去掉校验文件本身
                if filename == MD5_VALIDATION_FILE:
                    continue

                filepath = os.path.join(path, filename)
                # print(filepath)
                fileList.append(filepath)


        return fileList

    def createMD5(self):

        if not self.srcFolderPath.strip():
            messagebox.showwarning(u'错误', u'请先选择目录')
            return

        def real_create():
            allfiles = self._getAllFiles(self.srcFolderPath)

            self.txtCreating.delete(1.0, END)
            self.btnCreating['state'] = 'disabled'

            allfileMd5 = []
            for one in allfiles:
                basedir = self.srcFolderPath
                if not basedir.endswith('\\'):
                    basedir += '\\'
                curFile = one.replace(basedir, '')
                self.txtCreating.insert(END, curFile + '\n')
                md5Record = '%s|%s' % (generate_file_md5(one), curFile)
                allfileMd5.append(md5Record)
                self.txtCreating.see("end")

            with open(os.path.join(self.srcFolderPath, MD5_VALIDATION_FILE), 'w',encoding='utf8') as md5file:
                md5file.write('\n'.join(allfileMd5))

            messagebox.showinfo('OK', u'处理完成')
            self.btnCreating['state'] = 'normal'

        threading.Thread(target=real_create).start()




    def validateMD5(self):

        if not self.targetFolderPath.strip():
            messagebox.showwarning(u'错误', u'请先选择目录')
            return

        if not os.path.isfile(self.targetFilePath):
            messagebox.showwarning(u'错误', u'没有校验记录文件：'+self.targetFilePath)
            return


        def real_check():
            # 读取md5校验文件
            md5Table = {}
            with open(self.targetFilePath,'r',encoding='utf8') as md5file:
                for line in md5file.read().splitlines():
                    line = line.strip()
                    if line.startswith(';'):
                        continue
                    if line.count('|') != 1:
                        continue
                    md5str,filename = line.split('|')
                    md5Table[filename] = md5str

            if len(md5Table) == 0:
                messagebox.showwarning('warning',u'文件中没有md5记录信息')
                return

            allfiles = self._getAllFiles(self.targetFolderPath)


            self.txtValidating.delete(1.0, END)
            self.btnValidating['state']= 'disabled'

            errList = ''
            for one in allfiles:
                basedir = self.targetFolderPath
                if not basedir.endswith('\\'):
                    basedir += '\\'
                curFile = one.replace(basedir,'')
                self.txtValidating.insert(END, curFile+' ... ')
                self.txtValidating.see("end")

                if curFile not in md5Table:
                    self.txtValidating.insert(END, u'md5校验记录不存在!!!!!!!!!!!!\n')
                    errList += curFile + u'  md5校验记录不存在\n'
                    continue

                md5Str_ori = md5Table[curFile]
                md5Str_now = generate_file_md5(one)
                if md5Str_now != md5Str_ori:
                    self.txtValidating.insert(END, u'md5校验不匹配!!!!!!!!!!!!!!\n')
                    errList += curFile + u'  md5校验不匹配\n'
                    continue

                self.txtValidating.insert(END, u'ok\n')



            for one in md5Table.keys():
                if os.path.join(self.targetFolderPath, one) not in allfiles:
                    err = u'{} 文件丢失!!!!!!!!!!!!!\n'.format(one)

                    errList += err


            self.txtValidating.insert(END, u'\n\n============ 校验结果 =========== \n\n')
            if errList:
                info = u'校验结果有错误！！！'
                self.txtValidating.insert(END, errList)
            else:
                info = u'校验结果完全匹配'
                self.txtValidating.insert(END, u' ********* 通过 *********')

            self.txtValidating.see("end")
            messagebox.showinfo('OK',u'处理完毕 , ' + info)
            self.btnValidating['state']= 'normal'

        threading.Thread(target=real_check).start()

if __name__ == '__main__':

    app = MonApp()
    app.mainloop()
```
