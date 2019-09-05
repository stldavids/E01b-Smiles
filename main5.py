#!/usr/bin/env python3

import utils, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Smiley Face Example"

class Faces(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Show the mouse cursor
        self.set_mouse_visible(True)

        # Set base numbers to the center of the screen
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2

        #Set background to white
        arcade.set_background_color(open_color.white)

    def on_draw(self):
        """ Draw the face """
        arcade.start_render()

        #Face is set to the center defined above
        face_x,face_y = (self.x,self.y)
        #Set mouth positon on face
        smile_x,smile_y = (face_x + 0,face_y - 10)
        #Set left eye position
        eye1_x,eye1_y = (face_x - 30,face_y + 20) 
        #Set right eye position
        eye2_x,eye2_y = (face_x + 30,face_y + 20)
        #Set left eye catch position
        catch1_x,catch1_y = (face_x - 25,face_y + 25)
        #Set right eye catch position 
        catch2_x,catch2_y = (face_x + 35,face_y + 25) 

        #Draw yellow base
        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3)
        #Draw outline
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4)
        #Draw left eye
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black)
        #Draw right eye
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black)
        #Draw left eye catch
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2)
        #Draw right eye catch
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2)
        #Draw mouth
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4)


    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        self.x = x
        self.y = y



window = Faces()
arcade.run()