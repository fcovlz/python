import win32api, time


print("die screensaver!")
dif = 1
exc = False

while True:
    try:
        pos = win32api.GetCursorPos()
        time.sleep(30)
        curPos = win32api.GetCursorPos()
        if pos == curPos:
            newPos = (curPos[0], curPos[1] + dif)
            print("Let's move to %s from %s" % (newPos, pos))
            dif *= -1
            win32api.SetCursorPos(newPos)
    except():
        if not exc:
            print("Something bad happened.. But never mind")
            exc = True
