import pygame
import random
import math
import time

#cores do jogo
barra = (82, 84, 84)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (45, 227, 172)
azul = (61, 175, 179)
bic = (12, 82, 235)
azul_claro = (215, 246, 247)
branco = (255, 255, 255)
verde2 = (169, 196, 196)

window = pygame.display.set_mode([675, 600])

pygame.font.init()

#fonte do jogo
fonte = pygame.font.SysFont('Courier', 20, bold=True)

tabuleiro = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]
             
jogo = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
        ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
        ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
        ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
        ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
        ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
        ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
        ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
        ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]
        

esconder = True
tab_preenchido = True
click_last_status = False
cronometro_ativo = True
click_pos_x = -1
click_pos_y = -1
numero = 0
tipo_de_numero = [['n' for _ in range(9)] for _ in range(9)]
contador_erros = 0
menor_tempo = float('inf') 


def Tabuleiro_Hover(window, mouse_pos_x, mouse_pos_y):
    quadrado = 50
    ajuste = 50
    x = (math.ceil((mouse_pos_x - ajuste) / quadrado) - 1)
    y = (math.ceil((mouse_pos_y - ajuste) / quadrado) - 1)
    pygame.draw.rect(window, branco, (0, 0, 1000, 700))
    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        pygame.draw.rect(window, azul_claro, ((ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado)))

def Celula(window, mouse_pos_x, mouse_pos_y, click_last_status, click, x, y):
    quadrado = 50
    ajuste = 50
    if click_last_status == True and click == True:
        x = (math.ceil((mouse_pos_x - ajuste)/quadrado)-1)
        y = (math.ceil((mouse_pos_y - ajuste)/quadrado)-1)
    elif x >=0 and x <= 8 and y >=0 and y <=8:
        pygame.draw.rect(window, azul, ((ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado)))
    return x, y

def Grafico(window):
    pygame.draw.rect(window, barra, (50, 50, 450, 300), 6)
    pygame.draw.rect(window, barra, (50, 200, 450, 300), 6)
    pygame.draw.rect(window, barra, (200, 50, 150, 450), 6)
    pygame.draw.rect(window, barra, (50, 100, 450, 50), 2)
    pygame.draw.rect(window, barra, (50, 250, 450, 50), 2)
    pygame.draw.rect(window, barra, (50, 400, 450, 50), 2)
    pygame.draw.rect(window, barra, (100, 50, 50, 450), 2)
    pygame.draw.rect(window, barra, (250, 50, 50, 450), 2)
    pygame.draw.rect(window, barra, (400, 50, 50, 450), 2)

def Indice(window):


    pygame.draw.rect(window, preto, (510, 50, 170, 35))
    time = fonte.render("Tempo: ", True, branco)
    window.blit(time, (515, 55))

def Cronometro(window, tempo):
    if cronometro_ativo:
        minuto = tempo // 60
        segundo = tempo % 60
        texto_tempo = f"{minuto:02}:{segundo:02}"
        texto = fonte.render(texto_tempo, True, branco)
        window.blit(texto, (593,57))

def Restart(window):
    pygame.draw.rect(window, verde, (500, 525, 150, 50))
    palavra_f = fonte.render('Restart', True, preto)
    window.blit(palavra_f, (530, 540))

def Linha(tabuleiro, y):
    linha_escolhida = tabuleiro[y]
    return linha_escolhida

def Coluna(tabuleiro, x):
    coluna_escolhida = []
    for n in range(8):
        coluna_escolhida.append(tabuleiro[n][x])
    return coluna_escolhida

def Quadrante(tabuleiro, x, y):
    quadrante = []
    if x >= 0 and x <= 2 and y >= 0 and y <= 2:
        quadrante.extend([tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2],
                          tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2],
                          tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]])
    elif x >= 3 and x <= 5 and y >= 0 and y <= 2:
        quadrante.extend([tabuleiro[0][3], tabuleiro[0][4], tabuleiro[0][5],
                          tabuleiro[1][3], tabuleiro[1][4], tabuleiro[1][5],
                          tabuleiro[2][3], tabuleiro[2][4], tabuleiro[2][5]])
    elif x >= 6 and x <= 8 and y >= 0 and y <= 2:
        quadrante.extend([tabuleiro[0][6], tabuleiro[0][7], tabuleiro[0][8],
                          tabuleiro[1][6], tabuleiro[1][7], tabuleiro[1][8],
                          tabuleiro[2][6], tabuleiro[2][7], tabuleiro[2][8]])
    elif x >= 0 and x <= 2 and y >= 3 and y <= 5:
        quadrante.extend([tabuleiro[3][0], tabuleiro[3][1], tabuleiro[3][2],
                          tabuleiro[4][0], tabuleiro[4][1], tabuleiro[4][2],
                          tabuleiro[5][0], tabuleiro[5][1], tabuleiro[5][2]])
    elif x >= 3 and x <= 5 and y >= 3 and y <= 5:
        quadrante.extend([tabuleiro[3][3], tabuleiro[3][4], tabuleiro[3][5],
                          tabuleiro[4][3], tabuleiro[4][4], tabuleiro[4][5],
                          tabuleiro[5][3], tabuleiro[5][4], tabuleiro[5][5]])
    elif x >= 6 and x <= 8 and y >= 3 and y <= 5:
        quadrante.extend([tabuleiro[3][6], tabuleiro[3][7], tabuleiro[3][8],
                          tabuleiro[4][6], tabuleiro[4][7], tabuleiro[4][8],
                          tabuleiro[5][6], tabuleiro[5][7], tabuleiro[5][8]])
    elif x >= 0 and x <= 2 and y >= 6 and y <= 8:
        quadrante.extend([tabuleiro[6][0], tabuleiro[6][1], tabuleiro[6][2],
                          tabuleiro[7][0], tabuleiro[7][1], tabuleiro[7][2],
                          tabuleiro[8][0], tabuleiro[8][1], tabuleiro[8][2]])
    elif x >= 3 and x <= 5 and y >= 6 and y <= 8:
        quadrante.extend([tabuleiro[6][3], tabuleiro[6][4], tabuleiro[6][5],
                          tabuleiro[7][3], tabuleiro[7][4], tabuleiro[7][5],
                          tabuleiro[8][3], tabuleiro[8][4], tabuleiro[8][5]])
    elif x >= 6 and x <= 8 and y >= 6 and y <= 8:
        quadrante.extend([tabuleiro[6][6], tabuleiro[6][7], tabuleiro[6][8],
                          tabuleiro[7][6], tabuleiro[7][7], tabuleiro[7][8],
                          tabuleiro[8][6], tabuleiro[8][7], tabuleiro[8][8]])
    return quadrante

def Preenchendo_Quadrantes(tabuleiro, x2, y2):
    quadrante_preenchido = True
    loop = 0
    try_count = 0
    numero = 1
    while quadrante_preenchido == True:
        #random.randint passa numeros aleatórios inteiros
        x = random.randint(x2, x2 + 2)
        y = random.randint(y2, y2 + 2)
        linha_escolhida = Linha(tabuleiro, y)
        coluna_escolhida = Coluna(tabuleiro, x)
        quadrante = Quadrante(tabuleiro, x, y)
        if tabuleiro[y][x] == 'n' and numero not in linha_escolhida and numero not in coluna_escolhida and numero not in quadrante:
            tabuleiro[y][x] = numero
            numero += 1
        loop += 1
        if loop == 50:
            tabuleiro[y2][x2] = 'n'
            tabuleiro[y2][x2 + 1] = 'n'
            tabuleiro[y2][x2 + 2] = 'n'
            tabuleiro[y2 + 1][x2] = 'n'
            tabuleiro[y2 + 1][x2 + 1] = 'n'
            tabuleiro[y2 + 1][x2 + 2] = 'n'
            tabuleiro[y2 + 2][x2] = 'n'
            tabuleiro[y2 + 2][x2 + 1] = 'n'
            tabuleiro[y2 + 2][x2 + 2] = 'n'
            loop = 0
            numero = 1
            try_count += 1
        if try_count == 10:
            break
        count = 0
        for n in range(9):
            if quadrante[n] != 'n':
                count += 1
        if count == 9:
            quadrante_preenchido = False
    return tabuleiro

def Reiniciando_Tabuleiro(tabuleiro):
    tabuleiro = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                 ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                 ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                 ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                 ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                 ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                 ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                 ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                 ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]
    return tabuleiro

def Esconder(tabuleiro, jogo, esconder):
    if esconder == True:
        for n in range(40): #Nível intermediário
            num_sorteado = True
            while num_sorteado == True:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                if jogo[y][x] == 'n':
                    jogo[y][x] = tabuleiro[y][x]
                    num_sorteado = False
        esconder = False
    return jogo, esconder 

def Gabarito(tabuleiro, tab_preenchido):
    while tab_preenchido == True:
        tabuleiro = Preenchendo_Quadrantes(tabuleiro, 0, 0)
        tabuleiro = Preenchendo_Quadrantes(tabuleiro, 3, 0)
        tabuleiro = Preenchendo_Quadrantes(tabuleiro, 6, 0)

        tabuleiro = Preenchendo_Quadrantes(tabuleiro, 0, 3)
        tabuleiro = Preenchendo_Quadrantes(tabuleiro, 3, 3)
        tabuleiro = Preenchendo_Quadrantes(tabuleiro, 6, 3)

        tabuleiro = Preenchendo_Quadrantes(tabuleiro, 0, 6)
        tabuleiro = Preenchendo_Quadrantes(tabuleiro, 3, 6)
        tabuleiro = Preenchendo_Quadrantes(tabuleiro, 6, 6)
        for nn in range(9):
            for n in range(9):
                if tabuleiro[nn][n] == 'n':
                    tabuleiro = Reiniciando_Tabuleiro(tabuleiro)

        inicio = 0
        for nn in range(9):
            for n in range(9):
                if tabuleiro[nn][n] != 'n':
                    inicio += 1
        
        if inicio == 81:
            tab_preenchido = False
    return tabuleiro, tab_preenchido

def Preenchendo(window, jogo):
    quadrado = 50
    ajuste = 50
    for nn in range(9):
        for n in range(9):
            if jogo[nn][n] != 'n':
                if jogo[nn][n] == 'X': #Erro
                    num_font = fonte.render(str(jogo[nn][n]), True, vermelho)
                    window.blit(num_font, (ajuste + 20 + n * quadrado, ajuste + 15 + nn * quadrado))

def Digitando(numero):
    try:
        numero = int(numero[1])
    except:
        numero = int(numero)
    return numero

def Check_Num_Digitado(window, tabuleiro, jogo, click_pos_x, click_pos_y, numero):
    global contador_erros
    x = click_pos_x
    y = click_pos_y
    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        if tabuleiro[y][x] == 'n' and jogo[y][x] == 'n' and numero != 0:
            jogo[y][x] = numero  
            tipo_de_numero[y][x] = 'usuario'
            numero = 0
        elif tabuleiro[y][x] == numero and jogo[y][x] == 'n' and numero != 0:
            jogo[y][x] = numero  
            tipo_de_numero[y][x] = 'usuario'
            numero = 0
        elif tabuleiro[y][x] != numero and jogo[y][x] == 'n' and numero != 0:
            jogo[y][x] = 'X'  
            contador_erros += 1
            numero = 0
        elif tabuleiro[y][x] == numero and jogo[y][x] == 'X' and numero != 0:
            jogo[y][x] = numero  
            tipo_de_numero[y][x] = 'usuario'
            numero = 0
    return jogo, numero

def Click_Botao_Restart(mouse_pos_x, mouse_pos_y, click_last_status, click, tab_preenchido, esconder, tabuleiro, jogo, tempo_inicio, cronometro_ativo):
    x = mouse_pos_x
    y = mouse_pos_y
    global tipo_de_numero
    global contador_erros
    global jogando
    # Verificando se o clique aconteceu na área do botão de restart
    if x >= 500 and x <= 650 and y >= 525 and y <= 575:
        if not click_last_status and click:  
            tab_preenchido = True
            esconder = True
            tabuleiro = Reiniciando_Tabuleiro(tabuleiro)
            jogo = Reiniciando_Tabuleiro(jogo)
            # Reinicia o temporizador e contador de erros
            tempo_inicio = time.time()
            contador_erros = 0
            jogando = True
            cronometro_ativo = True
            tipo_de_numero = [['n' for _ in range(9)] for _ in range(9)]

            # Marca o status de clique para evitar múltiplos cliques acidentais
            click_last_status = True  
    elif not click:  
        click_last_status = False
    
    return tab_preenchido, esconder, tabuleiro, jogo, tempo_inicio, click_last_status, cronometro_ativo

def Contar_Numeros_Abertos(jogo):
    contagem = {i: 0 for i  in range(1, 10)}
    for row in jogo:
        for celula in row:
            if celula != 'n' and celula != 'X':
                contagem[celula] += 1
    return contagem

def Exibir_Contagem(window, contagem):
    for i in range(1, 10):
        pygame.draw.rect(window, barra, (60 + (i - 1) * 50, 510, 30, 30)) 
        palavra_f = fonte.render(f'{i}', True, branco) 
        window.blit(palavra_f, (63 + (i - 1) * 50 + 5, 515))
        pygame.draw.rect(window, verde2, (60 + (i - 1) * 50, 550, 30, 30))
        palavra_f = fonte.render(f'{contagem[i]}', True, preto)
        window.blit(palavra_f, (63 + (i - 1) * 50 + 5, 555))

def preencher_usuario(i, j, numero):
    global contador_erros  
    if jogo[i][j] != numero: 
        contador_erros += 1 
    tipo_de_numero[i][j] = 'usuario' 
    jogo[i][j] = numero  

def desenhar_contador_erros(window, contador_erros):
    texto_erro = fonte.render(f'Erros: {contador_erros}', True, vermelho) 
    window.blit(texto_erro, (10, 10))

def Desenhar_Num(window, jogo):
    for i in range(9):
        for j in range(9):
            numero = jogo[i][j]
            if numero != 'n' and numero != 'X':  
                if tipo_de_numero[i][j] == 'usuario':  
                    cor_numero = bic  
                else:
                    cor_numero = preto  
                num_font = fonte.render(str(numero), True, cor_numero)
                window.blit(num_font, (50 + 20 + j * 50, 50 + 15 + i * 50)) 

def Tabuleiro_Completo(tabuleiro):
    for linha in tabuleiro:
        for celula in linha:
            if celula == 'n':
                return False
            if celula == 'X':
                return False
    return True

def Valida_Linha(tabuleiro):
    for linha in tabuleiro:
        if len(set(linha)) != 9:
            return False
    return True

def Valida_Coluna(tabuleiro):
    for col in range(9):
        coluna = [tabuleiro[linha][col] for linha in range(9)]
        if len(set(coluna)) != 9:
            return False
    return True

def Grade(tabuleiro):
    for i in range(3):
        for j in range(3):
            grade = []
            for x in range(3):
                for y in range(3):
                    grade.append(tabuleiro[i*3 + x][j*3 + y])
            if len(set(grade)) != 9:
                return False
    return True

def Checa_Vitoria(jogo):
    if Tabuleiro_Completo(jogo):  
        if Valida_Linha(jogo) and Valida_Coluna(jogo) and Grade(jogo):  
            return True
    return False

def Fim_de_Jogo(contador_erros, resultado_jogo):
    
    if contador_erros >= 5:        
        resultado_jogo = "GAME OVER!"
   
    return resultado_jogo


def Desenhar_Fim(window, resultado_jogo):
    pygame.draw.rect(window, branco, (0, 225, 675, 150))
    text_fim = pygame.font.SysFont('Courier', 70, bold=True)
    fim = text_fim.render(f'{resultado_jogo}', True, vermelho)
    window.blit(fim, (100, 250))

     # Desenhar o tempo decorrido
    tempo_str = f" {tempo_final // 60:02}:{tempo_final % 60:02}"
    tempo = fonte.render(tempo_str, True, branco)
    window.blit(tempo, (593, 57))

    pygame.display.flip()

def Exibir_Melhor_Tempo(window, menor_tempo):
    if menor_tempo == float('inf'):
        menor_tempo_str2 = " "
        menor_tempo_texto2 = fonte.render(menor_tempo_str2, True, preto)
        window.blit(menor_tempo_texto2, (515, 125))
    else:
        record = pygame.font.SysFont('Courier', 18, bold=True)
        minuto = menor_tempo // 60
        segundo = menor_tempo % 60
        menor_tempo_str = "Melhor tempo: "
        menor_tempo_texto = record.render(menor_tempo_str, True, vermelho)
        window.blit(menor_tempo_texto, (515, 100))  
        menor_tempo_str2 = f"{minuto:02}:{segundo:02}"
        menor_tempo_texto2 = record.render(menor_tempo_str2, True, preto)
        window.blit(menor_tempo_texto2, (515, 125))  
 

#Iniciando o jogo


pygame.display.set_caption("Sudoku - Juliane")
icon = pygame.image.load('favicon.ico')  
pygame.display.set_icon(icon)

gameLoop = True
clock = pygame.time.Clock()

tempo_inicio = time.time()
menor_tempo = float('inf') 

jogando = True

if __name__ == "__main__":
    while gameLoop:
        if jogando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False

                elif event.type == pygame.KEYDOWN:
                    numero = pygame.key.name(event.key)
                    if numero.isdigit() and 1 <= int(numero) <= 9: 
                         
                        if jogo[mouse_pos_y][mouse_pos_x] == 'n': 
                            preencher_usuario(mouse_pos_y, mouse_pos_x, numero) 
                
                if contador_erros >= 5:
                    jogando = False
            game_over = False
            tempo_final = 0

            if Checa_Vitoria(jogo):
                resultado_jogo = "VOCÊ VENCEU!"
                tempo_final = int(time.time() - tempo_inicio)
                if tempo_final < menor_tempo:
                    menor_tempo = tempo_final
                Desenhar_Fim(window, resultado_jogo)
                cronometro_ativo = False
                pygame.display.update()
                time.sleep(0.5)
                game_over = True
                jogando = False  # Termina o jogo quando o jogador vence

            if contador_erros >= 5:
                resultado_jogo = "GAME OVER!"
                tempo_final = int(time.time() - tempo_inicio)
                Desenhar_Fim(window, resultado_jogo)
                cronometro_ativo = False
                game_over = True
                jogando = False  # Termina o jogo quando o jogador atinge 5 erros
            
            if cronometro_ativo:
                tempo_decorrido = int(time.time() - tempo_inicio)
                Cronometro(window, tempo_decorrido)

            mouse = pygame.mouse.get_pos()
            mouse_pos_x = mouse[0]
            mouse_pos_y = mouse[1]

            click = pygame.mouse.get_pressed()

                    
            tempo_decorrido = int(time.time() - tempo_inicio)
            Cronometro(window, tempo_decorrido)
            pygame.display.flip()
            clock.tick(30)
            Tabuleiro_Hover(window, mouse_pos_x, mouse_pos_y) 
            click_pos_x, click_pos_y = Celula(window, mouse_pos_x, mouse_pos_y, click_last_status, click[0], 
                                            click_pos_x, click_pos_y) 
            Desenhar_Num(window, jogo)
            desenhar_contador_erros(window, contador_erros)
            contagem = Contar_Numeros_Abertos(jogo)
            Exibir_Contagem(window, contagem)
            Grafico(window)
            Indice(window) 
            tabuleiro, tab_preenchido = Gabarito(tabuleiro, tab_preenchido)
            jogo, esconder = Esconder(tabuleiro, jogo, esconder)
            Preenchendo(window, jogo)
            numero = Digitando(numero)   
            jogo, numero = Check_Num_Digitado(window, tabuleiro, jogo, click_pos_x, click_pos_y, numero)
            tab_preenchido, esconder, tabuleiro, jogo, tempo_inicio, click_last_status, cronometro_ativo = Click_Botao_Restart(mouse_pos_x, mouse_pos_y, click_last_status, click[0], tab_preenchido, esconder, tabuleiro, jogo, tempo_inicio, cronometro_ativo)
            Restart(window)  
            tempo_decorrido = int(time.time() - tempo_inicio) if not game_over else tempo_decorrido
            Exibir_Melhor_Tempo(window, menor_tempo)            
            
            if click[0] == True:
                click_last_status = True

            else:
                click_last_status = False

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False
                    
            mouse = pygame.mouse.get_pos()
            mouse_pos_x = mouse[0]
            mouse_pos_y = mouse[1]
            tempo_decorrido = int(time.time() - tempo_inicio)
            Cronometro(window, tempo_decorrido)
            if Checa_Vitoria(tabuleiro):
                Fim_de_Jogo(contador_erros, resultado_jogo)
            click = pygame.mouse.get_pressed()
            pygame.display.flip()
            clock.tick(30)
            Tabuleiro_Hover(window, mouse_pos_x, mouse_pos_y) 
            click_pos_x, click_pos_y = Celula(window, mouse_pos_x, mouse_pos_y, click_last_status, click[0], 
                                            click_pos_x, click_pos_y) 
            Desenhar_Num(window, jogo)
            desenhar_contador_erros(window, contador_erros)
            contagem = Contar_Numeros_Abertos(jogo)
            Exibir_Contagem(window, contagem)
            Grafico(window)
            Indice(window) 
            tabuleiro, tab_preenchido = Gabarito(tabuleiro, tab_preenchido)
            jogo, esconder = Esconder(tabuleiro, jogo, esconder)
            jogo, numero = Check_Num_Digitado(window, tabuleiro, jogo, click_pos_x, click_pos_y, numero)
            Desenhar_Fim(window, resultado_jogo)
            tab_preenchido, esconder, tabuleiro, jogo, tempo_inicio, click_last_status, cronometro_ativo = Click_Botao_Restart(mouse_pos_x, mouse_pos_y, click_last_status, click[0], tab_preenchido, esconder, tabuleiro, jogo, tempo_inicio, cronometro_ativo)
            Restart(window)   
            tempo_decorrido = int(time.time() - tempo_inicio) if not game_over else tempo_decorrido
            Exibir_Melhor_Tempo(window, menor_tempo)
        pygame.display.update()

# ---X----Lista de afazeres---X---


# dicionar um Record 