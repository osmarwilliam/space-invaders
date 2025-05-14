from PPlay.sprite import *
import config

# todos sprites do jogos 

botao_jogar = Sprite("images/jogar.png", 1)
botao_jogar.set_position(config.window.width/2 - botao_jogar.width/2, 50)

botao_dificuldade = Sprite("images/dificuldade.png", 1)
botao_dificuldade.set_position(config.window.width/2 - botao_jogar.width/2, 25+150)

botao_rank = Sprite("images/raking.png", 1)
botao_rank.set_position(config.window.width/2 - botao_jogar.width/2, 50+250)

botao_sair = Sprite("images/sair.png", 1)
botao_sair.set_position(config.window.width/2 - botao_jogar.width/2, 75+350)

botao_dificuldade_facil = Sprite("images/facil.png", 1)
botao_dificuldade_facil.set_position(config.window.width/2 - botao_jogar.width/2, 100)

botao_dificuldade_medio = Sprite("images/medio.png", 1)
botao_dificuldade_medio.set_position(config.window.width/2 - botao_jogar.width/2, 250)

botao_dificuldade_hard = Sprite("images/dificil.png", 1)
botao_dificuldade_hard.set_position(config.window.width/2 - botao_jogar.width/2, 400)
