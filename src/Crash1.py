import pygame
import time
import pyautogui
import math
import os
display_width,display_height=1700,750
width,height=pyautogui.size()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((width-display_width)/2,(height-display_height)/2)
pygame.init()
pygame.display.set_caption("Crash1")
icon_program=pygame.image.load(r"assets\image\extraLife.png")
pygame.display.set_icon(icon_program)
game_display=pygame.display.set_mode((display_width,display_height))
#CenterForm
#---------------------------------------------------------------------
#Sounds
background_sound=pygame.mixer.Sound(r"assets\audio\BackgroundTheme.ogg")
rotate_crash_sound=pygame.mixer.Sound(r"assets\audio\CrashSpin.wav")
crash_jump_sound=pygame.mixer.Sound(r"assets\audio\CrashHop.wav")
grassfootstep_sound=pygame.mixer.Sound(r"assets\audio\grassFootStep.wav")
wumpahit_sound=pygame.mixer.Sound(r"assets\audio\WumpaHit.wav")
jumpenemydead_sound=pygame.mixer.Sound(r"assets\audio\CrateBounce.wav")
applepicked_sound=pygame.mixer.Sound(r"assets\audio\ApplePicked.wav")
crystalpicked_sound=pygame.mixer.Sound(r"assets\audio\CrystalPicked.wav")
tntcountdown_sound=pygame.mixer.Sound(r"assets\audio\TntCountdown.wav")
deathangel_sound=pygame.mixer.Sound(r"assets\audio\DeathAngel.wav")
tntexplosion_sound=pygame.mixer.Sound(r"assets\audio\TntExplosion.wav")
burned_sound=pygame.mixer.Sound(r"assets\audio\Burned.wav")
ironcratehit_sound=pygame.mixer.Sound(r"assets\audio\IronCrateHit.wav")
gecko_sound=pygame.mixer.Sound(r"assets\audio\gecko.wav")
lizard_sound=pygame.mixer.Sound(r"assets\audio\lizard.wav")
palnetattack_sounnd=pygame.mixer.Sound(r"assets\audio\birdAttack.wav")
blowgun_sound=pygame.mixer.Sound(r"assets\audio\blowGun.wav")
game_over_sound=pygame.mixer.Sound(r"assets\audio\gameOver.wav")
win_sound=pygame.mixer.Sound(r"assets\audio\AkuAkuPicked2.wav")
#-----------------globalVarible--------------------------------------
crash=pygame.image.load(r"assets\image\crash_normal.png")
wooden2=pygame.image.load(r"assets\image\wooden2.png")
selector=pygame.image.load(r"assets\image\Selector.png")
arrow_menu_01=pygame.image.load(r"assets\image\arrowMenu_01.png")
arrow_menu_02=pygame.image.load(r"assets\image\arrowMenu_02.png")
board=pygame.image.load(r"assets\image\board.png")
backgroud_main=pygame.image.load(r"assets\image\bg_crash.png")
crashLabel=pygame.image.load(r"assets\image\crashLabel.png")
game_over_background=pygame.image.load(r"assets\image\gameOverBackground.png")
bushdark2=pygame.image.load(r"assets\image\BushDark2.png")
#ALPHA NUMBERIC
latter_a=pygame.image.load(r"assets\image\Letter_A.png")
latter_b=pygame.image.load(r"assets\image\Letter_B.png")
latter_c=pygame.image.load(r"assets\image\Letter_C.png")
latter_d=pygame.image.load(r"assets\image\Letter_D.png")
latter_e=pygame.image.load(r"assets\image\Letter_E.png")
latter_f=pygame.image.load(r"assets\image\Letter_F.png")
latter_g=pygame.image.load(r"assets\image\Letter_G.png")
latter_h=pygame.image.load(r"assets\image\Letter_H.png")
latter_i=pygame.image.load(r"assets\image\Letter_I.png")
latter_j=pygame.image.load(r"assets\image\Letter_J.png")
latter_k=pygame.image.load(r"assets\image\Letter_K.png")
latter_l=pygame.image.load(r"assets\image\Letter_L.png")
latter_m=pygame.image.load(r"assets\image\Letter_M.png")
latter_n=pygame.image.load(r"assets\image\Letter_N.png")
latter_o=pygame.image.load(r"assets\image\Letter_O.png")
latter_p=pygame.image.load(r"assets\image\Letter_P.png")
latter_q=pygame.image.load(r"assets\image\Letter_Q.png")
latter_r=pygame.image.load(r"assets\image\Letter_R.png")
latter_s=pygame.image.load(r"assets\image\Letter_S.png")
latter_t=pygame.image.load(r"assets\image\Letter_T.png")
latter_u=pygame.image.load(r"assets\image\Letter_U.png")
latter_v=pygame.image.load(r"assets\image\Letter_V.png")
latter_w=pygame.image.load(r"assets\image\Letter_W.png")
latter_x=pygame.image.load(r"assets\image\Letter_X.png")
latter_y=pygame.image.load(r"assets\image\Letter_Y.png")
latter_z=pygame.image.load(r"assets\image\Letter_Z.png")
#-------------------------AddEarth-----------------------
earth_1=pygame.image.load(r"assets\image\earth_1.png")
earth_2=pygame.image.load(r"assets\image\earth_2.png")
earth_3=pygame.image.load(r"assets\image\earth_3.png")
earth_4=pygame.image.load(r"assets\image\earth_4.png")
earth_5=pygame.image.load(r"assets\image\earth_5.png")
earth_6=pygame.image.load(r"assets\image\earth_6.png")
earth_7=pygame.image.load(r"assets\image\earth_7.png")
earth_8=pygame.image.load(r"assets\image\earth_8.png")
earth_9=pygame.image.load(r"assets\image\earth_9.png")
earth_10=pygame.image.load(r"assets\image\earth_10.png")
earth_12=pygame.image.load(r"assets\image\earth_12.png")
earth_11=pygame.image.load(r"assets\image\earth_11.png")
earth_13=pygame.image.load(r"assets\image\earth_13.png")
#-----------------------------------------------
earth_1_dark=pygame.image.load(r"assets\image\earth_1_dark.png")
earth_2_dark=pygame.image.load(r"assets\image\earth_2_dark.png")
earth_3_dark=pygame.image.load(r"assets\image\earth_3_dark.png")
earth_4_dark=pygame.image.load(r"assets\image\earth_4_dark.png")
earth_5_dark=pygame.image.load(r"assets\image\earth_5_dark.png")
earth_6_dark=pygame.image.load(r"assets\image\earth_6_dark.png")
earth_7_dark=pygame.image.load(r"assets\image\earth_7_dark.png")
earth_8_dark=pygame.image.load(r"assets\image\earth_8_dark.png")
earth_9_dark=pygame.image.load(r"assets\image\earth_9_dark.png")
earth_10_dark=pygame.image.load(r"assets\image\earth_10_dark.png")
#------------------------------------------------------------
trapThorns=pygame.image.load(r"assets\image\trapThorns.png")
DeadBush=pygame.image.load(r"assets\image\DeadBush.png")
iron_cate=pygame.image.load(r"assets\image\ironCrate.png")
ArrowSign=pygame.image.load(r"assets\image\ArrowSign.png")
#Color------------------------------
jewels_01=pygame.image.load(r"assets\image\jewels_01.png")
jewels_02=pygame.image.load(r"assets\image\jewels_02.png")
black=(0,0,0)
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = black
FONT = pygame.font.Font(r"assets\Fonts\arial.ttf", 15)
white=(255,255,255)
blue=(0,0,255)
color_btn_go=(66, 103, 178)
color_btn_exit=(255,40,40)
color_btn_go_enter=(45, 103, 178)
color_btn_exit_enter=(230, 40, 40)
#--------------------------------------------------------------------
def set_character(character,x,y):
    game_display.blit(character,(x,y))
#--------------------------------------------------------------------
#Add Intersect Method
def intersect(x_object1,y_object1,object1_width,x_object2,y_object2,object2_width):
    if y_object1<y_object2+object2_width and not(y_object1<y_object2-object2_width):
        if x_object1>x_object2 and  x_object1<x_object2+object2_width or x_object1+object1_width>x_object2 and x_object1+object1_width<x_object2+object2_width:
            return True
    return False
#--------------------------------------------------------------------
def button(text,x,y,w,h,ic,ac,action,txt_user="",txt_pass="",alpha=0):
    mouse_position=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse_position[0]>x and y+h>mouse_position[1]>y:
        pygame.draw.rect(game_display,ac,(x,y,w,h),alpha)
        if click[0]==1 and action=="p":
            start_game()
        elif click[0]==1 and action=="q":
            pygame.quit()
            quit()
        elif click[0]==1 and action=="qmenu":
            main()
    else:
        pygame.draw.rect(game_display,ic,(x,y,w,h),alpha)
    smallText=pygame.font.Font(r"assets\Fonts\arial.ttf",20)
    TextSurf,TextRect=text_objects(text,smallText,white)
    TextRect.center=((x+(w/2)),(y+(h/2)))
    game_display.blit(TextSurf,TextRect)
#--------------------------------------------------------------------
def text_objects(text,font,color):
    textSurface=font.render(text,True,color)
    return textSurface,textSurface.get_rect()
#--------------------------------------------------------------------
def crashed():
    text="Game Over"
    largeText=pygame.font.Font(r"assets\Fonts\arial.ttf",100)
    TextSurf,TextRect=text_objects(text,largeText,color_btn_exit_enter)
    TextRect.center=((display_width/2),(display_height/2))
    game_display.blit(TextSurf,TextRect)
    game_over_sound.play()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        button("Tryagain",740,100,100,50,color_btn_go,color_btn_go_enter,"p")
        button("Exit",860,100,100,50,color_btn_exit,color_btn_exit_enter,"qmenu")
        pygame.display.update()
def youwin():
    stop_all_sound()
    win_sound.play()
    text="You Win"
    largeText=pygame.font.Font(r"assets\Fonts\arial.ttf",100)
    TextSurf,TextRect=text_objects(text,largeText,color_btn_exit_enter)
    TextRect.center=((display_width/2),(display_height/2))
    game_display.blit(TextSurf,TextRect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        button("Play again",740,100,100,50,color_btn_go,color_btn_go_enter,"p")
        button("Exit",860,100,100,50,color_btn_exit,color_btn_exit_enter,"q")
        pygame.display.update()
def set_earth(earth_positionx,earth_positiony):
    #earth Level 1
    set_character(earth_1,earth_positionx,earth_positiony)
    for i in range(1,6):
        set_character(earth_2,earth_positionx+38*i,earth_positiony)
    set_character(earth_3,earth_positionx+228,earth_positiony)
    #earth Level 2
    set_character(earth_4,earth_positionx,earth_positiony+38)
    for i in range(1,6):
        set_character(earth_5,earth_positionx+38*i,earth_positiony+38)
    set_character(earth_6,earth_positionx+228,earth_positiony+38)
    #earth Level 3
    set_character(earth_4,earth_positionx,earth_positiony+77)
    for i in range(1,7):
        if i==6:
            set_character(earth_10,earth_positionx+38*i,earth_positiony+77)
        else:
            set_character(earth_5,earth_positionx+38*i,earth_positiony+77)
    set_character(earth_8,earth_positionx+266,earth_positiony+77)
    set_character(earth_3,earth_positionx+305,earth_positiony+77)
    #earth Level 4
    set_character(earth_4,earth_positionx,earth_positiony+110)
    for i in range(1,8):
        set_character(earth_5,earth_positionx+38*i,earth_positiony+110)
    set_character(earth_6,earth_positionx+305,earth_positiony+110)

    earth_positionx_right=(earth_positionx+500)
    #earth Level 1
    set_character(earth_1,earth_positionx_right,earth_positiony)
    for i in range(1,6):
        set_character(earth_2,earth_positionx_right+38*i,earth_positiony)
    set_character(earth_3,earth_positionx_right+228,earth_positiony)
    #earth Level 2
    set_character(earth_4,earth_positionx_right,earth_positiony+38)
    for i in range(1,6):
        set_character(earth_5,earth_positionx_right+38*i,earth_positiony+38)
    set_character(earth_6,earth_positionx_right+228,earth_positiony+38)
    #earth Level 3
    set_character(earth_7,earth_positionx_right-38,earth_positiony+77)
    set_character(earth_1,earth_positionx_right-75,earth_positiony+77)
    for i in range(1,7):
        if i==1:
            set_character(earth_9,(earth_positionx_right+38*i)-38,earth_positiony+77)
        else:
            set_character(earth_5,(earth_positionx_right+38*i)-38,earth_positiony+77)
    set_character(earth_6,earth_positionx_right+228,earth_positiony+77)
    #earth Level 4
    set_character(earth_4,earth_positionx_right-75,earth_positiony+110)
    for i in range(1,8):
        set_character(earth_5,(earth_positionx_right+38*i)-75,earth_positiony+110)
    set_character(earth_6,earth_positionx_right+228,earth_positiony+110)
    #----------------------------------------------------------------------------
    #earth Level 1
    earth_positionx_right_2=earth_positionx_right+330
    set_character(earth_1,earth_positionx_right_2,earth_positiony)
    for i in range(1,3):
        set_character(earth_2,earth_positionx_right_2+38*i,earth_positiony)
    set_character(earth_3,earth_positionx_right_2+100,earth_positiony)
    #earth Level 2
    set_character(earth_4,earth_positionx_right_2,earth_positiony+38)
    for i in range(1,3):
        set_character(earth_5,earth_positionx_right_2+38*i,earth_positiony+38)
    set_character(earth_6,earth_positionx_right_2+100,earth_positiony+38)
    #earth Leve 3
    set_character(earth_12,earth_positionx_right_2,earth_positiony+68)
    for i in range(1,3):
        set_character(earth_11,earth_positionx_right_2+38*i,earth_positiony+68)
    set_character(earth_13,earth_positionx_right_2+98,earth_positiony+68)
    #set Wll Type_2
    for i in range(1,4):
        earth_type2_inSkys=pygame.image.load(r"assets\image\earth_type1_inSky"+str(i)+".png")
        set_character(earth_type2_inSkys,(earth_positionx+300)+38*i,earth_positiony-100)
    for i in range(1,4):
        earth_type2_inSkys=pygame.image.load(r"assets\image\earth_type2_inSky"+str(i)+".png")
        set_character(earth_type2_inSkys,(earth_positionx_right_2+300)+38*i,earth_positiony-100)
    #set Wall Dark------------------------------------------------------------------------------------
    #earth Level 1
    earth_dark_posiyion_x=earth_positionx_right_2+200
    set_character(earth_1_dark,earth_dark_posiyion_x,earth_positiony)
    for i in range(1,6):
        set_character(earth_2_dark,earth_dark_posiyion_x+38*i,earth_positiony)
    set_character(earth_3_dark,earth_dark_posiyion_x+228,earth_positiony)
    #earth Level 2
    set_character(earth_4_dark,earth_dark_posiyion_x,earth_positiony+38)
    for i in range(1,6):
        set_character(earth_5_dark,earth_dark_posiyion_x+38*i,earth_positiony+38)
    set_character(earth_6_dark,earth_dark_posiyion_x+228,earth_positiony+38)
    #earth Level 3
    set_character(earth_4_dark,earth_dark_posiyion_x,earth_positiony+77)
    for i in range(1,7):
        if i==6:
            set_character(earth_10_dark,earth_dark_posiyion_x+38*i,earth_positiony+77)
        else:
            set_character(earth_5_dark,earth_dark_posiyion_x+38*i,earth_positiony+77)
    set_character(earth_8_dark,earth_dark_posiyion_x+266,earth_positiony+77)
    set_character(earth_3_dark,earth_dark_posiyion_x+305,earth_positiony+77)
    #earth Level 4
    set_character(earth_4_dark,earth_dark_posiyion_x,earth_positiony+110)
    for i in range(1,8):
        set_character(earth_5_dark,earth_dark_posiyion_x+38*i,earth_positiony+110)
    set_character(earth_6_dark,earth_dark_posiyion_x+305,earth_positiony+110)

    earth_positionx_right_dark=(earth_dark_posiyion_x+450)
    # #earth Level 1
    set_character(earth_1_dark,earth_positionx_right_dark,earth_positiony)
    for i in range(1,4):
        set_character(earth_2_dark,earth_positionx_right_dark+38*i,earth_positiony)
    set_character(earth_3_dark,earth_positionx_right_dark+150,earth_positiony)
    #earth Level 2
    set_character(earth_4_dark,earth_positionx_right_dark,earth_positiony+38)
    for i in range(1,4):
        set_character(earth_5_dark,earth_positionx_right_dark+38*i,earth_positiony+38)
    set_character(earth_6_dark,earth_positionx_right_dark+150,earth_positiony+38)
    #earth Level 3
    set_character(earth_7_dark,earth_positionx_right_dark-38,earth_positiony+77)
    set_character(earth_1_dark,earth_positionx_right_dark-75,earth_positiony+77)
    for i in range(1,5):
        if i==1:
            set_character(earth_9_dark,(earth_positionx_right_dark+38*i)-38,earth_positiony+77)
        else:
            set_character(earth_5_dark,(earth_positionx_right_dark+38*i)-38,earth_positiony+77)
    set_character(earth_6_dark,earth_positionx_right_dark+150,earth_positiony+77)
    #earth Level 4
    set_character(earth_4_dark,earth_positionx_right_dark-75,earth_positiony+110)
    for i in range(1,6):
        set_character(earth_5_dark,(earth_positionx_right_dark+38*i)-75,earth_positiony+110)
    set_character(earth_6_dark,earth_positionx_right_dark+150,earth_positiony+110)
#-----------------------------End Wall Right----------------------------------------------
def radian(d):
    return d*math.pi/180
def stop_all_sound():
    rotate_crash_sound.stop()
    crash_jump_sound.stop()
    grassfootstep_sound.stop()
    wumpahit_sound.stop()
    jumpenemydead_sound.stop()
    applepicked_sound.stop()
    crystalpicked_sound.stop()
    tntcountdown_sound.stop()
    deathangel_sound.stop()
    tntexplosion_sound.stop()
    burned_sound.stop()
    ironcratehit_sound.stop()
    gecko_sound.stop()
    lizard_sound.stop()
    palnetattack_sounnd.stop()
#-----------------------------------------------------------------------------------------
def main():
    stop_all_sound()
    background_sound.stop()
    background_sound.play(-1)
    inPage=True
    y_change_selector=500
    bg_positionx,bg_positiony=0,0
    while inPage:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    y_change_selector=600
                if event.key==pygame.K_UP:
                    y_change_selector=500
                if event.key==pygame.K_RETURN:
                    if y_change_selector==600:
                        pygame.quit()
                        quit()
                    elif y_change_selector==500:
                        inPage=False
                        start_game()
        set_character(backgroud_main,bg_positionx-1000,bg_positiony)
        set_character(backgroud_main,bg_positionx,bg_positiony)
        set_character(backgroud_main,bg_positionx+1000,0)
        set_character(backgroud_main,bg_positionx+2000,0)
        set_character(board,(display_width-880)/2,(display_height-775)/2)
        set_character(crashLabel,(display_width-400)/2,(display_height-300)/2)
        #alphanumberic
        #play
        set_character(latter_p,(display_width-830)/2,500)
        set_character(latter_l,(display_width-800)/2,500)
        set_character(latter_a,(display_width-750)/2,500)
        set_character(latter_y,(display_width-700)/2,500)
        #exit
        set_character(latter_e,(display_width-830)/2,600)
        set_character(latter_x,(display_width-790)/2,600)
        set_character(latter_i,(display_width-750)/2,600)
        set_character(latter_t,(display_width-700)/2,600)
        #selector
        selector_surf=pygame.transform.flip(selector,True,False)
        set_character(selector_surf,(display_width-900)/2,y_change_selector)
        pygame.display.update()
def start_game():
    stop_all_sound()
    background_sound.stop()
    background_sound.play(-1)
    #------------------------------
    apple_ychange_1,apple_ychange_2=(display_height*0.8)-19,(display_height*0.8)-19
    apple_ychange_3,apple_ychange_4,apple_ychange_5,apple_ychange_6,apple_ychange_7=(display_height*0.8)-10,(display_height*0.8)-10,(display_height*0.8)-10,(display_height*0.8)-10,(display_height*0.8)-10
    apple_ychange_8=((display_height*0.8)+30)
    apple_ychange_9=((display_height*0.8)+50)
    apple_ychange_10=((display_height*0.8)+30)
    apple_ychange_11=(display_height*0.8)-19
    apple_ychange_12=(display_height*0.8)-19
    apple_ychange_13=(display_height*0.8)-19
    #crystal
    crystal_ychange_1,crystal_ychange_2,crystal_ychange_3,crystal_ychange_4=635,635,635,635
    #Jewels
    jewels_1_ychange,jewels_2_ychange=450,450
    #tnt
    smoke_puff_1_step_step=0
    smoke_puff_2_step_step=0
    crash_explosion_step=0
    smoke_puff_ychange=(display_height*0.8)-20
    smoke_puff_ychange2=(display_height*0.8)-20
    #------------------------------
    x_change_bg=0
    x_change_crash=0
    move=5
    die_step=1
    planet_rotate=False
    #die compersion
    isdie=False
    #-------------------------
    run_step=1
    lizard_step=1
    planet_step=1
    gecko_flip=True
    burnd_step=0
    step_reversed=1
    tnt_one_fire=False
    tnt2_one_fire=False
    fire_tnt_1=False
    fire_tnt_2=False
    is_reversed=False
    runaway_1=False
    runaway_2=False
    planet_xchange=1210
    fps=pygame.time.Clock()
    MOVE=3
    die_angele_step=0
    lizard_xchange=415
    gunman_xchange=1480
    gecko_xchange=620
    box=pygame.image.load(r"assets\image\box1.png")
    box1=pygame.image.load(r"assets\image\box1.png")
    #------------------------AddHome------------------------------
    house=pygame.image.load(r"assets\image\house.png")
    #box
    #coco
    coco=pygame.image.load(r"assets\image\cocoBandicoot.png")
    #wooden
    wooden=pygame.image.load(r"assets\image\wooden4.png")
    #liane
    liane=pygame.image.load(r"assets\image\liane1.png")
    #Trees
    tree_1=pygame.image.load(r"assets\image\tree_1.png")
    tree_2=pygame.image.load(r"assets\image\tree_2.png")
    tree_3=pygame.image.load(r"assets\image\tree_3.png")
    tree_4=pygame.image.load(r"assets\image\DeadTree.png")
    #gecko
    gecko=pygame.image.load(r"assets\image\gecko1.png")
    #bridge
    bridge=pygame.image.load(r"assets\image\bridge.png")
    fiori2=pygame.image.load(r"assets\image\fiori2.png")
    Stone=pygame.image.load(r"assets\image\Stone.png")
    blow_gun_bullet=pygame.image.load(r"assets\image\blowGunBullet.png")
    #-------------------------------------------------------------
    radios=20
    is_run=False
    isRight=False
    is_down=False
    permision_jump=True
    down_step=1
    is_jump=False
    apple_count=1
    jump_step=1
    jump_run_step=1
    jump_type2=False
    lizard_rotate=False
    gecko_step=1
    gun_blow_xchange=1480
    teta,teta1=90,90
    MOVE_IRON=1
    gunman_step=1
    fire_step=1
    box1_step1=1
    dx,dy,dx1,dy1=0,0,0,0
    box_step=1
    global crash
    crystal_step=1
    tnt_1_step=4
    tnt_2_step=4
    tnt=pygame.image.load(r"assets\image\tnt.png")
    tnt2=pygame.image.load(r"assets\image\tnt.png")
    MOVE_lizard=3
    irontrap_positiony=0
    y_change_crash=(display_height*0.8)-45
    crash_positionx,crash_positiony=110,(display_height*0.8)
    bg_positionx,bg_positiony=0,0
    earth_positionx,earth_positiony=0,display_height*0.8
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    if not is_down:
                        grassfootstep_sound.play(-1)
                    x_change_bg=-move
                    x_change_crash=(move+2)
                    is_run=True
                    isRight=False
                elif event.key==pygame.K_LEFT:
                    if not is_down:
                        grassfootstep_sound.play(-1)
                    x_change_bg=move
                    x_change_crash=-(move+2)
                    is_run=True
                    isRight=True
                elif event.key==pygame.K_SPACE:
                    crash_jump_sound.play()
                    if permision_jump:
                        if is_run:
                            is_jump=False
                            jump_type2=True
                            if isRight:      
                                y_change_crash-=move**2*2
                                x_change_crash-=move*4
                                
                            else:
                                y_change_crash-=move**2 *2
                                x_change_crash=move*4
                                
                        else:
                            jump_type2=False
                            is_jump=True
                            y_change_crash-=move**2*2
                elif event.key==pygame.K_DOWN:
                    is_down=True
                    if isRight:
                        x_change_crash-=2
                    else:
                        x_change_crash=2
                elif event.key==pygame.K_RSHIFT:
                    is_reversed=True
                    rotate_crash_sound.play()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT or event.key==pygame.K_DOWN or event.key==pygame.K_SPACE or event.key==pygame.K_RSHIFT:
                    x_change_bg=0 
                    x_change_crash=0
                    is_run=False
                    is_down=False
                    is_reversed=False
                    step_reversed=1
                    grassfootstep_sound.stop()
                    down_step=1
                    if not is_jump:
                        crash=pygame.image.load(r"assets\image\crash_normal.png")
        if crash_positiony>=670 or crash_positiony>=602 and crash_positionx>=790 and crash_positionx<=1024:
            x_change_crash=0
        crash_positionx+=x_change_crash
        crash_positiony=y_change_crash
        bg_positionx+=x_change_bg
        if y_change_crash <=(display_height*0.8)-50 or ((crash_positionx>=253 and crash_positionx<=316 and  crash_positiony<=630)or(crash_positionx>=407 and crash_positionx<=466 and crash_positiony<=630)  or (crash_positionx>=755 and crash_positionx<=800 )or ((crash_positionx>=320 and crash_positionx<=406) and crash_positiony >=540) or ((crash_positionx>=755 and crash_positionx<=800)and crash_positiony>=560)or
        (crash_positionx>=1280 and crash_positionx<=1443 and  crash_positiony<=630)or(crash_positionx>=1407 and crash_positionx<=1466 and crash_positiony<=630)or(crash_positionx>=949 and crash_positionx<=998)or (crash_positiony>=682 or crash_positiony<=450)):
            permision_jump=False
            if not((crash_positiony>=457 and crash_positiony<=467)and ((crash_positionx>=320 and crash_positionx<=432)or(crash_positionx>=1140 and crash_positionx<=1266))) :
                y_change_crash+=10
                grassfootstep_sound.stop()
            else:
                crash=pygame.image.load(r"assets\image\crash_normal.png")
                permision_jump=True
                jump_step=1
                is_jump=False
                jump_type2=False
                jump_run_step=1
        else:
            if is_jump or jump_type2:
                grassfootstep_sound.play()
            crash=pygame.image.load(r"assets\image\crash_normal.png")
            permision_jump=True
            jump_step=1
            is_jump=False
            jump_type2=False
            jump_run_step=1
        if is_run:
            if run_step==8:
                run_step=1
            crash=pygame.image.load(r"assets\image\crash_run"+str(run_step)+".png")
            if pygame.time.get_ticks()%500>=1:
                run_step=run_step+1
        if is_reversed:
            if step_reversed==12:
                step_reversed=11
            crash=pygame.image.load(r"assets\image\reversed_"+str(step_reversed)+".png")
            if pygame.time.get_ticks()%500>=1:
                step_reversed=step_reversed+1
        if is_down:
            if down_step==4:
                down_step=3
            crash=pygame.image.load(r"assets\image\crash_hit"+str(down_step)+".png")
            if pygame.time.get_ticks()%500>=1:
                down_step=down_step+1
        if is_jump:
            if jump_step==4:
                jump_step=3
            crash=pygame.image.load(r"assets\image\crash_jump"+str(jump_step)+".png")
            if pygame.time.get_ticks()%500>=1:
                jump_step=jump_step+1
        if jump_type2:
            if jump_run_step==7:
                jump_run_step=6
            crash=pygame.image.load(r"assets\image\crash_down"+str(jump_run_step)+".png")
            if pygame.time.get_ticks()%500>=1:
                jump_run_step=jump_run_step+1
        #background
        set_character(backgroud_main,bg_positionx-1000,bg_positiony)
        set_character(backgroud_main,bg_positionx,bg_positiony)
        set_character(backgroud_main,bg_positionx+1000,0)
        set_character(backgroud_main,bg_positionx+2000,0)
        #bounds
        if intersect(crash_positionx,crash_positiony,20,earth_positionx+455,earth_positiony+38,20):
            grassfootstep_sound.stop()
            if is_jump:
                jumpenemydead_sound.play()
            crash_positiony-=25
            move=8
            if box_step==10:
                box_step=1
            box=pygame.image.load(r"assets\image\box"+str(box_step)+".png")
            if pygame.time.get_ticks()%500>=1:
                box_step=box_step+1
        else:
            box_step=1
            box=pygame.image.load(r"assets\image\box"+str(box_step)+".png")
            move=5
        if  intersect(crash_positionx,crash_positiony,20,210,earth_positiony-40,20):
            grassfootstep_sound.stop()
            if is_jump:
                jumpenemydead_sound.play()
            crash_positiony-=25
            move=10
            if box1_step1==10:
                box1_step1=1
            box1=pygame.image.load(r"assets\image\box"+str(box1_step1)+".png")
            if pygame.time.get_ticks()%500>=1:
                box1_step1=box1_step1+1  
        else:
            box1_step1=1
            box1=pygame.image.load(r"assets\image\box"+str(box1_step1)+".png")

        if intersect(crash_positionx,crash_positiony,48,earth_positionx+255,earth_positiony+55,31):
            grassfootstep_sound.stop()
            if is_jump:
                jumpenemydead_sound.play()
            crash_positiony-=20
            move=8                   
        if intersect(crash_positionx,crash_positiony,48,1465,earth_positiony+55,28):
            grassfootstep_sound.stop()
            if is_jump:
                jumpenemydead_sound.play()
            crash_positiony-=20
            move=8
        if intersect(crash_positionx,crash_positiony,41,1260,earth_positiony+55,31):
            grassfootstep_sound.stop()
            if is_jump:
                jumpenemydead_sound.play()
            crash_positiony-=20
            move=8
        if intersect(crash_positionx,crash_positiony,25,1075,earth_positiony-25,20):
            grassfootstep_sound.stop()
            if is_jump:
                jumpenemydead_sound.play()
            crash_positiony-=20
            move=10
        print(crash_positionx," ",crash_positiony)
        #-------------------------------------------------------------------------------------
        #hit_def
        #Apples
        if intersect(crash_positionx,crash_positiony,31,(180)-19*1,apple_ychange_1,31):
            apple_ychange_1=-1000
            applepicked_sound.play()
        elif intersect(crash_positionx,crash_positiony,31,(180)-19*0,apple_ychange_2,31):
            apple_ychange_2=-1000
            applepicked_sound.play()    
        elif intersect(crash_positionx,crash_positiony,31,(1420)-19*0,apple_ychange_3,31):
            apple_ychange_3=-1000
            applepicked_sound.play()
        elif intersect(crash_positionx,crash_positiony,31,(1420)-19*1,apple_ychange_4,31):
            apple_ychange_4=-1000
            applepicked_sound.play()
        elif intersect(crash_positionx,crash_positiony,31,(1420)-19*2,apple_ychange_5,31):
            apple_ychange_5=-1000
            applepicked_sound.play()
        elif intersect(crash_positionx,crash_positiony,31,(1420)-19*3,apple_ychange_6,31):
            apple_ychange_6=-1000
            applepicked_sound.play()
        elif intersect(crash_positionx,crash_positiony,31,(1420)-19*4,apple_ychange_7,31):
            apple_ychange_7=-1000
            applepicked_sound.play()

        elif intersect(crash_positionx,crash_positiony,31,(550)-19*0,apple_ychange_11,31):
            apple_ychange_11=-1000
            applepicked_sound.play()
        elif intersect(crash_positionx,crash_positiony,31,(550)-19*1,apple_ychange_12,31):
            apple_ychange_12=-1000
            applepicked_sound.play()
        elif intersect(crash_positionx,crash_positiony,31,(550)-19*2,apple_ychange_13,31):
            apple_ychange_13=-1000
            applepicked_sound.play()
        #crystall
        elif intersect(crash_positionx,crash_positiony,41,1460-30*1,crystal_ychange_1,31):
            crystal_ychange_1=-1000
            crystalpicked_sound.play()
        elif intersect(crash_positionx,crash_positiony,41,1460-30*2,crystal_ychange_2,31):
            crystal_ychange_2=-1000
            crystalpicked_sound.play()
        elif intersect(crash_positionx,crash_positiony,41,1460-30*3,crystal_ychange_3,31):
            crystal_ychange_3=-1000
            crystalpicked_sound.play()
        elif intersect(crash_positionx,crash_positiony,41,1460-30*4,crystal_ychange_4,31):
            crystal_ychange_4=-1000
            crystalpicked_sound.play()
            #tnt 2
        #-------------------------------------------------------------------------------------
        #jewels
        elif intersect(crash_positionx,crash_positiony,41,350,jewels_1_ychange,31):
            jewels_1_ychange=-1000
            crystalpicked_sound.play()
        elif intersect(crash_positionx,crash_positiony,41,1160,jewels_2_ychange,31):
            jewels_2_ychange=-1000
            crystalpicked_sound.play()
       #one
        if crash_positionx<253  and crash_positiony>=570:
            crash_positionx=253
            print("1--------------------")
        #tow t1
        if (crash_positionx<=729 and crash_positionx>=463 ) and crash_positiony>=570:
            crash_positionx=463
            crash_positiony=640
            print("2--------------------")
        #tow t2
        if (crash_positionx>=408 and crash_positionx<=463) and crash_positiony>640:
            crash_positiony=640
            print("3--------------------")
        #drop
        if crash_positionx>=404 and crash_positionx<=408:
            crash_positionx=404
        if crash_positionx>=309 and crash_positionx<=316 and crash_positiony>=570:
            crash_positionx=320
        #-----------------------------
        #type2
        #one
        if (crash_positionx<1280 and crash_positionx>=1250) and crash_positiony>=580:
            crash_positionx=1280
            print("One")
        # #tow t1
        if (crash_positionx>=1444 and crash_positionx<=1468 ) and crash_positiony>580:
            crash_positionx=1444
            print("Tow")
        #house
        set_character(house,0,(display_height*0.8)-120)
        #Trees
        set_character(tree_1,120,(display_height*0.8)-18)
        set_character(tree_2,80,(display_height*0.8)-280)
        set_character(tree_3,480,(display_height*0.8)-230)
        set_character(tree_4,780,(display_height*0.8)-180)
        #other char------------------
        set_character(fiori2,earth_positionx+1050,earth_positiony-60)
        set_character(Stone,earth_positionx+1120,earth_positiony-30)
        set_character(trapThorns,1110,earth_positiony)
        #irontrap
        if pygame.time.get_ticks()%1000>=1:
            irontrap_positiony=irontrap_positiony+MOVE_IRON
            if irontrap_positiony==30:
                MOVE_IRON=-MOVE_IRON
            elif irontrap_positiony==0:
                MOVE_IRON=-MOVE_IRON
            set_character(trapThorns,1110,earth_positiony-irontrap_positiony)
        if intersect(crash_positionx,crash_positiony,30,1110,earth_positiony-irontrap_positiony,30):
            isdie=True
            ironcratehit_sound.play()
        #planet
        if pygame.time.get_ticks()%1000>=1:
            planet_step+=1
            if planet_step==17:
                planet_step=1
                planet_rotate=not planet_rotate
            planet=pygame.image.load(r"assets\image\planet_"+str(planet_step)+".png")
            planets=pygame.transform.flip(planet,planet_rotate,False)
            set_character(planets,planet_xchange,(display_height*0.8)-165)
        if intersect(crash_positionx,crash_positiony,30,planet_xchange,(display_height*0.8)-165,30):
            if is_reversed or is_down:
                planet_xchange+=1900
                jumpenemydead_sound.play()
            else:
                isdie=True
                palnetattack_sounnd.play()
        if pygame.time.get_ticks()%1000>=1:
            fire_step+=1
            if fire_step==17:
                fire_step=1
            fire=pygame.image.load(r"assets\image\fire_"+str(fire_step)+".png")
            t1=teta
            dx1=radios*math.cos(radian(t1))
            dy1=radios*math.sin(radian(t1))
            teta1-=8
            t=(t1+360/3)%360
            if teta1==-1:
                teta1=359
            set_character(fire,980+dx1,(display_height*0.8)-20-dy1)
            if intersect(crash_positionx,crash_positiony,30,980+dx1,(display_height*0.8)-20-dy1,30):
                isdie=True
                stop_all_sound()
                burned_sound.play()
        #dx,dy=circel(100)
        if pygame.time.get_ticks()%1000>=1:
            lizard_step+=1
            lizard_xchange+=MOVE_lizard
            if lizard_step==19:
                lizard_step=1
                lizard_rotate=not lizard_rotate
            if lizard_xchange==418:
                MOVE_lizard=-MOVE_lizard
            if lizard_xchange==364:
                MOVE_lizard=-MOVE_lizard
            lizard=pygame.image.load(r"assets\image\lizard_"+str(lizard_step)+".png")
            lizards=pygame.transform.flip(lizard,lizard_rotate,False)
            set_character(lizards,lizard_xchange,(display_height*0.8)-150)
        set_character(bushdark2,1225,(display_height*0.8)-125)
        set_earth(earth_positionx,earth_positiony)
        #deadBush
        set_character(DeadBush,1540,(display_height*0.8)-55)
        #arrow
        set_character(ArrowSign,1040,(display_height*0.8)-40)  
        #gunman
        if pygame.time.get_ticks()%1000>=1:
            gunman_step+=1
            if gunman_step==17:
                gunman_step=1
            fire=pygame.image.load(r"assets\image\gunman_"+str(gunman_step)+".png")
            set_character(fire,gunman_xchange,(display_height*0.8)-60)
            set_character(blow_gun_bullet,gun_blow_xchange,(display_height*0.8)-20)
            gun_blow_xchange-=20
            if intersect(crash_positionx,crash_positiony,30,gunman_xchange,(display_height*0.8)-60,30):
                if is_down or is_reversed:
                    gunman_xchange=-10000
                    gun_blow_xchange=100000000
                else:
                    isdie=True
                    blowgun_sound.play()            
            if gun_blow_xchange<-3:
                gun_blow_xchange=1480
            if intersect(crash_positionx,crash_positiony,30,gun_blow_xchange,(display_height*0.8)-20,30):
                if not(is_down or is_reversed):
                    isdie=True
                    blowgun_sound.play()
        set_character(tnt,850,smoke_puff_ychange)
        set_character(tnt2,910,smoke_puff_ychange2)
        set_character(box,earth_positionx+455,earth_positiony+38)
        set_character(iron_cate,earth_positionx+285,earth_positiony+55)
        set_character(iron_cate,1450,earth_positiony+55)
        set_character(iron_cate,1300,earth_positiony+55)
        set_character(iron_cate,1080,earth_positiony-25)
        set_character(bridge,1370, 677)
        #--------------------------------
        #coco
        set_character(coco,display_width-60,(display_height*0.8)-60)
        #wooden
        for i in range(1,4):
            set_character(wooden,100+38*i,(display_height*0.8)-38)
        for i in range(1,7):
            set_character(wooden,480+38*i,(display_height*0.8)-38)
        for i in range(4):
            set_character(liane,0+(display_width-55)/2*i,-15)
            #box
        set_character(box1,210,earth_positiony-40)
        #gecko
        if pygame.time.get_ticks()%1000>=1:
            gecko_step+=1
            gecko_xchange+=MOVE
            if gecko_xchange==572:
                MOVE=-MOVE
                gecko_flip=True
            elif gecko_xchange==710:
                MOVE=-MOVE
                gecko_flip=False
            if gecko_step==8:
                gecko_step=1
            gecko=pygame.image.load(r"assets\image\gecko"+str(gecko_step)+".png")
            geckos=pygame.transform.flip(gecko,gecko_flip,False)
        set_character(geckos,gecko_xchange,(display_height*0.8)-19)
        #-----------Crystal----------------------tnt
        if pygame.time.get_ticks()%500>=1:
            crystal_step=crystal_step+1
            if crystal_step==9:
                crystal_step=1
            crystal=pygame.image.load(r"assets\image\crystal_"+str(crystal_step)+".png")
        
        set_character(crystal,1460-30*1,crystal_ychange_1)
        set_character(crystal,1460-30*2,crystal_ychange_2)
        set_character(crystal,1460-30*3,crystal_ychange_3)
        set_character(crystal,1460-30*4,crystal_ychange_4)
        #-------------------Apple
        if pygame.time.get_ticks()%500>=1:
            apple_count=apple_count+1
            if apple_count==13:
                apple_count=1
            #apple
            apple=pygame.image.load(r"assets\image\apple_"+str(apple_count)+".png")
        #--------APPLE-------------------------------------------
        set_character(apple,(180)-19*0,apple_ychange_2)
        set_character(apple,(180)-19*1,apple_ychange_1)
        set_character(apple,(1420)-19*0,apple_ychange_3)
        set_character(apple,(1420)-19*1,apple_ychange_4)
        set_character(apple,(1420)-19*2,apple_ychange_5)
        set_character(apple,(1420)-19*3,apple_ychange_6)
        set_character(apple,(1420)-19*4,apple_ychange_7)
        set_character(apple,(550)-19*0,apple_ychange_11)
        set_character(apple,(550)-19*1,apple_ychange_12)
        set_character(apple,(550)-19*2,apple_ychange_13)
        #-----------------------------------------------------------------
        set_character(jewels_01,350,jewels_1_ychange)
        set_character(jewels_02,1160,jewels_2_ychange)
        t=teta
        dx=radios*math.cos(radian(t))
        dy=radios*math.sin(radian(t))
        teta-=8
        t=(t+360/3)%360
        if teta==-1:
            teta=359
        set_character(apple,((370)+dx),((apple_ychange_8-dy)))
        set_character(apple,((380)+dx),((apple_ychange_9-dy)))
        set_character(apple,((390)+dx),((apple_ychange_10-dy)))
        #-----
        if intersect(crash_positionx,crash_positiony,41,((370)+dx),(apple_ychange_8-dy),31):
            apple_ychange_8=-1000
            applepicked_sound.play()
        if intersect(crash_positionx,crash_positiony,41,((380)+dx),(apple_ychange_9-dy),31):
            apple_ychange_9=-1000
            applepicked_sound.play()
        if intersect(crash_positionx,crash_positiony,41,((390)+dx),(apple_ychange_10-dy),31):
            apple_ychange_10=-1000
            applepicked_sound.play()
        #die
        if intersect(crash_positionx,crash_positiony,30,gecko_xchange,(display_height*0.8)-19,30):
            if is_reversed or is_down:
                gecko_xchange+=11900
                jumpenemydead_sound.play()
            else:
                isdie=True
                gecko_sound.play()
               
        if intersect(crash_positionx,crash_positiony,30,lizard_xchange,(display_height*0.8)-150,30):
            if is_reversed or is_down:
                lizard_xchange+=11900
                jumpenemydead_sound.play()
            else:
                isdie=True
                lizard_sound.play()
        if isdie:
            if pygame.time.get_ticks()%1000>=1:
                crash=pygame.image.load(r"assets\image\dead"+str(die_step)+".png")
                crash_surf=pygame.transform.flip(crash,isRight,False)
                crash_positiony-=(die_step*2)
                set_character(crash_surf,crash_positionx,crash_positiony)
                die_step=die_step+1
                if die_step==10:
                    grassfootstep_sound.stop()
                    die_angele_step=die_angele_step+5
                    die_step=1
                    background_sound.stop()
                    deathangel_sound.play(-1)
                if die_angele_step==15:
                    deathangel_sound.stop()
                    crashed()
        #tnt
        if intersect(crash_positionx,crash_positiony,49,850,smoke_puff_ychange,49):
            #tnt1
            tnt_one_fire=True  
            runaway_1=True
        else: 
            runaway_1=False
        if intersect(crash_positionx,crash_positiony,49,910,smoke_puff_ychange2,49):
            tnt2_one_fire=True
            runaway_2=True
        else:
            runaway_2=False
    #fire
        if tnt_one_fire:
            tntcountdown_sound.play()
            if pygame.time.get_ticks()%1000<=180:
                tnt_1_step=tnt_1_step-1
                if tnt_1_step==0:
                    tnt_1_step=1
                    fire_tnt_1=True
                    tnt_one_fire=False
                else:
                    tnt=pygame.image.load(r"assets\image\tnt"+str(tnt_1_step)+".png")
                    set_character(tnt,850,smoke_puff_ychange)
        #------------------------------------------------------------
        if tnt2_one_fire:
            tntcountdown_sound.play()
            if pygame.time.get_ticks()%1000<=180:
                tnt_2_step=tnt_2_step-1
                if tnt_2_step==0:
                    tnt_2_step=1
                    tnt2_one_fire=False
                    fire_tnt_2=True
                else:
                    tnt2=pygame.image.load(r"assets\image\tnt"+str(tnt_2_step)+".png")
                    set_character(tnt2,910,smoke_puff_ychange2)
        #-------------------------------------------------------------
        if fire_tnt_1:
            stop_all_sound()
            tntexplosion_sound.play()
            tnt_one_fire=False
            if pygame.time.get_ticks()%1000>=1:
                smoke_puff_1_step_step=smoke_puff_1_step_step+1
                if smoke_puff_1_step_step==11:
                    smoke_puff_1_step_step=10
                    tntcountdown_sound.stop()
                    fire_tnt_1=False                
                tnt=pygame.image.load(r"assets\image\smoke_puff"+str(smoke_puff_1_step_step)+".png")
                set_character(tnt,850,smoke_puff_ychange)
                if runaway_1:
                    if pygame.time.get_ticks()%1000>=1:
                        crash_explosion_step=crash_explosion_step+1
                        if crash_explosion_step==14:
                            crash_explosion_step=1
                            burnd_step=burnd_step+10
                        crash=pygame.image.load(r"assets\image\crash_explosion"+str(crash_explosion_step)+".png")
                        crash_surf=pygame.transform.flip(crash,isRight,False)
                        set_character(crash_surf,crash_positionx,crash_positiony)
                        if burnd_step==10:
                            crashed()  
                else:
                    if smoke_puff_1_step_step==10:
                        tntcountdown_sound.stop()
                        smoke_puff_ychange=-1000
                        fire_tnt_1=False#----------------------------------------------------------------------
        if fire_tnt_2:
            stop_all_sound()
            tntexplosion_sound.play()
            if pygame.time.get_ticks()%1000>=1:
                smoke_puff_2_step_step=smoke_puff_2_step_step+1
                if smoke_puff_2_step_step==11:
                    smoke_puff_2_step_step=10
                    tntcountdown_sound.stop()
                    fire_tnt_2=False
                tnt2=pygame.image.load(r"assets\image\smoke_puff"+str(smoke_puff_2_step_step)+".png")
                set_character(tnt2,910,smoke_puff_ychange2)
                if runaway_2:
                    if pygame.time.get_ticks()%1000>=1:
                        crash_explosion_step=crash_explosion_step+1
                        if crash_explosion_step==14:
                            crash_explosion_step=1
                            burnd_step=burnd_step+10
                        crash=pygame.image.load(r"assets\image\crash_explosion"+str(crash_explosion_step)+".png")
                        crash_surf=pygame.transform.flip(crash,isRight,False)
                        set_character(crash_surf,crash_positionx,crash_positiony)
                        if burnd_step==10:
                            smoke_puff_ychange2=-1000
                            crashed()  
                else:
                    if smoke_puff_2_step_step==10:
                        tntcountdown_sound.stop()
                        smoke_puff_ychange2=-1000
                        fire_tnt_2=False
    #------------------------------------------------------------------------------
        crash_surf=pygame.transform.flip(crash,isRight,False)
        set_character(crash_surf,crash_positionx,crash_positiony)
        if (crash_positiony>display_height):
            crash_surf=pygame.transform.flip(pygame.image.load(r"assets\image\die.png"),isRight,False)
            set_character(crash_surf,crash_positionx,crash_positiony-100)
            pygame.display.update()
            background_sound.stop()
            wumpahit_sound.play()
            crashed()
        if intersect(crash_positionx,crash_positiony,30,display_width-60,(display_height*0.8)-60,30):
            youwin()
        fps.tick(18)
        pygame.display.update()
main()