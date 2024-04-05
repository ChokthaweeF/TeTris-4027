class Colors: # สร้าง class Colors
    lightgrey = (0, 0, 0) # สีเทาอ่อน
    lime = (102, 255, 102) # สีเขียวไลม์
    pink = (255, 102, 153) # สีชมพู
    lightorange = (255, 153, 102) # สีส้มอ่อน
    yellow = (255, 255, 153) # สีเหลือง
    purple = (153, 102, 255) # สีม่วง
    cyan = (204, 255, 255) # สีซีอัน (ฟ้าอมเขียว)
    lightblue = (102, 153, 255) # สีฟ้าอ่อน
    white = (255, 255, 255) # สีขาว
    red = (255, 0, 0) #  สีแดง
    green = (0, 255, 0) # สีเขียว
    blue = (0, 0, 255) # สีน้ำเงิน
    lightgreen = (204, 255, 255) #  สีเขียวอ่อน
    drakred = (204, 0, 102) #  สีแดงเข้ม
    gold = (255, 204, 0) # สีทอง
    
    @classmethod
    def get_cell_colors(cls): # ที่รับค่าจากคลาสเพื่อคืนค่ารายการสีนั้นๆ 
        return[cls.lightgrey, cls.lime, cls.pink, cls.lightorange, cls.yellow, cls.purple, cls.cyan, cls.lightblue]
            