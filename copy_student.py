from tkinter import Tk, Button, Label, Entry, messagebox
import tkinter.font as tkFont

import pymysql


class PyMySQLUTILS:
    # 获取连接
    def __int__(self):
        # 打开数据库
        self.db=pymysql.connect(host="localhost",user="root",password="1234",database="school")
        # 使用cursor()方法获取操作游标
        self.cursor=self.db.cursor()

    # 查询获取多条数据
    def fetchall(self,sql):
        # 使用execute()方法执行sql语句
        self.cursor.execute(sql)
        # 使用fetchall()方法获取多条数据
        results=self.cursor.fetchall()
        return results

    # 查询获取单条数据
    def fetchone(self,sql):
        # 使用execute()方法执行sql语句
        self.cursor.execute(sql)
        # 使用fetchone()方法获取单条数据
        result=self.cursor.fetchone()
        return result

    # 添加删除更新操作
    def execute(self,sql):
        try:
            # 使用execute()方法执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            print("数据库操作成功！")
        except:
            # 发生错误时回滚
            self.db.rollback()
            print("数据库连接失败")


    # 关闭连接
    def close(self):
        # 关闭游标
        self.cursor.close()
        # 关闭数据库连接
        self.db.close()



class StartMenu:
    def __init__(self, parent_window):
        parent_window.destroy()
        self.window=Tk()
        self.window.title("学生成绩管理系统-教师版")
        self.window.geometry("500x500")
        self.window.resizable(0,0)#创建固定大小的窗口
        Label(self.window,text="学生成绩管理系统",font=("宋体",20)).pack(pady=100)
        Button(self.window,text="教师注册",command=lambda:TeacherRegister(self.window),font=tkFont.Font(size=16),width=30,height=2,fg="white",bg="gray",activeforeground="white",activebackground="black").pack()
        Button(self.window,text="教师登录",command=lambda:TeacherLogin(self.window),font=tkFont.Font(size=16),width=30,height=2,fg="white",bg="gray",activeforeground="white",activebackground="black").pack()
        Button(self.window,text="退出系统",command=self.window.destroy(),font=tkFont.Font(size=16),width=30,height=2,fg="white",bg="gray",activeforeground="white",activebackground="black").pack()
        self.window.mainloop()


# 教师注册界面
class TeacherRegister:
    def __init__(self,parent_window):
        parent_window.destroy()
        self.window=Tk()
        self.window.title("学生成绩管理系统-教师版")
        self.window.geometry("500x500")
        self.window.resizable(0,0)
        Label(self.window,text="欢迎注册教师界面",font=("宋体",20)).pack(pady=100)
        Label(self.window,text="输入账号:",font=tkFont.Font(size=14)).place(x=100,y=200)
        self.my_username=Entry(self.window,width=20,font=tkFont.Font(size=14),bg='Ivory')
        self.my_username.place(x=200,y=200)
        Label(self.window,text="输入密码:",font=tkFont.Font(size=14)).place(x=100,y=250)
        self.my_password = Entry(self.window, width=20, font=tkFont.Font(size=14), bg='Ivory',show="*")
        self.my_password.place(x=200, y=250)
        Label(self.window, text="确认密码:", font=tkFont.Font(size=14)).place(x=100, y=300)
        self.re_password = Entry(self.window, width=20, font=tkFont.Font(size=14), bg='Ivory',show="*")
        self.re_password.place(x=200, y=300)
        Button(self.window,text="确定",width=8,font=tkFont.Font(size=12)).place(x=200,y=350)
        Button(self.window,text="返回",width=8,font=tkFont.Font(size=12)).place(x=330,y=350)
        self.window.protocol("WM_DELETE_WINDOW", self.back)#用于定义当用户使用窗口管理器显示关闭窗口时发生的情况，执行self.back功能
        self.window.mainloop()

    def register(self):
        utils=PyMySQLUTILS()
        result=utils.fetchone("select * from teacher_login where username='%s'" % self.my_username.get())
        if self.my_username.get()=="" or self.my_password.get()=="" or self.re_password.get()=="":
            messagebox.showerror(title="showerror",message="注册失败！注册信息不完整！")
        elif self.my_password.get()!=self.re_password.get():
            messagebox.showerror(title="showerror",message="注册失败！两次密码不相同")
        elif result:
            messagebox.showerror(title="showerror",message="注册失败！该账号已被注册过了！")
        else:
            print(self.my_username.get())
            print()
            utils.execute("insert into teacher_login(username,password) values('%s','%s')" %
                          (self.my_username.get(),self.my_password))
            utils.close()
            messagebox.showinfo(title="showinfo",message="注册成功！欢迎您登录使用！")
            TeacherLogin(self.window)

    def back(self):
        StartMenu(self.window)

# 教师登录界面
class TeacherLogin:
    def __init__(self,parent_window):
        parent_window.destroy()
        self.window=Tk()
        self.window.title("学生管理系统-教师版")
        self.window.geometry("500x500")
        self.window.resizable(0,0)
        Label(self.window, text="欢迎教师登录", font=("宋体", 20)).pack(pady=100)
        Label(self.window, text="账号:", font=tkFont.Font(size=14)).place(x=100, y=200)
        self.my_username = Entry(self.window, width=20, font=tkFont.Font(size=14), bg='Ivory')
        self.my_username.place(x=170, y=200)
        Label(self.window, text="密码:", font=tkFont.Font(size=14)).place(x=100, y=250)
        self.my_password = Entry(self.window, width=20, font=tkFont.Font(size=14), bg='Ivory', show="*")
        self.my_password.place(x=170, y=250)
        Button(self.window, text="确定", width=8, font=tkFont.Font(size=12)).place(x=170, y=350)
        Button(self.window, text="返回", width=8, font=tkFont.Font(size=12)).place(x=330, y=350)
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 用于定义当用户使用窗口管理器显示关闭窗口时发生的情况，执行self.back功能
        self.window.mainloop()

    def login(self):
        utils=PyMySQLUTILS()
        result=utils.fetchone("select * from teacher_login where username='%s'" % self.my_username.get())
        if self.my_username.get()=="" or self.my_password.get()=="":
            messagebox.showerror(title="showerror",message="登录失败！登录信息不完整！")
        elif result:
            utils.close()
            if self.my_password.get()==result[1]:
                messagebox.showinfo("showinfo","登录成功！欢迎您使用！")
                TeacherMenu(self.window)
            else:
                messagebox.showerror("showerror","登录失败！输入的密码错误")
        else:
            messagebox.showerror("showerror","登录失败！输入的账号有误！")


    def back(self):
        StartMenu(self.window)



class TeacherMenu:
    def __init__(self):
        pass



if __name__=='__main__':
    window = Tk()
    StartMenu(window)
