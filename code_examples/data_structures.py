# Python基础数据结构示例
# 这个文件展示了Python中常用的数据结构及其基本操作

# 1. 列表 (List) - 可变序列，可以存储不同类型的元素
print("===== 列表示例 =====")
my_list = [1, 2, 3, "Python", True]
print(f"原始列表: {my_list}")

# 列表常用操作
my_list.append(4)  # 添加元素
print(f"添加元素后: {my_list}")

my_list.insert(2, "插入的元素")  # 在指定位置插入元素
print(f"插入元素后: {my_list}")

popped_element = my_list.pop()  # 移除并返回最后一个元素
print(f"移除的元素: {popped_element}")
print(f"移除元素后: {my_list}")

my_list.remove("Python")  # 移除指定元素
print(f"移除'Python'后: {my_list}")

print(f"列表第一个元素: {my_list[0]}")
print(f"列表切片[1:3]: {my_list[1:3]}")  # 获取子列表

# 2. 元组 (Tuple) - 不可变序列
print("\n===== 元组示例 =====")
my_tuple = (1, 2, 3, "Python", True)
print(f"元组: {my_tuple}")
print(f"元组中的第三个元素: {my_tuple[2]}")
print(f"元组切片[2:4]: {my_tuple[2:4]}")

# 元组不支持修改操作，但可以合并
tuple_2 = ("A", "B")
combined_tuple = my_tuple + tuple_2
print(f"合并后的元组: {combined_tuple}")

# 3. 字典 (Dictionary) - 键值对集合
print("\n===== 字典示例 =====")
my_dict = {
    "name": "Python",
    "type": "编程语言",
    "created_year": 1991,
    "creator": "Guido van Rossum",
    "is_popular": True
}
print(f"字典: {my_dict}")

# 访问字典元素
print(f"字典中'name'的值: {my_dict['name']}")

# 修改字典元素
my_dict["is_popular"] = "非常流行"
print(f"修改后的字典: {my_dict}")

# 添加新元素
my_dict["features"] = ["简单", "易学", "功能强大"]
print(f"添加新元素后: {my_dict}")

# 删除元素
del my_dict["created_year"]
print(f"删除元素后: {my_dict}")

# 获取所有键和值
print(f"所有键: {list(my_dict.keys())}")
print(f"所有值: {list(my_dict.values())}")
print(f"所有键值对: {list(my_dict.items())}")

# 4. 集合 (Set) - 无序不重复元素集合
print("\n===== 集合示例 =====")
my_set = {1, 2, 3, 4, 5, 5, 4}  # 重复元素会被自动去除
print(f"集合: {my_set}")

# 添加元素
my_set.add(6)
print(f"添加元素后: {my_set}")

# 删除元素
my_set.remove(3)
print(f"删除元素后: {my_set}")

# 集合操作
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"集合A: {set_a}")
print(f"集合B: {set_b}")
print(f"并集: {set_a | set_b}")
print(f"交集: {set_a & set_b}")
print(f"差集(A-B): {set_a - set_b}")
print(f"对称差集: {set_a ^ set_b}")

# 5. 字符串操作 - 字符串也是一种序列
print("\n===== 字符串操作示例 =====")
my_string = "Python编程很有趣!"
print(f"原始字符串: {my_string}")
print(f"字符串长度: {len(my_string)}")
print(f"首字母大写: {my_string.capitalize()}")
print(f"所有字母大写: {my_string.upper()}")
print(f"查找'编程'的位置: {my_string.find('编程')}")
print(f"替换'有趣'为'简单': {my_string.replace('有趣', '简单')}")
print(f"字符串切片[0:6]: {my_string[0:6]}")

# 字符串格式化
name = "Python"
version = 3.9
print(f"使用f-string格式化: {name} 版本 {version}")
print("使用format()格式化: {} 版本 {}".format(name, version))

print("\n记住：多练习这些数据结构的操作，它们是Python编程的基础！")