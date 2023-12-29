import turtle
import pygame
import random
from tkinter import *
from tkinter import ttk
t = turtle.Turtle()
root = Tk()
def main():

    # pygame setup
    pygame.init()
    matching_game.__init__('self')



class matching_game:
    def __init__(self):

        screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption('Show Text')

        pygame.display.update()
        clock = pygame.time.Clock()
        running = True
        dt = 0
        pi = 3.14

        Players.__init__('self', screen, running, clock)




class Players:
    def __init__(self, screen, running, clock):
        player_pos = pygame.Vector2((screen.get_width() / 2), screen.get_height() / 2)
        player_pos_2 = pygame.Vector2((screen.get_width() / 2), (screen.get_height() / 2) - 30)
        player_2_pos = pygame.Vector2((screen.get_height() / 4), (screen.get_width() / 4) - 30)

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("purple")





            pygame.draw.circle(screen, "red", player_pos, 40)
            pygame.draw.circle(screen, "red", player_pos_2, 40)
            pygame.draw.circle(screen, "green", player_2_pos, 40)


            keys = pygame.key.get_pressed()
            player_1_y_list = []
            player_1_2_y_list = []
            player_1_x_list = []
            player_1_2_x_list = []
            Card_2(screen)
            if keys[pygame.K_w]:
                player_pos.y -= 200 * dt
                player_pos_2.y -= 200 * dt
                player_1_y_list.append(player_pos)
                player_1_2_y_list.append(player_pos_2)
            if keys[pygame.K_s]:
                player_pos.y += 200 * dt
                player_pos_2.y += 200 * dt
                player_1_y_list.append(player_pos)
                player_1_2_y_list.append(player_pos_2)
            if keys[pygame.K_a]:
                player_pos.x -= 200 * dt
                player_pos_2.x -= 200 * dt
                player_1_x_list.append(player_pos)
                player_1_2_x_list.append(player_pos)
            if keys[pygame.K_d]:
                player_pos.x += 200 * dt
                player_pos_2.x += 200 * dt
            if keys[pygame.K_LEFT]:
                player_2_pos.x -= 200 * dt
            if keys[pygame.K_RIGHT]:
                player_2_pos.x += 200 * dt
            if keys[pygame.K_UP]:
                player_2_pos.y -= 200 * dt
            if keys[pygame.K_DOWN]:
                player_2_pos.y += 200 * dt


            pygame.draw.circle(screen, "red", player_pos, 40)
            pygame.draw.circle(screen, "red", player_pos_2, 40)
            pygame.draw.circle(screen, "green", player_2_pos, 40)
            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = clock.tick(60) / 1000

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60

        pygame.quit()

        #Config_practice.button("")
        #FeetToMeters(root)

        # print_hierarchy(root)
        #root.mainloop()


class Card_2:
    def __init__(self, screen):
        Card_2.card_grid("self", screen)
    def card_grid(self, screen):
        #pygame.draw.line(screen, 'blue', [(screen.get_height() / 2), (base_y_top / 2)], [(screen.get_height() / 2), (base_y_top / 4)], 5)
        base_x_top = screen.get_height()
        base_y_top = screen.get_width()
        rect_pos_1 = [10, 10, 250, 200]
        modifier_x = 100
        modifier_y = 100
        card_width = 250
        card_height = 200
        card_number = 0

        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        X = 280
        Y = 220
        card_number_1 = 0
        card_list = []
        x_list = []
        y_list = []
        number = str(card_number_1)
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render(number, True, green, blue)
        Card_2.random_math('self')

        for i in range(12):
            card_list.append(card_number)
            x_list.append(X)
            y_list.append(Y)
            if card_number == 0:
                modifier_x = 90
                modifier_y = 25
            if card_number == 1:
                modifier_x = 0
                modifier_y = 220
                one_image = pygame.image.load("1.png")
                one_image = pygame.transform.scale(one_image, (50, 50))
            if card_number == 2:
                modifier_x = 0
                modifier_y = 220
            if card_number == 3:
                modifier_x = 280
                modifier_y = 0
            if card_number == 4:
                modifier_x = 0
                modifier_y = -220
            if card_number == 5:
                modifier_x = 0
                modifier_y = -220
            if card_number == 6:
                modifier_x = 280
                modifier_y = 0
            if card_number == 7:
                modifier_x = 0
                modifier_y = 220
            if card_number == 8:
                modifier_x = 0
                modifier_y = 220
            if card_number == 9:
                modifier_x = 280
                modifier_y = 0
            if card_number == 10:
                modifier_x = 0
                modifier_y = -220
            if card_number == 11:
                modifier_x = 0
                modifier_y = -220

            card_number += 1
            X += modifier_x*2
            Y += modifier_y*2
            rect_pos_changer_x = rect_pos_1[0] + modifier_x
            rect_pos_changer_y = rect_pos_1[1] + modifier_y
            keys = pygame.key.get_pressed()


            card_number_1 += 1
            number = str(card_number_1)
            font = pygame.font.Font('freesansbold.ttf', 60)
            text = font.render(number, True, green, blue)
            textRect = text.get_rect()
            textRect.center = (X // 2, Y // 2)
            screen.blit(text, textRect)

            rect_pos_1 = [rect_pos_changer_x, rect_pos_changer_y, card_width, card_height]

            pygame.draw.ellipse(screen, 'blue', rect_pos_1, 20)
            pygame.draw.rect(screen, 'blue', rect_pos_1, 20)
            one_image = pygame.image.load("1.png")
            zero_image = pygame.image.load("0_image.jpg")
            one_image = pygame.transform.scale(one_image, (50, 50))
            zero_image = pygame.transform.scale(zero_image, (200, 100))
            #print(one_image)




            #surface_1.fill((50, 50, 50))
            #rect = surface_1.get_rect()

        card_matched = False
        choices = []
        for i in range(2):
            choices.append(i)
        choice_1 = choices[0]
        choice_2 = choices[1]
        if choice_1 == choice_2:
            card_matched = True
        else:
            pass



        if keys[pygame.K_1]:
            press_number.__init__('self', 1)
            surface_1 = pygame.Surface.blit(screen, zero_image, (100, 50))
            surface_1.fit(surface_1)
            Card_2.random_math(self)

        if keys[pygame.K_2]:
            press_number.__init__('self', 2)
            Card_2.random_math(self)
        if keys[pygame.K_3]:
            press_number.__init__(3)
        if keys[pygame.K_4]:
            press_number.__init__(4)
        if keys[pygame.K_5]:
            press_number.__init__(5)
        if keys[pygame.K_6]:
            press_number.__init__(6)
        if keys[pygame.K_7]:
            press_number.__init__(7)
        if keys[pygame.K_8]:
            press_number.__init__(8)
        if keys[pygame.K_9]:
            press_number.__init__(9)
        if keys[pygame.K_z]:
            press_number.__init__(10)
        if keys[pygame.K_x]:
            press_number.__init__(11)
        if keys[pygame.K_c]:
            press_number.__init__(12)


        #pygame.draw.
        #pygame.draw.line(screen, 'blue', [base_y_top/8 - 75, base_y_top*0.2],
        #                 [base_y_top/8 - 75, (base_y_top * 0.05)], 5)
        #pygame.draw.line(screen, 'blue', [base_y_top/8 + 250 - 100, base_y_top*0.2],
        #                 [base_y_top/8 + 250 - 100, (base_y_top * 0.05)], 5)
        #pygame.draw.line(screen, 'blue', [base_y_top/8 + 300 - 100, base_y_top*0.2],
        #                 [base_y_top/8 + 300 - 100, (base_y_top * 0.05)], 5)
        #pygame.draw.line(screen, 'blue', [base_y_top/8 + 550 - 100, base_y_top*0.2],
        #                 [base_y_top/8 + 550 - 100, (base_y_top * 0.05)], 5)
        #pygame.draw.line(screen, 'blue', [base_y_top/8 + 1000 - 100, (base_y_top * 0.2)],
        #                 [base_y_top/8 + 1000 - 100, (base_y_top * 0.05)], 5)
        #pygame.draw.line(screen, 'blue', [base_y_top/8 + 1250 - 100, (base_y_top * 0.2)],
        #                 [base_y_top/8 + 1250 - 100, (base_y_top * 0.05)], 5)

        #pygame.draw.circle(screen, "red", [(screen.get_height() / 2), (base_y_top / 2)], 40)

    def card_frame(self):
        pygame.draw.line(screen, 'red', [10, 20], [10, 20], 5)
    def zero_plus_zero(self):
        #pygame.draw.line(screen, 'blue', )
        pygame.draw.arc(screen, 'red', [10, 10, 250, 200], 6, 7, 2)
    def random_math(self):
        matcher = []
        matcher_dict = {}
        level_0a_equa = ['0 + 0 =', '0 + 1 =', '0 + 2 =', '0 + 3 =', '0 + 4 =', '0 + 5 =']
        level_0a_ans = ['0', '1', '2', '3', '4', '5']
        level_0b_equa = ['0 + 6 =', '0 + 7 =', '0 + 8 =', '0 + 9 =', '0 + 10 =']
        level_0b_ans = ['6', '7', '8', '9', '10']



        def leveler_defined(leveler):
            try:
                if leveler == 0:
                    level = '0a'
                if level == '0a'.lower():
                    random.shuffle(level_0a_equa)
                    random.shuffle(level_0a_ans)
                    all_shuffled = level_0a_equa + level_0a_ans
                    level = '1'
                leveler = 1
            except:
                leveler = 0
                leveler_defined(leveler)

        try:
            matched = all_shuffled[0]
            print(matched)
            font = pygame.font.Font('freesansbold.ttf', 60)
            green = (0, 255, 0)
            blue = (0, 0, 128)
            text = font.render(matched, True, green, blue)
            surface_1 = pygame.Surface.blit(screen, matched, (100, 50))
            surface_1.fit(surface_1)

            #screen = pygame.surface.Surface((600, 40))
            textRect = text.get_rect()
            textRect.center = (X // 2, Y // 2)
            screen.blit(text, textRect)
            print("matched")
            #number = matcher_dict
        except:
            leveler_defined(500)

class press_number:
    def __int__(self, num):
        press_number.image_loader(num)
        pygame.draw.circle(screen, "red", player_pos+40, 40)
        pygame.draw.circle(screen, "red", player_pos_2+40, 40)
        pygame.draw.circle(screen, "green", player_2_pos+40, 40)

    def image_loader(self, num):
        one_image = pygame.image.load("1.png")
        one_image = pygame.transform.scale(one_image, (50, 50))
        surface_1 = pygame.Surface.blit(screen, one_image, (100, 50))
        font = pygame.font.Font('freesansbold.ttf', 60)
        text = font.render(number, True, green, blue)
        textRect = text.get_rect()
        x_list.append(X)
        y_list.append(Y)
        X = x_list[num]
        Y = y_list[num]
        textRect.center = (X // 2, Y // 2)










class Config_practice:
    def button(self):
        print("test")
        button = ttk.Button(root, text="Hello", command="buttonpressed")
        button.grid()
        button['text']
        l = ttk.Label(root, text= "Starting...")
        l.grid()
        l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
        l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
        l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
        l.bind('<3>', lambda e: l.configure(text='Double Clicked'))
        l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d, %d' % (e.x, e.y)))
        #root.mainloop()
        print("test 2")



class Draw_shapes:
    def draw_circle(self, _t, _x, _y, tilt, radius, extent, fillcolor, pencolor):
        """
        This is the atomic shape circle used for the ball on the sword and the shield in various places throughout.
        _x, and _y are for coordinates
        radius is used for the circle size
        fillcolor is for the color inside of the circles
        pencolor is for the circle borders
        """
        _t.up()
        _t.goto(_x,_y)
        _t.setheading(tilt)
        _t.down()
        _t.color(pencolor, fillcolor)
        _t.begin_fill()
        _t.circle(radius, extent)
        _t.end_fill()
        _t.speed(0)
class FeetToMeters:

    def __init__(self, root):

        root.title("Feet to Meters")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))
        self.meters = StringVar()

        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Calculate", command=self.calculate, width=50).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind("<Return>", self.calculate)

    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
        except ValueError:
            pass


def print_hierarchy(w, depth=0):
    print(' '*depth + w.winfo_class() + ' w=' + str(w.winfo_width()) + ' h=' + str(w.winfo_height()) + str(w.winfo_x()) + ' y=' + str(w.winfo_y()))
    for i in w.winfo_children():
        print_hierarchy(i, depth+1)

class Card:


    def __init__(self, root):
        root.title("Match")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))
        self.meters = StringVar()

        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Flip", command=self.flipper, width=50).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="Hola").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="Shalom").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind("<Return>", self.flipper)
        #Draw_shapes.draw_circle("self", t, 13, -4, 143, 21, 360, "purple", "black")

    def flipper(self, *args):
        try:

            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
            ttk.Button(mainframe, text="Calculate", command=calculate)
        except ValueError:
            pass





if __name__ == '__main__':
    main()
#root = Tk()
#Card(root)
#FeetToMeters(root)

#content = ttk.Frame(root)
#button = ttk.Button(content)
"""
print(root.winfo_class())
print(button.winfo_class())
print(root.winfo_children())
print(button.winfo_children())
print(button.winfo_parent())
print(button.winfo_toplevel())
print(button.winfo_width())
print(button.winfo_height())
print(button.winfo_reqwidth())
print(button.winfo_reqheight())
print(button.winfo_x())
print(button.winfo_y())
print(button.winfo_rootx())
print(button.winfo_rooty())
print(button.winfo_viewable())
print(root.winfo_viewable())
"""
#root.mainloop()
