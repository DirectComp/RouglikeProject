#!/user/bin/env python3
import sys
import os
os.environ["path"] = os.path.dirname(sys.executable) + ";" + os.environ["path"]
import glob

import tcod

#call the functions we wrote
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main() -> None:
    #defining the variables of the screen
    screen_width = 80
    screen_height = 50
    
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(
        #here we tell tcod what font to use
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    #event_handler is an instance of an EventHandler class.
    #we use it to receive events and process them
    event_handler = EventHandler()

    #this part creates the screen
    with tcod.context.new_terminal(
        screen_width,
        screen_width,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:

        #this is the console that we are drawing to. We set the width & height
        root_console = tcod.Console(screen_width, screen_height, order="F")

        #this is our game loop
        while True:
            #this line tells the program to put the '@' on the screen in the proper place
            root_console.print(x=player_x, y=player_y, string="@")

            #this line puts the info onto the screen
            #context.present updates the screen with what we've given it
            context.present(root_console)

            

            #capture user input
            for event in tcod.event.wait():
                
                #We send event to event_handler's "dispatch" method which sends it to the proper place
                #The Action returned will be assigned to action
                action = event_handler.dispatch(event)
                
                #if we receive no action we skip the rest of the loop
                if action is None:
                    continue
                
                #if action is an instance of the class MovementAction we move our '@' symbol
                #We grab the dx and dy values we gave earlier
                #Add dx and dy to player_x and player_y
                #Console is using player_x and player_y so this causes the symbol to move
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                #how to exit the program if Esc key is pressed
                elif isinstance(action, EscapeAction):
                    raise SystemExit()

if __name__ == "__main__":
    main()
