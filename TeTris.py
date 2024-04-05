import pygame # เพิ่มไลบารี่ pygame
from Game import Game # เพิ่มคลาส Game จากไฟล์ Game.py
from Colors import Colors # เพิ่มคลาส Colors จากไฟล์ Colors.py

pygame.init() # เรียกเมธอดเพื่อเริ่มต้นใช้งาน pygame

title_font = pygame.font.Font(None, 40) # สร้างอ็อบเจกต์ของฟอนต์  
score_surface = title_font.render("Score", True, Colors.white) 
# แสดง Surface ของ "Score" ที่ตำแหน่ง (x, y) บนหน้าจอ

next_surface = title_font.render("Next", True, Colors.white)
# แสดง Surface ของ "Next" ที่ตำแหน่ง (x, y) บนหน้าจอ

game_over_surface = title_font.render("GAME OVER", True, Colors.drakred)
# แสดง Surface ของ "GAME OVER" ที่ตำแหน่ง (x, y) บนหน้าจอ

# เรียกใช้เมธอดในการกำหนดตำแหน่งและตรวจสอบการชนกันสิ่งของในเกม
score_rect = pygame.Rect(320, 55, 170, 60) 
next_rect = pygame.Rect(320, 215, 170, 180)


screen_width=500 # กำหนดค่าให้ตัวแปร
screen_height=620 # กำหนดค่าให้ตัวแปร

screen=pygame.display.set_mode((screen_width,screen_height)) 
# เรียกใช้เมธอดเพื่อสร้างหน้าต่างเกม
pygame.display.set_caption("Tetris 4027") 
# เรียกใช้เมธอดเพืื่อแสดงชื่อหัวข้อของหน้าต่างเกม

clock = pygame.time.Clock() # กำหนดอ็อบเจกต์ของคลาส
FPS = 60 # กำหนดค่าตัวแปร

game = Game()

GAME_UPDATE = pygame.USEREVENT # กำหนดตัวแปรเพื่อเรียกใช้ event ต่างๆ
pygame.time.set_timer(GAME_UPDATE, 200)
# กำหนดเมธอดที่ใช้ตั้งค่าเวลาสำหรับ event ต่างๆ

# LOOP
run=True # กำหนดค่าตัวแปร
while run: 

    #event hand
    for event in pygame.event.get(): # กำหนดลูปของเหตุการณ์ต่างๆ
        if event.type == pygame.QUIT: # กำหนดเงื่อนไขเป็นตรวจสอบเหตุการณ์การปิดหน้าต่าง
            run = False # ออกจากลูป(ปิดโปรแกรม)
        if event.type == pygame.KEYDOWN: # กำหนดเงื่อนไขตรวจสอบแป้นพิมพ์
            if game.game_over == True: # กำหนดสถานะของเกม (True คือจบไปแล้ว)
                game.game_over = False # กำหนดสถานะของเกม (False คือการเริ่มรีเซ็ทเกม)
                game.reset() # เรียกใช้เมธอดเพื่อรีเซ็ทเกม
            if event.key == pygame.K_LEFT and game.game_over == False: 
                # กำหนดเงื่อนไขตรวจสอบแป้นพิมพ์และสถานะของเกม

                game.move_left() # เรียกใช้เมธอดเพื่อเลื่อนไปด้านซ้าย 1 ช่อง
            if event.key == pygame.K_RIGHT and game.game_over == False: 
                # กำหนดเงื่อนไขตรวจสอบแป้นพิมพ์และสถานะของเกม

                game.move_right() # เรียกใช้เมธอดเพื่อเลื่อนไปด้านขวา 1 ช่อง
            if event.key == pygame.K_DOWN and game.game_over == False: 
                # กำหนดเงื่อนไขตรวจสอบแป้นพิมพ์และสถานะของเกม

                game.move_down() # เรียกใช้เมธอดเพื่อเลื่อนไปด้านล่าง 1 ช่อง
            if event.key == pygame.K_UP and game.game_over == False: 
                # กำหนดเงื่อนไขตรวจสอบแป้นพิมพ์และสถานะของเกม

                game.rotate() # เรียกใช้เมธอดเพื่อหมุนทิศทางบล็อก
        if event.type == GAME_UPDATE and game.game_over == False: 
            # กำหนดเงื่อนไขเป็นตรวจสอบเหตุการณ์และสถานะของเกม

            game.move_down() # เรียกใช้เมธอดเพื่อเลื่อนไปด้านล่าง 1 ช่อง
    #draw
    score_value_surface = title_font.render(str(game.score), True, Colors.blue)
    # โหลดฟอนต์อ็อปเจกต์มา render เป็นค่า score 

    screen.fill(Colors.blue) # เติมสีพื้นหลัง
    screen.blit(score_surface, (365, 20, 50, 50)) # แสดง surface ของค่า score
    screen.blit(next_surface, (375, 180, 50, 50)) # แสดง surface ของค่า next

    #If game over
    if game.game_over == True: # เงื่อนไขตรวจสอบเกมจบหรือไม่
        screen.blit(game_over_surface, (320, 450, 50, 50)) 
         # ใช้แสดง Surface ของข้อความ "GAME OVER"

    # ใช้เมธอดในการสร้างสี่เหลี่ยมผืนผ้าและแสดงออกทางจอ
    pygame.draw.rect(screen, Colors. lightgreen, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, 
		centery = score_rect.centery))
    pygame.draw.rect(screen, Colors. lightgrey, next_rect, 0, 10)
    game.draw(screen)
    
    clock.tick(FPS)
    #update display
    pygame.display.update()
pygame.quit