alien_0= {
    'color' : 'green',
    'points' : '5'
}

print(f'{alien_0['color'].title()}')
print(f'{alien_0['points'].title()}')

print(f"You just earned {alien_0['points']} points")

alien_0['x_position'] = 0 
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2 
else:
    x_increment = 3
# The new position is the old position plus the increment. 
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

alien_0['speed'] = 'fast'

print(f"{ alien_0 }")
