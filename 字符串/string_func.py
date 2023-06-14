name = "Chao Wang"
namespace1 = "   Chao Wang  "
namespace2 = "666666Chao Wang6666666"

firstname = "Chao"
lastname = "Wang"
#切片[start:end]
print(name[2:4])
print(name[-3:])
print(name[-3:-1])
#切片[start:end:length]
print(name[0:4:2])
print(name[::-1])
#拼接
print(firstname+" "+lastname)
print(','.join((lastname,firstname)))

#常用func
#查找第一个字符
print(name.find("a"))
#返回总共的“a”
print(name.count("a"))
#替换
print(name.replace("a","x"))

#分割 return list
print(name.split('a'))

#去空格或字符
print(namespace1.strip())
print(namespace2.strip('6'))