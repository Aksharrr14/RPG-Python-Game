WIN_WIDTH =1850
WIN_HEIGHT=1080
TILESIZE=32
FPS=60
PLAYER_SPEED=4

GROUND_LAYER=1
PLAYER_LAYER=6
BEAR_LAYER=4
DOOR_LAYER=3
BLOCK_LAYER=2
WITCH_LAYER=5
 #So the ground layer is drawn first and the player get drawn on top of that
RED=(255, 0 ,0)
DARK_BLUE=(0,19,49)
BLACK=(0,0,0)
BLUE=(0, 0, 255)
WHITE=(255,255,255)
tilemap=[
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B..................D.....................................B',
    'B..................BBBB..BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B..................BBBB..BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B..................BBBB..................................B',
    'B..................B..B..................................B',
    'B..................B..B......BBBBBBBBBBBBB...............B',
    'B..................B..B....BB.............B..............B',
    'B..................B..B...B...BBBBBBBBBBB..B.............B',
    'B..................B..B..B...B...........B..B............B',
    'B..................B..B..B..B..B.BBB.B..B...B............B',
    'B..................B..B...B..B..B.D.B.B..B...B...........B',
    'B..................B...B...B..B......B..B...B............B',
    'B..................B....B...B..BBBBBB..B...B.............B',
    'B..................B.....B...B........B...B..............B',
    'B..................B......B...BBBBBBBB...B...............B',
    'B..................B.......B............B................B',
    'B..................B........BBBBBBBBBBBB.................B',
    'B..................B.....................................B',
    'B..................B.....................................B',
    'B..................B..............BBBBBBBBBBBB...........B',
    'B..................B..............B..........B...........B',
    'BB.D.BB...B........B..............B..........B...........B',
    'BBB.BBB...B........B..............B....BBB...B...........B',
    'BB...BB...B........B..............B....BBB...B...........B',
    'BB...BB...B........BBBBBBBBBBBBBBBB..BBBB..D.BBBBBBBBBBBBB',
    'BB.....A..BBBBBBBBBBBBBBBBBBBBBBBBB.....W....BBBBBBBBBBBBB',
    'BB.........D.......................D.....................B',
    'BB.....................P.................................B',
    'BBBBBBBBBBBBBBBBBBBBB.....BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
]