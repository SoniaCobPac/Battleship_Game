# keep calm and keep coding
import func as fc
import Inicializacion_Flota as init
import json
import numpy as np 
import random
import time
import os.path

#Se crean las variables necesarias para el juego
name_J1 = ""
board_J1 = []
fleet_J1 = {}
name_J2 = ""
board_J2 = []
fleet_J2 = {}

# Simulación de secuencia de juego
print("START THE GAME:")
init_load = input("Do you want to start a new game (Enter NG for New Game), \
    load the last unstarted game (LG for Last Game), or continue the last unfinished game (UG for Unfinished Game)?") 

# Empezamos una nueva partida
if init_load == 'NG':
    init.start_game(name_J1, board_J1, fleet_J1, name_J2, board_J2, fleet_J2)
    turn = 1

elif init_load == 'UG':
    # Cargamos una partida que se empezó a jugar pero no se finalizó
    path=__file__
    ruta= os.path.dirname(path)
    json_data = (ruta + "\\Partidas_Batalla_Naval\\Game_in_process.json")
    with open(f"{json_data}", "r+") as outfile:
        json_HundirFlota_reload = json.load(outfile)
    name_J1 = json_HundirFlota_reload['Name_J1']
    board_J1 = json_HundirFlota_reload['Board_J1']
    fleet_J1 = json_HundirFlota_reload['Fleet_J1']
    name_J2 = json_HundirFlota_reload['Name_J2']
    fleet_J2 = json_HundirFlota_reload['Fleet_J2']
    board_J2 = json_HundirFlota_reload['Board_J2']
    turn = json_HundirFlota_reload['Turn']
else:
    # Cargamos una partida donde ya tenemos los barcos de los dos jugadores pero el juego no se inició
    path=__file__
    ruta= os.path.dirname(path)
    json_data1 = (ruta + "\\Partidas_Batalla_Naval\\Game_J1.json")
    json_data2 = (ruta + "\\Partidas_Batalla_Naval\\Game_J2.json")

    with open(f"{json_data1}", 'r+') as outfile:
        json_HundirFlota1_readed = json.load(outfile)

    with open(f"{json_data2}", 'r+') as outfile:
        json_HundirFlota2_readed = json.load(outfile)

    name_J1 = json_HundirFlota1_readed['Name_J1']
    board_J1 = json_HundirFlota1_readed['Board_J1']
    fleet_J1 = json_HundirFlota1_readed['Fleet_J1']
    turn = json_HundirFlota1_readed['Turn']
    name_J2 = json_HundirFlota2_readed['Name_J2']
    fleet_J2 = json_HundirFlota2_readed['Fleet_J2']
    board_J2 = json_HundirFlota2_readed['Board_J2']
    turn = json_HundirFlota2_readed['Turn']

continue_game = True
time.sleep(1)
while continue_game:
    if turn%2 == 1:
        print("----------TURN OF PLAYER ONE J1--------")
        fc.print_board(board_J1)
        fc.print_board_enemy(board_J2)
        # los barcos están en el tablero y pedimos el ataque
        print("PLAYER ONE ATTACK TO PLAYER TWO")
        continue_game = fc.launch_torpedo(board_J2)
        turn +=1
        fc.auto_save(name_J1,board_J1, fleet_J1,name_J2,board_J2, fleet_J2, turn)
        fc.exit_save(name_J1,board_J1, fleet_J1,name_J2,board_J2, fleet_J2, turn)
        print("END OF THE PLAYER ONE'S (J1) TURN\n")
    else:
        print("----------TURN OF PLAYER TWO J2--------")
        fc.print_board(board_J2)
        fc.print_board_enemy(board_J1)
        print("PLAYER TWO ATTACK TO PLAYER ONE")
        continue_game = fc.launch_torpedo(board_J1)
        turn +=1
        fc.auto_save(name_J1,board_J1, fleet_J1,name_J2,board_J2, fleet_J2, turn)
        fc.exit_save(name_J1,board_J1, fleet_J1,name_J2,board_J2, fleet_J2, turn)
        print("END OF THE PLAYER TWO'S (J2) TURN\n")
print("GAME OVER")