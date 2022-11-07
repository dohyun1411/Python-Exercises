import random
from cs1robots import *

create_world(7, 8)
hubo = Robot(beepers=600, avenue=1, street=8)
hubo.set_pause(0.1)

year = random.randint(1000, 9999)
month = random.randint(1, 12)
print(f"{year} / {month}")
