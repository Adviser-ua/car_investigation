# coding: utf-8
# Konstantyn Davidenko


class SceneBase:
    def __init__(self, game):
        self.next = self
        self.game = game

    def ProcessInput(self, events):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene


class GameLevel(SceneBase):
    pass