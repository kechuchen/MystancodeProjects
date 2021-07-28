"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.
NUM_LIVES = 3


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        self._dyy = INITIAL_Y_SPEED * 2
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window_width-paddle_width)/2,
                            y=self.window_height-paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = "DarkTurquoise"

        self.window.add(self.paddle)

        # paddle bottom
        self.paddle_bottom = self.window_height-(paddle_offset-paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(self.window_width-ball_radius)/2,
                          y=(self.window_height-ball_radius)/2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self._dx = random.randint(1, MAX_X_SPEED)
        self._dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self._dx = -self._dx

        # Initialize our mouse listeners
        self.p = False
        onmousemoved(self.move_paddle)
        onmouseclicked(self.handle_click)

        # score label
        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.font = '-30'
        self.window.add(self.score_label, 0, 50)

        # lives label
        self.lives = NUM_LIVES
        self.lives_label = GLabel('Lives: ' + str(self.lives))
        self.lives_label.font = '-30'

        self.window.add(self.lives_label, 300, 50)

        # total score
        self.total_score = brick_rows * brick_cols

        # game over
        self.game_over = GLabel('GAME OVER', x=10, y=300)
        self.game_over.font = "-70"

        # win
        self.win = GLabel('Congratulations！\nWinner Winner, Chicken dinner!', x=50, y=300)
        self.win.font = "-20"

        # Draw bricks
        x = 2
        for i in range(brick_cols-x*5, brick_cols-x*4):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height,
                                   x=j*(brick_width + brick_spacing),
                                   y=brick_offset+(brick_height+brick_spacing)*i)
                self.brick.filled = True
                self.brick.fill_color = 'red'
                self.window.add(self.brick)

        for i in range(brick_cols-x*4, brick_cols-x*3):
            for j in range(brick_cols):
                self.brick1 = GRect(brick_width, brick_height,
                                    x=j*(brick_width + brick_spacing),
                                    y=brick_offset+(brick_height+brick_spacing)*i)
                self.brick1.filled = True
                self.brick1.fill_color = 'orange'
                self.window.add(self.brick1)

        for i in range(brick_cols-x*3, brick_cols-x*2):
            for j in range(brick_cols):
                self.brick3 = GRect(brick_width, brick_height,
                                    x=j*(brick_width + brick_spacing),
                                    y=brick_offset+(brick_height+brick_spacing)*i)
                self.brick3.filled = True
                self.brick3.fill_color = 'yellow'
                self.window.add(self.brick3)

        for i in range(brick_cols-x*2, brick_cols-x*1):
            for j in range(brick_cols):
                self.brick4 = GRect(brick_width, brick_height,
                                    x=j*(brick_width + brick_spacing),
                                    y=brick_offset+(brick_height+brick_spacing)*i)
                self.brick4.filled = True
                self.brick4.fill_color = 'green'
                self.window.add(self.brick4)

        for i in range(brick_cols-x*1, brick_cols-x*0):
            for j in range(brick_cols):
                self.brick5 = GRect(brick_width, brick_height,
                                    x=j*(brick_width + brick_spacing),
                                    y=brick_offset+(brick_height+brick_spacing)*i)
                self.brick5.filled = True
                self.brick5.fill_color = 'blue'
                self.window.add(self.brick5)

        self.ball_radius = BALL_RADIUS

    # on mouse move function
    def move_paddle(self, m):
        obj = self.window.get_object_at(m.x, m.y)
        self.window.add(self.paddle, x=m.x-self.paddle.width/2, y=self.paddle.y)
        if m.x <= self.paddle.width/2:
            self.paddle.x = 0
        if m.x >= self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width

    # on mouse click function
    def handle_click(self, n):
        self.p = True

    # remove the breaks and bounce back while colliding paddle and breaks
    def check(self):
        check1 = self.window.get_object_at(self.ball.x, self.ball.y)
        if check1 is self.score_label or check1 is self.lives:
            return None
        if check1 is self.paddle:
            return None
        if check1 is not None and check1 is not self.paddle:
            self.window.remove(check1)
            self.score += 1
            self.score_label.text = 'Score: ' + str(self.score)
            return True

        check2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        if check2 is self.score_label or check2 is self.lives:
            return None
        if check2 is self.paddle:
            return None
        if check2 is not None and check2 is not self.paddle:
            self.window.remove(check2)
            self.score += 1
            self.score_label.text = 'Score: ' + str(self.score)
            return True

        check3 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if check3 is self.score_label or check3 is self.lives:
            return None
        if check3 is self.paddle:
            return True
        if check3 is not None and check3 is not self.paddle:
            self.window.remove(check3)
            self.score += 1
            self.score_label.text = 'Score: ' + str(self.score)
            return True

        check4 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        if check4 is self.score_label or check4 is self.lives:
            return None
        if check4 is self.paddle:
            return True
        if check4 is not None and check4 is not self.paddle:
            self.window.remove(check4)
            self.score += 1
            self.score_label.text = 'Score: ' + str(self.score)
            return True
        else:
            return None

    def get_dx(self):
        return self._dx

    def get_dy(self):
        return self._dy

    # reset game
    def reset_ball(self):
        self.window.add(self.ball, x=(self.window_width-self.ball_radius)/2, y=(self.window_height-self.ball_radius)/2)

    # game over
    def game_over1(self):
        self.window.add(self.game_over)

    # Congratulations
    def congratulations(self):
        self.window.add(self.win)

    # count lives
    def count_lives(self):
        if self.ball.y >= self.paddle_bottom:
            self.lives -= 1
            self.lives_label.text = 'Lives: ' + str(self.lives)





