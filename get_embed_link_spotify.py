import pyautogui, pyperclip

links = []

# Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size()

currentMouseX, currentMouseY = pyautogui.position()

print(currentMouseX, currentMouseY)

time = .2

for i in range(0,10):

    # Move the mouse to XY primera cancion
    pyautogui.moveTo(513, 149, time)  
    pyautogui.rightClick()

    # Move the mouse to XY Share
    pyautogui.moveTo(556, 421, time)  
    pyautogui.moveTo(437, 654, time)  

    # aqui ya tenemos el link copiado
    pyautogui.click()  

    # Move the mouse to XY notepad
    pyautogui.moveTo(811, 1066, time)  
    pyautogui.click()

    # copiamos el iframe tag
    pyautogui.hotkey("ctrl", "v")  

    # Move el mouse a seleccionar el texto de link
    pyautogui.moveTo(1068, 63, .1)
    # Seleccionamos el link
    pyautogui.dragTo(x=1550, y=63, duration=2)
    pyautogui.hotkey("ctrl", "c")  

    #añadimos un nuevo link
    new = pyperclip.paste()
    print(new)
    links.append(new)

    #borramos el texto en notepad
    pyautogui.hotkey("ctrl", "a")
    pyautogui.keyDown("backspace")

    #scroll
    pyautogui.moveTo(950, 946, time)
    pyautogui.click(clicks=1)

print(links)