#这种解压赋值可以用在任何可迭代的对象上面，而不仅仅是列表或者元组，包括字符串，文件对象，迭代器和生成器
s = 'Hello'
a, b, c ,d ,e = s
print(a)
print(b)
print(c)
print(d)
print(e)

#使用任意变量名占位,需要保证选用的占位变量名在其他地方没有被使用到
data = ["ACME", 50, 91.1, (2012,12,21)]
_, shares, price, _ = data
print(shares)
print(price)