from Colors import Colors # เพิ่ม class Colors ไฟล์ Colors.py
import pygame # เพิ่มไลบารี่ pygame
from Position import Position # เพิ่ม class Position ไฟล์ Position.py

class Block: # สร้าง class Block
    def __init__(self, id):
        self.id = id
        self.cells ={} # สร้าง dictionary ที่ใช้เก็บเซลล์ (cells)
        self.cell_size = 30 # ขนาดของเซลล์ 30 พิกเซล
        self.row_offset = 0 # กำหนดค่า offset สำหรับการเคลื่อนที่แถวของเซลล์ในกริด
        self.column_offset = 0 # กำหนดค่า offset สำหรับการเคลื่อนที่คอลัมน์ของเซลล์ในกริด
        self.rotation_state =0 # กำหนดสถานะเริ่มต้นของการหมุนเซลล์ในกริด
        self.colors = Colors.get_cell_colors() # ดึงสีที่ใช้แสดงบนเซลล์มาจากคลาส Colors

    def move(self, rows, columns):
        self.row_offset += rows # เพิ่มหรือลดการเคลื่อนที่ของแถว
        self.column_offset += columns # เพิ่มหรือลดการเคลื่อนที่ของคอลัมน์
    
    def get_cell_position(self):
        tiles=self.cells[self.rotation_state]
        # เลือกตำแหน่งของเซลล์ที่มีการหมุนตาม self.rotation_state
        moved_tiles = []  # สร้างรายการเพื่อเก็บตำแหน่งของเซลล์หลังจากการเคลื่อนที่
        for position in tiles:
             # คำนวณตำแหน่งใหม่ของเซลล์หลังจากการเคลื่อนที่แล้วและเพิ่มเข้าไปในรายการ moved_tiles
            position = Position(position.row+ self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles # ส่งคืนรายการของตำแหน่งของเซลล์หลังจากการเคลื่อนที่แล้ว

    def rotate(self):
        self.rotation_state += 1 # เพิ่มค่าของการหมุนเซลล์
        if self.rotation_state == len(self.cells):
            # ตรวจสอบว่าเมื่อหมุนถึงขอบเขตของตำแหน่งที่เป็นไปได้หมดแล้ว
            self.rotation_state = 0
            # กลับมาที่สถานะเริ่มต้น

    def undo_rotation(self):
        self.rotation_state -= 1 # ลดค่าของการหมุนเซลล์
        if self.rotation_state == -1:  
            # ตรวจสอบว่าถ้าหมุนไปถึงสถานะ -1 ให้กลับมาที่สถานะสุดท้ายของการหมุน
            self.rotation_state = len(self.cells) - 1
            # กลับไปยังสถานะสุดท้ายของการหมุน

    def draw (self, screen, offset_x, offset_y):
        tiles = self.get_cell_position() # รับตำแหน่งของเซลล์ที่จะวาด
        for tile in tiles:
            # สร้าง rectangle สำหรับเซลล์แต่ละตัว
            tile_rect = pygame.Rect(offset_x + tile.column*self.cell_size+1, 
                offset_y + tile.row*self.cell_size+1, self.cell_size-1, self.cell_size-1) 
            # วาดเซลล์ด้วยสีที่กำหนดใน self.colors[self.id] บนหน้าจอ
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)