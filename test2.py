import win32gui

def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        txt = win32gui.GetWindowText(hwnd)
        if txt != '':
        	print(win32gui.GetWindowText(hwnd))

win32gui.EnumWindows(winEnumHandler, None)