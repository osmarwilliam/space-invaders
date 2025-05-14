import config 
import sprite
import states.menu as menu
import states.jogo as jogo
import states.ranking as ranking
import states.dificuldade as dificuldade

# control define qual o estado atual da tela
# tem como valor inicial o menu
config.control = config.menu

while config.running:

    # controle de telas  
    match config.control:
    
        case config.menu:
            menu.menu()

        case config.dificuldade:
            dificuldade.dificuldade()
  
        case config.jogo:
            jogo.jogar()
  
        case config.ranking:
            ranking.ranking()
