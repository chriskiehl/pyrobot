'''
This will likely develop slowly.. I have horrible testing practices... 
'''

import sys
sys.path.insert(0, '..')

from PIL import Image
import unittest
from ctypes import *
from pyrobot import Robot

class TestRobot(unittest.TestCase):
	def setUp(self):
		self.robot = Robot()

	def test_take_screenshot_full_screen(self):
		SM_CXVIRTUALSCREEN = 78 # width of the virtual screen
		SM_CYVIRTUALSCREEN = 79 # height of the virtual screen
		virtual_screen_size = (
			windll.user32.GetSystemMetrics(SM_CXVIRTUALSCREEN),
			windll.user32.GetSystemMetrics(SM_CYVIRTUALSCREEN)
		)

		im = self.robot.take_screenshot() # no args: full virtual screen
		self.assertEquals(im.size, virtual_screen_size)

	def test_take_screenshot_bounds(self):
		bounding_box = (0,0,100,100)
		box_size = (100,100)
		im = self.robot.take_screenshot(bounding_box)
		self.assertEquals(im.size, box_size)

	def test_get_display_monitors(self):
		# Since the code inside of the get_display_monitors func 
		# is the same I'd use here to test, I'm going to just 
		# assume that if the first is sucesfull, the rest will be 
		# too. 
		SM_CXSCREEN = 0 # width_flag for primary
		SM_CYSCREEN = 1 # height_flag for primary
		primary_screen_size = (
			0,0,
			windll.user32.GetSystemMetrics(SM_CXSCREEN),
			windll.user32.GetSystemMetrics(SM_CYSCREEN)
		)
		screen_coords = self.robot.get_display_monitors()
		self.assertEquals(screen_coords[0], primary_screen_size)




if __name__ == '__main__':
	unittest.main()
