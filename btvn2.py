from abc import ABC, abstractmethod

# Lớp cha: Khuôn mẫu Tướng sử dụng Abstract Base Class (ABC)
class Hero(ABC):
    
    @abstractmethod
    def use_ultimate(self):
        """Phương thức trừu tượng: Ép buộc tất cả các lớp con phải ghi đè"""
        pass

# Lớp con 1: Pháp Sư (Kế thừa và ghi đè đúng quy chuẩn)
class Mage(Hero):
    def use_ultimate(self):
        print("🔥 Pháp Sư tung chiêu: MƯA SAO BĂNG!")

# Lớp con 2: Sát Thủ (Đã được sửa tên hàm để override chính xác)
class Assassin(Hero):
    # SỬA LỖI: Đổi tên từ stealth_kill thành use_ultimate theo đúng thiết kế của Hero
    def use_ultimate(self):
        print("🗡️ Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")


print("--- LOADING TRẬN ĐẤU ---")

team_heroes = [Mage(), Assassin()] 
print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")

print("\n--- GIAO TRANH TỔNG BẮT ĐẦU ---")
for hero in team_heroes:
    hero.use_ultimate() 