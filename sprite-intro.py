#credits to Clear Code for the tutorial
import pygame, sys, os, random as rd

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1000,800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Introduction")

class Target(pygame.sprite.Sprite): #target class, inherits from Crosshair
    def __init__(self, x, y, path):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x,y))
        self.pew = pygame.mixer.Sound(os.path.join("art", "pew.wav"))
        self.pew.set_volume(0.2) #lower volume to not blow my eardrums
    
    def update(self):
        for t in target_group:
            if t.rect.collidepoint(pygame.mouse.get_pos()):
                t.remove(target_group)
        self.pew.play()

class GameState():
    def __init__(self):
        self.state = "intro"

    def intro(self):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAIT) #set cursor to waiting animation
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "main_game"
        
        screen.blit(ready, (WIDTH/2-ready.get_width()/2, HEIGHT/2-ready.get_height()/2))
    
    def main_game(self):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR) #set cursor to default crosshair
        target_group.draw(screen)
        

    def state_manager(self):
        if self.state == "intro":
            self.intro()
        else:
            self.main_game()

game_state = GameState()

#target stuff
target_group = pygame.sprite.Group()
for target in range(30):
    target = Target(rd.randrange(0,WIDTH), rd.randrange(0,HEIGHT), os.path.join("art", "target.png"))
    while pygame.sprite.spritecollideany(target, target_group):
        target = Target(rd.randrange(0,WIDTH), rd.randrange(0,HEIGHT), os.path.join("art", "target.png"))
    target_group.add(target)

#images
background = pygame.image.load(os.path.join("art", "background.png"))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

ready = pygame.image.load(os.path.join("art", "ready.png"))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            target.update() #pew

    screen.blit(background, (0,0)) #display background
    game_state.state_manager()
    pygame.display.flip()
    clock.tick(60)