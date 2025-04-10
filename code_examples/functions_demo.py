# Python函数示例
# 本文件展示了Python中函数的定义和使用方法

# 1. 基本函数定义和调用
print("===== 基本函数示例 =====")

def greet(name):
    """简单的问候函数
    
    参数:
        name: 要问候的人的名字
    
    返回:
        包含问候语的字符串
    """
    return f"你好，{name}！欢迎学习Python！"

# 调用函数
message = greet("小明")
print(message)

# 2. 带有默认参数的函数
print("\n===== 默认参数示例 =====")

def power(x, n=2):
    """计算x的n次方
    
    参数:
        x: 底数
        n: 指数，默认为2
    
    返回:
        计算结果
    """
    return x ** n

print(f"2的平方是：{power(2)}")  # 使用默认参数
print(f"2的3次方是：{power(2, 3)}")  # 指定参数

# 3. 关键字参数
print("\n===== 关键字参数示例 =====")

def student_info(name, age, gender, course="Python"):
    """显示学生信息
    
    参数:
        name: 姓名
        age: 年龄
        gender: 性别
        course: 课程，默认为Python
    """
    print(f"学生信息：姓名={name}, 年龄={age}, 性别={gender}, 学习课程={course}")

# 可以按照不同顺序提供参数，只要指定参数名
student_info(age=20, name="小红", gender="女")
student_info(name="小明", gender="男", age=22, course="Python高级编程")

# 4. 可变参数
print("\n===== 可变参数示例 =====")

def sum_numbers(*args):
    """计算所有传入数字的和
    
    参数:
        *args: 任意数量的位置参数
    
    返回:
        所有参数的总和
    """
    total = 0
    for num in args:
        total += num
    return total

print(f"1+2的和是：{sum_numbers(1, 2)}")
print(f"1+2+3+4+5的和是：{sum_numbers(1, 2, 3, 4, 5)}")

# 5. 关键字可变参数
print("\n===== 关键字可变参数示例 =====")

def person_info(name, **kwargs):
    """显示人物信息
    
    参数:
        name: 姓名
        **kwargs: 任意数量的关键字参数
        
    返回:
        包含所有信息的字典
    """
    info = {"name": name}
    info.update(kwargs)
    return info

person1 = person_info("张三", age=30, city="北京", job="程序员")
print(f"人物信息：{person1}")

# 6. 匿名函数(Lambda函数)
print("\n===== Lambda函数示例 =====")

# 定义一个lambda函数计算平方
square = lambda x: x * x

print(f"5的平方是：{square(5)}")

# 使用lambda结合内置函数
numbers = [1, 3, 5, 4, 2]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(f"排序后的数字：{sorted_numbers}")

# 7. 函数作为参数传递
print("\n===== 函数作为参数示例 =====")

def apply_operation(x, y, operation):
    """应用一个操作到两个数字
    
    参数:
        x, y: 两个数字
        operation: 一个接受两个参数并返回结果的函数
        
    返回:
        操作的结果
    """
    return operation(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(f"3+5={apply_operation(3, 5, add)}")
print(f"3*5={apply_operation(3, 5, multiply)}")
print(f"3-5={apply_operation(3, 5, lambda a, b: a - b)}")  # 使用lambda

# 8. 作用域示例
print("\n===== 作用域示例 =====")

global_var = "我是全局变量"

def scope_test():
    local_var = "我是局部变量"
    print(f"在函数内部：global_var = {global_var}")
    print(f"在函数内部：local_var = {local_var}")

scope_test()
print(f"在函数外部：global_var = {global_var}")
# print(f"在函数外部：local_var = {local_var}")  # 这行会报错，因为local_var是局部变量

# 9. 闭包示例
print("\n===== 闭包示例 =====")

def make_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

counter = make_counter()
print(f"计数：{counter()}")  # 1
print(f"计数：{counter()}")  # 2
print(f"计数：{counter()}")  # 3

print("\n函数是Python编程中非常重要的概念，好好掌握它们！")