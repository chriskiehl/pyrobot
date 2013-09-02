pyrobot
=======


What is it?
-----------  

PyRobot is a lightweight, pure python windows automation library loosely modeled after Java's Robot Class. It can be used to drive applications that don't provide an API or any way of hooking into them programatically. Good for when you can't (or don't want to) install the great, but a bit hefty, pywin32 libraries.   

Installation
------------

PyRobot is a sinlge Python file. So, you can either download it directly from this github page, or clone the repo: 

git clone https://github.com/chriskiehl/pyrobot  

Usuage
------

Similar to Java, everything is controlled via a single class.

 ```python

# Import the robot class from the pyrobot module
from pyrobot import Robot

# create an instance of the class
robot = Robot()

# Do cool stuff
pixel = robot.get_pixel(340,400)
if pixel == ((255,255,255)): 
	robot.set_mouse_pos(340,400)
	robot.click()
	robot.push_to_clipboard('Hello world! How are ya!")
	robot.paste()

# etc.. 

 ```  

Doc  
---  
   
| Method                             | Summary                    |
| -----------------------------------|-----------------------------
|def set_mouse_pos(self, x, y): | Moves mouse pointer to given screen coordinates. |
|def get_mouse_pos(self): | returns current mouse coordinates |
|def get_pixel(self, x, y): | Returns the pixel color of the given screen coordinate|
|def mouse_down(self, button): | Presses one mouse button. Left, right, or middle|
|def mouse_up(self, button): | Releases mouse button. Left, right, or middle|
|def click(self, button): | Simulates a full mouse click. One down event, one up event. |
|def scroll_mouse_wheel(self, direction, clicks):  | Scrolls the mouse wheel either up or down X number of 'clicks'. |
|def add_to_clipboard(self, string):  | Copy text into clip board for later pasting. |
|def clear_clipboard(self): | Clear everything out of the clipboard|
|def take_screenshot(self): | NOTE: REQUIRES: PYTHON IMAGE LIBRARY| Takes a snapshot of desktop and loads it into memory |
|def key_press(self, key): | Pesses a given key. |
|def key_release(self, key): | Releases a given key. |
|def type_string(self, input_string, delay=.005): | Convenience function for typing out stings. |
|def type_backwards(self, input_string, delay=.05): | Types right to left. Beacuse why not! |




Contact
-------

Feature request? Bug? Hate it?  
Drop me a line at audionautic@gmail.com, or on Twitter @thechriskiehl (though, I'm seldom on there..)









 