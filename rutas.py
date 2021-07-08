import copy

#verifica si un arreglo esta vacio o no
def is_empty(data_structure):
    if data_structure:
        return False
    else:
        return True

def create_answer_matrix(n,y):
    answer_matrix = []
    for i in range(n):
        answer_matrix.append([])
        for j in range(y):
            answer_matrix[i].append(0)
    return answer_matrix



#verifica si el movimiento hacia la derecha es valido
def right(partial_answer,matrix,target_row,target_column):
    limt_matrix = len(matrix[0])
    if target_column == limt_matrix:
        target_column-=1
        return False

    if (matrix[target_row][target_column]==0 and partial_answer[target_row][target_column]==0):
        return True

    return False

#verifica si el movimiento hacia abajo es valido
def down(partial_answer,matrix,target_row,target_column):
    limt_matrix = len(matrix)
    if target_row == limt_matrix:
        target_row-=1
        return False

    if (matrix[target_row][target_column] == 0 and partial_answer[target_row][target_column]==0):
        return True

    return False

#verifica si el movimiento hacia la izquierda es valido
def left(partial_answer,matrix,target_row,target_column):
    limt_matrix = -1
    if target_column == limt_matrix:
        target_column+=1
        return False

    if (matrix[target_row][target_column] == 0 and partial_answer[target_row][target_column]==0):
        return True

    return False

#verifica si el movimiento hacia arriba es valido
def up(partial_answer,matrix,target_row,target_column):
    limt_matrix = -1
    if target_row == limt_matrix:
        target_row+=1
        return False
    if (matrix[target_row][target_column] == 0 and partial_answer[target_row][target_column]==0):
        return True



#envia a verificar el movimiento hacia la derecha y si es valido marca la casilla como recorrida y llama la recursion
#para encontrar el siguente movimiento
def move_right(matrix,actual_row,actual_column,target_row,target_column,partial_answer,answer):
    if right(partial_answer,matrix,target_row,target_column)==True:
        partial_answer[actual_row][actual_column]=1
        matrix_traking(answer,partial_answer,matrix,target_row,target_column)
        partial_answer[actual_row][actual_column]=0
        return


#envia a verificar el movimiento hacia abajo y si es valido marca la casilla como recorrida y llama la recursion
#para encontrar el siguente movimiento
def move_down(matrix, actual_row, actual_column, target_row, target_column,partial_answer,answer):
    if down(partial_answer,matrix,target_row,target_column) == True:
        partial_answer[actual_row][actual_column]=1
        matrix_traking(answer,partial_answer,matrix,target_row,target_column)
        partial_answer[actual_row][actual_column]=0
        return 


#envia a verificar el movimiento hacia la izquierda y si es valido marca la casilla como recorrida y llama la recursion
#para encontrar el siguente movimiento
def move_left(matrix, actual_row, actual_column, target_row, target_column,partial_answer,answer):
    if left(partial_answer,matrix,target_row,target_column)==True:
        partial_answer[actual_row][actual_column]=1
        matrix_traking(answer,partial_answer,matrix,target_row,target_column)
        partial_answer[actual_row][actual_column]=0
        return


#envia a verificar el movimiento hacia la arriba y si es valido marca la casilla como recorrida y llama la recursion
#para encontrar el siguente movimiento
def move_up(matrix, actual_row, actual_column, target_row, target_column,partial_answer,answer):
    if up(partial_answer,matrix,target_row,target_column)==True:
        partial_answer[actual_row][actual_column]=1
        matrix_traking(answer,partial_answer,matrix,target_row,target_column)
        partial_answer[actual_row][actual_column]=0
        return

#funcion que se encarga de el siguente movimieno y enviar a revosar si es valido
def matrix_traking(answer,partial_answer,matrix,row,column):
    n = len(matrix)
    y = len(matrix[0])

    if n-1 == row and y-1 == column:
        if matrix[row][column]==0:
            partial_answer[row][column]=1
            ans = copy.deepcopy(partial_answer)
            answer.append(ans)
            partial_answer[row][column]=0

    else:
        movimientos = [[0,0, 1], [1,1, 0], [2,0, -1], [3,-1, 0]]
        for i in movimientos:
            target_row = row + i[1]
            target_column = column + i[2]

            moves = [move_right, move_down, move_left, move_up]
            next_move = moves[i[0]]
            next_move(matrix, row, column, target_row, target_column, partial_answer, answer)


#funcion que imprime una matriz en forma grafica
#[0,0,0,0]
#[0,0,0,0]
#[0,0,0,0]
#[0,0,0,0]
def print_matrix(matrix):
    x = len(matrix)
    for i in range (0,x):
        print("\nSolucion #"+str(i))
        for x in range (0,len(matrix[i])):
            print(matrix[i][x])

#Funcion main se encarga de enviar la primera orden para encontrar la ruta
def encontrar_ruta(C):
    x_de_inicio = 0
    y_de_inicio = 0
    n = len(C)
    y = len(C[0])

    answer=[]

    partial_answer = create_answer_matrix(n, y)

    matrix_traking(answer,partial_answer,C,y_de_inicio,x_de_inicio)
    
    if (is_empty(answer)):
        aux = []
        answer.append(aux)
    return answer[0]




