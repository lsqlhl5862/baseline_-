import re
my_str="[2019年10月 \n二十四日"
regex = "(.十)"
my_str1 = re.findall(regex, my_str)
print(my_str1)
aaa=re.split('年',my_str)
type(aaa)

CN_NUM={
    u'四':4,u'二': 2,
}

regex="(^.*二十四)"
my_str444=re.findall(regex, my_str)
print("str444是",my_str444)

for key in CN_NUM:
    my_str3=re.sub(key+'十',str(CN_NUM[key])+'十',my_str)
print(my_str3)

my_str33=re.sub('.年','.-',my_str)
print(my_str33)

print('O'=='Ο')

test_row=re.split('月',my_str)[0]
print(test_row)
print(type(test_row))
tag_head_row=my_str.replace('\n','$|$')
print('aaa',tag_head_row)
pppp=re.split('\$\|\$',tag_head_row)
print(aaa)
print(type(aaa))
aaa.reverse()
print(aaa)
print(type(aaa))
print(pppp)

head_row_a=re.split('年',my_str)[0]

print(head_row_a)

text_row1="子公司佛山欧神诺云商科技有限公司（以下简称“欧神诺云商”）购买"
regex = "(子公司.*公司.*购买)"
text1 = re.findall(regex, text_row1)
print(text1)