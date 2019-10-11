#什么是正则表达式
import re
# reg_string="ndaskjfhellodjsbfa,ND1234BFNFDSBCKJS@fsmfmmd"
# reg="hello"
# reg="\d"
# reg="^nd"
# result=re.findall(reg,reg_string)
# print(result)
# reg="\d{4}"
# result=re.findall(reg,reg_string)
# print(result)

# reg="[0-9a-z]{4}"
# result=re.findall(reg,reg_string)
# print(result)

# ip="this is ip:192.168.1.123:172.138.2.15"
# reg="\d{3}.\d+.\d+.\d+"
# result=re.findall(reg,ip)
# print(result)

# regg="(\d{1,3}.){3}\d{1,3}"
# resultt=re.search(regg,ip)
# print(resultt)

'''
组匹配
'''
s="this is phone:13888888888 and this is my postcode:012345"
reg="this is phone:(\d{11}) and this is my postcode:(\d{6})"
result=re.search(reg,s).group(0)
result1=re.search(reg,s).group(1)
result2=re.search(reg,s).group(2)
print(result)
print(result1)
print(result2)

reg_string="hellostringhellostring"
reg="hello"
result=re.match(reg,reg_string).group()
print(result)

reg_string="pythonnnnnnnnnnnnnnnnnnnnnpythonhellopytho"

#贪婪
reg="python*"
result=re.findall(reg,reg_string)
print(result)
# 非贪婪
reg="python*?"
result=re.findall(reg,reg_string)
print(result)

reg="python+?"
result=re.findall(reg,reg_string)
print(result)
reg="python??"
result=re.findall(reg,reg_string)
print(result)

# 练习部分  手机号码验证
'''
移动
139 138 137 136 135 134
150 151 152 157 158 159
182 183 187 188
147
联通
130 131 132
185 186 145
电信
133 153 180 189
'''
def checkCellphont(cellphone):
    regex="^((13[0-9])|(14[5|7])|(15[0-3]|[5-9])|(18[0,5-9]))\d{8}$"
    result=re.findall(regex,cellphone)
    if result:
        print("匹配成功");
        return True;
    else:
        print("匹配失败")
        return False;

checkCellphont("15044955856")
