import config 
import sprite


while (True):

    if config.keyboard.key_pressed("ESC"):
        config.control = 0        

    if config.mouse.is_over_object(sprite.botao_sair) and config.mouse.is_button_pressed(1):
        break
    
    if config.mouse.is_over_object(sprite.botao_dificuldade) and config.mouse.is_button_pressed(1):
        config.control = 1
    
    if config.mouse.is_over_object(sprite.botao_jogar) and config.mouse.is_button_pressed(1):
        config.control = 2
    
    if config.mouse.is_over_object(sprite.botao_rank) and config.mouse.is_button_pressed(1):
        config.control = 3
    
    config.window.set_background_color((128, 128, 128))
    
    if config.control == 0:
        sprite.botao_jogar.draw()
        sprite.botao_dificuldade.draw()
        sprite.botao_rank.draw()
        sprite.botao_sair.draw()
    
    if config.control == 1:
        sprite.botao_dificuldade_hard.draw()
        sprite.botao_dificuldade_facil.draw()
        sprite.botao_dificuldade_medio.draw()
    
    if config.control == 2:
        pass
    if config.control == 3:
        pass

    config.window.update()