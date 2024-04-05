from Grid import Grid # เพิ่ม class Grid จาก Grid.py
from Blocks import * # เพิ่ม class Blocks จาก Blocks.py
import random # เพิ่มไลบารี่ random
import pygame # เพิ่มไลบารี่ pygame

class Game: # สร้าง class Game
    def __init__(self): # รับพารามิเตอร์เพื่อเข้าถึงคุณสมบัติ
        self.grid = Grid() # สร้างกริดข้อมูลเปล่าๆ
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        # สร้างบล็อกทั้งหมดที่มีในเกม

        self.current_block = self.get_random_block()  # กำหนดบล็อกปัจจุบันที่จะใช้ในการเล่น
        self.next_block = self.get_random_block() # กำหนดบล็อกต่อไปที่จะใช้ในการเล่น
        self.game_over = False  # กำหนดสถานะเกมว่ายังไม่ Game Over
        self.score = 0 # กำหนดคะแนนเริ่มต้นให้เป็น 0
        self.rotate_sound = pygame.mixer.Sound("music/Cartoon Boing.mp3")
        # โหลดเสียงสำหรับการหมุนบล็อก
        self.clear_sound = pygame.mixer.Sound("music/Wood Plank Flicks.mp3")
         # โหลดเสียงสำหรับเมื่อลบแถว

        pygame.mixer.music.load("music/Girasol - Quincas Moreira.mp3")
        # โหลดเพลงเพื่อให้เป็นเสียงพื้นหลัง
        pygame.mixer.music.play()
        # เล่นเพลงเพื่อให้เป็นเสียงพื้นหลังของเกม
    
    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100  # เพิ่มคะแนน 100 เมื่อลบแถว 1 แถว
        elif lines_cleared == 2:
            self.score += 300 # เพิ่มคะแนน 300 เมื่อลบแถว 2 แถว
        elif lines_cleared == 3:
            self.score += 500 # เพิ่มคะแนน 500 เมื่อลบแถว 3 แถว
        self.score += move_down_points # เพิ่มคะแนนจากการเลื่อนลงของบล็อก
 
    def get_random_block(self):
        if len(self.blocks) == 0: # ถ้าไม่มีบล็อกที่เหลือในลิสต์
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
            # เพิ่มบล็อกทั้งหมดเข้าไปใหม่
        block = random.choice(self.blocks) # เลือกบล็อกจากลิสต์โดยสุ่ม
        self.blocks.remove(block) # ลบบล็อกที่ถูกสุ่มเลือกออกจากลิสต์
        return block # คืนค่าบล็อกที่ถูกสุ่มเลือกออกมา
    
    def move_left(self):
        self.current_block.move(0,-1) 
        # เคลื่อนที่บล็อกปัจจุบันไปทางซ้ายหนึ่งช่อง (เพิ่มตำแหน่ง column ลบออกหนึ่ง)
        if self.block_inside() == False or self.block_fits() == False:
            # ตรวจสอบว่าบล็อกอยู่ในกริดหรือไม่ และว่าบล็อกพอจะตั้งอยู่ในตำแหน่งนั้นหรือไม่ 
            self.current_block.move(0,1)

    def move_right(self):
        self.current_block.move(0,1)
        # เคลื่อนที่บล็อกปัจจุบันไปทางขวาหนึ่งช่อง (เพิ่มตำแหน่ง column ขึ้นอยู่ 1)
        if self.block_inside() == False or self.block_fits() == False:
            # ตรวจสอบว่าบล็อกอยู่ในกริดหรือไม่ และว่าบล็อกพอจะตั้งอยู่ในตำแหน่งนั้นหรือไม่
            self.current_block.move(0,-1)
    
    def move_down(self):
        self.current_block.move(1,0) 
        # เคลื่อนที่บล็อกปัจจุบันลงมาหนึ่งช่อง (เพิ่มตำแหน่ง row ขึ้นอยู่ 1)
        if self.block_inside() == False or self.block_fits() == False:
            # ตรวจสอบว่าบล็อกอยู่ในกริดหรือไม่ และว่าบล็อกพอจะตั้งอยู่ในตำแหน่งนั้นหรือไม่
            self.current_block.move(-1,0)
            self.lock_block()
    
    def lock_block(self):
        tiles = self.current_block.get_cell_position() 
        # ดึงตำแหน่งของแต่ละเซลล์ในบล็อกที่ตั้งอยู่ปัจจุบัน
        for position in tiles:
            self.grid.grid[position.row][position.column]=self.current_block.id
        self.current_block = self.next_block # กำหนดให้บล็อกปัจจุบันเป็นบล็อกถัดไป
        self.next_block = self.get_random_block() # สุ่มบล็อกใหม่ที่จะเป็นบล็อกถัดไป
        rows_cleard = self.grid.clear_full_rows() 
        # ตรวจสอบและลบแถวที่เต็มในกริดและนับจำนวนแถวที่ถูกลบ
        
        # หากมีแถวที่ถูกลบ ให้เล่นเสียงที่ต้องการ (เช่น เสียงเมื่อลบแถว) และอัปเดตคะแนน
        if rows_cleard > 0:
            self.clear_sound.play()
            self.update_score(rows_cleard, 0)
        if self.block_fits() == False:
            self.game_over = True 
            # ตรวจสอบว่าบล็อกถัดไปจะสามารถเข้าไปได้หรือไม่ หากไม่สามารถเข้าไปได้แสดงว่าเกมจบลง
    
    def reset(self):
        self.grid.reset() # เรียกเมธอดในการรีเซ็ท
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        # สร้างลิสต์ของบล็อกทั้งหมดใหม่
        self.current_block = self.get_random_block()
        # สุ่มบล็อกใหม่เพื่อเป็นบล็อกปัจจุบัน 
        self.next_block = self.get_random_block()
        # สุ่มบล็อกใหม่เพื่อเป็นบล็อกถัดไป

    def block_fits(self):
        tiles = self.current_block.get_cell_position()
        # ดึงตำแหน่งของเซลล์ในบล็อกปัจจุบัน 

        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                # ตรวจสอบว่าตำแหน่งใดๆ ของบล็อกไม่ว่าง
                return False # ถ้ามีตำแหน่งใดตำแหน่งหนึ่งไม่ว่าง คืนค่า False
        return True  # ถ้าทุกตำแหน่งของบล็อกว่าง คืนค่า True

    def rotate(self):
        self.current_block.rotate() # เรียกใช้เมธอดในการหมุน
        if self.block_inside() ==False: 
            # ตรวจสอบว่าหลังจากหมุนบล็อกแล้ว บล็อกนั้นอยู่ในตำแหน่งที่ถูกต้องหรือไม่ 
            self.current_block.undo_rotation()
            # หากบล็อกหมุนแล้วไม่ได้อยู่ในตำแหน่งที่ถูกต้อง (ไม่อยู่ภายในกริด) จะทำการย้อนกลับการหมุนให้เป็นตำแหน่งเดิม
        else:
            self.rotate_sound.play()
            # กรณีที่บล็อกหมุนแล้วอยู่ในตำแหน่งที่ถูกต้อง ให้เล่นเสียงการหมุนบล็อกด้วย 

    def block_inside(self):
        tiles = self.current_block.get_cell_position()
        # เรียกใช้เมธอดดึงตำแหน่งของแต่ละเซลล์ในบล็อกปัจจุบัน 
        for tile in tiles: # วนลูปผ่านเซลล์แต่ละตัวในบล็อกปัจจุบัน
            if self.grid.is_inside(tile.row, tile.column) == False:
                # ตรวจสอบว่าตำแหน่งของเซลล์นั้นอยู่ภายในขอบเขตของกริดหรือไม่ 
                return False
            # หากพบว่าเซลล์ใดๆ ในบล็อกปัจจุบันไม่ได้อยู่ภายในขอบเขตของกริด จะคืนค่า False
        return True
        # หากทุกเซลล์ในบล็อกปัจจุบันอยู่ภายในขอบเขตของกริดทั้งหมด จะคืนค่า True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 10, 10) 
        # เรียกใช้เมธอดของบล็อกปัจจุบัน
        
        if self.next_block.id == 3: # ตรวจสอบบล็อกถัดไป
            self.next_block.draw(screen, 255, 290)
            # หาก self.next_block.id == 3 ให้วาดบล็อกถัดไปที่ตำแหน่ง x=255 และ y=290
        elif self.next_block.id == 4:
            # หาก self.next_block.id == 4 ให้วาดบล็อกถัดไปที่ตำแหน่ง x=255 และ y=280
            self.next_block.draw(screen, 255, 280)
        else:
            # หากไม่ตรงกับเงื่อนไขข้างต้น ให้วาดบล็อกถัดไปที่ตำแหน่ง x=270 และ y=270
            self.next_block.draw(screen, 270, 270)
