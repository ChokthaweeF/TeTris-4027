from Block import Block # เพิ่ม class Block ไฟล์ Block.py
from Position import Position # เพิ่ม class Position ไฟล์ Position.py

class LBlock(Block):
    def __init__(self):
        # เรียก constructor ของ superclass (Block) ด้วย super().__init__(id=1)
        super().__init__(id=1)

         # กำหนดตำแหน่งของเซลล์แต่ละตัวในแต่ละการหมุนของบล็อก
        self.cells = {
            0: [Position(0,2),Position(1,0),Position(1,1),Position(1,2)],
            1: [Position(0,1),Position(1,1),Position(2,1),Position(2,0)],
            2: [Position(1,0),Position(1,1),Position(1,2),Position(2,0)],
            3: [Position(0,0),Position(0,1),Position(1,1),Position(2,1)]
        }
        self.move(0, 3)  # เลื่อนตำแหน่งเริ่มต้นของบล็อกไปที่แถว 0 และคอลัมน์ 3 ในกริด

class JBlock(Block):
    def __init__(self):
        # เรียก constructor ของ superclass (Block) ด้วย super().__init__(id=2)
        super().__init__(id = 2)

        # กำหนดตำแหน่งของเซลล์แต่ละตัวในแต่ละการหมุนของบล็อก
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        self.move(0, 3) # เลื่อนตำแหน่งเริ่มต้นของบล็อกไปที่แถว 0 และคอลัมน์ 3 ในกริด

class IBlock(Block):
    def __init__(self):
        # เรียก constructor ของ superclass (Block) ด้วย super().__init__(id=3)
        super().__init__(id = 3)

        # กำหนดตำแหน่งของเซลล์แต่ละตัวในแต่ละการหมุนของบล็อก
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        self.move(-1, 3) # เลื่อนตำแหน่งเริ่มต้นของบล็อกไปที่แถว -1 และคอลัมน์ 3 ในกริด

class OBlock(Block):
    def __init__(self):
        # เรียก constructor ของ superclass (Block) ด้วย super().__init__(id=4)
        super().__init__(id = 4)

        # กำหนดตำแหน่งของเซลล์แต่ละตัวในแต่ละการหมุนของบล็อก
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }
        self.move(0, 4) # เลื่อนตำแหน่งเริ่มต้นของบล็อกไปที่แถว 0 และคอลัมน์ 4 ในกริด

class SBlock(Block):
    def __init__(self):
        # เรียก constructor ของ superclass (Block) ด้วย super().__init__(id=5)
        super().__init__(id = 5)

        # กำหนดตำแหน่งของเซลล์แต่ละตัวในแต่ละการหมุนของบล็อก
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3) # เลื่อนตำแหน่งเริ่มต้นของบล็อกไปที่แถว 0 และคอลัมน์ 3 ในกริด

class TBlock(Block):
    def __init__(self):
        # เรียก constructor ของ superclass (Block) ด้วย super().__init__(id=6)
        super().__init__(id = 6)

        # กำหนดตำแหน่งของเซลล์แต่ละตัวในแต่ละการหมุนของบล็อก
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3) # เลื่อนตำแหน่งเริ่มต้นของบล็อกไปที่แถว 0 และคอลัมน์ 3 ในกริด

class ZBlock(Block):
    def __init__(self):
        # เรียก constructor ของ superclass (Block) ด้วย super().__init__(id=7)
        super().__init__(id = 7)

        # กำหนดตำแหน่งของเซลล์แต่ละตัวในแต่ละการหมุนของบล็อก
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        self.move(0, 3) # เลื่อนตำแหน่งเริ่มต้นของบล็อกไปที่แถว 0 และคอลัมน์ 3 ในกริด