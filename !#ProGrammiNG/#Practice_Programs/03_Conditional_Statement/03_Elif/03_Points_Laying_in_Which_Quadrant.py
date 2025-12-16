# Wap to check the given points are lying in which quadrant.

x = int(input('Enter X:'))
y = int(input('Enter Y:'))

if x > 0 and y > 0:
    print('First Quadrant')
    
elif x < 0 and y > 0:
    print('Second Quadrant')
    
elif x < 0 and y < 0:
    print('Third Quadrant')
    
elif x > 0 and y < 0:
    print('Fourth Quadrant')
    
else:
    print('Point lies on axis or origin')
