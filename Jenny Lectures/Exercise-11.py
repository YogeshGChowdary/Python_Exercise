#### Random module -> coin spin -> heads or tails ####

import random

side = random.randint(0, 1)
print(side)

if side == 0:
    print("Heads")
else:
    print("Tails")

    
