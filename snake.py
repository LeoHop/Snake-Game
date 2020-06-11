import pygame, sys, random
"""
I was able to write much of the code represented here 
by using the documentation for pygame (https://www.pygame.org/docs/).
Also tutorials on pygame and its relation to "snake" were very helpful (https://www.pygame.org/project-Snake+in+35+lines-818-.html) 
"""
"""
i noticed that maany oty=her programs for "snake" used varribales such as "snake_head" and "snake_margin"
"""
pygame.init()

# w = 2000
# h = 1000
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)      #defining all of my varriables
red = (255,0,0) 

snakeWidth = 15
snakeHeight = 15

snakeMargin = 3

snakeHead = [250,250] 

redBlock = pygame.image.load('redSquare.jpg') 

xChange = snakeWidth + snakeMargin
yChange = 0


end = 1

score = 0


snakePosition = [[250,250],[240,250],[230,250]] 

redBlockPosition = [random.randrange(1,50)*10,random.randrange(1,50)*10]
 


# snakePosition.insert(0,list(snakeHead))
# snakePosition.pop()

 
screen = pygame.display.set_mode((800, 600))

screen.fill(black)
pygame.display.update()

print("Hello and welcome to snake!")
print("You will control the snake by using the arrow keys")
print("Your first move cannot be going left")
print("You must navigate over to the block withought touching yourself and without touching the boundries")
print("When you 'eat' a block your score will increase by 1")
print("Have Fun!!!")
#how to draw a rectangle
# block = pygame.draw.rect(screen,blue,pygame.Rect(200,150,100,50))
def showSnake(snakePosition):

    for position in snakePosition:
        pygame.draw.rect(screen,red,pygame.Rect(position[0],position[1],10,10))
        # pygame.draw.rect(screen,black,pygame.Rect(position[-1]))
 
def showRedBlock(screen,redBlockPosition, redBlock):
    screen.blit(redBlock,(redBlockPosition[0], redBlockPosition[1]))


def hitWall(snakeHead):
    if snakeHead[0]>=500 or snakeHead[0]<0 or snakeHead[1]>=500 or snakeHead[1]<0:
        end = 2
        return 1
    else: 
        return 0

def hitSnake(snakePosition):                                                            #Creating all of my functions to be used later.
    snakeHead = snakePosition[0]
    if snakeHead in snakePosition[1:]:
        end = 2
        return 1
    else:
        return 0
score = 0

def hitRedBlock(redBlockPosition, score):
    redBlockPosition = [random.randrange(1,50)*10,random.randrange(1,50)*10]
    score += 1
    return redBlockPosition, score
 



clock = pygame.time.Clock()   #adjusting the framerate of my game
clock.tick(100)



pygame.display.set_caption("Snake")  #naming my screen


keyDirection = 0
keyPress = 0        #naming more varriables that i will need in the code below
remove = None
 
while end == 1:  #infanit loop until broken
    xChange = 0
    yChange = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = 2   #Ending the loop


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # and keyPress != 1:
                keyDirection = 0
                xChange = (snakeHeight + snakeMargin) * -1
                yChange = 0
            elif event.key == pygame.K_RIGHT: # and keyPress != 0:
                keyDirection = 1
                xChange = (snakeHeight + snakeMargin)
                yChange = 0
            elif event.key == pygame.K_UP: # and keyPress != 2:
                keyDirection = 3                                        #this is all of the code for arrow keys and if they are pushed
                xChange = 0
                yChange = (snakeHeight + snakeMargin) * -1
            elif event.key == pygame.K_DOWN: # and keyPress != 3:
                keyDirection = 2
                xChange = 0
                yChange = (snakeHeight + snakeMargin)
                    #I soucred https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed to help with this code
            if keyDirection == 1:
                snakeHead[0] += 10
            elif keyDirection == 0:
                snakeHead[0] -= 10
            elif keyDirection == 2:                 #this is the code that tells the snake how to move based on the arrow key pressing
                snakeHead[1] += 10
            elif keyDirection == 3:
                snakeHead[1] -= 10
            else:
                pass
             
            snakePosition.insert(0,list(snakeHead))
         
            pygame.draw.rect(screen,black,pygame.Rect(snakePosition[-1][0],snakePosition[-1][1],10,10))
            remove = snakePosition.pop()                #making the snake look as though its moving. instead of the snake constantly growing, it will move at all times with the same amount of blocks
            #https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed

        
    


    #update all the drawing
    # block = block.move(xChange, yChange)
    showSnake(snakePosition)
    showRedBlock(screen, redBlockPosition, redBlock)        #showing the snake and red block
    if hitWall(snakeHead):
        snakePosition.clear()
        screen.fill(black)
        pygame.display.update()
        print("game over!!!!!")
        print("Your score was:", score)
        break
        print("Your score was:", score)         #code for ending the program if you hit yourself or a wall
    elif hitSnake(snakePosition):
        snakePosition.clear()
        screen.fill(black)
        pygame.display.update()
        print("game over!!!!!")
        print("Your score was:", score)
        break
    if snakeHead == redBlockPosition:
        redBlockPosition, score = hitRedBlock(redBlockPosition, score)      #code for if you score
        snakePosition.append(remove)



        

    hitRedBlock(redBlockPosition, score)
    pygame.display.update()




 
        


