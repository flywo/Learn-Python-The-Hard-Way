#--coding:utf-8--

#输出字符串
print('Hello world !')

str = 'Hello world !'
print(str)

#格式化输出
strHello = "the length of (%s) is %d" % ('Hello World',len('Hello World'))
print(strHello)

#格式化输出16进制等
#%x --- hex 十六进制
#%d --- dec 十进制
#%o --- oct 八进制
nHex = 0xFF
print("nHex = %x,nDec = %d,nOct = %o" % (nHex, nHex, nHex))

#格式化浮点数
import math
print('PI=%f'%math.pi)
print("PI = %10.3f" % math.pi)
print("PI = %-10.3f" % math.pi)
print("PI = %06d" % int(math.pi))

#格式化输出字符串
print ("%.3s " % ("python"))