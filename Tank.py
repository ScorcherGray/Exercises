# Create a simple game. User will try to destroy an enemy tank.
import matplotlib.pyplot as plt
import numpy as np
import random as rand

# The game should randomly select a distance for the enemy tank somewhere from 50 to 150 meters away.
enemy_dist = rand.randint(50, 150)
print("The enemy tank is {} meters away".format(enemy_dist))

# Display to the user how far the tank is, ask how fast and at what angle they would like to shoot their projectile
v_0 = int(input('What initial velocity will you give your projectile (in m/s)? '))
theta = int(input('At what angle from horizontal will you fire your projectile (in degrees)? '))

# The game creates a plot with a size of 10 by 5 units. x axis should go from -10 to 160
# y axis should go from -10 to 80. Area below y=0 should be light brown. A green circle at the origin - the user's tank
fig = plt.figure(figsize=(6, 6)) 
xVals = np.array([-10, 160])
yVals = np.array([-1, 80])
ax = fig.add_subplot(111)
ground = -10
plt.fill_between(xVals,ground,y2=0, where=None, interpolate=False, step=None, color='#4B371C')
# A red x should be placed at the location of the enemy tank. A black line should show the path of the projectile
ax.plot(enemy_dist, 0, 'rx')
ax.set_ylim([-10, 80])
plt.show()

# An orange circle with radius of 10 meters should be centered at the point of impact to indicate blast radius.
# Game should tell the user how far from the enemy tank the projectile landed.
# If the user's tank is within the blast radius, the program should congratulate the user on destroying their own tank
# Then end the game. Otherwise, if the enemy tank is within the blast radius, notify the user they destroyed the
# enemy tank and end the game. If neither tank is within radius, the game should inform the user they missed and ask
# if they would like to try again. If yes, repeat using the same enemy tank distance. Otherwise, end the game.
