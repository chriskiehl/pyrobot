'''

Based on Java's Robot class. pyRobot is a pure python 

 BufferedImage	createScreenCapture(Rectangle screenRect) 
          Creates an image containing pixels read from the screen.
 
 void	delay(int ms) 
          Sleeps for the specified time.
 
 int	getAutoDelay() 
          Returns the number of milliseconds this Robot sleeps after generating an event.
 
 # Color	getPixelColor(int x, int y) 
 #          Returns the color of a pixel at the given screen coordinates.
 
 boolean	isAutoWaitForIdle() 
          Returns whether this Robot automatically invokes waitForIdle after generating an event.
 
 void	keyPress(int keycode) 
          Presses a given key.
 
 void	keyRelease(int keycode) 
          Releases a given key.
 
 # void	mouseMove(int x, int y) 
 #          Moves mouse pointer to given screen coordinates.
 
 # void	mousePress(int buttons) 
 #          Presses one or more mouse buttons.
 
 # void	mouseRelease(int buttons) 
 #          Releases one or more mouse buttons.
 
 # void	mouseWheel(int wheelAmt) 
 #          Rotates the scroll wheel on wheel-equipped mice.
 
 void	setAutoDelay(int ms) 
          Sets the number of milliseconds this Robot sleeps after generating an event.
 
 void	setAutoWaitForIdle(boolean isOn) 
          Sets whether this Robot automatically invokes waitForIdle after generating an event.
 
 String	toString() 
          Returns a string representation of this Robot.
 
 void	waitForIdle() 
          Waits until all events currently on the event queue have been processed.


'''


from ctypes import *
import ctypes 

class WIN32CON(object):
	def __init__(self):
		self.LEFT_DOWN = 0x0002
		self.LEFT_UP = 0x0004
		self.MIDDLE_DOWN = 0x0020
		self.MIDDLE_UP = 0x0040
		self.MOVE = 0x0001
		self.RIGHT_DOWN = 0x0008
		self.RIGHT_UP = 0x0010
		self.WHEEL = 0x0800
		self.XDOWN = 0x0080
		self.XUP = 0x0100
		self.HWHEEL = 0x01000

class Robot(object):
	def __init__(self):
		self.windll =windll.kernel32
		self.cdll = cdll.msvcrt
		self.win32con = WIN32CON()
		self.press_events = {
			'left' :  (self.win32con.LEFT_DOWN, None, None, None, None), 
			'right':  (self.win32con.RIGHT_DOWN, None, None, None, None), 
			'middle': (self.win32con.MIDDLE_DOWN, None, None, None, None)
		}

		self.release_events = {
			'left' :  (self.win32con.LEFT_UP, None, None, None, None), 
			'right':  (self.win32con.RIGHT_UP, None, None, None, None), 
			'middle': (self.win32con.MIDDLE_UP, None, None, None, None)
		}


	def set_mouse_pos(self, x, y):
		'''
		Moves mouse pointer to given screen coordinates.
		'''
		windll.user32.SetCursorPos(0,0)

	def get_mouse_pos(self):
		'''
		returns current mouse coordinates
		'''
		coords = pointer(c_long(0))
		windll.user32.GetCursorPos(coords)
		return (coords[0], coords[1])

	def get_pixel(self, x, y):
		'''
		Returns the pixel color of the given screen coordinate
		'''
		gdi= windll.gdi32
		RGBInt = gdi.GetPixel(
			windll.user32.GetDC(0),
			x, y
		)
		red = RGBInt & 255
		green = (RGBInt >> 8) & 255
		blue = (RGBInt >> 16) & 255
		return (red, green, blue)

	def mouse_down(self, button):
		'''
		Presses one mouse button. Left, right, or middle
		'''
		windll.user32.mouse_event(
			*self.press_events[button.lower()]
		)
		time.sleep(.2)

	def mouse_up(self, button):
		'''
		Releases mouse button. Left, right, or middle
		'''
		windll.user32.mouse_event(
			*self.release_events[button.lower()]
		)

	def scroll_mouse_wheel(self, direction, clicks): 
		for num in range(clicks):
			self._scrollup() if direction.lower() == 'up' else self._scrolldown()


	def _scrollup(self):
		windll.user32.mouse_event(self.win32con.WHEEL, None, None, 120, None)

	def _scrolldown(self):
		windll.user32.mouse_event(self.win32con.WHEEL, None, None, -120, None)

	def add_to_clipboard(self, string): 
		'''
		Copy text into clip board for later pasting. 
		'''
		# This is more or less ripped right for MSDN. 
		GHND = 0x0042
		# Allocate at
		hGlobalMemory = windll.kernel32.GlobalAlloc(GHND, len(bytes(string))+1)
		# Lock it
		lpGlobalMemory = windll.kernel32.GlobalLock(hGlobalMemory)
		# copy it
		lpGlobalMemory = windll.kernel32.lstrcpy(lpGlobalMemory, string)
		# unlock it
		windll.kernel32.GlobalUnlock(lpGlobalMemory)
		# open it
		windll.user32.OpenClipboard(None)
		# empty it
		windll.user32.EmptyClipboard()
		# add it
		hClipMemory = windll.user32.SetClipboardData(1, hGlobalMemory) # 1 = CF_TEXT
		# close it
		windll.user32.CloseClipboard()
		# better faster stronger

	def clear_clipboard(self):
		windll.user32.OpenClipboard(None)
		windll.user32.EmptyClipboard()
		windll.user32.CloseClipboard()

	def _get_monitor_coordinates(self):
		print windll.user32.EnumDisplayMonitors(hwnd, None, None, None)

# WORD 	:	ctypes.c_short
# DWORD : ctypes.c_uint32
# LONG 	: ctypes.c_int

class BITMAP(ctypes.Structure):
	_fields_ = [
		('bmType', c_int),
		('bmWidth', c_int),
		('bmHeight', c_int),
		('bmHeightBytes', c_int),
		('bmPlanes', c_short),
		('bmBitsPixel', c_short),
		('bmBits', c_void_p),

	]

class BITMAPFILEHEADER(ctypes.Structure):
	_fields_ = [
		('bfType', ctypes.c_short),
		('bfSize', ctypes.c_uint32),
		('bfReserved1', ctypes.c_short),
		('bfReserved2', ctypes.c_short),
		('bfOffBits', ctypes.c_uint32)
	]

class BITMAPINFOHEADER(ctypes.Structure):
	_fields_ = [
		('biSize', ctypes.c_uint32),
		('biWidth', ctypes.c_int),
		('biHeight', ctypes.c_int),
		('biPlanes', ctypes.c_short),
		('biBitCount', ctypes.c_short),
		('biCompression', ctypes.c_uint32),
		('biSizeImage', ctypes.c_uint32),
		('biXPelsPerMeter', ctypes.c_long),
		('biYPelsPerMeter', ctypes.c_long),
		('biClrUsed', ctypes.c_uint32),
		('biClrImportant', ctypes.c_uint32)
	]

class BITMAPINFO(ctypes.Structure):
	_fields_ = [
		('bmiHeader', BITMAPINFOHEADER),
		('bmiColors', ctypes.c_ulong * 3)
	]


# print get_pixel(*get_mouse_pos())
robot = Robot()
import time
# time.sleep(2)
# robot.scroll_mouse_wheel('down', 10)
# for i in dir(ctypes): print i
# SM_CMONITORS = 80
# SM_XVIRTUALSCREEN = 76
# SM_CXVIRTUALSCREEN = 78
SM_CXSCREEN = 0 # Width of primary screen
SM_CYSCREEN = 1 # Height of the primary screen

# def get_total_displays 
# print windll.user32.GetSystemMetrics(SM_CMONITORS)
# print windll.user32.GetSystemMetrics(16)

libc = ctypes.cdll.msvcrt

# handle to the entire desktop Window
# hdc = windll.user32.GetDC(None)

# # DC for the entire window
# h_dest = windll.gdi32.CreateCompatibleDC(hdc)

# width = windll.user32.GetSystemMetrics(SM_CXSCREEN)
# height = windll.user32.GetSystemMetrics(SM_CYSCREEN)

# hb_desktop = windll.gdi32.CreateCompatibleBitmap(hdc, width, height)
# windll.gdi32.SelectObject(h_dest, hb_desktop)

# print windll.gdi32.BitBlt(h_dest, 0,0, width, height, hdc, 0, 0, 'SRCCOPY')


hDesktopWnd = windll.user32.GetDesktopWindow()
hDesktopDC = windll.user32.GetDC (hDesktopWnd)
hCaptureDC = windll.gdi32.CreateCompatibleDC(hDesktopDC)
hCaptureBitmap = windll.gdi32.CreateCompatibleBitmap(hDesktopDC, 1920, 1080)
windll.gdi32.SelectObject(hCaptureDC, hCaptureBitmap)

SRCCOPY = 0x00CC0020
print windll.gdi32.BitBlt(hCaptureDC, 0, 0, 1920, 1080, hDesktopDC, 0, 0, 0x00CC0020)


# Save Section
# ==============




# Previous attempt
# ###############################
bmp_info = BITMAPINFO()
bmp_header = BITMAPFILEHEADER()
hdc = windll.user32.GetDC(None)

bmp_info.bmiHeader.biSize = sizeof(BITMAPINFOHEADER)
DIB_RGB_COLORS = 0
print windll.gdi32.GetDIBits(hdc, hCaptureBitmap, 0,0, None, byref(bmp_info), DIB_RGB_COLORS)

bmp_info.bmiHeader.biSizeImage = bmp_info.bmiHeader.biWidth *abs(bmp_info.bmiHeader.biHeight) * (bmp_info.bmiHeader.biBitCount+7)/8;

pBuf = (c_char * bmp_info.bmiHeader.biSizeImage)()

BI_RGB = 0
bmp_info.bmiHeader.biCompression = BI_RGB
print windll.gdi32.GetDIBits(hdc, hCaptureBitmap, 0, bmp_info.bmiHeader.biHeight, pBuf, byref(bmp_info), 0x00)

bmp_header.bfReserved1 = 0
bmp_header.bfReserved2 = 0

bmp_header.bfSize = sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER) + bmp_info.bmiHeader.biSizeImage
bmp_header.bfType = 0x4D42

bmp_header.bfOffBits = sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER)

fp = libc.fopen('test.bmp',"wb")

libc.fwrite(byref(bmp_header), sizeof(BITMAPFILEHEADER), 1, fp)

libc.fwrite(byref(bmp_info.bmiHeader), 
	sizeof(BITMAPFILEHEADER), 1, fp)

libc.fwrite(pBuf, bmp_info.bmiHeader.biSizeImage, 1, fp)

# END Previous attempt
# ###############################











# Half finished
# #############################
# bmpScreen = BITMAP()
# hbmScreen = hCaptureBitmap

# print windll.gdi32.GetObjectA(hbmScreen, sizeof(BITMAP), byref(bmpScreen))

# bmfHeader = BITMAPFILEHEADER()
# bi = BITMAPINFOHEADER()

# bi.biSize = sizeof(BITMAPINFOHEADER)
# bi.biWidth = bmpScreen.bmWidth
# bi.biHeight = bmpScreen.bmHeight
# bi.biPlanes = 1
# bi.biBitCount = 32
# bi.biCompression = 0
# bi.biSizeImage = 0
# bi.biXPelsPerMeter = 0
# bi.biYPelsPerMeter = 0
# bi.biClrUsed = 0
# bi.biClrImportant = 0

# dwBmpSize = ((bmpScreen.bmWidth * bi.biBitCount + 31) / 32) * 4 * bmpScreen.bmHeight
# GHND = 0x0042
# hDIB = windll.user32.GlobalAlloc(GHND, dwBmpSize)
# END