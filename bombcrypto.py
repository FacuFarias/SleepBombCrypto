import pyautogui
import time
import webbrowser

def recursive():
    url='https://app.bombcrypto.io/'
    webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)
    

    time.sleep(3)   
    boton=pyautogui.locateOnScreen('imagengrande.png')

    while not boton:
        boton=pyautogui.locateOnScreen('imagen.png')
        time.sleep(1)
    #im = pyautogui.screenshot('imagen.png',region=(550,510, 285, 125))

    pyautogui.moveTo(boton.left+int(boton.width/2),boton.top+int(boton.height/2))
    pyautogui.click()

    pyautogui.moveTo(boton.left+int(boton.width/2),438)
    pyautogui.click()


    b_firmar= pyautogui.locateOnScreen('firmar.png')

    while not b_firmar:
        b_firmar= pyautogui.locateOnScreen('firmar.png')
        time.sleep(1)

    pyautogui.moveTo(b_firmar.left+int(b_firmar.width/2),b_firmar.top+int(b_firmar.height/2))
    pyautogui.click()

    #Presionar en Heroes
    b_heroes=pyautogui.locateOnScreen('heroes.png')

    while not b_heroes:
        b_heroes= pyautogui.locateOnScreen('heroes.png')
        time.sleep(1)

    pyautogui.moveTo(b_heroes.left+int(b_heroes.width/2),b_heroes.top+int(b_heroes.height/2))
    pyautogui.click()

    time.sleep(3)
    bombers=4
    b_work=pyautogui.locateOnScreen('work.png')

    while b_work:
        pyautogui.moveTo(b_work.left+int(b_work.width/2),b_work.top+int(b_work.height/2))
        pyautogui.click()
        b_work=pyautogui.locateOnScreen('work.png')
        time.sleep(2)
    print("sali de los trabajadores")
    b_back=pyautogui.locateOnScreen('back.png')
    while not b_back:
        b_back=pyautogui.locateOnScreen('back.png')
        time.sleep(2)
        print("no encuentro el back")

    pyautogui.moveTo(b_back.left+int(b_back.width/2),b_back.top+int(b_back.height/2))
    pyautogui.click()


    b_treasure=pyautogui.locateOnScreen('treasure.png')

    while not b_treasure:
        b_treasure=pyautogui.locateOnScreen('treasure.png')
        time.sleep(2)
    pyautogui.moveTo(b_treasure.left+int(b_treasure.width/2),b_treasure.top+int(b_treasure.height/2))
    pyautogui.click()

    timer=0
    while timer<=7200:
        
        b_unknown=pyautogui.locateOnScreen('unknown.png')

        if b_unknown:
            timer=0
            recursive()
        
        else:
            time.sleep(5)
            timer=timer+5
            b_unknown=pyautogui.locateOnScreen('unknown.png')
            print(timer)

        b_newmap=pyautogui.locateOnScreen('newmap.png')
        if b_newmap:
            pyautogui.moveTo(b_newmap.left+int(b_newmap.width/2),b_newmap.top+int(b_newmap.height/2))
            pyautogui.click()


    recursive()

recursive()

