from cs1robots import *


load_world('worlds/harvest3.wld')

hubo = Robot()
hubo.set_trace('blue')
hubo.set_pause(1)

hubo.move()
hubo.move()
hubo.turn_left()
hubo.move()
