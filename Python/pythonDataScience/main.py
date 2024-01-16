# def add(x, y):
#     return x + y
#
#
# def default_parameter(x, y=20):
#     return x + y
# def profile(name, gender, country):
#     if gender:
#         print(f"Mr. {name} is from {country}")
#     else:
#         print(f"Miss. {name} is from {country}")
def profile(*args):
    for i in range(len(args)):
        print(args[i])

    # if gender:
    #     print(f"Mr. {name} is from {country}")
    # else:
    #     print(f"Miss. {name} is from {country}")


if __name__ == "__main__":
    profile("A", True, "UK")
    # result = add(20, 30)
    # sum_parameter = default_parameter(50)
    # print(result)
    # print(sum_parameter)
