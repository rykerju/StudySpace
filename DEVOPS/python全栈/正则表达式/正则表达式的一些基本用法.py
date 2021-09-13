'''
限定符
?:     used?    表示d可有可无，可以出现0次或1次
*：    ab*c     表示可以匹配0个b也可以匹配任意个b
+：    ab+c     表示b至少出现1次
{}：   ab{2,6}c 表示b可以出现2到6次，2次以上可以省略6
()：   (ab)+    表示匹配ab次数至少一次
运算符
|：    a (cat|dog) 表示想匹配a和空格，然后在匹配要么cat要么dog
字符类
[]:    [abc]+   表示字符只取自方括号内的
        几个用法：[a-zA-Z0-9]+
        前面加^则表示取除了后面的字符之外的数字
简写	描述
.	除换行符外的所有字符
\w	匹配所有字母数字，等同于 [a-zA-Z0-9_]
\W	匹配所有非字母数字，即符号，等同于： [^\w]
\d	匹配数字： [0-9]
\D	匹配非数字： [^\d]
\s	匹配所有空格字符，等同于： [\t\n\f\r\p{Z}]
\S	匹配所有非空格字符： [^\s]
\f	匹配一个换页符
\n	匹配一个换行符
\r	匹配一个回车符
\t	匹配一个制表符
\v	匹配一个垂直制表符
\p	匹配 CR/LF（等同于 \r\n），用来匹配 DOS 行终止符
'''
'''
贪婪匹配
'''
'''
例子“
ipv4地址：(([01]?\d\d?|2[0-4]\d|25[0-4])\.){3}([01]?\d\d?|2[0-4]\d|25[0-4])
'''