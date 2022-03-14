import heapq
import sys
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Canvas, ALL, NW

class Cons:

    BOARD_WIDTH = 500
    BOARD_HEIGHT = 400
    DELAY = 500
    DOT_SIZE = 20

class Board(Canvas):

    def __init__(self,mutari):
        super().__init__(width=Cons.BOARD_WIDTH, height=Cons.BOARD_HEIGHT,
            background="white", highlightthickness=0)
        #easy mode
        self.initGame3()
        self.mutari=mutari
        #medium mode
 #       self.initGame2()
        #hard mode
#        self.initGame3()
        self.pack()

    def initGame1(self):
        self.inGame = True
        self.holes = 6
        self.finish = 1
        self.score = 0
        self.moveX = 0
        self.moveY = 0
        self.loadImages()
        self.createObjects1()
        self.bind_all("<Key>", self.onKeyPressed)
        self.after(Cons.DELAY, self.onTimer)

    def initGame2(self):
        self.inGame = True
        self.holes = 18
        self.finish = 1
        self.score = 0
        self.moveX = 0
        self.moveY = 0
        self.loadImages()
        self.createObjects2()
        self.bind_all("<Key>", self.onKeyPressed)
        self.after(Cons.DELAY, self.onTimer)

    def initGame3(self):
        self.inGame = True
        self.holes = 40
        self.finish = 1
        self.score = 0
        self.moveX = 0
        self.moveY = 0
        self.loadImages()
        self.createObjects3()
        self.bind_all("<Key>", self.onKeyPressed)
        self.after(Cons.DELAY, self.onTimer)

    def loadImages(self):

        try:
            self.iball = Image.open("imgball.png")
            resized_image = self.iball.resize((15, 15), Image.ANTIALIAS)
            self.ball = ImageTk.PhotoImage(resized_image)

        except IOError as e:
            print(e)
            sys.exit(1)

    def createObjects1(self):

        self.create_text(30, 10, text="Score: {0}".format(self.score),tag="score", fill="white")
        self.create_image(22, 22, image=self.ball, anchor=NW,  tag="ball")
        self.create_rectangle(0, 0, 20, 20, fill='red', tag="wall")
        self.create_rectangle(20, 0, 40, 20, fill='red', tag="wall")
        self.create_rectangle(40, 0, 60, 20, fill='red', tag="wall")
        self.create_rectangle(60, 0, 80, 20, fill='red', tag="wall")
        self.create_rectangle(80, 0, 100, 20, fill='red', tag="wall")
        self.create_rectangle(100, 0, 120, 20, fill='red', tag="wall")
        self.create_rectangle(120, 0, 140, 20, fill='red', tag="wall")
        self.create_rectangle(140, 0, 160, 20, fill='red', tag="wall")
        self.create_rectangle(160, 0, 180, 20, fill='red', tag="wall")
        self.create_rectangle(180, 0, 200, 20, fill='red', tag="wall")
        self.create_rectangle(200, 0, 220, 20, fill='red', tag="wall")
        self.create_rectangle(0, 20, 20, 40, fill='red', tag="wall")
        # my_ball = my_canvas.create_image(20, 20, anchor=NW, image=ballImage)
        self.create_rectangle(80, 20, 100, 40, fill='red', tag="wall")
        self.create_oval(102, 22, 118, 38, fill='black', tag="hole")
        self.create_rectangle(120, 20, 140, 40, fill='red', tag="wall")
        self.create_oval(142, 22, 158, 38, fill='black', tag="hole")
        self.create_rectangle(200, 20, 220, 40, fill='red', tag="wall")
        self.create_rectangle(0, 40, 20, 60, fill='red', tag="wall")
        self.create_rectangle(80, 40, 100, 60, fill='red', tag="wall")
        self.create_rectangle(120, 40, 140, 60, fill='red', tag="wall")
        self.create_rectangle(200, 40, 220, 60, fill='red', tag="wall")
        self.create_rectangle(0, 60, 20, 80, fill='red', tag="wall")
        self.create_oval(22, 62, 38, 78, fill='black', tag="hole")
        self.create_rectangle(80, 60, 100, 80, fill='red', tag="wall")
        self.create_oval(182, 62, 198, 78, fill='black', tag="hole")
        self.create_rectangle(200, 60, 220, 80, fill='red', tag="wall")
        self.create_rectangle(0, 80, 20, 100, fill='red', tag="wall")
        self.create_rectangle(80, 80, 100, 100, fill='red', tag="wall")
        self.create_rectangle(120, 80, 140, 100, fill='red', tag="wall")
        self.create_rectangle(200, 80, 220, 100, fill='red', tag="wall")
        self.create_rectangle(0, 100, 20, 120, fill='red', tag="wall")
        self.create_oval(22, 102, 38, 118, fill='black', tag="hole")
        self.create_oval(142, 102, 158, 118, fill='black', tag="hole")
        self.create_oval(182, 102, 198, 118, fill='yellow', tag="finish")
        self.create_rectangle(200, 100, 220, 120, fill='red', tag="wall")
        self.create_rectangle(0, 120, 20, 140, fill='red', tag="wall")
        self.create_rectangle(20, 120, 40, 140, fill='red', tag="wall")
        self.create_rectangle(40, 120, 60, 140, fill='red', tag="wall")
        self.create_rectangle(60, 120, 80, 140, fill='red', tag="wall")
        self.create_rectangle(80, 120, 100, 140, fill='red', tag="wall")
        self.create_rectangle(100, 120, 120, 140, fill='red', tag="wall")
        self.create_rectangle(120, 120, 140, 140, fill='red', tag="wall")
        self.create_rectangle(140, 120, 160, 140, fill='red', tag="wall")
        self.create_rectangle(160, 120, 180, 140, fill='red', tag="wall")
        self.create_rectangle(180, 120, 200, 140, fill='red', tag="wall")
        self.create_rectangle(200, 120, 220, 140, fill='red', tag="wall")

    def createObjects2(self):
        self.create_text(30, 10, text="Score: {0}".format(self.score),tag="score", fill="white")
        self.create_image(22, 282, image=self.ball, anchor=NW, tag="ball")
        self.create_rectangle(0, 0, 20, 20, fill='red', tag="wall")
        self.create_rectangle(20, 0, 40, 20, fill='red', tag="wall")
        self.create_rectangle(40, 0, 60, 20, fill='red', tag="wall")
        self.create_rectangle(60, 0, 80, 20, fill='red', tag="wall")
        self.create_rectangle(80, 0, 100, 20, fill='red', tag="wall")
        self.create_rectangle(100, 0, 120, 20, fill='red', tag="wall")
        self.create_rectangle(120, 0, 140, 20, fill='red', tag="wall")
        self.create_rectangle(140, 0, 160, 20, fill='red', tag="wall")
        self.create_rectangle(160, 0, 180, 20, fill='red', tag="wall")
        self.create_rectangle(180, 0, 200, 20, fill='red', tag="wall")
        self.create_rectangle(200, 0, 220, 20, fill='red', tag="wall")
        self.create_rectangle(0, 20, 20, 40, fill='red', tag="wall")
        self.create_oval(22, 22, 38, 38, fill='black', tag="hole")
        self.create_oval(102, 22, 118, 38, fill='black', tag="hole")
        self.create_rectangle(120, 20, 140, 40, fill='red', tag="wall")
        self.create_oval(142, 22, 158, 38, fill='black', tag="hole")
        self.create_rectangle(160, 20, 180, 40, fill='red', tag="wall")
        self.create_rectangle(200, 20, 220, 40, fill='red', tag="wall")
        self.create_rectangle(0, 40, 20, 60, fill='red', tag="wall")
        self.create_rectangle(200, 40, 220, 60, fill='red', tag="wall")
        self.create_rectangle(0, 60, 20, 80, fill='red', tag="wall")
        self.create_oval(182, 62, 198, 78, fill='black', tag="hole")
        self.create_rectangle(200, 60, 220, 80, fill='red', tag="wall")
        self.create_rectangle(0, 80, 20, 100, fill='red', tag="wall")
        self.create_rectangle(20, 80, 40, 100, fill='red', tag="wall")
        self.create_rectangle(60, 80, 80, 100, fill='red', tag="wall")
        self.create_rectangle(80, 80, 100, 100, fill='red', tag="wall")
        self.create_rectangle(100, 80, 120, 100, fill='red', tag="wall")
        self.create_rectangle(120, 80, 140, 100, fill='red', tag="wall")
        self.create_rectangle(160, 80, 180, 100, fill='red', tag="wall")
        self.create_rectangle(200, 80, 220, 100, fill='red', tag="wall")
        self.create_rectangle(0, 100, 20, 120, fill='red', tag="wall")
        self.create_rectangle(60, 100, 80, 120, fill='red', tag="wall")
        self.create_oval(102, 102, 118, 118, fill='black', tag="hole")
        self.create_rectangle(120, 100, 140, 120, fill='red', tag="wall")
        self.create_rectangle(160, 100, 180, 120, fill='red', tag="wall")
        self.create_rectangle(200, 100, 220, 120, fill='red', tag="wall")
        self.create_rectangle(0, 120, 20, 140, fill='red', tag="wall")
        self.create_oval(22, 122, 38, 138, fill='black', tag="hole")
        self.create_rectangle(120, 120, 140, 140, fill='red', tag="wall")
        self.create_rectangle(160, 120, 180, 140, fill='red', tag="wall")
        self.create_rectangle(200, 120, 220, 140, fill='red', tag="wall")
        self.create_rectangle(0, 140, 20, 160, fill='red', tag="wall")
        self.create_rectangle(20, 140, 40, 160, fill='red', tag="wall")
        self.create_rectangle(40, 140, 60, 160, fill='red', tag="wall")
        self.create_rectangle(60, 140, 80, 160, fill='red', tag="wall")
        self.create_rectangle(120, 140, 140, 160, fill='red', tag="wall")
        self.create_rectangle(200, 140, 220, 160, fill='red', tag="wall")
        self.create_rectangle(0, 160, 20, 180, fill='red', tag="wall")
        self.create_oval(22, 162, 38, 178, fill='black', tag="hole")
        self.create_rectangle(120, 160, 140, 180, fill='red', tag="wall")
        self.create_oval(142, 162, 158, 178, fill='black', tag="hole")
        self.create_rectangle(160, 160, 180, 180, fill='red', tag="wall")
        self.create_rectangle(200, 160, 220, 180, fill='red', tag="wall")
        self.create_rectangle(0, 180, 20, 200, fill='red', tag="wall")
        self.create_oval(62, 182, 78, 198, fill='black', tag="hole")
        self.create_rectangle(80, 180, 100, 200, fill='red', tag="wall")
        self.create_oval(102, 182, 118, 198, fill='black', tag="hole")
        self.create_rectangle(120, 180, 140, 200, fill='red', tag="wall")
        self.create_rectangle(160, 180, 180, 200, fill='red', tag="wall")
        self.create_rectangle(200, 180, 220, 200, fill='red', tag="wall")
        self.create_rectangle(0, 200, 20, 220, fill='red', tag="wall")
        self.create_rectangle(40, 200, 60, 220, fill='red', tag="wall")
        self.create_rectangle(60, 200, 80, 220, fill='red', tag="wall")
        self.create_rectangle(80, 200, 100, 220, fill='red', tag="wall")
        self.create_rectangle(160, 200, 180, 220, fill='red', tag="wall")
        self.create_rectangle(200, 200, 220, 220, fill='red', tag="wall")
        self.create_rectangle(0, 220, 20, 240, fill='red', tag="wall")
        self.create_rectangle(80, 220, 100, 240, fill='red', tag="wall")
        self.create_rectangle(120, 220, 140, 240, fill='red', tag="wall")
        self.create_rectangle(160, 220, 180, 240, fill='red', tag="wall")
        self.create_oval(182, 222, 198, 238, fill='yellow', tag="finish")
        self.create_rectangle(200, 220, 220, 240, fill='red', tag="wall")
        self.create_rectangle(0, 240, 20, 260, fill='red', tag="wall")
        self.create_rectangle(40, 240, 60, 260, fill='red', tag="wall")
        self.create_rectangle(120, 240, 140, 260, fill='red', tag="wall")
        self.create_rectangle(160, 240, 180, 260, fill='red', tag="wall")
        self.create_rectangle(180, 240, 200, 260, fill='red', tag="wall")
        self.create_rectangle(200, 240, 220, 260, fill='red', tag="wall")
        self.create_rectangle(0, 260, 20, 280, fill='red', tag="wall")
        self.create_oval(22, 262, 38, 278, fill='black', tag="hole")
        self.create_rectangle(40, 260, 60, 280, fill='red', tag="wall")
        self.create_rectangle(60, 260, 80, 280, fill='red', tag="wall")
        self.create_rectangle(80, 260, 100, 280, fill='red', tag="wall")
        self.create_rectangle(120, 260, 140, 280, fill='red', tag="wall")
        self.create_oval(182, 262, 198, 278, fill='black', tag="hole")
        self.create_rectangle(200, 260, 220, 280, fill='red', tag="wall")
        self.create_rectangle(0, 280, 20, 300, fill='red', tag="wall")
        # my_ball = my_canvas.create_oval(20, 280, 40, 300, fill='black')
        self.create_rectangle(80, 280, 100, 300, fill='red', tag="wall")
        self.create_oval(102, 282, 118, 298, fill='black', tag="hole")
        self.create_rectangle(120, 280, 140, 300, fill='red', tag="wall")
        self.create_oval(142, 282, 158, 298, fill='black', tag="hole")
        self.create_rectangle(200, 280, 220, 300, fill='red', tag="wall")
        self.create_rectangle(0, 300, 20, 320, fill='red', tag="wall")
        self.create_rectangle(80, 300, 100, 320, fill='red', tag="wall")
        self.create_rectangle(120, 300, 140, 320, fill='red', tag="wall")
        self.create_rectangle(200, 300, 220, 320, fill='red', tag="wall")
        self.create_rectangle(0, 320, 20, 340, fill='red', tag="wall")
        self.create_oval(22, 322, 38, 338, fill='black', tag="hole")
        self.create_rectangle(80, 320, 100, 340, fill='red', tag="wall")
        self.create_oval(182, 322, 198, 338, fill='black', tag="hole")
        self.create_rectangle(200, 320, 220, 340, fill='red', tag="wall")
        self.create_rectangle(0, 340, 20, 360, fill='red', tag="wall")
        self.create_rectangle(80, 340, 100, 360, fill='red', tag="wall")
        self.create_rectangle(120, 340, 140, 360, fill='red', tag="wall")
        self.create_rectangle(200, 340, 220, 360, fill='red', tag="wall")
        self.create_rectangle(0, 360, 20, 380, fill='red', tag="wall")
        self.create_oval(22, 362, 38, 378, fill='black', tag="hole")
        self.create_oval(142, 362, 158, 378, fill='black', tag="hole")
        self.create_rectangle(200, 360, 220, 380, fill='red', tag="wall")
        self.create_rectangle(0, 380, 20, 400, fill='red', tag="wall")
        self.create_rectangle(20, 380, 40, 400, fill='red', tag="wall")
        self.create_rectangle(40, 380, 60, 400, fill='red', tag="wall")
        self.create_rectangle(60, 380, 80, 400, fill='red', tag="wall")
        self.create_rectangle(80, 380, 100, 400, fill='red', tag="wall")
        self.create_rectangle(100, 380, 120, 400, fill='red', tag="wall")
        self.create_rectangle(120, 380, 140, 400, fill='red', tag="wall")
        self.create_rectangle(140, 380, 160, 400, fill='red', tag="wall")
        self.create_rectangle(160, 380, 180, 400, fill='red', tag="wall")
        self.create_rectangle(180, 380, 200, 400, fill='red', tag="wall")
        self.create_rectangle(200, 380, 220, 400, fill='red', tag="wall")
    
    def createObjects3(self):
        self.create_text(30, 10, text="Score: {0}".format(self.score),tag="score", fill="white")
        self.create_image(262, 22, image=self.ball, anchor=NW,  tag="ball")
        self.create_rectangle(0, 0, 20, 20, fill='red', tag="wall")
        self.create_rectangle(20, 0, 40, 20, fill='red', tag="wall")
        self.create_rectangle(40, 0, 60, 20, fill='red', tag="wall")
        self.create_rectangle(60, 0, 80, 20, fill='red', tag="wall")
        self.create_rectangle(80, 0, 100, 20, fill='red', tag="wall")
        self.create_rectangle(100, 0, 120, 20, fill='red', tag="wall")
        self.create_rectangle(120, 0, 140, 20, fill='red', tag="wall")
        self.create_rectangle(140, 0, 160, 20, fill='red', tag="wall")
        self.create_rectangle(160, 0, 180, 20, fill='red', tag="wall")
        self.create_rectangle(180, 0, 200, 20, fill='red', tag="wall")
        self.create_rectangle(200, 0, 220, 20, fill='red', tag="wall")
        self.create_rectangle(220, 0, 240, 20, fill='red', tag="wall")
        self.create_rectangle(240, 0, 260, 20, fill='red', tag="wall")
        self.create_rectangle(260, 0, 280, 20, fill='red', tag="wall")
        self.create_rectangle(280, 0, 300, 20, fill='red', tag="wall")
        self.create_rectangle(300, 0, 320, 20, fill='red', tag="wall")
        self.create_rectangle(320, 0, 340, 20, fill='red', tag="wall")
        self.create_rectangle(340, 0, 360, 20, fill='red', tag="wall")
        self.create_rectangle(360, 0, 380, 20, fill='red', tag="wall")
        self.create_rectangle(380, 0, 400, 20, fill='red', tag="wall")
        self.create_rectangle(400, 0, 420, 20, fill='red', tag="wall")
        self.create_rectangle(420, 0, 440, 20, fill='red', tag="wall")
        self.create_rectangle(440, 0, 460, 20, fill='red', tag="wall")
        self.create_rectangle(460, 0, 480, 20, fill='red', tag="wall")
        self.create_rectangle(480, 0, 500, 20, fill='red', tag="wall")
        self.create_rectangle(0, 20, 20, 40, fill='red', tag="wall")
        self.create_oval(22, 22, 38, 38, fill='black', tag="hole")
        self.create_rectangle(120, 20, 140, 40, fill='red', tag="wall")
        self.create_rectangle(280, 20, 300, 40, fill='red', tag="wall")
        self.create_oval(302, 22, 318, 38, fill='black', tag="hole")
        self.create_oval(382, 22, 398, 38, fill='black', tag="hole")
        self.create_rectangle(400, 20, 420, 40, fill='red', tag="wall")
        self.create_oval(422, 22, 438, 38, fill='black', tag="hole")
        self.create_rectangle(440, 20, 460, 40, fill='red', tag="wall")
        self.create_rectangle(480, 20, 500, 40, fill='red', tag="wall")
        self.create_rectangle(0, 40, 20, 60, fill='red', tag="wall")
        self.create_rectangle(20, 40, 40, 60, fill='red', tag="wall")
        self.create_rectangle(40, 40, 60, 60, fill='red', tag="wall")
        self.create_rectangle(80, 40, 100, 60, fill='red', tag="wall")
        self.create_rectangle(160, 40, 180, 60, fill='red', tag="wall")
        self.create_rectangle(180, 40, 200, 60, fill='red', tag="wall")
        self.create_rectangle(200, 40, 220, 60, fill='red', tag="wall")
        self.create_rectangle(220, 40, 240, 60, fill='red', tag="wall")
        self.create_rectangle(240, 40, 260, 60, fill='red', tag="wall")
        self.create_rectangle(260, 40, 280, 60, fill='red', tag="wall")
        self.create_rectangle(280, 40, 300, 60, fill='red', tag="wall")
        self.create_rectangle(480, 40, 500, 60, fill='red', tag="wall")
        self.create_rectangle(0, 60, 20, 80, fill='red', tag="wall")
        self.create_rectangle(80, 60, 100, 80, fill='red', tag="wall")
        self.create_rectangle(160, 60, 180, 80, fill='red', tag="wall")
        self.create_oval(262, 62, 278, 78, fill='black', tag="hole")
        self.create_rectangle(280, 60, 300, 80, fill='red', tag="wall")
        self.create_oval(462, 62, 478, 78, fill='black', tag="hole")
        self.create_rectangle(480, 60, 500, 80, fill='red', tag="wall")
        self.create_rectangle(0, 80, 20, 100, fill='red', tag="wall")
        self.create_rectangle(40, 80, 60, 100, fill='red', tag="wall")
        self.create_oval(62, 82, 78, 98, fill='black', tag="hole")
        self.create_oval(102, 82, 118, 98, fill='black', tag="hole")
        self.create_rectangle(120, 80, 140, 100, fill='red', tag="wall")
        self.create_oval(142, 82, 158, 98, fill='black', tag="hole")
        self.create_rectangle(160, 80, 180, 100, fill='red', tag="wall")
        self.create_rectangle(200, 80, 220, 100, fill='red', tag="wall")
        self.create_rectangle(240, 80, 260, 100, fill='red', tag="wall")
        self.create_rectangle(280, 80, 300, 100, fill='red', tag="wall")
        self.create_rectangle(300, 80, 320, 100, fill='red', tag="wall")
        self.create_rectangle(340, 80, 360, 100, fill='red', tag="wall")
        self.create_rectangle(360, 80, 380, 100, fill='red', tag="wall")
        self.create_rectangle(380, 80, 400, 100, fill='red', tag="wall")
        self.create_rectangle(400, 80, 420, 100, fill='red', tag="wall")
        self.create_rectangle(440, 80, 460, 100, fill='red', tag="wall")
        self.create_rectangle(480, 80, 500, 100, fill='red', tag="wall")
        self.create_rectangle(0, 100, 20, 120, fill='red', tag="wall")
        self.create_rectangle(80, 100, 100, 120, fill='red', tag="wall")
        self.create_rectangle(200, 100, 220, 120, fill='red', tag="wall")
        self.create_rectangle(240, 100, 260, 120, fill='red', tag="wall")
        self.create_rectangle(280, 100, 300, 120, fill='red', tag="wall")
        self.create_rectangle(340, 100, 360, 120, fill='red', tag="wall")
        self.create_oval(382, 102, 398, 118, fill='black', tag="hole")
        self.create_rectangle(400, 100, 420, 120, fill='red', tag="wall")
        self.create_rectangle(440, 100, 460, 120, fill='red', tag="wall")
        self.create_rectangle(480, 100, 500, 120, fill='red', tag="wall")
        self.create_rectangle(0, 120, 20, 140, fill='red', tag="wall")
        self.create_rectangle(20, 120, 40, 140, fill='red', tag="wall")
        self.create_rectangle(40, 120, 60, 140, fill='red', tag="wall")
        self.create_rectangle(80, 120, 100, 140, fill='red', tag="wall")
        self.create_rectangle(120, 120, 140, 140, fill='red', tag="wall")
        self.create_oval(142, 122, 158, 138, fill='black', tag="hole")
        self.create_rectangle(160, 120, 180, 140, fill='red', tag="wall")
        self.create_rectangle(180, 120, 200, 140, fill='red', tag="wall")
        self.create_rectangle(200, 120, 220, 140, fill='red', tag="wall")
        self.create_rectangle(280, 120, 300, 140, fill='red', tag="wall")
        self.create_oval(302, 122, 318, 138, fill='black', tag="hole")
        self.create_rectangle(400, 120, 420, 140, fill='red', tag="wall")
        self.create_rectangle(440, 120, 460, 140, fill='red', tag="wall")
        self.create_rectangle(480, 120, 500, 140, fill='red', tag="wall")
        self.create_rectangle(0, 140, 20, 160, fill='red', tag="wall")
        self.create_rectangle(80, 140, 100, 160, fill='red', tag="wall")
        self.create_rectangle(120, 140, 140, 160, fill='red', tag="wall")
        self.create_rectangle(160, 140, 180, 160, fill='red', tag="wall")
        self.create_oval(182, 142, 198, 158, fill='black', tag="hole")
        self.create_oval(222, 142, 238, 158, fill='black', tag="hole")
        self.create_rectangle(240, 140, 260, 160, fill='red', tag="wall")
        self.create_rectangle(280, 140, 300, 160, fill='red', tag="wall")
        self.create_rectangle(300, 140, 320, 160, fill='red', tag="wall")
        self.create_rectangle(320, 140, 340, 160, fill='red', tag="wall")
        self.create_rectangle(340, 140, 360, 160, fill='red', tag="wall")
        self.create_rectangle(400, 140, 420, 160, fill='red', tag="wall")
        self.create_rectangle(480, 140, 500, 160, fill='red', tag="wall")
        self.create_rectangle(0, 160, 20, 180, fill='red', tag="wall")
        self.create_rectangle(40, 160, 60, 180, fill='red', tag="wall")
        self.create_rectangle(60, 160, 80, 180, fill='red', tag="wall")
        self.create_rectangle(80, 160, 100, 180, fill='red', tag="wall")
        self.create_rectangle(200, 160, 220, 180, fill='red', tag="wall")
        self.create_rectangle(240, 160, 260, 180, fill='red', tag="wall")
        self.create_rectangle(280, 160, 300, 180, fill='red', tag="wall")
        self.create_oval(302, 162, 318, 178, fill='black', tag="hole")
        self.create_rectangle(400, 160, 420, 180, fill='red', tag="wall")
        self.create_oval(422, 162, 438, 178, fill='black', tag="hole")
        self.create_rectangle(440, 160, 460, 180, fill='red', tag="wall")
        self.create_rectangle(480, 160, 500, 180, fill='red', tag="wall")
        self.create_rectangle(0, 180, 20, 200, fill='red', tag="wall")
        self.create_oval(102, 182, 118, 198, fill='black', tag="hole")
        self.create_rectangle(200, 180, 220, 200, fill='red', tag="wall")
        self.create_rectangle(280, 180, 300, 200, fill='red', tag="wall")
        self.create_oval(342, 182, 358, 198, fill='black', tag="hole")
        self.create_rectangle(360, 180, 380, 200, fill='red', tag="wall")
        self.create_oval(382, 182, 398, 198, fill='black', tag="hole")
        self.create_rectangle(400, 180, 420, 200, fill='red', tag="wall")
        self.create_rectangle(440, 180, 460, 200, fill='red', tag="wall")
        self.create_rectangle(480, 180, 500, 200, fill='red', tag="wall")
        self.create_rectangle(0, 200, 20, 220, fill='red', tag="wall")
        self.create_oval(22, 202, 38, 218, fill='black', tag="hole")
        self.create_rectangle(40, 200, 60, 220, fill='red', tag="wall")
        self.create_rectangle(80, 200, 100, 220, fill='red', tag="wall")
        self.create_rectangle(120, 200, 140, 220, fill='red', tag="wall")
        self.create_oval(142, 202, 158, 218, fill='black', tag="hole")
        self.create_rectangle(160, 200, 180, 220, fill='red', tag="wall")
        self.create_rectangle(200, 200, 220, 220, fill='red', tag="wall")
        self.create_rectangle(240, 200, 260, 220, fill='red', tag="wall")
        self.create_oval(262, 202, 278, 218, fill='black', tag="hole")
        self.create_rectangle(320, 200, 340, 220, fill='red', tag="wall")
        self.create_rectangle(340, 200, 360, 220, fill='red', tag="wall")
        self.create_rectangle(360, 200, 380, 220, fill='red', tag="wall")
        self.create_rectangle(440, 200, 460, 220, fill='red', tag="wall")
        self.create_rectangle(480, 200, 500, 220, fill='red', tag="wall")
        self.create_rectangle(0, 220, 20, 240, fill='red', tag="wall")
        self.create_rectangle(40, 220, 60, 240, fill='red', tag="wall")
        self.create_rectangle(80, 220, 100, 240, fill='red', tag="wall")
        self.create_rectangle(120, 220, 140, 240, fill='red', tag="wall")
        self.create_rectangle(160, 220, 180, 240, fill='red', tag="wall")
        self.create_rectangle(200, 220, 220, 240, fill='red', tag="wall")
        self.create_rectangle(280, 220, 300, 240, fill='red', tag="wall")
        self.create_rectangle(360, 220, 380, 240, fill='red', tag="wall")
        self.create_rectangle(400, 220, 420, 240, fill='red', tag="wall")
        self.create_rectangle(440, 220, 460, 240, fill='red', tag="wall")
        self.create_oval(462, 222, 478, 238, fill='yellow', tag="finish")
        self.create_rectangle(480, 220, 500, 240, fill='red', tag="wall")
        self.create_rectangle(0, 240, 20, 260, fill='red', tag="wall")
        self.create_oval(102, 242, 118, 258, fill='black', tag="hole")
        self.create_rectangle(200, 240, 220, 260, fill='red', tag="wall")
        self.create_rectangle(220, 240, 240, 260, fill='red', tag="wall")
        self.create_rectangle(240, 240, 260, 260, fill='red', tag="wall")
        self.create_rectangle(280, 240, 300, 260, fill='red', tag="wall")
        self.create_rectangle(320, 240, 340, 260, fill='red', tag="wall")
        self.create_rectangle(400, 240, 420, 260, fill='red', tag="wall")
        self.create_rectangle(440, 240, 460, 260, fill='red', tag="wall")
        self.create_rectangle(460, 240, 480, 260, fill='red', tag="wall")
        self.create_rectangle(480, 240, 500, 260, fill='red', tag="wall")
        self.create_rectangle(0, 260, 20, 280, fill='red', tag="wall")
        self.create_rectangle(40, 260, 60, 280, fill='red', tag="wall")
        self.create_rectangle(60, 260, 80, 280, fill='red', tag="wall")
        self.create_rectangle(80, 260, 100, 280, fill='red', tag="wall")
        self.create_oval(142, 262, 158, 278, fill='black', tag="hole")
        self.create_oval(182, 262, 198, 278, fill='black', tag="hole")
        self.create_rectangle(280, 260, 300, 280, fill='red', tag="wall")
        self.create_oval(302, 262, 318, 278, fill='black', tag="hole")
        self.create_rectangle(320, 260, 340, 280, fill='red', tag="wall")
        self.create_rectangle(340, 260, 360, 280, fill='red', tag="wall")
        self.create_rectangle(360, 260, 380, 280, fill='red', tag="wall")
        self.create_rectangle(400, 260, 420, 280, fill='red', tag="wall")
        self.create_oval(462, 262, 478, 278, fill='black', tag="hole")
        self.create_rectangle(480, 260, 500, 280, fill='red', tag="wall")
        self.create_rectangle(0, 280, 20, 300, fill='red', tag="wall")
        self.create_oval(62, 282, 78, 298, fill='black', tag="hole")
        self.create_rectangle(80, 280, 100, 300, fill='red', tag="wall")
        self.create_rectangle(160, 280, 180, 300, fill='red', tag="wall")
        self.create_rectangle(180, 280, 200, 300, fill='red', tag="wall")
        self.create_rectangle(200, 280, 220, 300, fill='red', tag="wall")
        self.create_rectangle(240, 280, 260, 300, fill='red', tag="wall")
        self.create_oval(262, 282, 278, 298, fill='black', tag="hole")
        self.create_rectangle(360, 280, 380, 300, fill='red', tag="wall")
        self.create_oval(382, 282, 398, 298, fill='black', tag="hole")
        self.create_rectangle(400, 280, 420, 300, fill='red', tag="wall")
        self.create_oval(422, 282, 438, 298, fill='black', tag="hole")
        self.create_rectangle(480, 280, 500, 300, fill='red', tag="wall")
        self.create_rectangle(0, 300, 20, 320, fill='red', tag="wall")
        self.create_oval(22, 302, 38, 318, fill='black', tag="hole")
        self.create_rectangle(80, 300, 100, 320, fill='red', tag="wall")
        self.create_oval(102, 302, 118, 318, fill='black', tag="hole")
        self.create_rectangle(120, 300, 140, 320, fill='red', tag="wall")
        self.create_rectangle(160, 300, 180, 320, fill='red', tag="wall")
        self.create_rectangle(240, 300, 260, 320, fill='red', tag="wall")
        self.create_rectangle(360, 300, 380, 320, fill='red', tag="wall")
        self.create_rectangle(400, 300, 420, 320, fill='red', tag="wall")
        self.create_rectangle(480, 300, 500, 320, fill='red', tag="wall")
        self.create_rectangle(0, 320, 20, 340, fill='red', tag="wall")
        self.create_rectangle(80, 320, 100, 340, fill='red', tag="wall")
        self.create_rectangle(120, 320, 140, 340, fill='red', tag="wall")
        self.create_rectangle(160, 320, 180, 340, fill='red', tag="wall")
        self.create_rectangle(200, 320, 220, 340, fill='red', tag="wall")
        self.create_rectangle(240, 320, 260, 340, fill='red', tag="wall")
        self.create_oval(302, 322, 318, 338, fill='black', tag="hole")
        self.create_rectangle(360, 320, 380, 340, fill='red', tag="wall")
        self.create_oval(462, 322, 478, 338, fill='black', tag="hole")
        self.create_rectangle(480, 320, 500, 340, fill='red', tag="wall")
        self.create_rectangle(0, 340, 20, 360, fill='red', tag="wall")
        self.create_oval(62, 342, 78, 358, fill='black', tag="hole")
        self.create_rectangle(160, 340, 180, 360, fill='red', tag="wall")
        self.create_rectangle(200, 340, 220, 360, fill='red', tag="wall")
        self.create_oval(222, 342, 238, 358, fill='black', tag="hole")
        self.create_rectangle(240, 340, 260, 360, fill='red', tag="wall")
        self.create_rectangle(280, 340, 300, 360, fill='red', tag="wall")
        self.create_rectangle(300, 340, 320, 360, fill='red', tag="wall")
        self.create_rectangle(360, 340, 380, 360, fill='red', tag="wall")
        self.create_rectangle(400, 340, 420, 360, fill='red', tag="wall")
        self.create_rectangle(440, 340, 460, 360, fill='red', tag="wall")
        self.create_rectangle(480, 340, 500, 360, fill='red', tag="wall")
        self.create_rectangle(0, 360, 20, 380, fill='red', tag="wall")
        self.create_rectangle(120, 360, 140, 380, fill='red', tag="wall")
        self.create_oval(142, 362, 158, 378, fill='black', tag="hole")
        self.create_oval(302, 362, 318, 378, fill='black', tag="hole")
        self.create_oval(422, 362, 438, 378, fill='black', tag="hole")
        self.create_rectangle(480, 360, 500, 380, fill='red', tag="wall")
        self.create_rectangle(0, 380, 20, 400, fill='red', tag="wall")
        self.create_rectangle(20, 380, 40, 400, fill='red', tag="wall")
        self.create_rectangle(40, 380, 60, 400, fill='red', tag="wall")
        self.create_rectangle(60, 380, 80, 400, fill='red', tag="wall")
        self.create_rectangle(80, 380, 100, 400, fill='red', tag="wall")
        self.create_rectangle(100, 380, 120, 400, fill='red', tag="wall")
        self.create_rectangle(120, 380, 140, 400, fill='red', tag="wall")
        self.create_rectangle(140, 380, 160, 400, fill='red', tag="wall")
        self.create_rectangle(160, 380, 180, 400, fill='red', tag="wall")
        self.create_rectangle(180, 380, 200, 400, fill='red', tag="wall")
        self.create_rectangle(200, 380, 220, 400, fill='red', tag="wall")
        self.create_rectangle(220, 380, 240, 400, fill='red', tag="wall")
        self.create_rectangle(240, 380, 260, 400, fill='red', tag="wall")
        self.create_rectangle(260, 380, 280, 400, fill='red', tag="wall")
        self.create_rectangle(280, 380, 300, 400, fill='red', tag="wall")
        self.create_rectangle(300, 380, 320, 400, fill='red', tag="wall")
        self.create_rectangle(320, 380, 340, 400, fill='red', tag="wall")
        self.create_rectangle(340, 380, 360, 400, fill='red', tag="wall")
        self.create_rectangle(360, 380, 380, 400, fill='red', tag="wall")
        self.create_rectangle(380, 380, 400, 400, fill='red', tag="wall")
        self.create_rectangle(400, 380, 420, 400, fill='red', tag="wall")
        self.create_rectangle(420, 380, 440, 400, fill='red', tag="wall")
        self.create_rectangle(440, 380, 460, 400, fill='red', tag="wall")
        self.create_rectangle(460, 380, 480, 400, fill='red', tag="wall")
        self.create_rectangle(480, 380, 500, 400, fill='red', tag="wall")

    def checkFinishCollision(self):
        finish = self.find_withtag("finish")
        ball = self.find_withtag("ball")
        x1, y1, x2, y2 = self.bbox(ball)
        overlap = self.find_overlapping(x1, y1, x2, y2)
        for ovr in overlap:
            if finish[0] == ovr:
                self.score += 1
                self.gameWon()

    def isWall(self):
        ball = self.find_withtag("ball")
        walls=self.find_withtag("wall")
        x1, y1, x2, y2 = self.bbox(ball)
        overlap = self.find_overlapping(x1, y1, x2, y2)
        for wall in walls:
            for over in overlap:
                if over == wall:
                    self.inGame = False

    def moveBall(self):
        ball = self.find_withtag("ball")
        self.move(ball, self.moveX, self.moveY)

    def checkCollisions(self):

        holes = self.find_withtag("hole")
        ball = self.find_withtag("ball")
        x1, y1, x2, y2 = self.bbox(ball)
        overlap = self.find_overlapping(x1, y1, x2, y2)
        for hole in holes:
            for over in overlap:
                if over == hole:
                  self.inGame = False

    def onKeyPressed(self, e):
        key = e.keysym
        LEFT_CURSOR_KEY = "Left"
        if key == LEFT_CURSOR_KEY:
            self.moveX = -Cons.DOT_SIZE
            self.moveY = 0
        RIGHT_CURSOR_KEY = "Right"
        if key == RIGHT_CURSOR_KEY:
            self.moveX = Cons.DOT_SIZE
            self.moveY = 0
        RIGHT_CURSOR_KEY = "Up"
        if key == RIGHT_CURSOR_KEY:
            self.moveX = 0
            self.moveY = -Cons.DOT_SIZE
        DOWN_CURSOR_KEY = "Down"
        if key == DOWN_CURSOR_KEY:
            self.moveX = 0
            self.moveY = Cons.DOT_SIZE
        Q_CURSOR_KEY = "q"
        if key == Q_CURSOR_KEY:
            ball = self.find_withtag("ball")
            for i in self.mutari:
                self.after(Cons.DELAY, self.onTimer)
                self.update()
                if i == 'LEFT':
                    self.after(250)
                    self.update()
                    self.move(ball, -Cons.DOT_SIZE, 0)
                elif i == 'RIGHT':
                    self.after(250)
                    self.update()
                    self.move(ball, Cons.DOT_SIZE, 0)
                elif i == 'UP':
                    self.after(250)
                    self.update()
                    self.move(ball, 0, -Cons.DOT_SIZE)
                elif i == 'DOWN':
                    self.after(250)
                    self.update()
                    self.move(ball, 0, Cons.DOT_SIZE)

    def onTimer(self):
        self.drawScore()
        self.checkCollisions()
        self.isWall()
        self.checkFinishCollision()
        if self.inGame:
            self.moveBall()
            self.after(Cons.DELAY, self.onTimer)
        else:
            self.gameOver()

    def drawScore(self):
        score = self.find_withtag("score")
        self.itemconfigure(score, text="Score: {0}".format(self.score))

    def gameOver(self):
        self.delete(ALL)
        self.create_text(self.winfo_width() /2, self.winfo_height()/2,
            text="Game Over with score {0}".format(self.score), fill="black")

    def gameWon(self):
        self.delete(ALL)
        self.create_text(self.winfo_width() /2, self.winfo_height()/2,
            text="Game Won with score {0}".format(self.score), fill="black")

class Stack:
    def __init__(self):
        self.list = []

    def push(self,item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0

class Queue:
    def __init__(self):
        self.list = []
    def push(self,item):
        self.list.insert(0,item)
    def pop(self):
        return self.list.pop()
    def isEmpty(self):
        return len(self.list) == 0

class PriorityQueue:
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)

class Search():
    UP='Up'
    DOWN='Down'
    LEFT='Left'
    RIGHT='Right'
    STOP='Stop'

    def __init__(self):
        super().__init__()
        self.l1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 2, 0, 0, 1, 1, 1, 1, 0, 0, 1],
                   [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                   [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
                   [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                   [1, 1, 0, 0, 0, 0, 0, 1, 0, 3, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.l2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                   [1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                   [1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                   [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                   [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
                   [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
                   [1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                   [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 0, 0, 1, 0, 1, 0, 1, 3, 1],
                   [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1],
                   [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
                   [1, 2, 0, 0, 1, 1, 1, 1, 0, 0, 1],
                   [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                   [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
                   [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                   [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.l3 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
                   [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                   [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                   [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                   [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                   [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
                   [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                   [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 3, 1],
                   [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1],
                   [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
                   [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
                   [1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                   [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
                   [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def getStartState(self, maze):
        if maze == 1:
            for i in range(len(self.l1)):
                for j in range(len(self.l1[i])):
                    if self.l1[i][j] == 2:
                        return (i, j)
        elif maze == 2:
            for i in range(len(self.l2)):
                for j in range(len(self.l2[i])):
                    if self.l2[i][j] == 2:
                        return (i, j)
        else:
            for i in range(len(self.l3)):
                for j in range(len(self.l3[i])):
                    if self.l3[i][j] == 2:
                        return (i, j)

    def getFinalState(self, maze):
        if maze == 1:
            for i in range(len(self.l1)):
                for j in range(len(self.l1[i])):
                    if self.l1[i][j] == 3:
                        return (i, j)
        elif maze == 2:
            for i in range(len(self.l2)):
                for j in range(len(self.l2[i])):
                    if self.l2[i][j] == 3:
                        return (i, j)
        else:
            for i in range(len(self.l3)):
                for j in range(len(self.l3[i])):
                    if self.l3[i][j] == 3:
                        return (i, j)

    def isGoalState(self, maze, node):
        if self.getFinalState(maze) == node:
            return True
        else:
            return False

    def bfs(self,maze):
        crt = (self.getStartState(maze), [])
        frontiera = Queue()
        frontiera.push(crt)
        teritoriu = []
        while not frontiera.isEmpty():
            nodcrt = frontiera.pop()
            teritoriu.append(nodcrt[0])
            if self.isGoalState(maze,nodcrt[0]):
                return nodcrt[1]

            childNodes = []
            ycrt, xcrt = nodcrt[0]
            print(ycrt, xcrt)
            if maze == 1:
                if self.l1[ycrt - 1][xcrt] != 1:
                    childNodes.append(((ycrt - 1, xcrt), 'UP'))
                if self.l1[ycrt][xcrt + 1] != 1:
                    childNodes.append(((ycrt, xcrt + 1), 'RIGHT'))
                if self.l1[ycrt + 1][xcrt] != 1:
                    childNodes.append(((ycrt + 1, xcrt), 'DOWN'))
                if self.l1[ycrt][xcrt - 1] != 1:
                    childNodes.append(((ycrt, xcrt - 1), 'LEFT'))
            elif maze == 2:
                if self.l2[ycrt - 1][xcrt] != 1:
                    childNodes.append(((ycrt - 1, xcrt), 'UP'))
                if self.l2[ycrt][xcrt + 1] != 1:
                    childNodes.append(((ycrt, xcrt + 1), 'RIGHT'))
                if self.l2[ycrt + 1][xcrt] != 1:
                    childNodes.append(((ycrt + 1, xcrt), 'DOWN'))
                if self.l2[ycrt][xcrt - 1] != 1:
                    childNodes.append(((ycrt, xcrt - 1), 'LEFT'))
            elif maze == 3:
                if self.l3[ycrt - 1][xcrt] != 1:
                    childNodes.append(((ycrt - 1, xcrt), 'UP'))
                if self.l3[ycrt][xcrt + 1] != 1:
                    childNodes.append(((ycrt, xcrt + 1), 'RIGHT'))
                if self.l3[ycrt + 1][xcrt] != 1:
                    childNodes.append(((ycrt + 1, xcrt), 'DOWN'))
                if self.l3[ycrt][xcrt - 1] != 1:
                    childNodes.append(((ycrt, xcrt - 1), 'LEFT'))


            for node in childNodes:
                (stare, actiune) = node
                front = []
                for nod in frontiera.list:
                    front.append(nod[0])
                if stare not in teritoriu and stare not in front:
                    cale = nodcrt[1] + [actiune]
                    frontiera.push((stare, cale))
        return []

    def ucs(self,maze):
        nodCrt = (self.getStartState(maze), [], 0)
        frontiera = PriorityQueue()
        teritoriu = []
        frontiera.push(nodCrt, 0)
        while not frontiera.isEmpty():
            nodCrt = frontiera.pop()
            if self.isGoalState(maze,nodCrt[0]):
                return nodCrt[1]
            teritoriu.append(nodCrt[0])
            succesori = []
            ycrt, xcrt = nodCrt[0]
            print(ycrt, xcrt, nodCrt[2])
            if maze == 1:
                if self.l1[ycrt - 1][xcrt] != 1:
                    succesori.append(((ycrt - 1, xcrt), 'UP', 1))
                if self.l1[ycrt][xcrt + 1] != 1:
                    succesori.append(((ycrt, xcrt + 1), 'RIGHT',1))
                if self.l1[ycrt + 1][xcrt] != 1:
                    succesori.append(((ycrt + 1, xcrt), 'DOWN',1))
                if self.l1[ycrt][xcrt - 1] != 1:
                    succesori.append(((ycrt, xcrt - 1), 'LEFT',1))
            elif maze == 2:
                if self.l2[ycrt - 1][xcrt] != 1:
                    succesori.append(((ycrt - 1, xcrt), 'UP',1))
                if self.l2[ycrt][xcrt + 1] != 1:
                    succesori.append(((ycrt, xcrt + 1), 'RIGHT',1))
                if self.l2[ycrt + 1][xcrt] != 1:
                    succesori.append(((ycrt + 1, xcrt), 'DOWN',1))
                if self.l2[ycrt][xcrt - 1] != 1:
                    succesori.append(((ycrt, xcrt - 1), 'LEFT',1))
            elif maze == 3:
                if self.l3[ycrt - 1][xcrt] != 1:
                    succesori.append(((ycrt - 1, xcrt), 'UP',1))
                if self.l3[ycrt][xcrt + 1] != 1:
                    succesori.append(((ycrt, xcrt + 1), 'RIGHT',1))
                if self.l3[ycrt + 1][xcrt] != 1:
                    succesori.append(((ycrt + 1, xcrt), 'DOWN',1))
                if self.l3[ycrt][xcrt - 1] != 1:
                    succesori.append(((ycrt, xcrt - 1), 'LEFT',1))
            for succesor in succesori:
                (stare, mutare, cost) = succesor
                if stare not in teritoriu and stare not in (nod[0] for nod in frontiera.heap):
                    cale = nodCrt[1] + [mutare]
                    g = nodCrt[2]+1
                    frontiera.push((stare, cale, g), g)
                elif stare in (nod[0] for nod in frontiera.heap):
                    cale = nodCrt[1] + [mutare]
                    g = nodCrt[2]+1
                    frontiera.update((stare, cale, g), g)
        return []

    def dfs(self,maze):
        crt = (self.getStartState(maze), [])
        print(crt)
        frontiera = Stack()
        frontiera.push(crt)
        teritoriu = []
        while not frontiera.isEmpty():
            nodcrt = frontiera.pop()
            teritoriu.append(nodcrt[0])
            if self.isGoalState(maze, nodcrt[0]):
                return nodcrt[1]
            succesori = []
            ycrt,xcrt=nodcrt[0]
            print(ycrt,xcrt)
            if maze==1:
                if self.l1[ycrt-1][xcrt] !=1:
                    succesori.append(((ycrt-1,xcrt),'UP'))
                if self.l1[ycrt][xcrt+1]!=1:
                    succesori.append(((ycrt,xcrt+1),'RIGHT'))
                if self.l1[ycrt + 1][xcrt] != 1:
                    succesori.append(((ycrt + 1, xcrt), 'DOWN'))
                if self.l1[ycrt][xcrt-1]!=1:
                    succesori.append(((ycrt,xcrt-1),'LEFT'))
            elif maze==2:
                if self.l2[ycrt - 1][xcrt] != 1:
                    succesori.append(((ycrt - 1, xcrt), 'UP'))
                if self.l2[ycrt][xcrt + 1] != 1:
                    succesori.append(((ycrt, xcrt + 1), 'RIGHT'))
                if self.l2[ycrt + 1][xcrt] != 1:
                    succesori.append(((ycrt + 1, xcrt), 'DOWN'))
                if self.l2[ycrt][xcrt - 1] != 1:
                    succesori.append(((ycrt, xcrt - 1), 'LEFT'))
            elif maze==3:
                if self.l3[ycrt-1][xcrt] !=1:
                    succesori.append(((ycrt-1,xcrt),'UP'))
                if self.l3[ycrt][xcrt+1]!=1:
                    succesori.append(((ycrt,xcrt+1),'RIGHT'))
                if self.l3[ycrt + 1][xcrt] != 1:
                    succesori.append(((ycrt + 1, xcrt), 'DOWN'))
                if self.l3[ycrt][xcrt-1]!=1:
                    succesori.append(((ycrt,xcrt-1),'LEFT'))
            for succesor in succesori:
                (stare, actiune) = succesor
                front = []
                for nod in frontiera.list:
                    front.append(nod[0])
                if stare not in teritoriu and stare not in front:
                    cale = nodcrt[1] + [actiune]
                    frontiera.push((stare, cale))
        return []

    def aStarSearch(self,maze):
        pass
        vizitat = {}
        goal = []
        queue = Queue()
        parinti = {}
        cost = {}

        start = self.getStartState(maze)
        queue.push((start, 'Undefined'), 0)
        vizitat[start] = 'Undefined'
        cost[start] = 0

        # daca start este nodu goal
        if self.isGoalState(maze,start):
            return goal

        reusit = False
        while queue.isEmpty() == False and reusit == False:
            nod = queue.pop()
            vizitat[nod[0]] = nod[1]
            if self.isGoalState(maze,nod[0]):
                solNod = nod[0]
                reusit = True
                break

            # daca succesorul nu e vizitat, calculam costul acestuia
            for elem in self.getSuccesors(nod[0]):
                if elem[0] not in vizitat.keys():
                    #priorityQueue = nod[2] + elem[2] + heuristic(elem[0], problem)
                    #queue.push((elem[0], elem[1], nod[2] + elem[2]), priorityQueue)
                    #cost[elem[0]] = priorityQueue
                    parinti[elem[0]] = nod[0]

        while solNod in parinti.keys():
            solNodPrev = parinti[solNod]
            goal.insert(0, vizitat[solNod])
            solNod = solNodPrev

        return goal

class GameStart(Frame):

    def __init__(self,mutari):
        super().__init__()
        self.master.title('BallGame')
        self.board = Board(mutari)
        self.pack()

def main():

    algoritmi=Search()
    mutari=algoritmi.bfs(3)
    print(algoritmi.bfs(3))
    root = Tk()
    nib = GameStart(mutari)
    root.mainloop()


if __name__ == '__main__':
    main()