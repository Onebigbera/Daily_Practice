常见几种进制转换
bin() | oct() | int() | hex()


       2进制        8进制          10进制          16进制


2进制     ·         bin(int(x,8))  bin(int(x,10))  bin(int(x,16))


8进制  oct(int(x,2)) .             oct(int(x,10))  oct(int(x,16))


10进制 int(x,2)      int(x,8)        .              int(x,16)


16进制 hex(int(x,2)) hex(int(x,8))  hex(int(x,10))     .

PS : bin() oct() hex() 返回值均为字符串 分别带有0b、0o、0x前缀
