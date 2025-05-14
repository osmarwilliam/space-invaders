import config

# caso o botão ranking seja clicado
def ranking():
    while True:

        config.window.set_background_color((20,20,20))

        config.window.update()
        
        # caso Esc seja clicado, control será resetado para o menu
        if config.keyboard.key_pressed("ESC"):
            config.control = config.menu
            return 0