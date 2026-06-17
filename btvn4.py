from abc import ABC, abstractmethod  

class Champion: 
    def __init__(self,champion_id, name, base_hp, base_atk):
        self.champion_id = champion_id
        self.name = name
        self.base_hp = base_hp
        self.base_atk = base_atk
    
    @abstractmethod 
    def caculate_skill_damage(self):
        pass 

    @abstractmethod 
    def get_he(self):
        pass 

    def get_combat_power(self):
        return self.base_hp + (self.caculate_skill_damage() * 1.5)
    
    def __add__(self, other):
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power() 
        elif isinstance(other,(int,float)):
            return self.get_combat_power() + other 
        return NotImplementedError
    
    def __gt__(self,other):
        return self.get_combat_power() > other.get_combat_power 
    def display_info(self):
        print("--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")
        print("Mã     | Tên tướng            | Hệ       | HP    | ATK   | Chỉ số riêng      | Chiến lực")
        
class Warrior(Champion):
    def __init__(self, champion_id, name, base_hp, base_atk,shield_bonus):
        super().__init__(champion_id, name, base_hp, base_atk) 
        self.shield_bonus = shield_bonus

    def caculate_skill_damage(self):
        return (self.base_atk * 2) + self.shield_bonus 
    def get_he(self):
        return "Warrior" 
    def display_info(self):
        stat_val = f"Armor: {self.shield_bonus}"
        print(f"{self.champion_id:<7} | {self.name:<18} | {self.get_he():<8} | {self.base_hp:<5} | {self.base_atk:<5} | {stat_val:<15} | {int(self.get_combat_power())}")

    
class Mage(Champion):
    def __init__(self, champion_id, name, base_hp, base_atk,ability_power):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power
    def caculate_skill_damage(self):
        return self.base_atk   *  self.ability_power  
    def get_he(self):
        return "Mage" 
    def display_info(self):
        stat_val = f"Mana: {self.base_atk * self.ability_power}"
        print(f"{self.champion_id:<7} | {self.name:<18} | {self.get_he():<8} | {self.base_hp:<5} | {self.base_atk:<5} | {stat_val:<15} | {int(self.get_combat_power())}") 


champion_pool = {
    "WAR01": Warrior(
        champion_id="WAR01", 
        name="Rikkei Knight", 
        base_hp=1200, 
        base_atk=300, 
        shield_bonus=150
    ),
    "WAR02": Warrior(
        champion_id="WAR02", 
        name="Steel Guardian", 
        base_hp= 1200,            
        base_atk=250, 
        shield_bonus=200
    ),
    "MAG01": Mage(
        champion_id="MAG01", 
        name="Rikkei Wizard", 
        base_hp=800, 
        base_atk=500, 
        ability_power=0.5    
    )
}


def display_all(champion):
    print("--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")
    print("Mã     | Tên tướng            | Hệ       | HP    | ATK   | Chỉ số riêng      | Chiến lực")

    for c in champion.values():
        c.display_info()

def add_new_champion(pool):
    print("\n--- THÊM QUÂN CỜ MỚI ---")
    he_choice = input("Chọn Hệ (1 - Warrior, 2 - Mage): ")
    if he_choice not in ["1", "2"]:
        print("Lựa chọn hệ không hợp lệ!")
        return
    
    cid = input("Nhập mã tướng: ").strip()
    # Bẫy trùng mã tướng
    if cid in pool:
        print(f"Lỗi: Mã tướng [{cid}] đã tồn tại trong bể tướng!")
        return
        
    name = input("Nhập tên tướng: ")
    hp = int(input("Nhập HP: "))
    atk = int(input("Nhập ATK: "))
    
    if he_choice == "1":
        armor = int(input("Nhập Armor: "))
        new_champ = Warrior(cid, name, hp, atk, armor)
        pool[cid] = new_champ
        print(f"\nThêm tướng Warrior thành công!")
    else:
        ap = float(input("Nhập hệ số phép thuật (Ability Power): "))
        new_champ = Mage(cid, name, hp, atk, ap)
        pool[cid] = new_champ
        print(f"\nThêm tướng Mage thành công!")
        
    print(f"Mã: {new_champ.champion_id} | Tên: {new_champ.name} | Chiến lực: {int(new_champ.get_combat_power())}")

def compare_two_champions(pool):
    print("\n--- SO SÁNH SỨC MẠNH 2 QUÂN CỜ ---")
    id1 = input("Nhập mã tướng thứ nhất: ").strip()
    id2 = input("Nhập mã tướng thứ hai: ").strip()
    
    # Bẫy mã tướng không tồn tại
    c1 = pool.get(id1)
    c2 = pool.get(id2)
    
    if not c1:
        print(f"Mã tướng [{id1}] không hợp lệ!")
        return
    if not c2:
        print(f"Mã tướng [{id2}] không hợp lệ!")
        return
        
    print("\nThông tin so sánh:")
    print(f"{c1.champion_id} - {c1.name} | Hệ: {c1.get_he()} | Chiến lực: {int(c1.get_combat_power())}")
    print(f"{c2.champion_id} - {c2.name} | Hệ: {c2.get_he()} | Chiến lực: {int(c2.get_combat_power())}")
    
    if c1 > c2:
        print(f"Kết quả: {c1.champion_id} - {c1.name} mạnh hơn {c2.champion_id} - {c2.name}.")
    elif c2 > c1:
        print(f"Kết quả: {c2.champion_id} - {c2.name} mạnh hơn {c1.champion_id} - {c1.name}.")
    else:
        print("Kết quả: Hai quân cờ có chiến lực ngang nhau.")

def calculate_team_total_power(pool):
    print("\n--- TÍNH TỔNG CHIẾN LỰC ĐỘI HÌNH RA SÂN ---")
    input_str = input("Nhập danh sách mã tướng, cách nhau bằng dấu phẩy: ")
    list_ids = [cid.strip() for cid in input_str.split(",") if cid.strip()]
    
    print("\nDanh sách đội hình:")
    total_power = 0
    count = 1
    
    for cid in list_ids:
        if cid not in pool:
            print(f"Mã tướng [{cid}] không hợp lệ, bỏ qua!")
            continue
            
        c = pool[cid]
        print(f"{count}. {c.champion_id} - {c.name} | Chiến lực: {int(c.get_combat_power())}")
        
        total_power = total_power + c
        count += 1
        
    print(f"Tổng chiến lực đội hình: {int(total_power)}")



def main():
    while True: 
        print("""
        1. Xem danh sách tướng 
        2. Thêm tướng mới
        3. So sánh 2 quân cờ 
        4. Tính tổng chiến lực đội hình ra sân 
        5. Thoát chương trình 
         """)
        
        choice = input("Nhập lựa chọn của bạn từ(1-5): ")
        match choice:
            case "1":
                display_all(champion_pool) 
            case "2":
                add_new_champion(champion_pool)
            case "3":
                compare_two_champions(champion_pool)
            case "4":
                calculate_team_total_power(champion_pool)
            case "5":
                print("Chọn chức năng (1-5): 5")
                print("Cảm ơn bạn đã sử dụng Rikkei RPG - Auto-Battler Manager!")
                break

if __name__ == "__main__":
    main() 