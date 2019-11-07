import pygame
screen = pygame.display.set_mode((1000, 800))
clock=pygame.time.Clock()
import random
#1
'''running = True
x = 1
g = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.circle(screen, (0, g, 0), (320, 240), 50)
    pygame.display.update()
    g += x
    clock.tick(60)
    if g>=255 or g<=0:
        x=x*-1'''

#2
'''running= True
r_1=2
r_2=2
r_3=2
r_4=2
r_5=2
x_1=1
x_2=2
x_3=3
x_4=4
x_5=5
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (50, 240), r_1)
    pygame.draw.circle(screen, (255, 255, 255), (150, 240), r_2)
    pygame.draw.circle(screen, (255, 255, 255), (250, 240), r_3)
    pygame.draw.circle(screen, (255, 255, 255), (350, 240), r_4)
    pygame.draw.circle(screen, (255, 255, 255), (450, 240), r_5)
    pygame.display.update()
    r_1+=x_1
    r_2+=x_2
    r_3+=x_3
    r_4+=x_4
    r_5+=x_5
    clock.tick(60)
    if r_1<=2 or r_1>=50:
        x_1=x_1*-1
    if r_2<=2 or r_2>=50:
        x_2=x_2*-1
    if r_3<=2 or r_3>=50:
        x_3=x_3*-1
    if r_4<=2 or r_4>=50:
        x_4=x_4*-1
    if r_5<=2 or r_5>=50:
        x_5=x_5*-1'''

#3
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(300, 30, -10):
        a=random.randint(0,255)
        b=random.randint(0,255)
        c=random.randint(0,255)
        pygame.draw.circle(screen, (a, b, c), (500, 400), i)
        pygame.draw.circle(screen, (0, 0, 0), (500, 400), i-10)
    pygame.display.update()
    clock.tick(60)
