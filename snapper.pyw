import win32gui
import win32api
import keyboard
from win32con import MONITOR_DEFAULTTONEAREST

import time

# we want to move the active window
# Python script to snap windows to upper/lower half of the screen to use especially for monitors used in portrait mode
while True:
    hwnd = win32gui.GetForegroundWindow()
    mnhd = win32api.MonitorFromWindow(hwnd, MONITOR_DEFAULTTONEAREST)
    monitorinfo = win32api.GetMonitorInfo(mnhd)

    rcmonitor = monitorinfo["Monitor"]
    rcwork = monitorinfo["Work"]

    coord = []
    for c in rcmonitor:
        coord.append(c)

    work = []
    for w in rcwork:
        work.append(w)

    # work out the differences in x, y, w, h to figure out where the taskbar is
    for v in range(4):
        if coord[v] != work[v]:
            coord[v] = coord[v] - abs(coord[v] - work[v])

    coord[3] = coord[3] - coord[1]  # we do this to get the proper rectangle height
    coord[2] = coord[2] - coord[0]  # with -8 as an offset on each side, thanks windows

    if keyboard.is_pressed('ctrl + alt + up'):
        win32gui.MoveWindow(hwnd, coord[0] - 8, coord[1] - 8, coord[2] + 16, int(coord[3]/2), True)
    if keyboard.is_pressed('ctrl + alt + down'):
        win32gui.MoveWindow(hwnd, coord[0] - 8, coord[1] + int(coord[3] / 2) - 8, coord[2] + 16, int(coord[3] / 2) + 16, True)

    time.sleep(0.1)



