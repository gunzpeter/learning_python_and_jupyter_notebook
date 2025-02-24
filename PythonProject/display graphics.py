import graphics
from graphics import*
import ctypes

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)

print('A monitor felbontása:' 'x:' + str(screensize[0]) + ' ' + 'y: ' + str(screensize[1]))

a = input('Maximális felbontású ablakot szeretnél? (i/n): ')

if a == 'i':
   x = screensize[0]
   y = screensize[1]
else:
    x = int(input('X tengely hossza:'))
    y = int(input('Y tengely hossza:'))

    if x > screensize[0]:
        x=int(input('adj meg' + str(screensize[0]) + '-nél kisebb számot'))
    if y > screensize[1]:
        y = int(input('adj meg' + str(screensize[0] )+ '-nél kisebb számot'))

win=graphics.GraphWin("Windows",x,y)

c = Circle(Point(50,50), 10)
c.draw(win)

win.getMouse()
win.close()



