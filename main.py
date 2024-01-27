import pygame
import random

def main():
    """
    Runs the program as a whole
    :return:
    """
    # pygame setup
    pygame.init()
    matching_game.__init__('self')



class matching_game:
    """
    Starts the game
    """
    def __init__(self):


        screen = pygame.display.set_mode((1280, 720))

        card_value = str(Math.__init__('self', screen))
        #card_value = [0,0]
        pygame.display.set_caption('Show Text')

        pygame.display.update()
        clock = pygame.time.Clock()
        running = True
        #dt = 0
        #pi = 3.14

        Players.__init__('self', screen, running, clock, card_value)

        #Card_2.__init__("self", screen)
        #Card_2.leveler_defined(leveler)




class Players:
    """
    Creates the players that are playable. Player 1 can be moved with WASD, and Player 2
    can be played with the arrow keys.
    """
    def __init__(self, screen, running, clock, card_value):
        """
        Starts the players
        :param screen: This is the game screen, variable set in the matching game class.
        :param running: This is set to True while the game is still being played.
        :param clock: This is used to keep the game moving, each tick progresses the game.
        """
        player_pos = pygame.Vector2((screen.get_width() / 2), screen.get_height() / 2)
        player_pos_2 = pygame.Vector2((screen.get_width() / 2), (screen.get_height() / 2) - 30)
        player_2_pos = pygame.Vector2((screen.get_height() / 4), (screen.get_width() / 4) - 30)
        player_3_pos = pygame.Vector2((screen.get_height() / 2 - 40), (screen.get_width() / 4) - 70)
        player_3_pos_2 = pygame.Vector2((screen.get_width() / 4), (screen.get_height() / 3) - 40)
        player_4_pos = pygame.Vector2((screen.get_height()*3 / 4), (screen.get_width() / 2) - 70)
        player_4_pos_2 = pygame.Vector2((screen.get_width()*2 / 4 - 40), (screen.get_height()*7 / 8 + 30) - 100)


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
            pygame.draw.circle(screen, "orange", player_3_pos, 40)
            pygame.draw.circle(screen, "orange", player_3_pos_2, 40)
            pygame.draw.circle(screen, "light blue", player_4_pos, 40)
            pygame.draw.circle(screen, "light blue", player_4_pos_2, 40)


            keys = pygame.key.get_pressed()
            player_1_y_list = []
            player_1_2_y_list = []
            player_1_x_list = []
            player_1_2_x_list = []
            Card_2.__init__("self", screen, card_value)

            if keys[pygame.K_w]:
                # Moves player 1 up on the screen.
                player_pos.y -= 200 * dt
                player_pos_2.y -= 200 * dt
                player_1_y_list.append(player_pos)
                player_1_2_y_list.append(player_pos_2)
            if keys[pygame.K_s]:
                # Moves player 1 down on the screen.
                player_pos.y += 200 * dt
                player_pos_2.y += 200 * dt
                player_1_y_list.append(player_pos)
                player_1_2_y_list.append(player_pos_2)
            if keys[pygame.K_a]:
                # Moves player 1 left on the screen.
                player_pos.x -= 200 * dt
                player_pos_2.x -= 200 * dt
                player_1_x_list.append(player_pos)
                player_1_2_x_list.append(player_pos)
            if keys[pygame.K_d]:
                # Moves player 1 right on the screen.
                player_pos.x += 200 * dt
                player_pos_2.x += 200 * dt
                player_1_y_list.append(player_pos)
                player_1_2_y_list.append(player_pos_2)
            if keys[pygame.K_LEFT]:
                # Moves player 2 left on the screen.
                player_2_pos.x -= 200 * dt
            if keys[pygame.K_RIGHT]:
                # Moves player 2 right on the screen.
                player_2_pos.x += 200 * dt
            if keys[pygame.K_UP]:
                # Moves player 2 up on the screen.
                player_2_pos.y -= 200 * dt
            if keys[pygame.K_DOWN]:
                # Moves player 2 down on the screen.
                player_2_pos.y += 200 * dt
            if keys[pygame.K_i]:
                # Moves player 1 up on the screen.
                player_3_pos.y -= 200 * dt
                player_3_pos_2.y -= 200 * dt
            if keys[pygame.K_k]:
                # Moves player 1 down on the screen.
                player_3_pos.y += 200 * dt
                player_3_pos_2.y += 200 * dt
                player_1_y_list.append(player_pos)
                player_1_2_y_list.append(player_pos_2)
            if keys[pygame.K_j]:
                # Moves player 1 left on the screen.
                player_3_pos.x -= 200 * dt
                player_3_pos_2.x -= 200 * dt
                player_1_x_list.append(player_pos)
                player_1_2_x_list.append(player_pos)
            if keys[pygame.K_l]:
                # Moves player 1 right on the screen.
                player_3_pos.x += 200 * dt
                player_3_pos_2.x += 200 * dt
                player_1_y_list.append(player_pos)
                player_1_2_y_list.append(player_pos_2)
            if keys[pygame.K_t]:
                # Moves player 1 up on the screen.
                player_4_pos.y -= 200 * dt
                player_4_pos_2.y -= 200 * dt
            if keys[pygame.K_g]:
                # Moves player 1 down on the screen.
                player_4_pos.y += 200 * dt
                player_4_pos_2.y += 200 * dt
                player_1_y_list.append(player_pos)
                player_1_2_y_list.append(player_pos_2)
            if keys[pygame.K_f]:
                # Moves player 1 left on the screen.
                player_4_pos.x -= 200 * dt
                player_4_pos_2.x -= 200 * dt
                player_1_x_list.append(player_pos)
                player_1_2_x_list.append(player_pos)
            if keys[pygame.K_h]:
                # Moves player 1 right on the screen.
                player_4_pos.x += 200 * dt
                player_4_pos_2.x += 200 * dt
                player_1_y_list.append(player_pos)
                player_1_2_y_list.append(player_pos_2)


            #pygame.draw.circle(screen, "red", player_pos, 40)
            #pygame.draw.circle(screen, "red", player_pos_2, 40)
            #pygame.draw.circle(screen, "green", player_2_pos, 40)
            try:
                tail_1_x = player_1_x_list[-4]
                tail_1_y= player_1_y_list[-4]
                new_player_pos = pygame.Vector2(tail_1_x, tail_1_y)
                pygame.draw.circle(screen, "red", new_player_pos, 40)
            except:
                pass



            # flip() the display to put your work on screen
            pygame.display.flip()

            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = clock.tick(60) / 1000

            clock.tick(60)  # limits FPS to 60

        pygame.quit()
        # Ends the game

        #Config_practice.button("")
        #FeetToMeters(root)

        # print_hierarchy(root)
        #root.mainloop()


class Math:
    def __init__(self, screen):
        """
        Randomizes the position of the equations for the cards
        :param screen: The screen size.
        :return:
        """
        matcher = []
        matcher_dict = {}
        Math.leveler_defined(0, screen)




    def leveler_defined(leveler, screen):

        try:
            if leveler == 0:
                level = '0a'
            if level == '0a'.lower():
                level_0a_equa = ['0 + 0 =', '0 + 1 =', '0 + 2 =', '0 + 3 =', '0 + 4 =', '0 + 5 =']
                level_0a_ans = ['0', '1', '2', '3', '4', '5']
                level_0b_equa = ['0 + 6 =', '0 + 7 =', '0 + 8 =', '0 + 9 =', '0 + 10 =']
                level_0b_ans = ['6', '7', '8', '9', '10']

                all_shuffled = level_0a_equa + level_0a_ans
                random.shuffle(all_shuffled)

                Math.card_1_value = all_shuffled[0]
                Math.card_2_value = all_shuffled[1]
                Math.card_3_value = all_shuffled[2]
                Math.card_4_value = all_shuffled[3]
                Math.card_5_value = all_shuffled[4]
                Math.card_6_value = all_shuffled[5]
                Math.card_7_value = all_shuffled[6]
                Math.card_8_value = all_shuffled[7]
                Math.card_9_value = all_shuffled[8]
                Math.card_10_value = all_shuffled[9]
                Math.card_11_value = all_shuffled[10]
                Math.card_12_value = all_shuffled[11]
                level = '1'
                leveler = 1

        except:
            if leveler == 1:
                pass
            else:
                leveler = 0
                #Card_2.leveler_defined(leveler, screen)

        #print(all_shuffled)


        try:

            matched = all_shuffled[0]
            print(matched)
            font = pygame.font.Font('freesansbold.ttf', 60)
            green = (0, 255, 0)
            blue = (0, 0, 128)
            text = font.render(matched, True, green, blue)
            surface_1 = pygame.Surface.blit(screen, matched, (100, 50))
            surface_1.fit(surface_1)

            screen = pygame.surface.Surface((600, 40))
            textRect = text.get_rect()
            textRect.center = (X // 2, Y // 2)
            screen.blit(text, textRect)
            print("matched")
            #number = matcher_dict

        except:
            #Card_2.leveler_defined(500, screen)
            pass
    """
    try:
        card_1_value = all_shuffled[0]
        card_2_value = all_shuffled[1]
    except:
        card_1_value = 3
    #print(all_shuffled)
    """

class Card_2(Math):

    """
    Draws the cards.
    """
    def __init__(self, screen, card_value):
        """
        Initiates the card grid method
        :param screen: defines the game screen size.
        """
        #Card_2.card_grid("self", screen)

        card = Card_2.card_values("self", screen, 1)
        X = Card_2.x_value("self", card)
        Y = Card_2.y_value("self", card)
        Card_2.card_draw("self", screen, X, Y, card, card_value)
        card = Card_2.card_values("self", screen, 2)
        X = Card_2.x_value("self", card)
        Y = Card_2.y_value("self", card)
        Card_2.card_draw("self", screen, X, Y, card, card_value)
        card = Card_2.card_values("self", screen, 3)
        X = Card_2.x_value("self", card)
        Y = Card_2.y_value("self", card)
        Card_2.card_draw("self", screen, X, Y, card, card_value)
        card = Card_2.card_values("self", screen, 4)
        X = Card_2.x_value("self", card)
        Y = Card_2.y_value("self", card)
        Card_2.card_draw("self", screen, X, Y, card, card_value)
        card = Card_2.card_values("self", screen, 5)
        X = Card_2.x_value("self", card)
        Y = Card_2.y_value("self", card)
        Card_2.card_draw("self", screen, X, Y, card, card_value)
        card = Card_2.card_values("self", screen, 6)
        X = Card_2.x_value("self", card)
        Y = Card_2.y_value("self", card)
        Card_2.card_draw("self", screen, X, Y, card, card_value)
        card = Card_2.card_values("self", screen, 7)
        X = Card_2.x_value("self", card)
        Y = Card_2.y_value("self", card)
        Card_2.card_draw("self", screen, X, Y, card, card_value)
        card = Card_2.card_values("self", screen, 8)
        X = Card_2.x_value("self", card)
        Y = Card_2.y_value("self", card)
        Card_2.card_draw("self", screen, X, Y, card, card_value)
        card = Card_2.card_values("self", screen, 9)
        X = Card_2.x_value("self", card)
        Y = Card_2.y_value("self", card)
        Card_2.card_draw("self", screen, X, Y, card, card_value)
        card = Card_2.card_values("self", screen, 10)
        X = Card_2.x_value("self", card)
        Y = Card_2.y_value("self", card)
        Card_2.card_draw("self", screen, X, Y, card, card_value)
        card = Card_2.card_values("self", screen, 11)
        X = Card_2.x_value("self", card)
        Y = Card_2.y_value("self", card)
        Card_2.card_draw("self", screen, X, Y, card, card_value)
        card = Card_2.card_values("self", screen, 12)
        X = Card_2.x_value("self", card)
        Y = Card_2.y_value("self", card)
        Card_2.card_draw("self", screen, X, Y, card, card_value)


    def card_values(self, screen, card_value):
        """
        To set the value based on the card.
        :param screen: Defines the screen size.
        :return:
        """

        return card_value

    def x_value(self, card):
        if card == 1 or card == 5 or card == 9:
            X = 50
        elif card == 2 or card == 6 or card == 10:
            X = 330
        elif card == 3 or card == 7 or card == 11:
            X = 610
        elif card == 4 or card == 8 or card == 12:
            X = 890
        return X

    def y_value(self, card):
        if card == 1 or card == 2 or card == 3 or card == 4:
            Y = 50
        if card == 5 or card == 6 or card == 7 or card == 8:
            Y = 270
        if card == 9 or card == 10 or card == 11 or card == 12:
            Y = 490

        return Y

    def card_draw(self, screen, X, Y, card_number, card_value):
        """
        Draws the cards
        :param screen: The screen size
        :param X: The X coordinate
        :param Y:  The Y coordinate
        :param card_number: This determines the cards value to show on the screen.
        :return:
        """
        card_width = 250
        card_height = 200
        rect_pos_1 = [X, Y, card_width, card_height]

        pygame.draw.ellipse(screen, 'blue', rect_pos_1, 20)
        pygame.draw.rect(screen, 'blue', rect_pos_1, 20)

        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        keys = pygame.key.get_pressed()
        number = str(card_number)
        font = pygame.font.Font('freesansbold.ttf', 60)
        text = font.render(number, True, green, blue)
        textRect = text.get_rect()
        textRect.center = (X + 120, Y + 100)
        screen.blit(text, textRect)

        if keys[pygame.K_1]:
            V = 160
            W = 150
            press_number.__init__('self', 1, screen, V, W, Math.card_1_value)
            """
            number = str(100)
            font = pygame.font.Font('freesansbold.ttf', 60)
            text = font.render(number, True, green, blue)
            textRect = text.get_rect()
            textRect.center = (X + 100, Y + 100)
            screen.blit(text, textRect)
            """

        if keys[pygame.K_2]:
            V = 450
            W = 150
            press_number.__init__('self', 2, screen, V, W, Math.card_2_value)
            """
            #V += 100
            #W += 100
            #surface_1 = pygame.Surface.blit(screen, zero_image, (V, W))
            #surface_1.fit(surface_1)
            number = str(100)
            font = pygame.font.Font('freesansbold.ttf', 60)
            text = font.render(number, True, green, blue)
            textRect = text.get_rect()
            textRect.center = (X, Y)
            screen.blit(text, textRect)
            """
        if keys[pygame.K_3]:
            V = 730
            W = 150
            press_number.__init__('self', 3, screen, V, W, Math.card_3_value)
        if keys[pygame.K_4]:
            V = 1008
            W = 150
            press_number.__init__('self', 4, screen, V, W, Math.card_4_value)
        if keys[pygame.K_5]:
            V = 170
            W = 370
            press_number.__init__('self', 5, screen, V, W, Math.card_5_value)
        if keys[pygame.K_6]:
            V = 450
            W = 370
            press_number.__init__('self', 6, screen, V, W, Math.card_6_value)
        if keys[pygame.K_7]:
            V = 730
            W = 370
            press_number.__init__('self', 7, screen, V, W, Math.card_7_value)
        if keys[pygame.K_8]:
            V = 1008
            W = 370
            press_number.__init__('self', 8, screen, V, W, Math.card_8_value)
        if keys[pygame.K_9]:
            V = 160
            W = 590
            press_number.__init__('self', 9, screen, V, W, Math.card_9_value)
        if keys[pygame.K_z]:
            V = 450
            W = 590
            press_number.__init__('self', 10, screen, V, W, Math.card_10_value)
        if keys[pygame.K_x]:
            V = 730
            W = 590
            press_number.__init__('self', 11, screen, V, W, Math.card_11_value)
        if keys[pygame.K_c]:
            V = 1008
            W = 590
            press_number.__init__('self', 12, screen, V, W, Math.card_12_value)



    def card_grid(self, screen):
        """
        Creates the cards for play.
        :param screen: defines the game screen size.
        :return:
        Displays cards
        """
        #pygame.draw.line(screen, 'blue', [(screen.get_height() / 2), (base_y_top / 2)], [(screen.get_height() / 2), (base_y_top / 4)], 5)
        #base_x_top = screen.get_height()
        #base_y_top = screen.get_width()
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




        for i in range(12):
            card_list.append(card_number)
            x_list.append(X)
            y_list.append(Y)
            if card_number == 0:
                modifier_x = 90
                modifier_y = 25
            if card_number == 1:
                #modifier_x = 0
                #modifier_y = 220
                modifier_x = 280
                modifier_y = 0
                one_image = pygame.image.load("1.png")
                one_image = pygame.transform.scale(one_image, (50, 50))
            if card_number == 2:
                #modifier_x = 0
                #modifier_y = 220
                modifier_x = 280
                modifier_y = 0
            if card_number == 3:
                modifier_x = 280
                modifier_y = 0
            if card_number == 4:
                modifier_x = -840
                modifier_y = 220
            if card_number == 5:
                modifier_x = 0
                modifier_y = -220
                modifier_x = 280
                modifier_y = 0
            if card_number == 6:
                modifier_x = 280
                modifier_y = 0
            if card_number == 7:
                modifier_x = 0
                modifier_y = 220
                modifier_x = 280
                modifier_y = 0
            if card_number == 8:
                modifier_x = 0
                modifier_y = 220
                modifier_x = -840
                modifier_y = 220
            if card_number == 9:
                modifier_x = 280
                modifier_y = 0
            if card_number == 10:
                modifier_x = 0
                modifier_y = -220
                modifier_x = 280
                modifier_y = 0
            if card_number == 11:
                modifier_x = 0
                modifier_y = -220
                modifier_x = 280
                modifier_y = 0

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

        V = 100
        W = 50

        if keys[pygame.K_1]:
            press_number.__init__('self', 1)
            """
            surface_1 = pygame.Surface.blit(screen, zero_image, (V, W))
            surface_1.fit(surface_1)
            number = str(100)
            font = pygame.font.Font('freesansbold.ttf', 60)
            text = font.render(number, True, green, blue)
            textRect = text.get_rect()
            textRect.center = (X // 2, Y // 2)
            #screen.blit(text, textRect)
            """

        if keys[pygame.K_2]:
            press_number.__init__('self', 2)
            """
            V += 100
            W += 100
            surface_1 = pygame.Surface.blit(screen, zero_image, (V, W))
            surface_1.fit(surface_1)
            textRect = text.get_rect()
            textRect.center = (X // 2, Y // 2)
            screen.blit(text, textRect)
            """
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
        #Math.__init__("self", screen)

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


class press_number(Math):
    def __init__(self, num, screen, X, Y, card_value):

        #card_value = Math.leveler_defined(0, screen)
        if num == 1:
            matched = str(Math.card_1_value)
        if num == 2:
            matched = str(Math.card_2_value)
        if num == 3:
            matched = str(Math.card_3_value)
        if num == 4:
            matched = str(Math.card_4_value)
        if num == 5:
            matched = str(Math.card_5_value)
        if num == 6:
            matched = str(Math.card_6_value)
        if num == 7:
            matched = str(Math.card_7_value)
        if num == 8:
            matched = str(Math.card_8_value)
        if num == 9:
            matched = str(Math.card_9_value)
        if num == 10:
            matched = str(Math.card_10_value)
        if num == 11:
            matched = str(Math.card_11_value)
        if num == 12:
            matched = str(Math.card_12_value)

        #matched = str(100)
        font = pygame.font.Font('freesansbold.ttf', 60)
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        text = font.render(matched, True, green, blue)
        #surface_1 = pygame.Surface.blit(screen, matched, (100, 50))
        #surface_1.fit(surface_1)
        textRect = text.get_rect()
        textRect.center = (X, Y)
        screen.blit(text, textRect)
        #press_number.image_loader(num)

        """
        number = str(100)
        
        text = font.render(number, True, green, blue)
        textRect = text.get_rect()
        textRect.center = (X + 100, Y + 100)
        screen.blit(text, textRect)
        """



    def image_loader(self, num):
        pass
        """
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
        """










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

if __name__ == '__main__':
    main()
