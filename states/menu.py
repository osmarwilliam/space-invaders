import config 
import sprite

def menu():
    while True:
        

        config.window.set_background_color((20,20,20))
        
        # Desenha os sprites do menu
        sprite.botao_jogar.draw()
        sprite.botao_dificuldade.draw()
        sprite.botao_rank.draw()
        sprite.botao_sair.draw()

        # Caso botão "sair" seja clicado
        if config.mouse.is_over_object(sprite.botao_sair) and config.mouse.is_button_pressed(1):
            # termina o loop
            config.running = False
            break

        # Caso botão "dificuldade" seja clicado
        if config.mouse.is_over_object(sprite.botao_dificuldade) and config.mouse.is_button_pressed(1):
            config.control = config.dificuldade
            return 0

        # Caso botão "jogar" seja clicado
        if config.mouse.is_over_object(sprite.botao_jogar) and config.mouse.is_button_pressed(1):
            config.control = config.jogo
            return 0

        # Caso botão "ranking" seja clicado
        if config.mouse.is_over_object(sprite.botao_rank) and config.mouse.is_button_pressed(1):
            config.control = config.ranking
            return 0



        config.window.update()