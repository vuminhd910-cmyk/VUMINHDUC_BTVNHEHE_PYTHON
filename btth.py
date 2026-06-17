from abc import ABC, abstractmethod 
class Employee: 
    def __init__(self, employee_id, name):
        self.id = employee_id
        self.name = name
    @abstractmethod 
    def caculate_salary(self):
        pass 
    @abstractmethod 
    def get_loai(self):
        pass 
    def display_info(self):
        print(f"ma nv:{self.id} | ho va ten: {self.name} | loai: {self.get_loai()}")  

class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name) 
        self.base_salary = base_salary
        self.bonus = bonus 

    def caculate_salary(self):
        return self.base_salary + self.bonus 
    def get_loai(self):
        return "Full Time"
    

class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, working_hour, hourly_rate):
        super().__init__(employee_id, name)
        self.working_hour = working_hour
        self.hourly_rate = hourly_rate
    def caculate_salary(self):
        return self.working_hour * self.hourly_rate
    def get_loai(self):
        return "Part time" 


class InternEmployee(Employee):
    def __init__(self, employee_id, name, allowance):
        super().__init__(employee_id, name)  
        self.allowance = allowance 
    def caculate_salary(self):
        return self.allowance 
    def get_loai(self):
        return "Intern" 
    
employees = [
    FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
    PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
    InternEmployee("E003", "Le Van C", 3000000)
] 

def display(employee):
    for i in employee:
        i.display_info() 
def display_salary(employee):
    for employ in employee:
        salary = employ.caculate_salary() 
        print(f"id: {employ.id} | ten: {employ.name:<12} | lương: {salary:,.0f} VND")  

def main():
    while True: 
        print("""
        === EMPLOYEE SALARY MANAGER ===
        1. Xem danh sách nhân viên
        2. Tính lương toàn bộ nhân viên
        3. Thoát chương trình
        ================================
        Chọn chức năng (1-3):
       """)
        
        choice = input("Nhập lựa chọn của bạn(1-3): ")
        match choice: 
            case "3":
                print("Thoát chương trình tạm biệt tình yêu moa moa") 
            case "1":
                print('HIển thị danh sách')
                display(employees) 
            case "2":
                print("Tính lương nhân viên") 
                display_salary(employees) 
            case _:
                print("YEAH YEAH ") 
  

if __name__ == "__main__":
    main()  