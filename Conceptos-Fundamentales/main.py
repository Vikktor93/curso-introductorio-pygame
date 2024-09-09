import pygame

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ejemplo con pygame.draw")

# Color de fondo
background_color = (0, 0, 0)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pintar el fondo
    screen.fill(background_color)

    # Formas geométricas
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)  # Círculo rojo
    pygame.draw.rect(screen, (0, 255, 0), (150, 200, 100, 50))  # Rectángulo verde
    pygame.draw.line(screen, (0, 0, 255), (100, 100), (700, 100), 5)  # Línea azul
    
    # Triángulo
    triangle_points = [(400, 100), (350, 200), (450, 200)]  # Tres puntos del triángulo
    pygame.draw.polygon(screen, (255, 255, 0), triangle_points)  # Triángulo amarillo

    # Actualizar la pantalla
    pygame.display.update()

# Cerrar Pygame
pygame.quit()
