import win32gui
import win32con

dialog = win32gui.FindWindow('#32770', u'打开')
ComboBoxEx32 = win32gui.FindWindowEx(dialog, None, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, None, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, None, 'Edit', None)
win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'hello')
button = win32gui.FindWindowEx(dialog, None, 'Button', '打开(&O)')
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
print(button)
