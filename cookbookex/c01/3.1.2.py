p =(4,5)
x, y = p
print(x)
print(y)
data = ['ACME', 50, 91.1, (2012, 12,21)]
name, shares, price,date = data
print(name)
print(date)
name, shares, price, (year, mon, day) = data
print(name)
print(year)
print(mon)
print(day)
#如果变量个数和序列元素的个数不匹配，会产生一个异常
# p = (4, 5)
# x, y, z = p