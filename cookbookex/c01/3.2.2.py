# #星号表达式
# def drop_first_last(grades):
#     first, *middle, last = grades
#     return avg(middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

#星号表达式用在列表开始的部分
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)