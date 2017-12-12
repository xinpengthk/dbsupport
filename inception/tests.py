#!/usr/bin/python

a = ["zhangsan","lisi","laowang"]
print("添加请按1")
print("查询请按2")
print("删除请按3")

Worker = input("请输入你的要办理的业务：")

if  Worker == "1":
    name = input("请输入你要添加的名字：")
    a.append(name)
    print(a)
elif Worker == "2":
    name = input("请输入你要查询的名字：")
    if name in a:
        print("Yes")
elif Worker == "3":
    name = input("请输入你要删除的名字：")
    a.remove(name)
    print(a)

#为什么不能添加和删除呢