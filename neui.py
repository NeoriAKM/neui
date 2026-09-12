# NeUI Beta 0.1
import os, time, sys

def clear(): print("\033[H\033[2J", end="")
def movetostart(): print("\033[H", end="")

class Draw:
    def __init__(self, delay=10, width=30, height=18):
        self.pos = [] # X, Y, SYMBOL, ID
        self.ui = [] # left:0-right:1, y, content, UI-ID

        self.w = width # ширина width
        self.h = height
        self.tact = delay / 1000 # милисекунды ms
    
    def find_index_by_id(self, target_id, ui=0):
        for i, (x, y, sym, id) in enumerate(self.pos if ui == 0 else self.ui):
            if id == target_id:
                return i
        return -1  # не найден notfound
    
    def find_length_ui(self):
        best = 0
        for i, (lr, y, content, id) in enumerate(self.ui):
            if lr == 0:
                if len(content) > best:
                    best = len(content)
        return best

    def draw(self):
        """No arguments
        Без аргументов"""
        
        margin = self.find_length_ui() + 2  # +2 для пробелов
        grid = [["." for _ in range(self.w)] for _ in range(self.h)]
        
        for x, y, sym, id in self.pos:
            if 0 <= x < self.w and 0 <= y < self.h:
                grid[y][x] = sym
        
        left_ui = {}
        right_ui = {}
        for lr, y, content, id in self.ui:
            if 0 <= y < self.h:
                if lr == 0:
                    left_ui[y] = content
                else:
                    right_ui[y] = content
        
        for y, row in enumerate(grid):
            left = left_ui.get(y, "")
            right = right_ui.get(y, "")
            field = " ".join(row)
            
            if left:
                print(f"{left}  {field}  {right}")
            else:
                print(" " * margin + field + " " + right)
        
        time.sleep(self.tact)
        clear()

    def add(self, pos):
        """(x, y, sym, ID)"""
        _, _, sym, id = pos
        if self.find_index_by_id(id) != -1: raise IndexError("this ID is taken")
        self.pos.append(pos)

    def move(self, id, x, y):
        index = self.find_index_by_id(id)
        _, _, sym, _ = self.pos[index]
        self.pos[index] = (x, y, sym, id)
    
    def remove(self, id):
        del self.pos[self.find_index_by_id(id)]

    def add_ui(self, pos):
        """(left_or_right_0_or_1, y, content)"""
        lr, y, content, id = pos

        if self.find_index_by_id(id, 1) != -1: raise IndexError("this UI ID is taken")
        self.ui.append(pos)

    def remove_ui(self, id):
        if self.find_index_by_id(id, 1) == -1: raise IndexError("UI ID not found. Maybe you got a mistake")
        del self.ui[self.find_index_by_id(id, 1)]
    
    def update_ui(self, content, id):
        index = self.find_index_by_id(id, 1)
        if index == -1: raise IndexError("UI ID not found. Maybe you got a mistake")
        lr, y, _, _ = self.ui[index]
        self.ui[index] = (lr, y, content, id)

    def getinfo(self, id, cortege_position):
        """0=x, 1=y, 2=symbol, 3=id"""
        index = self.find_index_by_id(id)
        return self.pos[index][cortege_position]

    def isempty(self, xt, yt):
        """Возвращает True или False, в зависимости от того, занята ли
        клетка или пуста. Занята - True. Пуста - False
        ---
        Returns True if cell is taken, else - False"""
        
        for i, (x, y, sym, id) in enumerate(self.pos):

            if x == xt and y == yt: return True
        return False
    
    def endsession(self, msg=''):
        clear()
        print(msg)
        sys.exit()