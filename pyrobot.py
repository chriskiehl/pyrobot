'''

A pure python windows automation library loosely modeled after Java's Robot Class.


TODO:
	* Mac support  
	* Allow window section for relative coordinates.
	* ability to 'paint' target window. 



I can never remember how these map... 
----  LEGEND ----

BYTE      = c_ubyte
WORD      = c_ushort
DWORD     = c_ulong
LPBYTE    = POINTER(c_ubyte)
LPTSTR    = POINTER(c_char) 
HANDLE    = c_void_p
PVOID     = c_void_p
LPVOID    = c_void_p
UNIT_PTR  = c_ulong
SIZE_T    = c_ulong

'''


import sys
import time
import ctypes 
import multiprocessing 
from ctypes import *
from ctypes.wintypes import *



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
		# No. I refuse to shorten this! 
		# You can't make me!
		# Pep8 Schmep 8!
		self.key_names = [" ", "left_mouse_button", "right_mouse_button", "control-break_processing", "middle_mouse_button_(three-button_mouse)", "x1_mouse_button", "x2_mouse_button", "undefined", "backspace", "tab", "reserved", "clear", "enter", "undefined", "shift", "ctrl", "alt", "pause", "caps_lock", "ime_kana_mode", "ime_hanguel_mode_(maintained_for_compatibility;_use_vk_hangul)", "ime_hangul_mode", "undefined", "ime_junja_mode", "ime_final_mode", "ime_hanja_mode", "ime_kanji_mode", "undefined", "esc", "ime_convert", "ime_nonconvert", "ime_accept", "ime_mode_change_request", "spacebar", "page_up", "page_down", "end", "home", "left_arrow", "up_arrow", "right_arrow", "down_arrow", "select", "print", "execute", "print_screen", "ins", "del", "help", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "undefined", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "left_windows__(natural_board)", "right_windows__(natural_board)", "applications__(natural_board)", "reserved", "computer_sleep", "numeric_pad_0", "numeric_pad_1", "numeric_pad_2", "numeric_pad_3", "numeric_pad_4", "numeric_pad_5", "numeric_pad_6", "numeric_pad_7", "numeric_pad_8", "numeric_pad_9", "multiply", "add", "separator", "subtract", "decimal", "divide", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12", "f13", "f14", "f15", "f16", "f17", "f18", "f19", "f20", "f21", "f22", "f23", "f24", "unassigned", "num_lock", "scroll_lock", "oem_specific", "unassigned", "left_shift", "right_shift", "left_control", "right_control", "left_menu", "right_menu", "browser_back", "browser_forward", "browser_refresh", "browser_stop", "browser_search", "browser_favorites", "browser_start_and_home", "volume_mute", "volume_down", "volume_up", "next_track", "previous_track", "stop_media", "play/pause_media", "start_mail", "select_media", "start_application_1", "start_application_2", "reserved", ";", "=", ",", "-",".","/","`", "reserved", "unassigned", "[", "\\", "]", "'", "used_for_miscellaneous_characters;_it_can_vary_by_board.", "reserved", "oem_specific", "either_the_angle_bracket__or_the_backslash__on_the_rt_102-_board", "oem_specific", "ime_process", "oem_specific", "used_to_pass_unicode_characters_as_if_they_were_strokes._the_vk_packet__is_the_low_word_of_a_32-bit_virtual_key_value_used_for_non-board_input_methods._for_more_information,_see_remark_in_keybdinput,_sendinput,_wm_keydown,_and_wm_keyup", "unassigned", "oem_specific", "attn", "crsel", "exsel", "erase_eof", "play", "zoom", "reserved", "pa1", "clear"]
		self.vk_codes = [0x20, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0C, 0x0D, 0x0E, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x15, 0x15, 0x16, 0x17, 0x18, 0x19, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3A-40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F, 0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57, 0x58, 0x59, 0x5A, 0x5B, 0x5C, 0x5D, 0x5E, 0x5F, 0x60, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E, 0x6F, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78, 0x79, 0x7A, 0x7B, 0x7C, 0x7D, 0x7E, 0x7F, 0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86, 0x87, 0x88, 0x90, 0x91, 0x92, 0x97, 0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5, 0xA6, 0xA7, 0xA8, 0xA9, 0xAA, 0xAB, 0xAC, 0xAD, 0xAE, 0xAF, 0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5, 0xB6, 0xB7, 0xB8, 0xBA, 0xBB, 0xBC, 0xBD, 0xBE, 0xBF, 0xC0, 0xC1, 0xD8, 0xDB, 0xDC, 0xDD, 0xDE, 0xDF, 0xE0, 0xE1, 0xE2, 0xE3, 0xE5, 0xE6, 0xE7, 0xE8, 0xE9,0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE]
		self.special_keys = '~ ! @ # $ % ^ & * ( ) _ + | } { " : ? > <'.split()
		self.special_map  = "` 1 2 3 4 5 6 7 8 9 0 - = \\ ] [ ' ; / . ,".split()

class Keys(object): 
	space=32;left_mouse_button=1;right_mouse_button=2;control_break_processing=3;middle_mouse_button_three_button_mouse=4;x1_mouse_button=5;x2_mouse_button=6;undefined=7;backspace=8;tab=9;reserved=10;clear=12;enter=13;undefined=14;shift=16;ctrl=17;alt=18;pause=19;caps_lock=20;undefined=22;undefined=26;esc=27;spacebar=32;page_up=33;page_down=34;end=35;home=36;left_arrow=37;up_arrow=38;right_arrow=39;down_arrow=40;select=41;print_key=42;execute=43;print_screen=44;ins=45;delete=46;help_key=47;zero=48;one=49;two=50;three=51;four=52;five=53;six=54;seven=55;eight=56;nine=57;undefined=18;a=65;b=66;c=67;d=68;e=69;f=70;g=71;h=72;i=73;j=74;k=75;l=76;m=77;n=78;o=79;p=80;q=81;r=82;s=83;t=84;u=85;v=86;w=87;x=88;y=89;z=90;left_windows__natural_board=91;right_windows__natural_board=92;applications__natural_board=93;reserved=94;computer_sleep=95;numeric_pad_0=96;numeric_pad_1=97;numeric_pad_2=98;numeric_pad_3=99;numeric_pad_4=100;numeric_pad_5=101;numeric_pad_6=102;numeric_pad_7=103;numeric_pad_8=104;numeric_pad_9=105;multiply=106;add=107;separator=108;subtract=109;decimal=110;divide=111;f1=112;f2=113;f3=114;f4=115;f5=116;f6=117;f7=118;f8=119;f9=120;f10=121;f11=122;f12=123;f13=124;f14=125;f15=126;f16=127;f17=128;f18=129;f19=130;f20=131;f21=132;f22=133;f23=134;f24=135;unassigned=136;num_lock=144;scroll_lock=145;oem_specific=146;unassigned=151;left_shift=160;right_shift=161;left_control=162;right_control=163;left_menu=164;right_menu=165;browser_back=166;browser_forward=167;browser_refresh=168;browser_stop=169;browser_search=170;browser_favorites=171;browser_start_and_home=172;volume_mute=173;volume_down=174;volume_up=175;next_track=176;previous_track=177;stop_media=178;play_pause_media=179;start_mail=180;select_media=181;start_application_1=182;start_application_2=183;reserved=184;semicolon=186;equals=187;comma=188;minus=189;peiod=190;forward_slash=191;back_tick=192;reserved=193;unassigned=216;open_brace=219;backslash=220;close_brace=221;apostrophe=222;reserved=224;oem_specific=225;either_the_angle_bracket__or_the_backslash__on_the_rt_102__board=226;oem_specific=227;oem_specific=230;unassigned=232;oem_specific=233;attn=246;crsel=247;exsel=248;erase_eof=249;play=250;zoom=251;reserved=252;pa1=253;clear=254;

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
		windll.user32.SetCursorPos(x,y)

	def get_mouse_pos(self):
		'''
		Returns current mouse coordinates
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
		# time.sleep(.2)

	def mouse_up(self, button):
		'''
		Releases mouse button. Left, right, or middle
		'''
		windll.user32.mouse_event(
			*self.release_events[button.lower()]
		)

	def click_mouse(self, button):
		'''
		Simulates a full mouse click. One down event, one up event. 
		'''
		self.mouse_down(button)
		self.mouse_up(button)

	def double_click_mouse(self, button):
		'''
		Two full mouse clicks. One down event, one up event. 
		'''
		self.click_mouse(button)
		self.sleep(.1)
		self.click_mouse(button)

	def move_and_click(self, x, y, button):
		"convenience function: Move to corrdinate and click mouse"
		self.set_mouse_pos(x,y)

	def scroll_mouse_wheel(self, direction, clicks): 
		'''
		Scrolls the mouse wheel either up or down X number of 'clicks'

		direction: String: 'up' or 'down'

		clicks: int: how many times to click
		'''
		for num in range(clicks):
			self._scrollup() if direction.lower() == 'up' else self._scrolldown()


	def _scrollup(self):
		windll.user32.mouse_event(self.win32con.WHEEL, None, None, 120, None)

	def _scrolldown(self):
		windll.user32.mouse_event(self.win32con.WHEEL, None, None, -120, None)

	def get_clipboard_data(self):
		'''
		Retrieves text from the Windows clipboard
		as a String
		'''
		CF_TEXT = 1
		windll.user32.OpenClipboard(None)
		hglb = windll.user32.GetClipboardData(CF_TEXT)
		
		text_ptr = c_char_p(windll.kernel32.GlobalLock(hglb))
		windll.kernel32.GlobalUnlock(hglb)

		return text_ptr.value

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
		'''
		Clear everything out of the clipboard
		'''
		windll.user32.OpenClipboard(None)
		windll.user32.EmptyClipboard()
		windll.user32.CloseClipboard()

	def _get_monitor_coordinates(self):
		raise NotImplementedError(".. still working on things :)")
	
	def take_screenshot(self, bounds=None):
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

		return self._make_image_from_buffer(self._get_screen_buffer(bounds))

	


	def _get_screen_buffer(self, bounds=None):
		# Grabs a DC to the entire virtual screen, but only copies to 
		# the bitmap the the rect defined by the user. 

		SM_XVIRTUALSCREEN = 76  # coordinates for the left side of the virtual screen. 
		SM_YVIRTUALSCREEN = 77  # coordinates for the right side of the virtual screen.  
		SM_CXVIRTUALSCREEN = 78 # width of the virtual screen
		SM_CYVIRTUALSCREEN = 79 # height of the virtual screen

		hDesktopWnd = windll.user32.GetDesktopWindow() #Entire virtual Screen

		left = windll.user32.GetSystemMetrics(SM_XVIRTUALSCREEN)
		top = windll.user32.GetSystemMetrics(SM_YVIRTUALSCREEN)
		width = windll.user32.GetSystemMetrics(SM_CXVIRTUALSCREEN)
		height = windll.user32.GetSystemMetrics(SM_CYVIRTUALSCREEN)

		if bounds:
			left, top, right, bottom = bounds
			width = right - left 
			height = bottom - top
		
		hDesktopDC = windll.user32.GetWindowDC(hDesktopWnd)
		if not hDesktopDC: print 'GetDC Failed'; sys.exit()
		
		hCaptureDC = windll.gdi32.CreateCompatibleDC(hDesktopDC)
		if not hCaptureDC: print 'CreateCompatibleBitmap Failed'; sys.exit()

		hCaptureBitmap = windll.gdi32.CreateCompatibleBitmap(hDesktopDC, width, height)
		if not hCaptureBitmap: print 'CreateCompatibleBitmap Failed'; sys.exit()
		
		windll.gdi32.SelectObject(hCaptureDC, hCaptureBitmap)

		SRCCOPY = 0x00CC0020
		windll.gdi32.BitBlt(
			hCaptureDC, 
			0, 0, 
			width, height, 
			hDesktopDC, 
			left, top, 
			0x00CC0020
		)
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
		# print size
		pBuf = (c_char * bmp_info.bmiHeader.biSizeImage)()

		windll.gdi32.GetBitmapBits(hCaptureBitmap, bmp_info.bmiHeader.biSizeImage, pBuf)

		return Image.frombuffer('RGB', size, pBuf, 'raw', 'BGRX', 0, 1)

	def press_and_release(self, key):
		'''
		Simulates pressing a key: One down event, one release event.
		'''
		self.key_press(key)
		self.key_release(key)

	def key_press(self, key):
		''' Presses a given key. '''
		KEY_PRESS = 0

		if isinstance(key, str):
			vk_code = self._vk_from_char(key)
		else:
			vk_code = key
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
		
	def _get_unshifted_key(self, key):
		index = self.keys.special_keys.index(key)
		return self.keys.special_map[index]

	def type_string(self, input_string, delay=.005):
		'''
		Convenience function for typing out strings. 
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
			normalized_key = self._get_unshifted_key(key)
			self._capitalize(normalized_key)
		else:
			self.key_press(key)
			self.key_release(key)

	def type_backwards(self, input_string, delay=.05):
		'''
		Types right to left. Because why not! 
		'''
		for letter in reversed(input_string):
			self._handle_input(letter)
			self.key_press('left_arrow')
			self.key_release('left_arrow')
			time.sleep(delay)

	def start_program(self, full_path):
		'''
		Starts a windows applications. Currently, you must pass in 
		the full path to the exe, otherwise it will fail. 

		TODO: 
			* return Handle to started program. 
			* Search on program name
		'''

		class STARTUPINFO(ctypes.Structure):
			_fields_ = [
			('cb', c_ulong),
			('lpReserved', POINTER(c_char)),
			('lpDesktop', POINTER(c_char)),
			('lpTitle', POINTER(c_char)),
			('dwX', c_ulong),
			('dwY', c_ulong),
			('dwXSize', c_ulong),
			('dwYSize', c_ulong),
			('dwXCountChars', c_ulong),
			('dwYCountChars', c_ulong),
			('dwFillAttribute', c_ulong),
			('dwFlags', c_ulong),
			('wShowWindow', c_ushort),
			('cbReserved2', c_ushort),
			('lpReserved2', POINTER(c_ubyte)),
			('hStdInput', c_void_p),
			('hStdOutput', c_void_p),
			('hStdError', c_void_p)
		]
		class PROCESS_INFORMATION(ctypes.Structure):
			_fields_ = [
				('hProcess', c_void_p),
				('hThread', c_void_p),
				('dwProcessId', c_ulong),
				('dwThreadId', c_ulong),
			]
		NORMAL_PRIORITY_CLASS = 0x00000020
		
		startupinfo = STARTUPINFO()
		processInformation = PROCESS_INFORMATION()
		
		windll.kernel32.CreateProcessA(
			full_path, 
			None, 
			None,
			None,
			True,
			0,
			None, 
			None,
			byref(startupinfo),
			byref(processInformation)
			)

	def copy(self): 
		'''
		convenience function for issuing Ctrl+C copy command
		'''
		self.key_press('ctrl')
		self.key_press('c')
		self.key_release('c')
		self.key_release('ctrl')

	def paste(self):
		''' 
		convenience function for pasting whatever is in the clipboard
		'''
		self.key_press('ctrl')
		self.key_press('v')
		self.key_release('v')
		self.key_release('ctrl')

	def sleep(self, duration):
		'''
		Pauses the robot for `duration` number of seconds. 
		'''
		time.sleep(duration)





	def _enumerate_windows(self, visible=True):
		'''
		Loops through the titles of all the "windows."
		Spits out too much junk to to be of immidiate use. 
		Keeping it here to remind me how the ctypes 
		callbacks work. 
		'''

		# raise NotImplementedError('Not ready yet. Git outta here!')

		titles = []
		def enumWindowsProc(hwnd, lParam):
			# print hwnd, lParam
			l = windll.user32.GetWindowTextLengthA(hwnd)
			title = create_string_buffer(l + 1)
			windll.user32.GetWindowTextA(
				hwnd, 
				title,
				l + 1
				)
			if lParam:
				if windll.user32.IsWindowVisible(hwnd) == 0:
					#Window is not visible, don't add it to the list
					return
			titles.append(''.join(title).strip("\x00"))

		BoolEnumWindowsProc = WINFUNCTYPE(
			ctypes.c_bool, 
			ctypes.wintypes.HWND, 
			ctypes.wintypes.LPARAM 
			)

		mycallback = BoolEnumWindowsProc(enumWindowsProc)

		#If we want to enumerate only visibles
		if visible:
			windll.user32.EnumWindows(mycallback, True)
		else:
			windll.user32.EnumWindows(mycallback, False)

		titles = [t for t in titles if t is not ""]

		return titles

	def wait_for_window(self, wname, timeout=0, interval=0.005):
		if timeout < 0:
			raise ValueError("'timeout' must be a positive number")
		start_time = time.time()
		while True:
			for window in self._enumerate_windows():
				if wname.lower() in window.lower():
					#If the window exists return True
					return True

			if time.time() - start_time > timeout:
				#If we passed the timeout, return False
				#Not sure if it's best to raise an Exception though
				return False

			time.sleep(interval)


	def get_display_monitors(self):
		''' 
		Enumerates and returns a list of virtual screen 
		coordinates for the attached display devices 

		output = [
			(left, top, right, bottom), # Monitor 1
			(left, top, right, bottom)  # Monitor 2
			# etc... 
		]

		'''

		display_coordinates = []
		def _monitorEnumProc(hMonitor, hdcMonitor, lprcMonitor, dwData):
			# print 'call result:', hMonitor, hdcMonitor, lprcMonitor, dwData
			# print 'DC:', windll.user32.GetWindowDC(hMonitor)
			
			coordinates = (
				lprcMonitor.contents.left,
				lprcMonitor.contents.top,
				lprcMonitor.contents.right,
				lprcMonitor.contents.bottom
			) 
			display_coordinates.append(coordinates)
			return True
		
		# Callback Factory
		MonitorEnumProc = WINFUNCTYPE(
			ctypes.c_bool, 
			ctypes.wintypes.HMONITOR,
			ctypes.wintypes.HDC,
			ctypes.POINTER(RECT),
			ctypes.wintypes.LPARAM
		)

		# Make the callback function
		enum_callback = MonitorEnumProc(_monitorEnumProc)

		# Enumerate the windows
		windll.user32.EnumDisplayMonitors(
			None, 
			None,
			enum_callback,
			0
		)
		return display_coordinates


	def draw_box(self, location, rgb_value): 
		p1_x, p1_y, p2_x, p2_y = location
		
		width = p2_x - p1_x 
		height = p2_y - p1_y 

		for pix in range(width):
			self.draw_pixel((p1_x + pix, p1_y), rgb_value)
			self.draw_pixel((p1_x + pix, p2_y), rgb_value)

			self.draw_pixel((p1_x + pix, p1_y - 1), rgb_value) # Add thicker top
			self.draw_pixel((p1_x + pix, p2_y + 1), rgb_value) # Add thicker bottom
		
		for i in range(height):
			self.draw_pixel((p1_x, p1_y + i), rgb_value)
			self.draw_pixel((p2_x, p1_y + i), rgb_value)

			self.draw_pixel((p1_x - 1, p1_y + i), rgb_value) # Thicker left
			self.draw_pixel((p2_x + 1, p1_y + i), rgb_value) # Thicker right



	def draw_pixel(self, coordinate, rgb_value):
		'''
		Draw pixels on the screen. 

		Eventual plan is to use this to draw bounding boxes for template matching.
		Idea is to have it seek out anything that looks vaguely like a text-box 
		(or something). Who knows. 

		'''
		def _convert_rgb(r, g, b):
		    r = r & 0xFF
		    g = g & 0xFF
		    b = b & 0xFF
		    return (b << 16) | (g << 8) | r

		# raise NotImplementedError('Not ready yet. Git outta here!')

		rgb = _convert_rgb(*rgb_value)
		hdc = windll.user32.GetDC(None)
		
		x, y = coordinate

		windll.gdi32.SetPixel(
			hdc, 
			c_int(x),
			c_int(y),
			rgb
			)

	def match_template(self):
		import ImageOps 
		im = ImageOps.grayscale(self.take_screenshot(self.get_display_monitors()[0]))
		# im = ImageOps.grayscale(self.take_screenshot())
		return im.size, im.getdata()


class RECT(ctypes.Structure):
	_fields_ = [
		('left', c_long),
		('top', c_long),
		('right', c_long),
		('bottom', c_long)
	]

# GAH! Look not at this! 
#
#
# Me no smart at template matching.. 
#
#
#
# def build_match_box2(data, source): 
# 	data = data 
# 	source = source
# 	while True: 
# 		row, col, img_size = yield
# 		match_box = [data[row + x][col : img_size + col] for x in xrange(img_size)]
# 		yield match_box == source

# def mmmm(dataa, sourcee):
# 	def build_match_box(x):
# 		data = dataa 
# 		source = sourcee 
# 		row, col, img_size = x
# 		match_box = [data[row + x][col : img_size + col] for x in xrange(img_size)]
# 		return match_box == source
# 	return build_match_box

# def build_match_box(x):
# 	data, source, row, col, img_size = x
# 	match_box = [data[row + x][col : img_size + col] for x in xrange(img_size)]
# 	return match_box == source

# def builder(p,t):
# 	p_matrix = p 
# 	template = t 
# 	while True: 
# 		row, col, img_size = yield
# 		match_box = [data[row + x][col : img_size + col] for x in xrange(img_size)]
# 		yield match_box == source


# class Worker(multiprocessing.Process):
# 	def __init__(self, p_queue, o_queue, search_image,
# 			search_image_width, template, template_width, template_height): 
# 		multiprocessing.Process.__init__(self)
# 		self.in_queue = p_queue
# 		self.out_queue = o_queue
# 		self.search_image = search_image
# 		self.search_image_width = search_image_width
# 		self.template = template
# 		self.template_width = template_width
# 		self.template_height = template_height

# 	def run(self):
# 		robot = Robot()
# 		def get_matches(j):
# 			row_index = self.search_image_width * j
# 			return (self.search_image[
# 						col + row_index : self.template_width + row_index + col] 
# 						== self.template[(self.template_width * j) : (self.template_width * (j + 1))])

# 		while True: 
# 			queue_item = self.in_queue.get()
			
# 			if isinstance(queue_item, str): 
# 				break 
			
# 			start_pos, end_pos = queue_item					

# 			for col in range(start_pos, end_pos):
# 				if (self.search_image[col : self.template_width + col] == self.template[0:self.template_width] and 
# 					self.search_image[col + self.search_image_width * 4: self.template_width + (self.search_image_width * 4) + col] == self.template[(self.template_width * 4) : (self.template_width * (4 + 1))]):
# 					results = map(get_matches, range(1, self.template_height))
# 					if sum(results) == self.template_height - 1: 
# 						y = col/self.search_image_width
# 						x = col % self.search_image_width
# 						# self.out_queue.put((x, y, x + self.template_width, y + self.template_height))
# 						# print self.out_queue.qsize()
# 						print 'Match found at:', (x, y, x + self.template_width, y + self.template_height)
# 						robot.draw_box((x, y, x + self.template_width, y + self.template_height), (0,255,0))


# def _playing_around_ignore_me():
# 	robot = Robot()

# 	# # robot.draw_pixels((255,255,255))	
# 	# # print robot.get_mouse_pos()
# 	# # (546, 212)

# 	import array
# 	import Image
# 	import math
# 	import ImageOps
# 	import multiprocessing 

# 	# im = ImageOps.grayscale(robot.take_screenshot((100,100, 150, 150)))
# 	# im = ImageOps.grayscale(robot.take_screenshot((500,520, 600, 700)))
# 	# im.save('whooo.png', 'png')
# 	im = ImageOps.grayscale(Image.open('template2.png'))
# 	# img_to_match = Image.open('whooo.bmp')
# 	import time 

# 	template = multiprocessing.Array('i', list(im.getdata()))
# 	template_width, template_height = im.size
# 	print template, template_width, template_height

# 	# source_line = to_match_data[0:img_to_match.size[0]]
# 	# source = [to_match_data[x:img_to_match.size[0] + x] for x in xrange(0, len(to_match_data), img_to_match.size[0])]
# 	# # print 'Source:', len(source[0]), len(source[1])
# 	# # cross_section = [source[x][x] for x in range(len(source))]
# 	# # print cross_section

# 	search_image_size, data = robot.match_template()
# 	search_image_width, search_image_height = search_image_size
# 	search_image = multiprocessing.Array('i', list(data))

# 	cpus = 2
# 	print len(search_image)
# 	stepsize = len(search_image) / (cpus)
# 	search_ranges = [_ for _ in range(0, len(search_image) + 1, stepsize)]
# 	search_ranges[-1] = search_ranges[-1] - template_width
# 	print search_ranges

# 	pool = []
# 	process_queue = multiprocessing.Queue()
# 	output_queue = multiprocessing.Queue()
# 	for i in range(cpus):
# 		p = Worker(process_queue, output_queue, 
# 			search_image, search_image_width, 
# 			template, template_width, template_height) 
# 		p.start()
# 		pool.append(p) 

# 	print 'Searching...'
# 	for i in zip(search_ranges, search_ranges[1:]):
# 		process_queue.put(i)
# 	for i in range(10): process_queue.put('')
# 	for i in pool: i.join() 

# 	for i in range(output_queue.qsize()):
# 		a = output_queue.get() 
# 		print a 
# 		robot.draw_box(a, (0,255,0)) 
		


# 	# print search_image, search_image_size 

# 	# matches = []
# 	# for col in xrange(len(search_image) - template_width):
# 	# 	if search_image[col : template_width + col] == template[0:template_width]:
# 	# 		print True, col/search_image_width, col % search_image_width 
# 	# 		# results = map(get_matches, range(1, template_height))
# 	# 		# if sum(results) > (template_height / 2): # see if at least half of the tests were matches. If so, sure, let's call it a match! 
# 	# 		# 	matches.append((col/search_image_width, col % search_image_width, col/search_image_width + template_width, col%search_image_width + template_height))

# 	# # 		# DO NOT REMOVE. WORKS. 
# 	# 		r = []
# 	# 		for j in range(1, template_height):
# 	# 			r.append(search_image[col + (search_image_width * j): template_width + (search_image_width * j) + col] == template[(template_width * j) : (template_width * (j + 1))])
# 	# # 		break 
# 	# print matches
	# def get_matches(j):
	# 	row_index = search_image_width * j
	# 	return (search_image[
	# 				col + row_index : template_width + row_index + col] 
	# 				== template[(template_width * j) : (template_width * (j + 1))])

	
	# for col in range(len(search_image) - template_width):
	# 	if (search_image[col : template_width + col] == template[0:template_width] and 
	# 		search_image[col + search_image_width * 4: template_width + (search_image_width * 4) + col] == template[(template_width * 4) : (template_width * (4 + 1))]):
	# 		results = map(get_matches, range(1, template_height))
	# 		if sum(results) == template_height - 1: 
	# 			y = col/search_image_width
	# 			x = col % search_image_width
				# out_queue.put((x, y, x + template_width, y + template_height))
				# print out_queue.qsize()
				# robot.draw_box((x, y, x + template_width, y + template_height), (0,255,0))


# # No threads: [Finished in 20.2s]
# # No threads: [Finished in 20.3s]
# # w/ 8 cores: [Finished in 17.6s]
# # w/ 8 cores: [Finished in 17.6s]
# # w/ 4 cores: [Finished in 16.3s]
# # w/ 4 cores: [Finished in 16.2s]
# # w/ 2 cores: 

def get_cpus():
	cpus = multiprocessing.cpu_count()
	if cpus >2:
		return cpus/2 
	return 1 


if __name__ == '__main__':
	robot = Robot()
	print robot._enumerate_windows()
	print robot.wait_for_window("GitHub")



















