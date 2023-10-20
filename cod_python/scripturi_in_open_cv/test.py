import pyautogui
import time
import keyboard

def cautare_google():
    search_bar_google = "scripturi_in_open_cv/search_bar_up.png"
    if pyautogui.locateOnScreen(search_bar_google, confidence=0.7) != None:
        print("works")
        camp_google = pyautogui.locateOnScreen(search_bar_google, confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write("https://www.youtube.com/@markiplier")
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(4)
        subscribe_button = pyautogui.locateOnScreen("scripturi_in_open_cv/subscribe.png", confidence=0.9)
        if subscribe_button != None:
            pyautogui.click(subscribe_button)
        else:
            print("button negasit")

response = pyautogui.confirm("Doriti sa incepeti rularea programului?", "Confirmare")
if (response == "OK"):
    cautare_google()
else:
    pyautogui.alert("Ati ales Anulare", "Anulare")
