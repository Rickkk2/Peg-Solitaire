# -*- coding: utf-8 -*-
"""
------------------------
bastillav3 (final). 04/05/2021
------------------------
Ricardo Pacheco Ruiz
z17m077

Bernardo Soto Raya
a18m037

Gonzalo Losada Alvarez
z17m049
"""
#!/usr/bin/env python
 # -*- coding: utf-8 -*-


import pygame, numpy, sys
from pygame.locals import *

LC, N = 85, 9
F0 = [pygame.Rect(i*LC, 0, LC, LC) for i in range(3, 6)] 
F1 = [pygame.Rect(i*LC, LC, LC, LC) for i in range(3, 6)]
F2 = [pygame.Rect(i*LC, 2*LC, LC, LC) for i in range(3, 6)]
F3 = [pygame.Rect(i*LC, 3*LC, LC, LC) for i in range(N)]
F4 = [pygame.Rect(i*LC, 4*LC, LC, LC) for i in range(N)]
F5 = [pygame.Rect(i*LC, 5*LC, LC, LC) for i in range(N)]
F6 = [pygame.Rect(i*LC, 6*LC, LC, LC) for i in range(3, 6)]
F7 = [pygame.Rect(i*LC, 7*LC, LC, LC) for i in range(3, 6)]
F8 = [pygame.Rect(i*LC, 8*LC, LC, LC) for i in range(3, 6)]
# El tablero
R = [F0, F1, F2, F3, F4, F5, F6, F7, F8]
# Inicialmente, todas las casillas están ocupadas a excepción de la central
P = [[1, 1, 1], [1, 1, 1], [1, 1, 1] , [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1, 1], 
     [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]


# Devuelve el número de casillas ocupadas por una pieza
def casillasOcupadas():
    n, k = 0, 0
    for i in range(9):
        n = numpy.count_nonzero(numpy.array(P[i]))
        k = k + n
    return k


# El juego se acaba si sólo hay una casilla ocupada y es alguna de las centrales
def casilla_final_valida():
    if P[1][1] == 1 : return True
    elif P[4][1] == 1 : return True
    elif P[4][4] == 1 : return True
    elif P[4][7] == 1 : return True
    elif P[7][1] == 1 : return True
    return False


# Movimientos del tablero
def movimiento(ventana, x1, y1, x2, y2):
    Pp0 = [-2, -2, -2, P[0][0], P[0][1], P[0][2], -2, -2, -2]
    Pp1 = [-2, -2, -2, P[1][0], P[1][1], P[1][2], -2, -2, -2]
    Pp2 = [-2, -2, -2, P[2][0], P[2][1], P[2][2], -2, -2, -2]
    Pp6 = [-2, -2, -2, P[6][0], P[6][1], P[6][2], -2, -2, -2]
    Pp7 = [-2, -2, -2, P[7][0], P[7][1], P[7][2], -2, -2, -2]
    Pp8 = [-2, -2, -2, P[8][0], P[8][1], P[8][2], -2, -2, -2]
    # Pp es el cuadrado 9x9 que contiene al tablero. Así pues, el número de columna varía según la fila
    Pp = [Pp0, Pp1, Pp2, P[3], P[4], P[5], Pp6, Pp7, Pp8]

    # Columnas y1 e y2 respecto de Pp
    y1p, y2p = y1, y2 
    if len(P[x1])==3 : y1p = y1p + 3
    if len(P[x2])==3 : y2p = y2p + 3
        
    # d es la columna intermedia, que dependerá de en qué fila esté situada
    d = y1p

    # Bajamos dos filas, mantenemos la columna
    if x2 == x1 + 2 and y1p == y2p and Pp[x1+1][y1p] == 1:
        if len(P[x1+1]) == 3 : d = y1p - 3
        P[x1][y1] = 0
        P[x1+1][d] = 0
        P[x2][y2] = 1
    # Subimos dos filas, mantenemos la columna
    elif x2 == x1 - 2 and y1p == y2p and Pp[x1-1][y1p] == 1:
        if len(P[x1-1]) == 3 : d = y1p - 3
        P[x1][y1] = 0 
        P[x1-1][d] = 0
        P[x2][y2] = 1
    # Avanzamos dos columnas, mantenemos la fila
    elif y2 == y1 + 2 and x1 == x2 and Pp[x1][y1p+1] == 1:
        if len(P[x1])==3 : y1p = y1p - 3
        P[x1][y1] = 0
        P[x1][y1p+1] = 0
        P[x2][y2] = 1
    # Retrocedemos dos columnas, mantenemos la fila
    elif y2 == y1 - 2 and x1 == x2 and Pp[x1][y1p-1] == 1:
        if len(P[x1])==3 : y1p = y1p - 3
        P[x1][y1] = 0
        P[x1][y1p-1] = 0
        P[x2][y2] = 1
    # Movimiento inválido
    else: P[x1][y1] = 1
        

def tablero(ventana):
    AZ, VRD_CLR, VRD_OSC, BL, RJ = (0, 0, 128), (0, 255, 153), (23, 63, 53), (250, 250, 250), (200, 0, 0)
    for i in range(len(R)):
        for j in range(len(R[i])):
            #Dibujamos las casillas
            if P[i][j] == -1 : pygame.draw.rect(ventana, RJ, R[i][j])
            else : pygame.draw.rect(ventana, VRD_OSC, R[i][j])
            #Dibujamos las fichas
            if P[i][j] != 0: pygame.draw.circle(ventana, AZ, R[i][j].center, 25)
    #Dibujamos las líneas interiores del tablero
    for i in range(N): #lineas horizontales
        if i > 2 and i < 7 : pygame.draw.line(ventana, BL, [0, i*LC], [N*LC, i*LC], 1)
        else : pygame.draw.line(ventana, BL, [3*LC, i*LC], [6*LC, i*LC], 1)
    for i in range(N): #lineas verticales
        if i > 2 and i < 7 : pygame.draw.line(ventana, BL, [i*LC, 0], [i*LC, N*LC], 1)
        else : pygame.draw.line(ventana, BL, [i*LC, 3*LC], [i*LC, 6*LC], 1)
    #Dibujamos las líneas exteriores del tablero
    pygame.draw.polygon(ventana, BL, [[3*LC,0], [3*LC,N*LC], [6*LC,900], [6*LC,0]], 5)
    pygame.draw.polygon(ventana, BL, [[0,3*LC], [N*LC,3*LC], [N*LC,6*LC], [0,6*LC]], 5)
    

def main():
 ventana = pygame.display.set_mode((N*LC, N*LC))
 pygame.display.set_caption("Juego de la Bastilla")
 tablero(ventana)
 pygame.display.update()
 final = False
 x1, y1, x2, y2 = 0, 0, 0, 0
 casilla_activada = False
 
 # Bucle del juego 
 while not final:
    for event in pygame.event.get():
        # Cierre del juego
        if event.type == pygame.QUIT:
            final = True
        
        # Click del raton
        elif event.type == MOUSEBUTTONDOWN:
            raton = pygame.mouse.get_pos()           
            for i in range(len(R)):
                for j in range(len(R[i])):
                    if R[i][j].collidepoint(raton):
                        if casilla_activada == False : x1, y1 = i, j
                        else: x2, y2 = i, j         
            # Primera casilla
            if P[x1][y1] == 1 and not casilla_activada:
                            casilla_activada = True
                            P[x1][y1] = -1
            # Segunda casilla (incorrecta)
            elif P[x2][y2] == 1 and casilla_activada:
                            casilla_activada = False
                            P[x1][y1] = 1
            # Segunda casilla == Primera casilla
            elif P[x2][y2] == -1 and casilla_activada: 
                            casilla_activada = False
                            P[x1][y1] = 1
            # Segunda casilla (puede que correcta)
            elif P[x2][y2] == 0 and casilla_activada:
                            casilla_activada = False
                            movimiento(ventana, x1, y1, x2, y2) 
            tablero(ventana)     
        
        # Condiciones de victoria
        if casillasOcupadas() == 1 and casilla_final_valida():
            pygame.display.set_caption("¡CONSEGUIDO!")
            
    pygame.display.update()
 pygame.quit()
 sys.exit()


if __name__ == '__main__':
 pygame.init()
 main()
