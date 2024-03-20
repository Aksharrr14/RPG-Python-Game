import pygame
from sprites import *
import sys
from config import *
# Create your views here.
class Game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock=pygame.time.Clock()
        self.font=pygame.font.Font('arial.ttf', 32)
        self.running=True
        
        self.character_spritesheet=Spritesheet('./img/character.png')
        self.terrain_spritesheet=Spritesheet('./img/terrain.png')
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.bear_spritesheet=Spritesheet('./img/singlebeerchoota.png')
        self.door_spritesheet=Spritesheet('./img/singledoorchoota.png')
        self.doors = pygame.sprite.LayeredUpdates()
        self.bear=pygame.sprite.LayeredUpdates()
        self.witch_spritesheet=Spritesheet('./img/singlewitchchoota.png')
        self.witch=pygame.sprite.LayeredUpdates()
        self.intro_background=pygame.image.load('./img/Gameintroscreen.png')
        self.player=Player(self, 0, 0)
        self.all_sprites.add(self.player)
        self.go_background=pygame.image.load('./img/gameoverscreenbig.png')
        self.winner_background=pygame.image.load('./img/winnerphotobig.png')

    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column =="B":
                    Block(self, j, i)
                if column=="D":
                    Door(self,self.player,j,i)
                if column=="A":
                    Bear(self,self.player,j,i)
                if column=="W":
                    Witch(self,self.player,j,i)
                if column=="P":
                    Player(self, j, i)
                

    def new(self):
        #a new game starts
        self.createTilemap()
        self.playing =True
        self.all_sprites=pygame.sprite.LayeredUpdates()  #Its a object that is going to contain all the sprites in our game
        #Its going to contain our character, its going to contain all the walls, bear
        #So this will help us to update them all at once
        self.blocks=pygame.sprite.LayeredUpdates()
        self.doors=pygame.sprite.LayeredUpdates()
        self.gold=pygame.sprite.LayeredUpdates()
        self.bear=pygame.sprite.LayeredUpdates()
        self.cthulu=pygame.sprite.LayeredUpdates()
        self.createTilemap()


    def events(self):
        #game loop events 
        for event in pygame.event.get():   #Will get every single event that is going to happen in pygame and we will iterate over that list
            if event.type ==pygame.QUIT:
                self.playing=False
                self.running=False         #pygame.quit is when we press the cross button, constantly checking if we press this button
    



    def update(self):
        #game loop updates
        door_hits = pygame.sprite.spritecollide(self.player, self.doors, False)
        witch_hits=pygame.sprite.spritecollide(self.player, self.witch,False)
        if door_hits:
            for door in door_hits:
                door.interact()  # Show the dropdown menu and update player position
        if witch_hits:
            for witch in witch_hits:
                witch.interact()          #Interacts with the witch
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    
        
        


    def draw(self):
        #game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
        



    def main(self):
        #game loop
        while self.playing:
            self.events()   #Will see our key press method(any event)
            self.update()   #Will update the game to make sure it isnt just a static image
            self.draw()     #And draw is going to display all the sprites onto our screen 
            
        self.running=False


    def game_over(self,custom_text=None):
        if custom_text:
            text=self.font.render(custom_text,True,WHITE)
        else:
            text= self.font.render('Game Over:You are dead',True,WHITE)

        text_rect=text.get_rect(center=(WIN_WIDTH/2,WIN_HEIGHT/3))

        restart_button=Button(840, WIN_HEIGHT-200,150,50,WHITE,RED,'RESTART',32)
        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running =False

            mouse_pos=pygame.mouse.get_pos()
            mouse_pressed=pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()

            self.screen.blit(self.go_background, (0,0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image,restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def winner(self,custom_text=None):
        if custom_text:
            text=self.font.render(custom_text,True,WHITE)
        else:
            text= self.font.render('Winner',True,WHITE)

        text_rect=text.get_rect(center=(WIN_WIDTH/2,WIN_HEIGHT/3))

        restart_button=Button(840, WIN_HEIGHT-200,150,50,WHITE,RED,'RESTART',32)
        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running =False

            mouse_pos=pygame.mouse.get_pos()
            mouse_pressed=pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()

            self.screen.blit(self.winner_background, (0,0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image,restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()





    def intro_screen(self):
       intro= True
       title=self.font.render('Best Game Ever',True,WHITE)
       title_rect = title.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2)) 
       credit_text = self.font.render('Developer of the game: Akshar Bhatnagar', True, WHITE)
       credit_rect = credit_text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT - 200))
      
       thanks_text=self.font.render('Special Thanks to: Vikas sharma    Rajat Sharma    Kumar Shantanu    Dhiraj Talwar',True,WHITE)
       thanks_rect= thanks_text.get_rect(center=(WIN_WIDTH//2, WIN_HEIGHT-100))
       play_button = Button(WIN_WIDTH // 2 - 50, WIN_HEIGHT // 2 + 50, 100, 50, WHITE, BLACK, 'Play', 32)  # Centering the button
       print("Game Started")
       

       while intro:
        # Setup an event loop now
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                self.running = False

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        #Checking if play button has been pressed
        if play_button.is_pressed(mouse_pos, mouse_pressed):
            intro=False
        self.screen.blit(self.intro_background, (0,0))
        self.screen.blit(title, title_rect)
        self.screen.blit(play_button.image, play_button.rect)
        self.screen.blit(credit_text,credit_rect)
        self.screen.blit(thanks_text,thanks_rect)
        self.clock.tick(FPS)
        pygame.display.update()
        

g=Game()
g.intro_screen() # As soon as you will run this file it is going to create a game object and it is going to run the intro screen method
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()

