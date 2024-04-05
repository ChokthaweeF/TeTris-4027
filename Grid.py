import pygame # เพิ่มไลบารี่ pygame
from Colors import Colors # เพิ่มคลาส Colors จากไฟล์ Colors.py

class Grid: # สร้าง class Grid
    def __init__(self): # รับพารามิเตอร์เพื่อเข้าถึงคุณสมบัติ
        self.num_rows =20 # กำหนดจำนวนแถวในกริด
        self.num_cols =10 # กำหนดจำนวนคอลัมน์ในกริด
        self.cell_size =30 # กำหนดขนาดของเซลล์ในกริด
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
         # สร้างกริดเปล่าๆ โดยกำหนดค่าเริ่มต้นให้เป็น 0
        self.colors = Colors.get_cell_colors()
         # ดึงข้อมูลสีของเซลล์จาก Colors class โดยใช้เมทอด get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end= " ")
                # แสดงค่าในเซลล์นั้นๆ และใช้ end=" " เพื่อให้เคอร์เซอร์เคลื่อนไปในบรรทัดถัดไป
            print() # ขึ้นบรรทัดใหม่หลังจากแสดงค่าในแต่ละคอลัมน์ในแถวนั้นเสร็จ

    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True # ถ้าตำแหน่งอยู่ภายในกริด ให้คืนค่า True
        return False # ถ้าตำแหน่งอยู่นอกกริด ให้คืนค่า False
    
    def is_empty(self, row, column):
        if self.grid[row][column] == 0: # ถ้าค่าในเซลล์ตำแหน่งที่กำหนดเป็น 0 (หมายถึงว่าว่าง)
            return True # คืนค่า True ว่าเซลล์นี้ว่าง
        return False # คืนค่า False ว่าเซลล์นี้ไม่ว่าง

    
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0: # ถ้ามีเซลล์ในแถวที่ยังว่าง
                return False # คืนค่า False ว่าแถวนี้ยังไม่เต็ม
        return True # คืนค่า True ว่าแถวนี้เต็มทั้งแถว
    
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0  
            # กำหนดค่าของทุกเซลล์ในแถวที่กำหนดให้เป็น 0 (ค่าว่าง)

    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            # เลื่อนค่าในเซลล์ในแถว row ลงไป num_rows แถวด้านล่าง
            self.grid[row+num_rows][column] = self.grid[row][column]
             # หลังจากเลื่อนแล้วให้เซลล์ในแถว row เป็นค่าว่าง (0)
            self.grid[row][column] = 0

    def clear_full_rows(self):
        complete = 0 # นับจำนวนแถวที่ถูกเต็มและถูกลบ
        for row in range(self.num_rows-1, 0, -1):
            # วนลูปจากแถวล่างสุดไปข้างบน
            if self.is_row_full(row): # ถ้าแถวนี้เต็ม
                self.clear_row(row) # ลบแถวนี้
                complete += 1 # เพิ่มจำนวนแถวที่ถูกลบ
            elif complete > 0: # ถ้ามีแถวที่ถูกลบอยู่
                self.move_row_down(row, complete) 
                # เลื่อนแถวลงเพื่อกระเทียบกับจำนวนแถวที่ถูกลบ
        return complete
    # คืนค่าจำนวนแถวที่ถูกลบ
    
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0         
                # กำหนดค่าในเซลล์ทุกเซลล์ในกริดให้เป็น 0 (ค่าว่าง)    
    
    def draw(self,screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column] # ดึงค่าที่อยู่ในเซลล์นั้นๆ จากกริด
                # สร้างสี่เหลี่ยมสี่เหลี่ยมเล็กที่จะเป็นเซลล์ในกริด
                cell_rect = pygame.Rect(column*self.cell_size+11, row*self.cell_size+11, 
                self.cell_size-1, self.cell_size-1)
                # วาดสี่เหลี่ยมสี่เหลี่ยมเล็กที่จะแสดงเซลล์ในกริดด้วยสีที่เกี่ยวข้องกับค่าในเซลล์
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)