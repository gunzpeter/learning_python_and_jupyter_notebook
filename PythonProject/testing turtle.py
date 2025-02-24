import turtle as t
import ctypes

user32 = ctypes.windll.user32
scrsize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)

t.screensize(*scrsize)

t.screen.title('Object-oriented turtle demo')
t.screen.bgcolor("orange")

