import pyautogui
import time

time.sleep(5)

# Pega a posição da tela onde o mouse está
print(pyautogui.position())

# Scroll da tela em pixels, valor positivo: pra cima. valor negativo: pra baixo.
pyautogui.scroll(100)