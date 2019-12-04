import pygame
import random
from pygame.locals import *
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

MAX_X = 1920
QUARTER_X = MAX_X / 4
HALF_X = MAX_X / 2
THIRD_X = MAX_X / 3

SCENE = 0

MAX_Y = 1080
HALF_Y = MAX_Y / 2
THIRD_Y = MAX_Y / 3

order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
locations = [(50, 50), (MAX_X - 50, 50), (MAX_X - 50, MAX_Y - 50), (50, MAX_Y - 50), (.5 * MAX_X, .25 * MAX_Y), (.33 * MAX_X, .33 *
                                                                                                                 MAX_Y), (.66 * MAX_X, .33 * MAX_Y), (.33 * MAX_X, .66 * MAX_Y), (.66 * MAX_X, .66 * MAX_Y), (.5 * MAX_X, .75 * MAX_Y)]


class App:

    # these variables are used in some of the functions below
    testNumber = 1
    stepsMade = 0
    side = 0
    newBall = True
    OKNInit = True
    OKNrects = []

    def mainMenu(self):     # this function renders the main menu every frame -- it is called from the render function when the SCENE == 0
        font = pygame.font.Font('freesansbold.ttf', 64)
        text = font.render(
            "PSION Eye Tracker Test Application", True, black, white)
        textRect = text.get_rect()
        textRect.center = (MAX_X // 2, MAX_Y // 2)
        self._display_surf.fill(white)
        self._display_surf.blit(text, textRect)

        mouse = pygame.mouse.get_pos()

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        buttonText1 = smallText.render("Saccade Test", True, black)
        buttonText1Rect = buttonText1.get_rect()
        buttonText1Rect.center = (THIRD_X, THIRD_Y * 2)

        buttonText2 = smallText.render("Smooth Test", True, black)
        buttonText2Rect = buttonText2.get_rect()
        buttonText2Rect.center = (THIRD_X * 2, THIRD_Y * 2)

        buttonText3 = smallText.render("OKN Test", True, black)
        buttonText3Rect = buttonText3.get_rect()
        buttonText3Rect.center = (THIRD_X * 2, THIRD_Y * 2 + 200)

        buttonText4 = smallText.render("VOR Test", True, black)
        buttonText4Rect = buttonText4.get_rect()
        buttonText4Rect.center = (THIRD_X, THIRD_Y * 2 + 200)

        # this code provides the functionality to hilight the buttons on hover
        if(THIRD_X - 100 < mouse[0] < THIRD_X + 100 and THIRD_Y * 2 - 50 < mouse[1] < THIRD_Y * 2 + 50):
            pygame.draw.rect(self._display_surf, blue,
                             (THIRD_X - 100, THIRD_Y * 2 - 50, 200, 100))
            buttonText1 = smallText.render("Saccade Test", True, white)

        else:
            pygame.draw.rect(self._display_surf, green,
                             (THIRD_X - 100, THIRD_Y * 2 - 50, 200, 100))
            buttonText1 = smallText.render("Saccade Test", True, black)

        if (THIRD_X * 2 - 100 < mouse[0] < THIRD_X * 2 + 100 and THIRD_Y * 2 - 50 < mouse[1] < THIRD_Y * 2 + 50):
            pygame.draw.rect(self._display_surf, blue,
                             (THIRD_X * 2 - 100, THIRD_Y * 2 - 50, 200, 100))
            buttonText2 = smallText.render("Smooth Test", True, white)
        else:
            pygame.draw.rect(self._display_surf, green,
                             (THIRD_X * 2 - 100, THIRD_Y * 2 - 50, 200, 100))
            buttonText2 = smallText.render("Smooth Test", True, black)

        if (THIRD_X * 2 - 100 < mouse[0] < THIRD_X * 2 + 100 and THIRD_Y * 2 + 150 < mouse[1] < THIRD_Y * 2 + 250):
            pygame.draw.rect(self._display_surf, blue,
                             (THIRD_X * 2 - 100, THIRD_Y * 2 + 150, 200, 100))
            buttonText3 = smallText.render("OKN Test", True, white)
        else:
            pygame.draw.rect(self._display_surf, green,
                             (THIRD_X * 2 - 100, THIRD_Y * 2 + 150, 200, 100))
            buttonText3 = smallText.render("OKN Test", True, black)

        if(THIRD_X - 100 < mouse[0] < THIRD_X + 100 and THIRD_Y * 2 + 150 < mouse[1] < THIRD_Y * 2 + 250):
            pygame.draw.rect(self._display_surf, blue,
                             (THIRD_X - 100, THIRD_Y * 2 + 150, 200, 100))
            buttonText4 = smallText.render("VOR Test", True, white)

        else:
            pygame.draw.rect(self._display_surf, green,
                             (THIRD_X - 100, THIRD_Y * 2 + 150, 200, 100))
            buttonText4 = smallText.render("VOR Test", True, black)

        self._display_surf.blit(buttonText1, buttonText1Rect)
        self._display_surf.blit(buttonText2, buttonText2Rect)
        self._display_surf.blit(buttonText3, buttonText3Rect)
        self._display_surf.blit(buttonText4, buttonText4Rect)

    def smoothTest(self):   # This Function Contains the code for the smooth movement eye test
        largeFont = pygame.font.Font("freesansbold.ttf", 64)
        smallFont = pygame.font.Font("freesansbold.ttf", 24)
        steps = 100  # change this to change the speed of the ball -- the lower, the faster

        if self.stepsMade == 0:             # when there is a new ball, steps are 0 and it has to choose a side
            self.side = random.randint(0, 1)

        if(self.side == 0):  # go from left to right
            # only perform this if statement once per new ball, because otherwise it doesnt move correctly
            if self.newBall == True:
                self.newBall = False
                self.xLocation = 0
                self.yLocation = random.randint(0, MAX_Y)

                self.xLocationEnd = MAX_X
                self.yLocationEnd = random.randint(0, MAX_Y)

                self.xSteps = (self.xLocationEnd - self.xLocation) / steps
                self.ySteps = (self.yLocationEnd - self.yLocation) / steps

                self.stepsMade = 0

                pygame.draw.circle(self._display_surf, blue, (int(
                    self.xLocation), int(self.yLocation)), 20)

            # add the xSteps and ySteps to the location while the steps made are less than the steps prescribed, and then draw the circle again
            if self.stepsMade in range(steps):
                self.xLocation += self.xSteps
                self.yLocation += self.ySteps
                self.stepsMade += 1
                self._display_surf.fill(white)

                pygame.draw.circle(self._display_surf, blue, (int(
                    self.xLocation), int(self.yLocation)), 20)
            else:                                       # if the steps made is not in the range of steps, i.e. it reached the end of the screen, then reset the ball
                self.stepsMade = 0
                self.newBall = True

        elif(self.side == 1):  # go from right to left --- same exact code as above, but will move backwards instead
            if self.newBall == True:
                self.newBall = False
                self.xLocation = MAX_X
                self.yLocation = random.randint(0, MAX_Y)

                self.xLocationEnd = 0
                self.yLocationEnd = random.randint(0, MAX_Y)

                self.xSteps = (self.xLocationEnd - self.xLocation) / steps
                self.ySteps = (self.yLocationEnd - self.yLocation) / steps

                self.stepsMade = 0

                pygame.draw.circle(self._display_surf, blue, (int(
                    self.xLocation), int(self.yLocation)), 20)

            if self.stepsMade in range(steps):
                self.xLocation += self.xSteps
                self.yLocation += self.ySteps
                self.stepsMade += 1
                self._display_surf.fill(white)

                pygame.draw.circle(self._display_surf, blue, (int(
                    self.xLocation), int(self.yLocation)), 20)
            else:
                self.stepsMade = 0
                self.newBall = True
        else:
            pass

    # contains the code for the saccade eye test, that randomizes the positons of numbers
    def randomSaccade(self):
        font = pygame.font.Font('freesansbold.ttf', 64)

        if(self.testNumber < 10):  # essentially every frame it makes a new font object for each number in order[] and places it in the locations specified in locations[] -- this is probably inefficient but it's fine for this purpose
            text1 = font.render(str(order[0]), True, black, white)
            text2 = font.render(str(order[1]), True, black, white)
            text3 = font.render(str(order[2]), True, black, white)
            text4 = font.render(str(order[3]), True, black, white)
            text5 = font.render(str(order[4]), True, black, white)
            text6 = font.render(str(order[5]), True, black, white)
            text7 = font.render(str(order[6]), True, black, white)
            text8 = font.render(str(order[7]), True, black, white)
            text9 = font.render(str(order[8]), True, black, white)
            text10 = font.render(str(order[9]), True, black, white)

            textRect1 = text1.get_rect()
            textRect2 = text2.get_rect()
            textRect3 = text3.get_rect()
            textRect4 = text4.get_rect()
            textRect5 = text5.get_rect()
            textRect6 = text6.get_rect()
            textRect7 = text7.get_rect()
            textRect8 = text8.get_rect()
            textRect9 = text9.get_rect()
            textRect10 = text10.get_rect()

            textRect1.center = locations[0]
            textRect2.center = locations[1]
            textRect3.center = locations[2]
            textRect4.center = locations[3]
            textRect5.center = locations[4]
            textRect6.center = locations[5]
            textRect7.center = locations[6]
            textRect8.center = locations[7]
            textRect9.center = locations[8]
            textRect10.center = locations[9]

            self._display_surf.fill(white)
            self._display_surf.blit(text1, textRect1)
            self._display_surf.blit(text2, textRect2)
            self._display_surf.blit(text3, textRect3)
            self._display_surf.blit(text4, textRect4)
            self._display_surf.blit(text5, textRect5)
            self._display_surf.blit(text6, textRect6)
            self._display_surf.blit(text7, textRect7)
            self._display_surf.blit(text8, textRect8)
            self._display_surf.blit(text9, textRect9)
            self._display_surf.blit(text10, textRect10)
        # once 10 randomized tests have been created, it will say that the test is over
        elif(self.testNumber == 10):
            text1 = font.render("Test is Over. Stop Recording", True, blue)
            text2 = font.render(
                "Click anywhere to go to Main Menu", True, blue)
            textRect1 = text1.get_rect()
            textRect2 = text2.get_rect()
            textRect1.center = (MAX_X // 2, MAX_Y // 2)
            textRect2.center = (MAX_X // 2, MAX_Y // 2 + 80)
            self._display_surf.fill(white)
            self._display_surf.blit(text1, textRect1)
            self._display_surf.blit(text2, textRect2)
        else:                       # after the test over screen, it will go back to the main menu with the next click
            self.SCENE = 0

    def randomize(self):  # helper function to randomSaccade -- randomizes the order of the numbers
        random.shuffle(order)
        self.testNumber = self.testNumber + 1

    def OKNTest(self):
        rectWidth = 48
        rectNum = (MAX_X / (rectWidth * 2)) + 1

        rectXAppender = -96

        if self.OKNInit == True:
            self.OKNrects = []
            for i in range(int(rectNum)):

                self.OKNrects.append(rectXAppender)
                rectXAppender += rectWidth * 2
            self.OKNInit = False
        else:
            self._display_surf.fill(white)
            for i in range(len(self.OKNrects)):
                pygame.draw.rect(self._display_surf, green,
                                 (self.OKNrects[i], 0, rectWidth, MAX_Y))
                if(self.OKNrects[i] < MAX_X):
                    self.OKNrects[i] += 10
                else:
                    self.OKNrects[i] = -96

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((MAX_X, MAX_Y))
        self._running = True
        pygame.display.set_caption('Saccade Tester')
        self.SCENE = 0

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if(self.SCENE == 0):
                mouse = pygame.mouse.get_pos()
                if(THIRD_X - 100 < mouse[0] < THIRD_X + 100 and THIRD_Y * 2 - 50 < mouse[1] < THIRD_Y * 2 + 50):
                    self.testNumber = 0
                    self.SCENE = 1
                elif(THIRD_X * 2 - 100 < mouse[0] < THIRD_X * 2 + 100 and THIRD_Y * 2 - 50 < mouse[1] < THIRD_Y * 2 + 50):
                    self.SCENE = 2  # TEMPORARY BEFORE I CREATE A ONK BUTTON
                    self.testNumber = 0
                elif(THIRD_X * 2 - 100 < mouse[0] < THIRD_X * 2 + 100 and THIRD_Y * 2 + 150 < mouse[1] < THIRD_Y * 2 + 250):
                    self.SCENE = 3

            elif self.SCENE == 1:
                self.randomize()
            elif self.SCENE == 2:
                self.SCENE = 0
                self.stepsMade = 0
                self.newBall = True
            elif self.SCENE == 3:
                self.SCENE = 0

    def on_loop(self):
        pass

    def on_render(self):
        if self.SCENE == 0:
            self.mainMenu()
        elif self.SCENE == 1:
            self.randomSaccade()
        elif self.SCENE == 2:
            self.smoothTest()
        elif self.SCENE == 3:
            self.OKNTest()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

            pygame.display.update()
            pygame.time.wait(15)
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
