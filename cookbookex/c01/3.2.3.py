records = [('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4)]
def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)#该例子没看懂


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/user/bin/flase'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(fields)
print(homedir)
print(sh)


record = ('ACME', 50, 123.45, (12, 18, 2017))
name, *_, (*_, year) = record
print(name)
print(year)


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
items = [1, 10, 7, 4, 5, 9]
print(sum(items))#没看懂

