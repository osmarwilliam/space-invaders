import config 
import sprite
import states.menu as menu
import states.jogo as jogo
import states.ranking as ranking
import states.dificuldade as dificuldade

config.control = config.menu

while config.running:
    
    match config.control:
  
        case config.menu:
            menu.menu()

        case config.dificuldade:
            dificuldade.dificuldade()
  
        case config.jogo:
            jogo.jogar()
  
        case config.ranking:
            ranking.ranking()
