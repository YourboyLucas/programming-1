# main.py
# Midnight Rider
# A text-based adventure game.
# Gamespot gives it 9 out of 10

import sys
import textwrap
import time


INTRODUCTION = """
WELCOM TO MIDNIGHT

WE'VE STOLRN A CAR. WE NEED TO GET IT HOME.
THE CAR IS SPECIAL

THAT'S WHY THE GOVERMENT WANTS IT.
"""

def main():
    pass
    for char in textwrap.dedent(INTRODUCTION):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    # TODO: Display introduction

    # MAIN LOOP

        # TODO: Present the user their choices

        # TODO: Change the environment based on
        #       user choice, and RNG
        # TODO: Rnadom event generator

