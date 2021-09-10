import func as fc
import numpy as np 
import random
import json
import os.path


def create_board (board):
    for i in range (10):
        columnas = []
        for j in range(10):
            columnas.append("~")
        board.append(columnas)

def insert_boat_check(pos_str, boat_len, board):

    # lo primero es comprobar si el formato de insercion es el correcto
    # los dos puntos son un elemento constante en la inserción de posición
    if pos_str.count(':')==1:

        # comprobación de elementos de una inserción vertical 
        if pos_str.count("v")==1:   # Debe haber una única letra de orientación
            if pos_str.count ("h") == 0:    # no puede ser horizontal
                ori = "v"
            else:
                print("Position format error for this boat, type it again.")
                return False

        # comprobación de elementos de una inserción horizontal 
        elif pos_str.count("h")==1: # Debe haber una única letra de orientación
            if pos_str.count ("v") == 0:    # no puede ser vertical
                ori = "h"
            else:
                print("Position format error for this boat, type it again.")
                return False
        else:
            print("Position format error for this boat, type it again.")
            return False
    else:
        print("Position format error for this boat, type it again.")
        return False
        
    # A continuación se descompone el string para obtener los números
    try:
        list1 = pos_str.split(ori)
        list2 = list1[-1].split(":")
        num1 = int(list1[0])
        num2 = int(list2[0])
        num3 = int(list2[1])
        
        # Se comprueban la coherencia de las coordenadas
        coord_OK = False
        if (num1 >= 1 and num1 <= 10) and (num2 >= 1 and num2 <= 10) and (num3 >= 1 and num3 <= 10):
            coord_OK = True

        # Se comprueba que el largo del barco y las coordenadas coinciden
        len_coord_OK = False
        if num3-num2+1 == boat_len:
            len_coord_OK = True
        # Si no hay error de formato y la función prosigue, se devuelve una lista con la orientación y las coordenadas del barco
        if coord_OK:
            if len_coord_OK:
                list_posi = [ori, num1, num2, num3]
            else:
                print ("Coordenates do not match with the boat lenght, type it again.") 
                return False   
        else:
            print("A coordenate is out of range, type it again.")
            return False
    except ValueError:
        print("Position format error for this boat, type it again.")
        return False

    # Por último, se comprueban las posiciones ya ocupadas del tablero
    if list_posi[0] == 'h':
        for i in range(list_posi[2]-1, list_posi[3]):
            if board[list_posi[1]-1][i] == '~':
                board[list_posi[1]-1][i] = '#'
            else:
                print("One of the positions of the boat is already taken.")
                return False
        return True
    else: 
        for i in range(list_posi[2]-1, list_posi[3]):
            if board[i][list_posi[1]-1] == '~':
                board[i][list_posi[1]-1] = '#'
            else:
                print("One of the positions of the boat is alreaady taken.")
                return False
        return True

    return list_posi

def insert_fleet(board, fleet):
    # Bloque de inserción de los 4 barcos 2x1
    for i in range (4):
        test_boat_type = 2
        insert2x1 = False
        while insert2x1 != True:
            test_position = input("Please insert a 2x1 boat position (type 'BOARD' to display the current setting of the fleet):")
            if test_position == "BOARD":
                fc.print_board(board)
            else:
                insert2x1 = insert_boat_check(test_position, test_boat_type, board)
        fleet["2x1_"+str(i+1)] = test_position
    # Bloque de inserción de los 3 barcos 3x1
    for i in range (3):
        test_boat_type = 3
        insert3x1 = False
        while insert3x1 != True:
            test_position = input("Please insert a 3x1 boat position (type 'BOARD' to display the current setting of the fleet):")
            if test_position == "BOARD":
                fc.print_board(board)
            else:
                insert3x1 = insert_boat_check(test_position, test_boat_type, board)
        fleet["3x1_"+str(i+1)] = test_position

    # Bloque de inserción de los 2 barcos 4x1
    for i in range (2):
        test_boat_type = 4
        insert4x1 = False
        while insert4x1 != True:
            test_position = input("Please insert a 4x1 boat position (type 'BOARD' to display the current setting of the fleet):")
            if test_position == "BOARD":
                fc.print_board(board)
            else:
                insert4x1 = insert_boat_check(test_position, test_boat_type, board)
        fleet["4x1_"+str(i+1)] = test_position
            
    # Bloque de inserción del barco 5x1
    test_boat_type = 5
    insert5x1 = False
    while insert5x1 != True:
        test_position = input("Please insert a 5x1 boat position (type 'BOARD' to display the current setting of the fleet):")
        if test_position == "BOARD":
            fc.print_board(board)
        else:
            insert5x1 = insert_boat_check(test_position, test_boat_type, board)
    fleet["5x1_1"] = test_position

def start_game(name_J1,board_J1, fleet_J1,name_J2,board_J2, fleet_J2):
    # Se inician los perfiles de los jugadores y se elige cual de ellos es el primero
    name_one = input("Please insert the name of one player:")
    name_other = input("Please insert the name of the other player:")
    player_numbers = []
    for i in range(2):
        output = (random.randint(1,6))
        player_numbers.append(output)
    if player_numbers[0] == player_numbers[1]:
        print("What are the odds! That's a tie, try again")
        start_game(name_J1,board_J1, fleet_J1,name_J2,board_J2, fleet_J2)
    elif player_numbers[0] > player_numbers[1]:
        name_J1 = name_one
        name_J2 = name_other
        print (f"{name_one} is the first player. {name_other}, you are the second player")
    else:
        name_J2 = name_one
        name_J1 = name_other
        print(f"{name_other} is the second player. {name_one}, you are the first player, you start!")
        

    # Se generan el tablero y la flota del jugador 1
    create_board(board_J1)

    insert_fleet(board_J1, fleet_J1)
    board_J1 = np.array(board_J1)

    print(fleet_J1)
    fc.print_board(board_J1)

    # Se generan el tablero y la flota del jugador 2
    create_board(board_J2)

    insert_fleet(board_J2, fleet_J2)
    board_J2 = np.array(board_J2)

    print(fleet_J2)
    fc.print_board (board_J2)

    # Se guarda la partida inicializada
    #file_name_J1 = "Game_J1.json"
    my_dictionary_J1 = {"Name_J1": name_J1, 
                    "Fleet_J1": fleet_J1, 
                    "Board_J1":board_J1.tolist(),
                    "Turn":1}

    #file_name_J2 = "Game_J2.json"
    my_dictionary_J2 = {"Name_J2": name_J2, 
                    "Fleet_J2": fleet_J2, 
                    "Board_J2":board_J2.tolist(),
                    "Turn":1}
    
    # Seleccionamos donde queremos guardar los archivos json
    path=__file__
    ruta= os.path.dirname(path)

    json_data1 = (ruta + "\\Partidas_Batalla_Naval\\Game_J1.json")
    json_data2 = (ruta + "\\Partidas_Batalla_Naval\\Game_J2.json")

    with open(f"{json_data1}", 'w+') as outfile:
        json.dump(my_dictionary_J1, outfile, indent=4)

    with open(f"{json_data2}", 'w+') as outfile:
        json.dump(my_dictionary_J2, outfile, indent=4)


