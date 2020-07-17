from typing import Optional

import tcod.event

#import actions from actions.py
from actions import Action, EscapeAction, MovementAction

#EventHandler is a subclass of tcod's EventDispatch
#EventDispatch is a class that allows us to send an event to its proper
#method based on what type of event it is
class EventHandler(tcod.event.EventDispatch[Action]):

    #this is calling the ev_quit method and quitting the program when "X" is pressed
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    #this method receives the key press events and returs an Action or None, if no valid key was pressed
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:

        #action is the variable we use to hold whatever subclass of Action
        action: Optional[Action] = None

        key = event.sym

        #possible keys pressed
        if key == tcod.event.K_UP:
            action == MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action == MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action == MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action == MovementAction(dx=1, dy=0)

        #used to escape the game
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        #No valid key was pressed
        return action