import sys

input_string = input("input a string:")
input_char = input("input a char:")

#因为不区分大小写，所以把字符都转换成大写或者小写
input_string = input_string.upper()
input_char = input_char.upper()

#不用count函数的方法
# number = 0
# for i in  input_string:
#     if input_char == i:
#         number=number+1
#
# print(number)


print(input_string.count(input_char))
