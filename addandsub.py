#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
import random
from docx import Document
from docx.shared import Pt

## 输入条件
def inputCondition():
    print("输入生成的种类，混合的用连续数字组合即可（1:加法；2:减法；3:乘法；4:除法）")
    ruleType = input("请输入：") or "1"

    print("输入计算式的混合数量（2～4）")
    digit = int(input("请输入：") or 2)

    print("输入计算式数值范围（1～100）")
    scope = int(input("请输入：") or 1)

    print("是否允许负数出现(1:允许 0:不允许<默认>")
    neg = int(input("请输入：") or 0)

    print("生成试题的数量（默认120道）")
    num = int(input("请输入：") or 120)

    print("用户输入的生成规则需要生成 ")
    return ruleType, digit, scope, neg, num

def analyseRule():
    pass

def randomArithmetic(ruleType, digit, scope, neg, num):
    data = []
    for i in range(0, num):
        # 先随机计算式参与计算的数有几个
        n = random.randint(2, digit)
        # 创建一个生成数2倍的数组
        dataSubList = [0] * (n * 2)
        # 隔位把数插入单数位置
        for x in range(0, n * 2, 2):
            dataSubList[x] = str(random.randint(0,scope))
        for x in range(1, n * 2, 2):
            ruleList = list(ruleType)
            d = int(random.sample(ruleList, 1)[0])
            if d == 1:
                dataSubList[x] = "+"
            elif d == 2:
                dataSubList[x] = "-"
            elif d == 3:
                dataSubList[x] = "*"
            elif d == 4:
                dataSubList[x] = "/"
        # 隔位插入运算符号 最后补上“=”
        dataSubList[n * 2 - 1] = "="
        # 转换成str输出
        dataStr = "".join(dataSubList)
        data.append(dataStr)
    return data
        

def 计算结果():
    pass
        
## 输出到word
def outPutWord(data):
    document = Document()
    # paragraph = document.add_paragraph('')
    # # 增加文字
    # paragraph.add_run('add text')
    # document.add_paragraph('111')
    # document.add_paragraph('2222')
    # for s in data:
    #     document.add_paragraph(s)
    
    # 设置word字体大小
    # style = document.styles['Normal']
    # font = style.font
    # font.size = Pt(10)


    document = Document()
    document.add_heading('小学生数学计算练习题')
    tab = document.add_table(rows=23, cols=4)
    item = 0
    for x in range(0,23):
        for y in range(0,4):
            cell = tab.cell(x,y)
            cell.text = data[item]
            item += 1
    # rowmath = ''
    # rownum = 0
   
    # for item in data:
    #     rownum = rownum + 1
    #     rowmath = item + "  " + rowmath
    #     #每3题输出到一行
    #     if rownum % 3 == 0 :
    #         # p = document.add_paragraph(item)
    #         p = document.add_paragraph('')
    #         p.add_run(rowmath).bold = True
    #         rowmath =''
    # #最后一行补充输出到文档上
    # if rownum % 3 > 0 :
    #     p = document.add_paragraph('    ')
    #     p.add_run(rowmath).bold = True

    document.save('test.docx')


if __name__ == "__main__":
    ruleType, digit, scope, neg, num = inputCondition()
    data = randomArithmetic(ruleType, digit, scope, neg, num)
    outPutWord(data)
    pass