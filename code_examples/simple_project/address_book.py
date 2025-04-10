# 简单通讯录项目
# 这是一个简单的通讯录程序，演示了Python基础知识的实际应用

class Contact:
    """联系人类"""
    
    def __init__(self, name, phone, email=None, address=None):
        """初始化联系人
        
        参数:
            name: 联系人姓名
            phone: 电话号码
            email: 电子邮件地址（可选）
            address: 地址（可选）
        """
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    
    def __str__(self):
        """返回联系人信息的字符串表示"""
        info = f"姓名: {self.name}, 电话: {self.phone}"
        if self.email:
            info += f", 邮箱: {self.email}"
        if self.address:
            info += f", 地址: {self.address}"
        return info
    
    def update(self, phone=None, email=None, address=None):
        """更新联系人信息
        
        参数:
            phone: 新的电话号码（可选）
            email: 新的电子邮件地址（可选）
            address: 新的地址（可选）
        """
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address
        return self


class AddressBook:
    """通讯录类"""
    
    def __init__(self):
        """初始化空通讯录"""
        self.contacts = {}
    
    def add_contact(self, contact):
        """添加联系人到通讯录
        
        参数:
            contact: 联系人对象
        
        返回:
            成功添加返回True，否则返回False
        """
        if contact.name in self.contacts:
            print(f"联系人 '{contact.name}' 已存在!")
            return False
        
        self.contacts[contact.name] = contact
        print(f"联系人 '{contact.name}' 已添加成功!")
        return True
    
    def remove_contact(self, name):
        """从通讯录中删除联系人
        
        参数:
            name: 联系人姓名
        
        返回:
            成功删除返回True，否则返回False
        """
        if name not in self.contacts:
            print(f"联系人 '{name}' 不存在!")
            return False
        
        del self.contacts[name]
        print(f"联系人 '{name}' 已删除!")
        return True
    
    def find_contact(self, name):
        """查找联系人
        
        参数:
            name: 联系人姓名
        
        返回:
            联系人对象，如果找不到则返回None
        """
        if name in self.contacts:
            return self.contacts[name]
        else:
            print(f"联系人 '{name}' 不存在!")
            return None
    
    def list_contacts(self):
        """列出所有联系人
        
        返回:
            联系人数量
        """
        if not self.contacts:
            print("通讯录为空!")
            return 0
        
        print("\n所有联系人:")
        print("-" * 50)
        for i, (name, contact) in enumerate(self.contacts.items(), 1):
            print(f"{i}. {contact}")
        print("-" * 50)
        return len(self.contacts)


def display_menu():
    """显示菜单选项"""
    print("\n===== 通讯录管理系统 =====")
    print("1. 添加联系人")
    print("2. 查找联系人")
    print("3. 删除联系人")
    print("4. 列出所有联系人")
    print("5. 更新联系人信息")
    print("0. 退出程序")
    print("==========================")


def get_contact_info(update=False):
    """获取联系人信息
    
    参数:
        update: 是否是更新操作
    
    返回:
        联系人信息的字典
    """
    info = {}
    
    if not update:
        info["name"] = input("请输入姓名: ")
    
    info["phone"] = input("请输入电话号码: ")
    if not info["phone"] and update:
        info["phone"] = None
    
    info["email"] = input("请输入电子邮件 (可选): ")
    if not info["email"]:
        info["email"] = None
    
    info["address"] = input("请输入地址 (可选): ")
    if not info["address"]:
        info["address"] = None
    
    return info


def main():
    """主程序"""
    address_book = AddressBook()
    
    # 预先添加一些联系人用于测试
    address_book.add_contact(Contact("张三", "13800138000", "zhangsan@example.com", "北京市海淀区"))
    address_book.add_contact(Contact("李四", "13900139000", "lisi@example.com"))
    address_book.add_contact(Contact("王五", "13700137000"))
    
    while True:
        display_menu()
        choice = input("请选择功能 (0-5): ")
        
        if choice == "1":
            # 添加联系人
            info = get_contact_info()
            contact = Contact(info["name"], info["phone"], info["email"], info["address"])
            address_book.add_contact(contact)
            
        elif choice == "2":
            # 查找联系人
            name = input("请输入要查找的联系人姓名: ")
            contact = address_book.find_contact(name)
            if contact:
                print(f"\n找到联系人: {contact}")
                
        elif choice == "3":
            # 删除联系人
            name = input("请输入要删除的联系人姓名: ")
            address_book.remove_contact(name)
            
        elif choice == "4":
            # 列出所有联系人
            address_book.list_contacts()
            
        elif choice == "5":
            # 更新联系人信息
            name = input("请输入要更新的联系人姓名: ")
            contact = address_book.find_contact(name)
            if contact:
                print(f"当前信息: {contact}")
                print("请输入新的信息 (直接回车保持不变):")
                info = get_contact_info(update=True)
                contact.update(info["phone"], info["email"], info["address"])
                print(f"联系人已更新: {contact}")
                
        elif choice == "0":
            # 退出程序
            print("感谢使用通讯录管理系统，再见！")
            break
            
        else:
            print("无效的选择，请重新输入!")


if __name__ == "__main__":
    print("欢迎使用通讯录管理系统！")
    print("这是一个演示Python基础知识应用的示例项目。")
    main()