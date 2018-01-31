#--coding:utf-8--

'''
Keywords(关键字)
and
del 删除引用，不删除数据
from
not
while

with as 自动做清理工作：
file = open("/tmp/foo.txt")
data = file.read()
file.close()
等价于下方：
with open("/tmp/foo.txt") as file:
    data = file.read()

elif
global 声明变量作用于，可以修改和重新定义全局变量
or

with
1.紧跟with后面的语句被求值后，返回对象的 __enter__() 方法被调用，这个方法的返回值将被赋值给as后面的变量。
2.当with后面的代码块全部被执行完之后，将调用前面返回对象的 __exit__()方法。

assert 断言：assert len(lists) >=5,'列表元素个数小于5'
else
if
pass
yield 生成器
break
except
import
print
class 创建类
exec 执行string类型存储的ptyhon代码
in
raise raise显示地引发异常。一旦执行了raise语句，raise后面的语句将不能执行
continue
finally
is
return
def
for
lambda
try

数据类型
True
False
None
strings
numbers
floats
lists

字符串转义序列(Escape Sequences)
\ \
\'
\"
\a
\b
\f
\n
\r
\t
\v

字符串格式化(String Formats)
% d 打印整数
% i 有符号十进制
% o 无符号八进制
% u 无符号十进制
% x 无符号十六
% X 无符号十六大写
% e 科学计数
% E
% f 打印浮点数
% F 浮点数，小数部分截断
% g
% G
% c 转换成字符ascii
% r 使用repr()进行字符串转换
% s 打印字符串
% %

操作符号
+  - * ** / // % < > <= >= == != <> ()[] {} @,:.=; += -= *= /= //= %= **=
'''