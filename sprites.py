import pygame
from config import *
import math 
import random
import sys



class Spritesheet:
    def __init__(self, file):
        self.sheet=pygame.image.load(file).convert()

    def get_sprite(self, x,y,width,height):
        sprite=pygame.Surface([width,height])
        sprite.blit(self.sheet, (0,0),(x,y,width,height))
        sprite.set_colorkey(BLACK)
        return sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x , y):               #To set x coordinate and y coordinate to appear on the screen
        self.game=game
        self._layer=PLAYER_LAYER
#This self._layer here is like we have we pygame.sprite.layeredupdates by setting this layer we can tell pygame in what layer of this screen we want the sprite to appear we might say that the grass 
#of the game is going to be at the bottom then the rocks and then the player over top so the player will be drawn
#above everything.
        self.groups=self.game.all_sprites #here we are basically adding in the player to the all sprites group 
#and we are able to access the all sprites group because we are going to pass in the game as an object
        pygame.sprite.Sprite.__init__(self, self.groups)  #calling the init method for the inherited class
        self.x=x*TILESIZE
        self.y=y*TILESIZE
        self.width=TILESIZE
        self.height=TILESIZE
        self.x_change=0
        self.y_change=0
        self.facing='down'
        self.animation_loop=1
        # image_to_load=pygame.image.load("./img/single.png")

        self.image=self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
        # self.image.blit(image_to_load,(0,0))
        # self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y

    def update(self):
        self.movement()
        self.animate()
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y +=self.y_change
        self.collide_blocks('y')
        self.x_change=0
        self.y_change=0

    def movement(self):
        keys=pygame.key.get_pressed()          #List of key that is pressed your keyboard
        if keys[pygame.K_LEFT]:
            # for sprite in self.game.all_sprites:
            #     sprite.rect.x += PLAYER_SPEED   
            self.x_change -=PLAYER_SPEED        #To move left we are going to move from the left axis(so take the value)
            self.facing='left'
        if keys[pygame.K_RIGHT]:
            # for sprite in self.game.all_sprites:
            #     sprite.rect.x -= PLAYER_SPEED
            self.x_change +=PLAYER_SPEED
            self.facing='right'
        if keys[pygame.K_UP]:
            # for sprite in self.game.all_sprites:
            #     sprite.rect.y += PLAYER_SPEED
            self.y_change -=PLAYER_SPEED
            self.facing='up'
        if keys[pygame.K_DOWN]:
            # for sprite in self.game.all_sprites:
            #     sprite.rect.y -= PLAYER_SPEED
            self.y_change +=PLAYER_SPEED
            self.facing='down'

    def collide_blocks(self,direction):
        if direction=="x":
            hits=pygame.sprite.spritecollide(self, self.game.blocks, False)     #We check if the rect of one sprite is inside another spirte
            # hits+=pygame.sprite.spritecollide(self,self.game.doors, False)
            if hits:   #Checking if player moves left or right
                if self.x_change > 0:           #Which means moving right
                    self.rect.x =hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x =hits[0].rect.right 

            door_hits= pygame.sprite.spritecollide(self,self.game.doors, False)
            if door_hits:
                for door in door_hits:
                    door.interact()

            witch_hits=pygame.sprite.spritecollide(self,self.game.witch,False)
            if witch_hits:
                for witch in witch_hits:
                    witch.interact()

            bear_hits=pygame.sprite.spritecollide(self, self.game.bear,False)
            if bear_hits:
                for bear in bear_hits:
                    bear.interact()

        if direction=="y":
            hits=pygame.sprite.spritecollide(self, self.game.blocks, False)
            # hits += pygame.sprite.spritecollide(self, self.game.doors, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y=hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y=hits[0].rect.bottom 

            door_hits = pygame.sprite.spritecollide(self, self.game.doors, False)
            if door_hits:
                # If colliding with a door, reset player's position and show dropdown menu
               for door in door_hits:
                door.interact()

            witch_hits = pygame.sprite.spritecollide(self, self.game.witch, False)
            if witch_hits:
                # If colliding with a witch, reset player's position and show dropdown menu
               for witch in witch_hits:
                witch.interact()

            bear_hits=pygame.sprite.spritecollide(self,self.game.bear, False)
            if bear_hits:
                #If colliding with a bear, reset player's position and show dropdown menu
                for bear in bear_hits:
                    bear.interact()

    def animate(self):
        down_animations=[self.game.character_spritesheet.get_sprite(3,2,self.width,self.height),
                         self.game.character_spritesheet.get_sprite(35,2,self.width,self.height),
                         self.game.character_spritesheet.get_sprite(68,2,self.width,self.height)] 
        up_animations=[self.game.character_spritesheet.get_sprite(3,34,self.width,self.height),
                       self.game.character_spritesheet.get_sprite(35,34,self.width,self.height),
                       self.game.character_spritesheet.get_sprite(68,34,self.width,self.height)]
        left_animations=[self.game.character_spritesheet.get_sprite(3,98,self.width,self.height),
                         self.game.character_spritesheet.get_sprite(35,98,self.width,self.height),
                         self.game.character_spritesheet.get_sprite(68,98,self.width,self.height) ]
        right_animations=[self.game.character_spritesheet.get_sprite(3,66,self.width,self.height),
                          self.game.character_spritesheet.get_sprite(35,66,self.width,self.height),
                          self.game.character_spritesheet.get_sprite(68,66,self.width,self.height)]   
        
        if self.facing=="down":
            if self.y_change==0:
                self.image=self.game.character_spritesheet.get_sprite(3,2,self.width,self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop +=0.1
                if self.animation_loop >= 3:
                    self.animation_loop=1

        if self.facing=="up":
            if self.y_change==0:
                self.image=self.game.character_spritesheet.get_sprite(3,34,self.width,self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop +=0.1
                if self.animation_loop >= 3:
                    self.animation_loop=1
        
        if self.facing=="left":
            if self.x_change==0:
                self.image=self.game.character_spritesheet.get_sprite(3,98,self.width,self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop +=0.1
                if self.animation_loop >= 3:
                    self.animation_loop=1

        if self.facing=="right":
            if self.x_change==0:
                self.image=self.game.character_spritesheet.get_sprite(3,66,self.width,self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop +=0.1
                if self.animation_loop >= 3:
                    self.animation_loop=1


class Block(pygame.sprite.Sprite):
    def __init__(self,game, x,y):
        self.game=game
        self._layer=BLOCK_LAYER
        self.groups=self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x=x*TILESIZE
        self.y=y*TILESIZE
        self.width=TILESIZE
        self.height=TILESIZE
        self.image=self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)
        # print("hello")
        self.rect= self.image.get_rect()
        self.rect.x= self.x 
        self.rect.y=self.y  

class Ground(pygame.sprite.Sprite):
    def __init__(self,game, x, y):
        self.game= game
        self._layer=GROUND_LAYER
        self.groups=self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x=x*TILESIZE
        self.y=y*TILESIZE
        self.width=TILESIZE
        self.height=TILESIZE
        self.image=self.game.terrain_spritesheet.get_sprite(64,352,self.width,self.height)
        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y

   
class Door(pygame.sprite.Sprite):
    def __init__(self, game, player,x, y, options=None):
        self.game=game
        self.player=player
        self._layer=DOOR_LAYER
        print("Player object received:",self.player)
        self.groups=self.game.all_sprites, self.game.doors
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x= x*TILESIZE
        self.y= y*TILESIZE
        self.width= 2*TILESIZE
        self.height=2*TILESIZE

        self.x_change=0
        self.y_change=0
        self.image=self.game.door_spritesheet.get_sprite(0,0,self.width,self.height)
        self.image.set_colorkey(BLACK)    #we remove the background black of the image


        self.rect= self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y
        self.options= options or []
    
    def interact(self):
        options=["Enter"]
        dropdown_menu=DropdownMenu(self.game.screen, options)
        choice=dropdown_menu.show()
        player_x=self.player.rect.x
        print(player_x)
        if choice=="Enter":
            print("Enter chosen")
            print("door coordinate x",self.rect.x)
            print("door coordinate y",self.rect.y)
            print("Window width",WIN_WIDTH)
            if self.rect.x == 352:                                           #left door coordinate
                self.rect.x = self.rect.right+(self.rect.width)
                self.rect.y = self.rect.centery - self.rect.height // 2
                print("this is running")

            elif self.rect.x == 480:
                self.rect.x= 365
            elif self.rect.x== 1005:
                self.rect.x = self.rect.left+(self.rect.width*1.8)
                self.rect.y = self.rect.centery - self.rect.height // 2
            elif self.rect.x==1120:                                          #right door coordinate
                self.rect.x = self.rect.left-(self.rect.width*1.8)
                self.rect.y = self.rect.centery - self.rect.height // 2
                print("No this is running")
            elif self.rect.y==868 or self.rect.x==760:
                self.rect.x==760
                self.rect.y=1000
            elif self.rect.y==736:
                self.rect.y=840
            elif self.rect.x==608:
                print("kinda last door")
                self.rect.x=515
                self.rect.y=64
            elif self.rect.x==1088:
                print("last door or gold room")
                gold_options=["Less than or equal to 50", "More than 50"]
                gold_dropdown=DropdownMenu(self.game.screen, gold_options)
                gold_choice= gold_dropdown.show()

                if gold_choice=="More than 50":
                    self.game.game_over("You are greeedy!")
                else:
                    self.game.winner("Congratulations you won! You are not greedy")


class DropdownMenu:
    def __init__(self, screen, options):
        self.screen = screen
        self.options = options
        self.font = pygame.font.SysFont(None, 30)
        self.option_rects = []
        self.selected_option = None

    def show(self):
        option_height = 40
        total_height = option_height * len(self.options)
        start_y = (WIN_HEIGHT - total_height) // 2

        for option in self.options:
            text_surface = self.font.render(option, True, WHITE)
            text_rect = text_surface.get_rect(center=(WIN_WIDTH // 2, start_y))
            self.option_rects.append((text_rect, option))
            start_y += option_height

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for rect, option in self.option_rects:
                        if rect.collidepoint(pygame.mouse.get_pos()):
                            self.selected_option = option
                            running = False

            self.screen.fill(BLACK)
            for rect, _ in self.option_rects:
                pygame.draw.rect(self.screen, DARK_BLUE, rect, border_radius=5)
            for rect, option in self.option_rects:
                self.screen.blit(self.font.render(option, True, WHITE), rect)
            pygame.display.flip()

        return self.selected_option



class Bear(pygame.sprite.Sprite):
    def __init__(self,game,player, x, y,options=None):
        self.game=game
        self.player=player
        self._layer=BEAR_LAYER
        print("Player received in Bear:",self.player)
        self.groups=self.game.all_sprites, self.game.bear
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x=x*TILESIZE
        self.y=y*TILESIZE
        self.width=2.9*TILESIZE
        self.height=2.9*TILESIZE

        self.x_change=0
        self.y_change=0
        self.image=self.game.bear_spritesheet.get_sprite(0,0,self.width,self.height)

        self.image.set_colorkey(WHITE)    #we remove the background black of the image
        #self.image.set_colorkey(BLACK) 
        self.rect= self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y
        self.options=options or []

    def interact(self):
        options=["Take honey", "Taunt bear"]
        dropdown_menu=DropdownMenu(self.game.screen, options)
        choice=dropdown_menu.show()
        player_x=self.player.rect.x
        print(player_x)
        print("bear x coordinate:",self.rect.x)
        print("bear y coordinate:",self.rect.y)
        if choice=="Take honey":
            print("Dead")
            self.game.game_over('The bear looks at you then slaps your face off')
        elif choice=="Taunt bear":
            print("Move the bear")
            # Gradually move the bear to y-coordinate 890
            target_y = 750
            if self.rect.y < target_y:
                while self.rect.y < target_y:
                    self.rect.y += 1 
                    self.rect.x=648 # Adjust the step size as needed
                    # You might need to add some delay here to control the speed of movement
                    # For example, you could use pygame's clock.tick() method
                    pygame.time.delay(10)  # Delay in milliseconds
            elif self.rect.y > target_y:
                while self.rect.y > target_y:
                    self.rect.y -= 1  # Adjust the step size as needed
                    pygame.time.delay(10)  # Delay in milliseconds
                

    # def update(self):
    #     self.rect.x += self.x_change
    #     self.rect.y += self.y_change

    #     self.x_change=0
    #     self.y_change=0


class Witch(pygame.sprite.Sprite):
    def __init__(self,game,player, x, y,options=None ):
        self.player=player
        self.game=game
        self._layer=WITCH_LAYER
        print("Player received in witch:",self.player)
        self.groups=self.game.all_sprites, self.game.witch
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x= x*TILESIZE
        self.y= y*TILESIZE
        self.width= 2.9*TILESIZE
        self.height=2.9*TILESIZE

        self.x_change=0
        self.y_change=0
        self.image=self.game.witch_spritesheet.get_sprite(0,0,self.width,self.height)
        self.image.set_colorkey(WHITE)    #we remove the background black of the image

        self.rect= self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y
        self.options=options or []

    def interact(self):
        options=["Eat your own Head", "Flee for life"]
        dropdown_menu=DropdownMenu(self.game.screen, options)
        choice=dropdown_menu.show()
        player_x=self.player.rect.x
        print(player_x)
        if choice=="Eat your own Head":
            print("Dead")
            self.game.game_over('Well, that was tasty!')
        elif choice=="Flee for life":
            print("Game restart")
            self.game.new()
            self.game.main()

    # def update(self):
    #     self.rect.x += self.x_change
    #     self.rect.y += self.y_change

    #     self.x_change=0
    #     self.y_change=0




#Creating a button now
class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font= pygame.font.Font('arial.ttf', fontsize)
        self.content=content
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.fg=fg
        self.bg=bg
        self.image=pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect=self.image.get_rect()
        
        self.rect.x=self.x
        self.rect.y=self.y

        self.text=self.font.render(self.content, True, self.fg)
        self.text_rect= self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False
