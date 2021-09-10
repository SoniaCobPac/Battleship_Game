import numpy as np 
from re import split
import json
import os.path

# Esta función recibe una lista con los elementos de la posición de un barco 
# y modifica el tablero de juego para dibujarlo
def print_board(board):
    print("--------------OWN BOARD-------------------")
    boardNP = np.array(board)
    print(boardNP)
    print("--------------------------------------------")

def print_board_enemy(board):
    print("--------------ENEMY BOARD------------------")
    boardNP = np.array(board)
    boardShade = np.where(boardNP == '#', '~', boardNP)
    print(boardShade)          
    print("--------------------------------------------")   

def launch_torpedo(board):
    coord = input("Enter coordinates (row x column) or EXIT to exit game: ")
    if coord == "EXIT":
        return False
    else:
        # comprobamos el formato del input
        try:
            while coord.count("x")==1:
                # Restamos 1 a las coordinadas porque el jugador asume que el tablero empieza en la posición 1 y no 0
                coord = split("\D+", coord)
                coord_x = int(coord[0]) - 1
                coord_y = int(coord[1]) - 1

                # Comprobamos si el jugador ha dado a algun barco
                if board[coord_x][coord_y] == "#":
                    print("You have hit me!")
                    board[coord_x][coord_y] = "X"
                    #print(board)
                # Comprobamos si el jugador introduce una posición ya mencionada antes
                elif board[coord_x][coord_y] == "X" or board[coord_x][coord_y] == "o":
                    print("You have already said that position before. Try another")
                # Comprobamos si el jugador ha fallado
                else:
                    print("Water! maybe next time")
                    board[coord_x][coord_y] = "o"
                    #print(board)
                # Comprobamos si ya no quedan mas barcos
                if "#" not in np.array(board):
                    print("You have destroyed my fleet, you win!")
                    return False
                else:
                    return True  
            else:
                print("Position format error, type it again.")
                launch_torpedo(board)
                return True
        except IndexError:
            print("You are outside the board, type the coordinate again.") 
            launch_torpedo(board)
            return True
   

def auto_save(name_J1,board_J1, fleet_J1,name_J2,board_J2, fleet_J2, turn):
    # Se guarda el avance de la partida en la carpeta del histórico
    #file_name = f"Game_history.json"
    my_dictionary = {"Name_J1": name_J1, 
                    "Fleet_J1": fleet_J1, 
                    "Board_J1":board_J1,
                    "Name_J2": name_J2, 
                    "Fleet_J2": fleet_J2, 
                    "Board_J2":board_J2,
                    "Turn":turn}
    
    # Re-escribimos el archivo json en cada turno  
    path=__file__
    ruta= os.path.dirname(path)
    json_data = (ruta + "\\Partidas_Batalla_Naval\\Game_History.json")

    with open(f"{json_data}", 'a+') as outfile:
        json.dump(my_dictionary, outfile, indent=4)

def exit_save(name_J1,board_J1, fleet_J1,name_J2,board_J2, fleet_J2, turn):
    # Se guarda el avance de la partida en la carpeta del histórico
    #file_name = f"Game_in_process.json"
    my_dictionary = {"Name_J1": name_J1, 
                    "Fleet_J1": fleet_J1, 
                    "Board_J1":board_J1,
                    "Name_J2": name_J2, 
                    "Fleet_J2": fleet_J2, 
                    "Board_J2":board_J2,
                    "Turn":turn}
    
    # Re-escribimos el archivo json en cada turno  
    path=__file__
    ruta= os.path.dirname(path)
    json_data = (ruta + "\\Partidas_Batalla_Naval\\Game_in_process.json")

    with open(f"{json_data}", 'w+') as outfile:
        json.dump(my_dictionary, outfile, indent=4)

  