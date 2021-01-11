#Yuelin Liu
#101154473

import pygame,sys

pygame.init()

#provide instructions for users if they need
instruction = input("Do you need any instructions? ")
if instruction.lower() == "yes":
    print("input the file names for background image and ghost image")
    print("give the x and y co-ordinates of the ghost")
    print("when the co-ordinates are valid")
    print("the ghost with semi-transparency effect")
    print("will be put on the background image")

#get the filenames for the ghost image and the background image
bg = input("What is the name for the background image? ")
gh = input("What is the name for the ghost image? ")

#display the background image
#load background image and ghost image
bg_surface = pygame.image.load(bg)
gh_surface = pygame.image.load(gh)
#get the size of background image and ghost image
(bg_w, bg_h) = bg_surface.get_rect().size
(gh_w, gh_h) = gh_surface.get_rect().size
#set the screen with the same size as background image
screen = pygame.display.set_mode((bg_w,bg_h))
#put the background image on the screen
screen.blit(bg_surface,(0,0))
pygame.display.update()


#ask the users for the x and y co-ordinates
cox = int(input("Give the x-coordinate of the ghost"))
coy = int(input("GIve the y-coordinate of the ghost"))
#co-ordinates cannot be negative or outside the background image
#because we need to center the ghost,x and y co-ordinates represent
#the centre of the ghost
while cox < (gh_w / 2) or cox > (bg_w - (gh_w / 2)) or coy < (gh_h / 2) or coy > (bg_h - (gh_h / 2)):
    print("coordinates are invalid")
    print("coodinates cannot be negative or outside the background image")
    cox = int(input("Give the x-coordinate of the ghost "))
    coy = int(input("GIve the y-coordinate of the ghost "))

#put the ghost image on the background image   
#check each of pixels form ghost image
for x in range(gh_w):
    for y in range(gh_h):
        #get the colour of each pixels from ghost image
        (gh_r,gh_g,gh_b,gh_) = gh_surface.get_at((x,y))
        #if the colour of pixels from ghost image is not green
        if (gh_r,gh_g,gh_b) != (0,255,0):
            #get the colour of corresponding pixels in the background image
            (bg_r,bg_g,bg_b,bg_) = bg_surface.get_at((int(cox+x-gh_w/2),int(coy+y-gh_h/2)))
            #average the rgb value from the ghost and background image
            #set the new colour of the pixel in the background image
            bg_surface.set_at((int(cox+x-gh_w/2),int(coy+y-gh_h/2)),((gh_r+bg_r)/2,(gh_g+bg_g)/2,(gh_b+bg_g)/2))

#put the new background image on the screen
screen.blit(bg_surface,(0,0))

#leave the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
