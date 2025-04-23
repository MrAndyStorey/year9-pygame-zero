alien = Actor('alien')

TITLE = "Y9 Game Development"
WIDTH = 600
HEIGHT = 400


# The initial position of the alien
alien.topright = 0, 10


def draw():
    """Clear the screen and draw the alien."""
    screen.clear()
    alien.draw()


def update():
    """Move the alien by one pixel."""
    alien.x += 1

    # If the alien is off the right hand side of the screen,
    # move it back off screen to the left-hand side
    if alien.left > WIDTH:
        alien.right = 0

def on_key_down(key):
    if key == keys.UP:
        alien.y -= 10
    elif key == keys.DOWN:
        alien.y += 10
