class Settings:
    def __init__(self, stages:str, constants:dict[str]):
        self.stages = stages
        self.constants = constants
        pass


class Player_Stats: 
    def __init__(self,frame_rate:int,speed_walk:int,speed_run:int,gravity:int,jump:int):
        self.frame_rate = frame_rate
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump = jump

class Enemy_stats:
    def __init__(self,quantity:int,frame_rate:int,speed_walk:int,speed_run:int,gravity:int,jump:int):
        self.frame_rate = frame_rate
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump = jump
        self.quantity = quantity