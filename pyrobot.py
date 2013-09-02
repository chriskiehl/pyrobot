'''

A pure python windows automation library loosely modeled after Java's Robot Class.

'''

import sys
import time
import ctypes 
from ctypes import *
from ctypes.wintypes import *




# WORD 	:	ctypes.c_short
# DWORD : ctypes.c_uint32
# LONG 	: ctypes.c_int
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


class MOUSEINPUT(Structure):
    _fields_ = [
        ('dx', LONG),
        ('dy', LONG),
        ('mouseData', DWORD),
        ('dwFlags', DWORD),
        ('time', DWORD),
        ('dwExtraInfo', POINTER(ULONG)),
    ]

class KEYBDINPUT(Structure):
    _fields_ = [
        ('wVk', WORD),
        ('wScan', WORD),
        ('dwFlags', DWORD),
        ('time', DWORD),
        ('dwExtraInfo', POINTER(ULONG)),
    ]

class HARDWAREINPUT(Structure):
    _fields_ = [
        ('uMsg', DWORD),
        ('wParamL', WORD),
        ('wParamH', DWORD)
    ]

class INPUT(Structure):
    class _I(Union):
        _fields_ = [
            ('mi', MOUSEINPUT),
            ('ki', KEYBDINPUT),
            ('hi', HARDWAREINPUT),
        ]

    _anonymous_ = 'i'
    _fields_ = [
        ('type', DWORD),
        ('i', _I),
    ]


class KeyConsts(object):
	def __init__(self):
		self.key_names = [" ", "left_mouse_button", "right_mouse_button", "control-break_processing", "middle_mouse_button_(three-button_mouse)", "x1_mouse_button", "x2_mouse_button", "undefined", "backspace", "tab", "reserved", "clear", "enter", "undefined", "shift", "ctrl", "alt", "pause", "caps_lock", "ime_kana_mode", "ime_hanguel_mode_(maintained_for_compatibility;_use_vk_hangul)", "ime_hangul_mode", "undefined", "ime_junja_mode", "ime_final_mode", "ime_hanja_mode", "ime_kanji_mode", "undefined", "esc", "ime_convert", "ime_nonconvert", "ime_accept", "ime_mode_change_request", "spacebar", "page_up", "page_down", "end", "home", "left_arrow", "up_arrow", "right_arrow", "down_arrow", "select", "print", "execute", "print_screen", "ins", "del", "help", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "undefined", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "left_windows__(natural_board)", "right_windows__(natural_board)", "applications__(natural_board)", "reserved", "computer_sleep", "numeric_pad_0", "numeric_pad_1", "numeric_pad_2", "numeric_pad_3", "numeric_pad_4", "numeric_pad_5", "numeric_pad_6", "numeric_pad_7", "numeric_pad_8", "numeric_pad_9", "multiply", "add", "separator", "subtract", "decimal", "divide", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12", "f13", "f14", "f15", "f16", "f17", "f18", "f19", "f20", "f21", "f22", "f23", "f24", "unassigned", "num_lock", "scroll_lock", "oem_specific", "unassigned", "left_shift", "right_shift", "left_control", "right_control", "left_menu", "right_menu", "browser_back", "browser_forward", "browser_refresh", "browser_stop", "browser_search", "browser_favorites", "browser_start_and_home", "volume_mute", "volume_down", "volume_up", "next_track", "previous_track", "stop_media", "play/pause_media", "start_mail", "select_media", "start_application_1", "start_application_2", "reserved", ";", "=", ",", "-",".","/","`", "reserved", "unassigned", "[", "\\", "]", "'", "used_for_miscellaneous_characters;_it_can_vary_by_board.", "reserved", "oem_specific", "either_the_angle_bracket__or_the_backslash__on_the_rt_102-_board", "oem_specific", "ime_process", "oem_specific", "used_to_pass_unicode_characters_as_if_they_were_strokes._the_vk_packet__is_the_low_word_of_a_32-bit_virtual_key_value_used_for_non-board_input_methods._for_more_information,_see_remark_in_keybdinput,_sendinput,_wm_keydown,_and_wm_keyup", "unassigned", "oem_specific", "attn", "crsel", "exsel", "erase_eof", "play", "zoom", "reserved", "pa1", "clear"]
		self.vk_codes = [0x20, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0C, 0x0D, 0x0E, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x15, 0x15, 0x16, 0x17, 0x18, 0x19, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3A-40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F, 0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57, 0x58, 0x59, 0x5A, 0x5B, 0x5C, 0x5D, 0x5E, 0x5F, 0x60, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E, 0x6F, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78, 0x79, 0x7A, 0x7B, 0x7C, 0x7D, 0x7E, 0x7F, 0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86, 0x87, 0x88, 0x90, 0x91, 0x92, 0x97, 0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5, 0xA6, 0xA7, 0xA8, 0xA9, 0xAA, 0xAB, 0xAC, 0xAD, 0xAE, 0xAF, 0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5, 0xB6, 0xB7, 0xB8, 0xBA, 0xBB, 0xBC, 0xBD, 0xBE, 0xBF, 0xC0, 0xC1, 0xD8, 0xDB, 0xDC, 0xDD, 0xDE, 0xDF, 0xE0, 0xE1, 0xE2, 0xE3, 0xE5, 0xE6, 0xE7, 0xE8, 0xE9,0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE]
		self.special_keys = '~ ! @ # $ % ^ & * ( ) _ + | } { " : ? > <'.split()
		self.special_map  = "` 1 2 3 4 5 6 7 8 9 0 - = \\ ] [ ' ; / . ,".split()



class Robot(object):
	'''
	A pure python windows automation library loosely modeled after Java's Robot Class.
	'''

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

		self.keys = KeyConsts()

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
		# Technologic

	def clear_clipboard(self):
		windll.user32.OpenClipboard(None)
		windll.user32.EmptyClipboard()
		windll.user32.CloseClipboard()

	def _get_monitor_coordinates(self):
		raise NotImplementedError(".. still working on things :)")
	
	def take_screenshot(self):
		'''
		NOTE:
			REQUIRES: PYTHON IMAGE LIBRARY

		Takes a snapshot of desktop and loads it into memory as a PIL object. 
		
		TODO: 
			* Add multimonitor support
		'''

		try: 
			import Image
		except ImportError as e:
			print e
			print "Need to have PIL installed! See: effbot.org for download"
			sys.exit()

		return self._make_image_from_buffer(self._get_screen_buffer())



	def _get_screen_buffer(self):
		SM_CXSCREEN = 0 # Width of primary screen
		SM_CYSCREEN = 1 # Height of the primary screen
		hDesktopWnd = windll.user32.GetDesktopWindow()
		width = windll.user32.GetSystemMetrics(SM_CXSCREEN)
		height = windll.user32.GetSystemMetrics(SM_CYSCREEN)
		hDesktopDC = windll.user32.GetDC (hDesktopWnd)
		hCaptureDC = windll.gdi32.CreateCompatibleDC(hDesktopDC)
		hCaptureBitmap = windll.gdi32.CreateCompatibleBitmap(hDesktopDC, width, height)
		windll.gdi32.SelectObject(hCaptureDC, hCaptureBitmap)

		SRCCOPY = 0x00CC0020
		windll.gdi32.BitBlt(hCaptureDC, 0, 0, 1920, 1080, hDesktopDC, 0, 0, 0x00CC0020)
		return hCaptureBitmap

	def _make_image_from_buffer(self, hCaptureBitmap):
		import Image
		bmp_info = BITMAPINFO()
		bmp_header = BITMAPFILEHEADER()
		hdc = windll.user32.GetDC(None)

		bmp_info.bmiHeader.biSize = sizeof(BITMAPINFOHEADER)

		DIB_RGB_COLORS = 0
		windll.gdi32.GetDIBits(hdc, 
			hCaptureBitmap, 
			0,0, 
			None, byref(bmp_info), 
			DIB_RGB_COLORS
		)

		bmp_info.bmiHeader.biSizeImage = bmp_info.bmiHeader.biWidth *abs(bmp_info.bmiHeader.biHeight) * (bmp_info.bmiHeader.biBitCount+7)/8;
		size = (bmp_info.bmiHeader.biWidth, bmp_info.bmiHeader.biHeight )
		pBuf = (c_char * bmp_info.bmiHeader.biSizeImage)()

		windll.gdi32.GetBitmapBits(hCaptureBitmap, bmp_info.bmiHeader.biSizeImage, pBuf)

		return Image.frombuffer('RGB', size, pBuf, 'raw', 'BGRX', 0, 1)


	def key_press(self, key):
		''' Presses a given key. '''
		KEY_PRESS = 0

		vk_code = self._vk_from_char(key)
		self._key_control(key=vk_code, action=KEY_PRESS)

	def key_release(self, key):
		''' Releases a given key. '''
		KEY_RELEASE = 0x0002

		vk_code = self._vk_from_char(key)
		self._key_control(key=vk_code, action=KEY_RELEASE)

	def _key_control(self, key, action):
		ip = INPUT()

		INPUT_KEYBOARD = 0x00000001
		ip.type = INPUT_KEYBOARD
		ip.ki.wScan = 0
		ip.ki.time = 0
		a = windll.user32.GetMessageExtraInfo()
		b = cast(a, POINTER(c_ulong))
		# ip.ki.dwExtraInfo 

		ip.ki.wVk = key
		ip.ki.dwFlags = action
		windll.user32.SendInput(1, byref(ip), sizeof(INPUT))

	def _vk_from_char(self, key_char):
		try:
			index = self.keys.key_names.index(key_char.lower())
		except ValueError as e:
			print e
			print ('Usage Note: all keys are underscor delimted, '
				'e.g. "left_mouse_button", or "up_arrow."\n'
				'View KeyConsts class for list of key_names')
			sys.exit()
		return self.keys.vk_codes[index]

	def _capitalize(self, letter):
		self.key_press('shift')
		self.key_press(letter)
		self.key_release('shift')
		self.key_release(letter)
		
	def get_unshifted_key(self, key):
		index = self.keys.special_keys.index(key)
		return self.keys.special_map[index]

	def type_string(self, input_string, delay=.005):
		'''
		Convenience function for typing out stings. 
		Delay controls the time between each letter. 

		For the most part, large tests should be pushed
		into the clipboard and pasted where needed. However, 
		they typing serves the useful purpose of looking neat. 
		'''

		for letter in input_string:
			self._handle_input(letter)
			time.sleep(delay)
	
	def _handle_input(self, key):
		if ord(key) in range(65, 91):
			# print 'Capital =', True
			self._capitalize(key)
		elif key in self.keys.special_keys:
			# print 'Punctuation =', True
			normalized_key = self.get_unshifted_key(key)
			self._capitalize(normalized_key)
		else:
			self.key_press(key)
			self.key_release(key)

	def type_backwards(self, input_string, delay=.05):
		'''
		Types right to left. Beacuse why not! 
		'''
		for letter in reversed(input_string):
			self._handle_input(letter)
			self.key_press('left_arrow')
			self.key_release('left_arrow')
			time.sleep(delay)


if __name__ == '__main__':
	import time 
	robot = Robot()



# stock codes: "+", ",", "-", "." 





#			 	Figuring out stuff below here					# 
# ------------------------------------------------------------- #

# print get_pixel(*get_mouse_pos())
# robot = Robot()
# import time
# time.sleep(1)
# robot.key_press('a')
# time.sleep(5)
# time.sleep(2)
# robot.scroll_mouse_wheel('down', 10)
# for i in dir(ctypes): print i
# SM_CMONITORS = 80
# SM_XVIRTUALSCREEN = 76
# SM_CXVIRTUALSCREEN = 78
# def get_total_displays 
# print windll.user32.GetSystemMetrics(SM_CMONITORS)
# print windll.user32.GetSystemMetrics(16)

# SM_CXSCREEN = 0 # Width of primary screen
# SM_CYSCREEN = 1 # Height of the primary screen


# libc = ctypes.cdll.msvcrt

# # handle to the entire desktop Window
# hdc = windll.user32.GetDC(None)

# # DC for the entire window
# h_dest = windll.gdi32.CreateCompatibleDC(hdc)

# width = windll.user32.GetSystemMetrics(SM_CXSCREEN)
# height = windll.user32.GetSystemMetrics(SM_CYSCREEN)

# hb_desktop = windll.gdi32.CreateCompatibleBitmap(hdc, width, height)
# windll.gdi32.SelectObject(h_dest, hb_desktop)

# print windll.gdi32.BitBlt(h_dest, 0,0, width, height, hdc, 0, 0, 'SRCCOPY')



# hCaptureBitmap = _get_screen_buffer()
# im = _make_image_from_buffer(hCaptureBitmap)
# im.save('image.bmp', 'bmp')





# BI_RGB = 0
# bmp_info.bmiHeader.biCompression = BI_RGB
# print windll.gdi32.GetDIBits(hdc, hCaptureBitmap, 0, bmp_info.bmiHeader.biHeight, pBuf, byref(bmp_info), 0x00)

# bmp_header.bfReserved1 = 0
# bmp_header.bfReserved2 = 0

# bmp_header.bfSize = sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER) + bmp_info.bmiHeader.biSizeImage
# bmp_header.bfType = 0x4D42

# bmp_header.bfOffBits = sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER)

# # fp = libc.fopen('test.bmp',"wb")

# # libc.fwrite(byref(bmp_header), sizeof(BITMAPFILEHEADER), 1, fp)

# # libc.fwrite(byref(bmp_info.bmiHeader), 
# # 	sizeof(BITMAPFILEHEADER), 1, fp)

# # libc.fwrite(pBuf, bmp_info.bmiHeader.biSizeImage, 1, fp)

# with open('test1.bmp', 'wb') as f:
# 	f.write(bmp_header)
# 	f.write(bmp_info.bmiHeader)
# 	f.write(pBuf)

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




# 						END 							#
# ----------------------------------------------------- #