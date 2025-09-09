import pyautogui, time

# print(pyautogui.position()) -> posição do mouse na tela
# print(pyautogui.size()) -> tamanho do munitor

# print(time.sleep(3)) -> da um delay para depois o código rodar
# print(pyautogui.click(x=603, y=888)) -> faz o mouse clicar em algo

# print(time.sleep(4))
# print(pyautogui.moveTo(x=276, y=241, duration=1)) -> move o mouse

print(time.sleep(1))
pyautogui.click(x=604, y=878, duration=1)
print(time.sleep(1))
pyautogui.moveTo(x=276, y=241, duration=1)
pyautogui.click(x=266, y=331, duration=1)
pyautogui.click(x=468, y=338, duration=1)
pyautogui.click(x=822, y=308, duration=1)

print(time.sleep(4))
pyautogui.click(x=99, y=150, duration=1)

pyautogui.click(x=609, y=181, duration=1)
print(time.sleep(3))

# time.sleep(5)
# pyautogui.scroll(-500)

pyautogui.write('Monitor Gamer', interval=0.3)
pyautogui.press('enter')

# = = = = = = = = = = = =

# print(time.sleep(7))
# print(pyautogui.click(x=214, y=836))
# print(time.sleep(1.5))
# print(pyautogui.click(x=1160, y=272))

# time.sleep(3)
# print(pyautogui.position())