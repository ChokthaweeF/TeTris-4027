class Colors: 
    lightgrey = (0, 0, 0)
    lime = (102, 255, 102)
    pink = (255, 102, 153)
    lightorange = (255, 153, 102)
    yellow = (255, 255, 153)
    purple = (153, 102, 255)
    cyan = (204, 255, 255)
    lightblue = (102, 153, 255)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    lightgreen = (204, 255, 255)
    drakred = (204, 0, 102)
    gold = (255, 204, 0)
    
    @classmethod
    def get_cell_colors(cls):
        return[cls.lightgrey, cls.lime, cls.pink, cls.lightorange, cls.yellow, cls.purple, cls.cyan, cls.lightblue]