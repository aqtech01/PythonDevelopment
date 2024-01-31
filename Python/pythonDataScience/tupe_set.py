# sales = (200,100,300,4444)
# for si in sales:
#     print(si)


# set unordered, no duplicate, unchangeable

# sales = {"lahore", "karachi", "Islamabad", "Karachi"}
# for i in sales:
#     print(i.lower())


# f = lambda x: x + 10

# def calculate(op):
#     if op == "+":
#         return lambda x, y: x + y
#     elif op == "-":
#         return lambda x, y: x - y
#
#
# f = calculate("+")
# print(f(10, 20))


sales = [10, 20, 30, 40, 50]
f = lambda x: x * 1.10
map(f, sales)