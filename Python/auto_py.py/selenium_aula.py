import time
from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.maximize_window()

navegador.get('https://www.python.org/')

lista_botoes = navegador.find_elements(By.CLASS_NAME, 'button')
for botao in lista_botoes:
    if 'Become a Member' in botao.text:
        botao.click()
        break

abas = navegador.window_handles
if len(abas) > 1:
    navegador.switch_to.window(abas[1])

navegador.get('https://www.python.org/community/')

time.sleep(10)
navegador.quit()








# = = = = = = = = = = = =

# import time
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# import undetected_chromedriver as uc

# navegador = webdriver.Chrome()

# navegador = uc.Chrome()
# navegador.get('https://www.google.com')

# caixa_buscar = navegador.find_element(By.NAME, 'q')

# caixa_buscar.send_keys('Monitor Gamer')

# caixa_buscar.submit()

# time.sleep(5)
# navegador.quit()