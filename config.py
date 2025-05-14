from PPlay.window import *

# Instancio o tamanho da tela
window = Window(1240, 620)
window.set_title('Osmar William')

# Instancio o teclado
keyboard = window.get_keyboard()

# Instancio o mouse
mouse = window.get_mouse()

# Define os valores que serão atribuidos a cada tela para o control.
menu = 0
ranking = 1
dificuldade = 2
jogo = 3

# Define o valor inicial de control para menu
control = menu    

# Define uma variável para controlar o loop principal do jogo
running = True