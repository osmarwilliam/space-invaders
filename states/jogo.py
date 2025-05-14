import config

# caso botão "jogar" seja clicado
def jogar():

    while True:
        config.window.set_background_color((20,20,20))

        config.window.update()
        
        # caso "Esc" seja clicado irá retornar para a tela do menu
        if config.keyboard.key_pressed("ESC"):
            config.control = config.menu
            return 0