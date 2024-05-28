import pyautogui
import time

posicao_barra_pesquisa = (200, 110)
posicao_clicar_na_pessoa = (200, 200)

a = input('Para quem você quer mandar mensagem?')
msg = input('Que mensagem você quer deixar?')

pyautogui.press('win')
time.sleep(1)
pyautogui.write('WhatsApp')
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)
pyautogui.moveTo(posicao_barra_pesquisa)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.write(a)
time.sleep(1)
pyautogui.moveTo(posicao_clicar_na_pessoa)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.write(msg)
time.sleep(1)
pyautogui.press('enter')
