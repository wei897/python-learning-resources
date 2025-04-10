# 这是一个简单的Python Hello World程序
# 学习Python的第一步

# 打印欢迎信息
print("Hello, World!")
print("欢迎开始Python学习之旅!")

# 变量使用示例
name = "Python初学者"
days_learning = 1
print(f"你好，{name}！你已经学习Python {days_learning} 天了。")

# 简单的条件语句示例
if days_learning < 7:
    print("你刚刚开始学习，继续坚持！")
else:
    print("你已经学习一周了，很棒！")

# 简单的循环示例
print("\n打印数字1到5:")
for i in range(1, 6):
    print(f"数字: {i}")

# 简单的函数定义和调用
def greet(person_name):
    """这是一个简单的问候函数"""
    return f"你好，{person_name}！祝你学习Python愉快！"

# 调用函数
message = greet("初学者")
print("\n" + message)

# 列表使用示例
programming_languages = ["Python", "JavaScript", "Java", "C++", "Go"]
print("\n热门编程语言:")
for language in programming_languages:
    print(f"- {language}")

print("\nPython是一个易于学习且功能强大的编程语言！")
print("记住：多练习，多编码，学习编程最重要的是实践！")