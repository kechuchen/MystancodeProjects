"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
import random

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    dx = graphics.get_dx()
    dy = graphics.get_dy()

    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        if graphics.p and graphics.lives > 0:
            graphics.ball.move(dx, dy)
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                dx = -dx
            if graphics.ball.y <= 0:
                dy = -dy
            if graphics.ball.y >= graphics.paddle_bottom:
                graphics.count_lives()
                graphics.p = False
                graphics.reset_ball()
            if graphics.check():
                dy = -dy
        if graphics.lives == 0:
            graphics.game_over1()
            break
        if graphics.score is graphics.total_score:
            graphics.congratulations()
            break


if __name__ == '__main__':
    main()
