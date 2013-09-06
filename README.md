pyrobot
=======


What is it?
-----------  

PyRobot is a lightweight, pure Python Windows automation library loosely modeled after Java's Robot Class. It can be used to drive applications that don't provide an API or any way of hooking into them programatically. Good for when you can't (or don't want to) install the great, but a bit hefty, pywin32 libraries.   

Installation
------------

PyRobot is a single Python file. So, you can either download it directly from this github page, or clone the repo: 

git clone https://github.com/chriskiehl/pyrobot  

Usage
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
	robot.add_to_clipboard('Hello world! How are ya!")
	robot.paste()

# etc.. 

 ```  

Doc  
---  
   
| Method                                | Summary                    |
| --------------------------------------|-----------------------------
| set_mouse_pos(x, y): | Moves mouse pointer to given screen coordinates. |
| get_mouse_pos(): 		| Returns current mouse coordinates |
| get_pixel(x, y): 	| Returns the pixel color of the given screen coordinate|
| mouse_down(button): | Presses one mouse button. Left, right, or middle|
| mouse_up(button):	 | Releases mouse button. Left, right, or middle|
| click(button): 	| Simulates a full mouse click. One down event, one up event. |
| scroll_mouse_wheel(), direction, clicks):  | Scrolls the mouse wheel either up or down X number of 'clicks'. |
| add_to_clipboard(string):  | Copy text into clip board for later pasting. |
| clear_clipboard(): | Clear everything out of the clipboard|
| take_screenshot(): | NOTE: REQUIRES: PYTHON IMAGE LIBRARY| Takes a snapshot of desktop and loads it into memory |
| key_press(key): | Presses a given key. |
| key_release(key): | Releases a given key. |
| type_string(input_string, delay=.005): | Convenience function for typing out strings. |
| type_backwards(input_string, delay=.05): | Types right to left. Because why not! |
| start_program(full_path) | Starts a windows applications.  |
		'''


Special take_snapshot Note
-----------------------  

Being that Python has no built in Image library (that I know of), it seemed of little use to include a snapshot method which simply saves the picture to disk. For 90% of program automation, I find that querying pixels works fairly well (e.g. `robot.get_pixel`). However, if you need to do more advanced display searching, or want to do template matching, you'll need an external library. So there is a method in there to contruct a PIL Image object. It just, of course, requires that PIL be installed. Other than that, dependency free! :-)  

TODO
----  

* Multi-monitor support for screen_grab functions
* Allow specific window/program targeting so that relative coordinates can be used while scripting. 


Contact
-------

Feature request? Bug? Hate it?  
Drop me a line at audionautic@gmail.com, or on Twitter @thechriskiehl 









 