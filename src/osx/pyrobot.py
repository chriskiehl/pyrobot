'''
Created on Jan 19, 2014

@author: devbox
'''

import ctypes 
from ctypes.util import find_library


class Robot(object):
  def __init__(self):
    self.cg = ctypes.cdll.LoadLibrary(find_library('CoreGraphics'))
  
  def get_display_ids(self):
    displayCount = ctypes.c_int()
    # Array to hold the displayIDs
    displays = (ctypes.c_int * 5)()
    # Populates displays array with IDs of all attached monitors
    self.cg.CGGetActiveDisplayList(5, displays, ctypes.byref(displayCount))
    return [ID for ID in displays if ID is not 0]




if __name__ == '__main__':
  print cg