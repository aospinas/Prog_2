import pygame
import sys

# Definir constantes para la ventana
WIDTH = 800
HEIGHT = 600
FPS = 60

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (200, 200, 0)
GRAY = (200, 200, 200)
ORANGE = (255,175,0)
# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mi juego con Pygame para la recuperación de Prog 2")
clock = pygame.time.Clock()

# Cargar imagen de fondo
fondo = pygame.image.load("OIG.jpg").convert()

font = pygame.font.Font(None, 35)

# Clase Nodo para la lista simplemente enlazada
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Clase LinkedList para la lista simplemente enlazada
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __len__(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    # Funcion insertar nodo al inicio
    def insert_node_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Funcion insertar nodo al final
    def insert_node_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node


    # Funcion insertar nodo por posicion
    def insert_node_at_position(self, data, position):
        if position <= 0:
            self.insert_node_at_beginning(data)
        else:
            count = 0
            current_node = self.head
            while current_node.next and count < position - 1:
                current_node = current_node.next
                count += 1
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

    # Funcion para eliminar el primer nodo 
    def delete_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    # Funcion para eliminar el ultimo  nodo 
    def delete_last_node(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    # Funcion para imprimir elementos de la lista 
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # Funcion para obtener el tamaño de la lista
    def tamaño_lista(self):
        contador = 0
        current_node = self.head
        while current_node is not None:
            contador += 1
            current_node = current_node.next
        return contador

# Crear instancia de la lista simplemente enlazada
my_list = LinkedList()

# Función para dibujar el footer
def draw_footer():
    font = pygame.font.SysFont(None, 24)
    footer_surface = pygame.Surface((WIDTH, 40))
    footer_surface.fill(GRAY)
    footer_rect = footer_surface.get_rect()
    footer_rect.topleft = (0, HEIGHT - 600)
    screen.blit(footer_surface, footer_rect)

    # Dibujar el nombre del desarrollador en el footer
    text = font.render("Desarrollado por: Andrés Ospina Silva", True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = footer_rect.center
    screen.blit(text, text_rect)

# Funcion para dibujar botones
def draw_buttons():
    font = pygame.font.SysFont(None, 24)

    # Botón para agregar al inicio
    button_surface = pygame.Surface((150, 30))
    button_surface.fill(GREEN)
    button_rect = button_surface.get_rect()
    button_rect.center = (WIDTH // 4, HEIGHT - 100)
    screen.blit(button_surface, button_rect)
    text = font.render("Agregar al inicio", True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = button_rect.center
    screen.blit(text, text_rect)

    # Botón para agregar al final
    button_surface = pygame.Surface((150, 30))
    button_surface.fill(BLUE)
    button_rect = button_surface.get_rect()
    button_rect.center = (WIDTH // 2, HEIGHT - 100)
    screen.blit(button_surface, button_rect)
    text = font.render("Agregar al final", True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = button_rect.center
    screen.blit(text, text_rect)

    # Botón para agregar en posición específica
    button_surface = pygame.Surface((170, 30))
    button_surface.fill(RED)
    button_rect = button_surface.get_rect()
    button_rect.center = (3 * WIDTH // 4, HEIGHT - 100)
    screen.blit(button_surface, button_rect)
    text = font.render("Agregar en posición", True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = button_rect.center
    screen.blit(text, text_rect)

    # Botón para eliminar el primer elemento
    button_surface = pygame.Surface((150, 30))
    button_surface.fill(RED)
    button_rect = button_surface.get_rect()
    button_rect.center = (3 * WIDTH // 4, HEIGHT - 50)
    screen.blit(button_surface, button_rect)
    text = font.render("Eliminar el primero", True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = button_rect.center
    screen.blit(text, text_rect)

    # Botón para eliminar el último elemento
    button_surface = pygame.Surface((150, 30))
    button_surface.fill(YELLOW)
    button_rect = button_surface.get_rect()
    button_rect.center = (WIDTH // 4, HEIGHT - 50)
    screen.blit(button_surface, button_rect)
    text = font.render("Eliminar el último", True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = button_rect.center
    screen.blit(text, text_rect)

# Funcion para boton de tamaño
def draw_size_button():
    font = pygame.font.SysFont(None, 24)

    # Botón para obtener el tamaño de la lista
    button_surface = pygame.Surface((150, 30))
    button_surface.fill(ORANGE)
    button_rect = button_surface.get_rect()
    button_rect.center = (WIDTH // 2, HEIGHT - 50)
    screen.blit(button_surface, button_rect)
    text = font.render("Obtener tamaño", True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = button_rect.center
    screen.blit(text, text_rect)

# Función para abrir un cuadro de entrada de texto
def open_input_box(prompt="Ingrese un número:"):
    input_box_rect = pygame.Rect(250, HEIGHT // 2, WIDTH - 500, 30)
    color_inactive = BLACK
    color_active = RED
    font = pygame.font.Font(None, 24)
    input_box_active = True
    input_text = ""

    while input_box_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text:
                        return input_text
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill(WHITE)
        screen.blit(fondo, (0, 0))
        draw_footer()
        draw_buttons()

        txt_surface = font.render(input_text, True, color_inactive)
        pygame.draw.rect(screen, color_active if input_box_active else color_inactive, input_box_rect, 2)
        screen.blit(txt_surface, (input_box_rect.x + 5, input_box_rect.y + 5))

        # Color de Ingrese un numero:
        prompt_text = font.render(prompt, True, BLACK)
        prompt_rect = prompt_text.get_rect()
        prompt_rect.center = (WIDTH // 2, HEIGHT // 2 - 100)
        screen.blit(prompt_text, prompt_rect)

        pygame.display.flip()
        clock.tick(FPS)

# Funcion para dibujar el boton de salir
def draw_exit_button():
    font = pygame.font.SysFont(None, 24)

    # Botón de salida
    button_surface = pygame.Surface((100, 30))
    button_surface.fill(RED)
    button_rect = button_surface.get_rect()
    button_rect.center = (WIDTH - 70, HEIGHT - 30)
    screen.blit(button_surface, button_rect)
    text = font.render("Salir", True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = button_rect.center
    screen.blit(text, text_rect)

# Funcion para mostrar el tamaño de la lista
def show_list_size():
    size = len(my_list)
    font = pygame.font.SysFont(None, 24)
    text = font.render("Tamaño de la lista: " + str(size), True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT - 150)
    screen.blit(text, text_rect)

# Loop principal del juego
running = True
while running:
    # Procesamiento de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botón izquierdo del ratón
                mouse_pos = pygame.mouse.get_pos()
                # Verificar si se hizo clic en el botón "Agregar al principio"
                if (
                    WIDTH // 4 - 100 <= mouse_pos[0] <= WIDTH // 4 + 100
                    and HEIGHT - 130 <= mouse_pos[1] <= HEIGHT - 70
                ):
                    input_text = open_input_box()
                    my_list.insert_node_at_beginning(input_text)

                # Verificar si se hizo clic en el botón "Agregar al final"
                if (
                    WIDTH // 2 - 100 <= mouse_pos[0] <= WIDTH // 2 + 100
                    and HEIGHT - 130 <= mouse_pos[1] <= HEIGHT - 70
                ):
                    input_text = open_input_box()
                    my_list.insert_node_at_end(input_text)

                # Verificar si se hizo clic en el botón "Agregar en posición específica"
                if (
                    3 * WIDTH // 4 - 100 <= mouse_pos[0] <= 3 * WIDTH // 4 + 100
                    and HEIGHT - 130 <= mouse_pos[1] <= HEIGHT - 70
                ):
                    input_text = open_input_box("Ingrese un número:")
                    position_text = open_input_box("Ingrese la posición:")
                    try:
                        number = int(input_text)
                        position = int(position_text)
                        my_list.insert_node_at_position(number, position)
                    except ValueError:
                        print("¡Error! Por favor, ingrese un número válido.")

                # Verificar si se hizo clic en el botón "Eliminar el primero"
                if (
                    3 * WIDTH // 4 - 100 <= mouse_pos[0] <= 3 * WIDTH // 4 + 100
                    and HEIGHT - 80 <= mouse_pos[1] <= HEIGHT - 20
                ):
                    my_list.delete_first_node()

                # Verificar si se hizo clic en el botón "Eliminar el último"
                if (
                    WIDTH // 4 - 100 <= mouse_pos[0] <= WIDTH // 4 + 100
                    and HEIGHT - 80 <= mouse_pos[1] <= HEIGHT - 20
                ):
                    my_list.delete_last_node()

                # Verificar si se hizo clic en el botón "Salir"
                if (
                    WIDTH - 120 <= mouse_pos[0] <= WIDTH - 20
                    and HEIGHT - 60 <= mouse_pos[1] <= HEIGHT - 30
                ):
                    running = False
                # Verificar si se hizo clic en el botón "Obtener tamaño de la lista"
                if (
                    WIDTH // 2 - 100 <= mouse_pos[0] <= WIDTH // 2 + 100
                    and HEIGHT - 80 <= mouse_pos[1] <= HEIGHT - 20
                ):
                    show_list_size()
                    size = len(my_list)
                    print("Tamaño de la lista:", size)
    # Actualizar

    # Dibujar
    screen.fill(WHITE)
    screen.blit(fondo, (0, 0))
    draw_footer()
    draw_buttons()
    draw_size_button()
    draw_exit_button()

    # Mostrar la lista simplemente enlazada en la pantalla
    #current_node = my_list.head
    #y = 50
    #while current_node:
        #font = pygame.font.SysFont(None, 24)
        #text = font.render(str(current_node.data), True, WHITE)  # Cambiar el color aquí
        #screen.blit(text, (50, y))
        #y += 30
        #current_node = current_node.next

    #pygame.display.flip()
    #clock.tick(FPS)
    #Mostrar el tamaño de la lista actualizada en tiempo real
    tamaño = my_list.tamaño_lista()
    text_surface = font.render(" Tamaño Lista: " + str(tamaño), True, BLACK)
    screen.blit(text_surface, (570, 50))

    current_node = my_list.head
    num_nodes = 0
    node_height = 30  # Altura de cada nodo en píxeles
    top_margin = 50  # Margen superior en píxeles

    # Calcular la cantidad de elementos en la lista
    while current_node:
        num_nodes += 1
        current_node = current_node.next

    # Calcular la posición inicial en el eje x
    start_x = (WIDTH - (num_nodes * 30)) // 2

    # Reiniciar el puntero al inicio de la lista
    current_node = my_list.head
    x = start_x
    y = top_margin  # Posición vertical desde el margen superior

    while current_node:
        font = pygame.font.SysFont(None, 26)
        text = font.render(str(current_node.data), True, BLACK)
        text_rect = text.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text, text_rect)

        # Aumentar la posición en el eje x
        x += 20

        current_node = current_node.next


    pygame.display.flip()
    clock.tick(FPS)

# Salir del juego
pygame.quit()
sys.exit()