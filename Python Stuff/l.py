Python 3.6.8 (default, Aug 20 2019, 17:12:48) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> mul(2,3)

====================== RESTART: /home/whit2945/lab4.py ======================
>>> mul(2,3)
24
>>> mul(2,3)
24
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> mul(2,3)
12
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> mul(2,3)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    mul(2,3)
  File "/home/whit2945/lab4.py", line 4, in mul
    c += 3
UnboundLocalError: local variable 'c' referenced before assignment
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> mul(2,3)
6
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(2, 3)
9
>>> expo(2,3)
9
>>> expo(3, 2)
6
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(2,3)
6
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(2,3)
6
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(2,3)
18
>>> expo(2,3)
18
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(2,3)
12
>>> mul(2,3)
6
>>> mul(4,4)
16
>>> mul(8,2)
16
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> mul(2,3)
6
>>> mul(2,4)
8
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(2,4)
16
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(2,3)
0
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(2,3)
36
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(2,3)
12
>>> expo(2,0)
0
>>> expo(2,1)
4
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(2,3)
36
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(2,3)
16
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(2,3)
16
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(2,3)
8
>>> expo(4,4)
256
>>> expo(1,1)
0
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(1,1)
0
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(1,1)
1
>>> expo(1,2)
1
>>> expo(1,3)
1
>>> expo(2,2)
8
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(2,2)
4
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> expo(1,0)
1
>>> expo(2,2)
4
>>> expo(4,4)
256
>>> expo(4,2)
16
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> div27(15)
True
>>> 
====================== RESTART: /home/whit2945/lab4.py ======================
>>> 
====================== RESTART: /home/whit2945/race.py ======================
Traceback (most recent call last):
  File "/home/whit2945/race.py", line 4, in <module>
    leo.shape("Turtle")
  File "/usr/lib/python3.6/turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named Turtle
>>> 
====================== RESTART: /home/whit2945/race.py ======================
>>> 
====================== RESTART: /home/whit2945/race.py ======================
>>> 
====================== RESTART: /home/whit2945/race.py ======================
>>> 
====================== RESTART: /home/whit2945/race.py ======================
>>> 
====================== RESTART: /home/whit2945/race.py ======================
>>> 
====================== RESTART: /home/whit2945/race.py ======================
>>> 
====================== RESTART: /home/whit2945/race.py ======================
>>> 
====================== RESTART: /home/whit2945/race.py ======================
>>> 
====================== RESTART: /home/whit2945/race.py ======================
Traceback (most recent call last):
  File "/home/whit2945/race.py", line 15, in <module>
    leo.forward(randint(1,16))
NameError: name 'randint' is not defined
>>> 
====================== RESTART: /home/whit2945/race.py ======================
Traceback (most recent call last):
  File "/home/whit2945/race.py", line 16, in <module>
    leo.forward(randint(1,16))
NameError: name 'randint' is not defined
>>> 
====================== RESTART: /home/whit2945/race.py ======================

====================== RESTART: /home/whit2945/race.py ======================
>>> 
==================== RESTART: /home/whit2945/checkher.py ====================
>>> 
==================== RESTART: /home/whit2945/checkher.py ====================
>>> 
==================== RESTART: /home/whit2945/checkher.py ====================
Traceback (most recent call last):
  File "/home/whit2945/checkher.py", line 2, in <module>
    turtle.begin_fill("Red")
TypeError: begin_fill() takes 0 positional arguments but 1 was given
>>> 
==================== RESTART: /home/whit2945/checkher.py ====================
>>> 
==================== RESTART: /home/whit2945/checkher.py ====================
Traceback (most recent call last):
  File "<string>", line 8, in forward
  File "/usr/lib/python3.6/turtle.py", line 1637, in forward
    self._go(distance)
  File "/usr/lib/python3.6/turtle.py", line 1605, in _go
    self._goto(ende)
  File "/usr/lib/python3.6/turtle.py", line 3178, in _goto
    self._pencolor, self._pensize, top)
  File "/usr/lib/python3.6/turtle.py", line 545, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "/usr/lib/python3.6/tkinter/__init__.py", line 2469, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/whit2945/checkher.py", line 7, in <module>
    turtle.forward(80)
  File "<string>", line 12, in forward
turtle.Terminator
>>> 
==================== RESTART: /home/whit2945/checkher.py ====================

==================== RESTART: /home/whit2945/checkher.py ====================
Traceback (most recent call last):
  File "/home/whit2945/checkher.py", line 16, in <module>
    turtle.left(90)
  File "<string>", line 8, in left
  File "/usr/lib/python3.6/turtle.py", line 1699, in left
    self._rotate(angle)
  File "/usr/lib/python3.6/turtle.py", line 3276, in _rotate
    self._update()
  File "/usr/lib/python3.6/turtle.py", line 2660, in _update
    self._update_data()
  File "/usr/lib/python3.6/turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "/usr/lib/python3.6/turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
==================== RESTART: /home/whit2945/checkher.py ====================
Traceback (most recent call last):
  File "<string>", line 8, in forward
  File "/usr/lib/python3.6/turtle.py", line 1637, in forward
    self._go(distance)
  File "/usr/lib/python3.6/turtle.py", line 1605, in _go
    self._goto(ende)
  File "/usr/lib/python3.6/turtle.py", line 3178, in _goto
    self._pencolor, self._pensize, top)
  File "/usr/lib/python3.6/turtle.py", line 545, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "/usr/lib/python3.6/tkinter/__init__.py", line 2469, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/whit2945/checkher.py", line 15, in <module>
    turtle.forward(80)
  File "<string>", line 12, in forward
turtle.Terminator
>>> 
==================== RESTART: /home/whit2945/checkher.py ====================
Traceback (most recent call last):
  File "<string>", line 8, in forward
  File "/usr/lib/python3.6/turtle.py", line 1637, in forward
    self._go(distance)
  File "/usr/lib/python3.6/turtle.py", line 1605, in _go
    self._goto(ende)
  File "/usr/lib/python3.6/turtle.py", line 3178, in _goto
    self._pencolor, self._pensize, top)
  File "/usr/lib/python3.6/turtle.py", line 545, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "/usr/lib/python3.6/tkinter/__init__.py", line 2469, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/whit2945/checkher.py", line 15, in <module>
    turtle.forward(80)
  File "<string>", line 12, in forward
turtle.Terminator
>>> 
==================== RESTART: /home/whit2945/checkher.py ====================
Traceback (most recent call last):
  File "/home/whit2945/checkher.py", line 16, in <module>
    turtle.left(90)
  File "<string>", line 8, in left
  File "/usr/lib/python3.6/turtle.py", line 1699, in left
    self._rotate(angle)
  File "/usr/lib/python3.6/turtle.py", line 3276, in _rotate
    self._update()
  File "/usr/lib/python3.6/turtle.py", line 2660, in _update
    self._update_data()
  File "/usr/lib/python3.6/turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "/usr/lib/python3.6/turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
==================== RESTART: /home/whit2945/checkher.py ====================
Traceback (most recent call last):
  File "/home/whit2945/checkher.py", line 16, in <module>
    turtle.left(90)
  File "<string>", line 8, in left
  File "/usr/lib/python3.6/turtle.py", line 1699, in left
    self._rotate(angle)
  File "/usr/lib/python3.6/turtle.py", line 3276, in _rotate
    self._update()
  File "/usr/lib/python3.6/turtle.py", line 2660, in _update
    self._update_data()
  File "/usr/lib/python3.6/turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "/usr/lib/python3.6/turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
==================== RESTART: /home/whit2945/checkher.py ====================
Traceback (most recent call last):
  File "/home/whit2945/checkher.py", line 30, in <module>
    turtle.left(90)
  File "<string>", line 8, in left
  File "/usr/lib/python3.6/turtle.py", line 1699, in left
    self._rotate(angle)
  File "/usr/lib/python3.6/turtle.py", line 3276, in _rotate
    self._update()
  File "/usr/lib/python3.6/turtle.py", line 2660, in _update
    self._update_data()
  File "/usr/lib/python3.6/turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "/usr/lib/python3.6/turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
==================== RESTART: /home/whit2945/checkher.py ====================
600
360
360
360
Traceback (most recent call last):
  File "/home/whit2945/checkher.py", line 31, in <module>
    turtle.left(90)
  File "<string>", line 5, in left
turtle.Terminator
>>> 
==================== RESTART: /home/whit2945/checkher.py ====================
600
Traceback (most recent call last):
  File "/home/whit2945/checkher.py", line 31, in <module>
    turtle.left(90)
  File "<string>", line 8, in left
  File "/usr/lib/python3.6/turtle.py", line 1699, in left
    self._rotate(angle)
  File "/usr/lib/python3.6/turtle.py", line 3276, in _rotate
    self._update()
  File "/usr/lib/python3.6/turtle.py", line 2660, in _update
    self._update_data()
  File "/usr/lib/python3.6/turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "/usr/lib/python3.6/turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
==================== RESTART: /home/whit2945/checkher.py ====================
600
600
520
440
360
280
200
120
>>> 
==================== RESTART: /home/whit2945/checkher.py ====================
600
520
440
360
280
200
120
40
>>> 
