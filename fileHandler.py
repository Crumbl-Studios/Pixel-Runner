import pygame  # To load files
import json  # To save files
from json.decoder import JSONDecodeError  # For error handling
import os  # To find files

# Create directories
current_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.join(current_dir, 'bin')
font_dir = os.path.join(current_dir, 'Font')

audio_dir = os.path.join(current_dir, 'Audio')
player_audio_dir = os.path.join(audio_dir, 'Player')
textures_dir = os.path.join(current_dir, 'Textures')

ui_dir = os.path.join(textures_dir, 'UI')
sky_button_dir = os.path.join(ui_dir, 'sky_buttons')

other_dir = os.path.join(textures_dir, 'Other')

coin_dir = os.path.join(other_dir, 'Coin')

collected_dir = os.path.join(other_dir, 'Collected')

world_dir = os.path.join(textures_dir, 'World')
backgrounds_dir = os.path.join(world_dir, 'Backgrounds')
grounds_dir = os.path.join(world_dir, 'Grounds')

characters_dir = os.path.join(textures_dir, 'Characters')
enemies_dir = os.path.join(textures_dir, 'Enemies')

other_textures_dir = os.path.join(textures_dir, 'Other')

vr_guy_dir = os.path.join(characters_dir, 'Virtual Guy')
ninja_frog_dir = os.path.join(characters_dir, 'Ninja Frog')
mask_dude_dir = os.path.join(characters_dir, 'Mask Dude')
purple_man_dir = os.path.join(characters_dir, 'Purple Man')

turtle_dir = os.path.join(enemies_dir, 'Turtle')
bird_dir = os.path.join(enemies_dir, 'Bird')
chameleon_dir = os.path.join(enemies_dir, 'Chameleon')
mushroom_dir = os.path.join(enemies_dir, 'Mushroom')
chicken_dir = os.path.join(enemies_dir, 'Chicken')
radish_dir = os.path.join(enemies_dir, 'Radish')
ghost_dir = os.path.join(enemies_dir, 'Ghost')
bat_dir = os.path.join(enemies_dir, 'Bat')

music = os.path.join(audio_dir, 'Adventure_chiptune.mp3')

# Load audio
pygame.mixer.init()
jump_sound = pygame.mixer.Sound(os.path.join(player_audio_dir, 'Jump.wav'))
game_over_sound = pygame.mixer.Sound(os.path.join(player_audio_dir, 'Game_over.wav'))
collect_sound = pygame.mixer.Sound(os.path.join(player_audio_dir, 'Collect.wav'))
hover_sound = pygame.mixer.Sound(os.path.join(audio_dir, 'Hover.wav'))
click_sound = pygame.mixer.Sound(os.path.join(audio_dir, 'Click.wav'))
pause_sound = pygame.mixer.Sound(os.path.join(audio_dir, 'Pause.wav'))

# Load images
# Misc. files:
icon = pygame.image.load(os.path.join(ui_dir, 'Icon.png'))

cursor1 = pygame.image.load(os.path.join(ui_dir, 'Cursor.png'))
cursor2 = pygame.image.load(os.path.join(ui_dir, 'Cursor1.png'))
cursor_files = [cursor1, cursor2]

pygame.font.init()
font_default = pygame.font.Font(os.path.join(font_dir, 'Pixelar.ttf'), 30)
font_big = pygame.font.Font(os.path.join(font_dir, 'Pixelar.ttf'), 50)
font_small = pygame.font.Font(os.path.join(font_dir, 'Pixelar.ttf'), 25)

# Terrain files:
grass_floor = pygame.image.load(os.path.join(grounds_dir, 'Grass_floor.png'))
mythic_floor = pygame.image.load(os.path.join(grounds_dir, 'Mythic_floor.png'))
hay_floor = pygame.image.load(os.path.join(grounds_dir, 'Hay_floor.png'))
stone_floor = pygame.image.load(os.path.join(grounds_dir, 'Stone_floor.png'))

# Sky files:
green_sky = pygame.image.load(os.path.join(backgrounds_dir, 'Green.png'))
purple_sky = pygame.image.load(os.path.join(backgrounds_dir, 'Purple.png'))
brown_sky = pygame.image.load(os.path.join(backgrounds_dir, 'Brown.png'))
mint_sky = pygame.image.load(os.path.join(backgrounds_dir, 'Mint.png'))
blue_purple_sky = pygame.image.load(os.path.join(backgrounds_dir, 'Blue_Purple.png'))
blue_purple_2_sky = pygame.image.load(os.path.join(backgrounds_dir, 'Blue_Purple_2.png'))

# Sky shop thumbnails
green_sky_thumb = pygame.image.load(os.path.join(backgrounds_dir, 'Green.png'))
purple_sky_thumb = pygame.image.load(os.path.join(backgrounds_dir, 'Purple.png'))
brown_sky_thumb = pygame.image.load(os.path.join(backgrounds_dir, 'Brown.png'))
mint_sky_thumb = pygame.image.load(os.path.join(backgrounds_dir, 'Mint.png'))
blue_purple_sky_thumb = pygame.image.load(os.path.join(backgrounds_dir, 'Blue_Purple.png'))
blue_purple_2_sky_thumb = pygame.image.load(os.path.join(backgrounds_dir, 'Blue_Purple_2.png'))

# Button files:
button_select = pygame.image.load(os.path.join(ui_dir, 'Button_select.png'))
button_hover = pygame.image.load(os.path.join(ui_dir, 'Button_hover.png'))
button = pygame.image.load(os.path.join(ui_dir, 'Button.png'))
button_states = [button_select, button_hover, button]

up_button = [pygame.image.load(os.path.join(ui_dir, 'Up.png')),
             pygame.image.load(os.path.join(ui_dir, 'Up_click.png'))]
right_button = [pygame.image.load(os.path.join(ui_dir, 'Right.png')),
                pygame.image.load(os.path.join(ui_dir, 'Right_click.png'))]
down_button = [pygame.image.load(os.path.join(ui_dir, 'Down.png')),
               pygame.image.load(os.path.join(ui_dir, 'Down_click.png'))]
left_button = [pygame.image.load(os.path.join(ui_dir, 'Left.png')),
               pygame.image.load(os.path.join(ui_dir, 'Left_click.png'))]
directional_buttons = [up_button, right_button, down_button, left_button]

# Settings button icons
settings_button = pygame.image.load(os.path.join(ui_dir, 'settings_button.png'))
settings_hover = pygame.image.load(os.path.join(ui_dir, 'settings_button_hover.png'))
settings_select = pygame.image.load(os.path.join(ui_dir, 'settings_button_select.png'))


# Character files:
appear_1 = pygame.image.load(os.path.join(characters_dir, 'Appearing1.png'))
appear_2 = pygame.image.load(os.path.join(characters_dir, 'Appearing2.png'))
appear_3 = pygame.image.load(os.path.join(characters_dir, 'Appearing3.png'))
appear_4 = pygame.image.load(os.path.join(characters_dir, 'Appearing4.png'))
appear_5 = pygame.image.load(os.path.join(characters_dir, 'Appearing5.png'))
appear_6 = pygame.image.load(os.path.join(characters_dir, 'Appearing6.png'))
appear_7 = pygame.image.load(os.path.join(characters_dir, 'Appearing7.png'))
appear = [appear_1, appear_2, appear_3, appear_4, appear_5, appear_6, appear_7]

disappear_1 = pygame.image.load(os.path.join(characters_dir, 'Disappearing1.png'))
disappear_2 = pygame.image.load(os.path.join(characters_dir, 'Disappearing2.png'))
disappear_3 = pygame.image.load(os.path.join(characters_dir, 'Disappearing3.png'))
disappear_4 = pygame.image.load(os.path.join(characters_dir, 'Disappearing4.png'))
disappear_5 = pygame.image.load(os.path.join(characters_dir, 'Disappearing5.png'))
disappear_6 = pygame.image.load(os.path.join(characters_dir, 'Disappearing6.png'))
disappear_7 = pygame.image.load(os.path.join(characters_dir, 'Disappearing7.png'))
disappear = [disappear_1, disappear_2, disappear_3, disappear_4, disappear_5, disappear_6, disappear_7]

vr_guy_run_1 = pygame.image.load(os.path.join(vr_guy_dir, 'Run1.png'))
vr_guy_run_2 = pygame.image.load(os.path.join(vr_guy_dir, 'Run2.png'))
vr_guy_run_3 = pygame.image.load(os.path.join(vr_guy_dir, 'Run3.png'))
vr_guy_run_4 = pygame.image.load(os.path.join(vr_guy_dir, 'Run4.png'))
vr_guy_run_5 = pygame.image.load(os.path.join(vr_guy_dir, 'Run5.png'))
vr_guy_run_6 = pygame.image.load(os.path.join(vr_guy_dir, 'Run6.png'))
vr_guy_run_7 = pygame.image.load(os.path.join(vr_guy_dir, 'Run7.png'))
vr_guy_run_8 = pygame.image.load(os.path.join(vr_guy_dir, 'Run8.png'))
vr_guy_run_9 = pygame.image.load(os.path.join(vr_guy_dir, 'Run9.png'))
vr_guy_run_10 = pygame.image.load(os.path.join(vr_guy_dir, 'Run10.png'))
vr_guy_run_11 = pygame.image.load(os.path.join(vr_guy_dir, 'Run11.png'))
vr_guy_run_12 = pygame.image.load(os.path.join(vr_guy_dir, 'Run12.png'))
vr_guy_run = [vr_guy_run_1, vr_guy_run_2, vr_guy_run_3, vr_guy_run_4, vr_guy_run_5,
              vr_guy_run_6, vr_guy_run_7, vr_guy_run_8, vr_guy_run_9, vr_guy_run_10,
              vr_guy_run_11, vr_guy_run_12]
vr_guy_jump = pygame.image.load(os.path.join(vr_guy_dir, 'Jump.png'))
vr_guy_fall = pygame.image.load(os.path.join(vr_guy_dir, 'Fall.png'))
vr_guy_files = [vr_guy_run, vr_guy_jump, vr_guy_fall]

ninja_frog_run_1 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run1.png'))
ninja_frog_run_2 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run2.png'))
ninja_frog_run_3 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run3.png'))
ninja_frog_run_4 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run4.png'))
ninja_frog_run_5 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run5.png'))
ninja_frog_run_6 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run6.png'))
ninja_frog_run_7 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run7.png'))
ninja_frog_run_8 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run8.png'))
ninja_frog_run_9 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run9.png'))
ninja_frog_run_10 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run10.png'))
ninja_frog_run_11 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run11.png'))
ninja_frog_run_12 = pygame.image.load(os.path.join(ninja_frog_dir, 'Run12.png'))
ninja_frog_run = [ninja_frog_run_1, ninja_frog_run_2, ninja_frog_run_3, ninja_frog_run_4, ninja_frog_run_5,
                  ninja_frog_run_6, ninja_frog_run_7, ninja_frog_run_8, ninja_frog_run_9, ninja_frog_run_10,
                  ninja_frog_run_11, ninja_frog_run_12]
ninja_frog_jump = pygame.image.load(os.path.join(ninja_frog_dir, 'Jump.png'))
ninja_frog_fall = pygame.image.load(os.path.join(ninja_frog_dir, 'Fall.png'))
ninja_frog_files = [ninja_frog_run, ninja_frog_jump, ninja_frog_fall]

mask_dude_run_1 = pygame.image.load(os.path.join(mask_dude_dir, 'Run1.png'))
mask_dude_run_2 = pygame.image.load(os.path.join(mask_dude_dir, 'Run2.png'))
mask_dude_run_3 = pygame.image.load(os.path.join(mask_dude_dir, 'Run3.png'))
mask_dude_run_4 = pygame.image.load(os.path.join(mask_dude_dir, 'Run4.png'))
mask_dude_run_5 = pygame.image.load(os.path.join(mask_dude_dir, 'Run5.png'))
mask_dude_run_6 = pygame.image.load(os.path.join(mask_dude_dir, 'Run6.png'))
mask_dude_run_7 = pygame.image.load(os.path.join(mask_dude_dir, 'Run7.png'))
mask_dude_run_8 = pygame.image.load(os.path.join(mask_dude_dir, 'Run8.png'))
mask_dude_run_9 = pygame.image.load(os.path.join(mask_dude_dir, 'Run9.png'))
mask_dude_run_10 = pygame.image.load(os.path.join(mask_dude_dir, 'Run10.png'))
mask_dude_run_11 = pygame.image.load(os.path.join(mask_dude_dir, 'Run11.png'))
mask_dude_run_12 = pygame.image.load(os.path.join(mask_dude_dir, 'Run12.png'))
mask_dude_run = [mask_dude_run_1, mask_dude_run_2, mask_dude_run_3, mask_dude_run_4, mask_dude_run_5,
                 mask_dude_run_6, mask_dude_run_7, mask_dude_run_8, mask_dude_run_9, mask_dude_run_10,
                 mask_dude_run_11, mask_dude_run_12]
mask_dude_jump = pygame.image.load(os.path.join(mask_dude_dir, 'Jump.png'))
mask_dude_fall = pygame.image.load(os.path.join(mask_dude_dir, 'Fall.png'))
mask_dude_files = [mask_dude_run, mask_dude_jump, mask_dude_fall]

purple_man_run_1 = pygame.image.load(os.path.join(purple_man_dir, 'Run1.png'))
purple_man_run_2 = pygame.image.load(os.path.join(purple_man_dir, 'Run2.png'))
purple_man_run_3 = pygame.image.load(os.path.join(purple_man_dir, 'Run3.png'))
purple_man_run_4 = pygame.image.load(os.path.join(purple_man_dir, 'Run4.png'))
purple_man_run_5 = pygame.image.load(os.path.join(purple_man_dir, 'Run5.png'))
purple_man_run_6 = pygame.image.load(os.path.join(purple_man_dir, 'Run6.png'))
purple_man_run_7 = pygame.image.load(os.path.join(purple_man_dir, 'Run7.png'))
purple_man_run_8 = pygame.image.load(os.path.join(purple_man_dir, 'Run8.png'))
purple_man_run_9 = pygame.image.load(os.path.join(purple_man_dir, 'Run9.png'))
purple_man_run_10 = pygame.image.load(os.path.join(purple_man_dir, 'Run10.png'))
purple_man_run_11 = pygame.image.load(os.path.join(purple_man_dir, 'Run11.png'))
purple_man_run_12 = pygame.image.load(os.path.join(purple_man_dir, 'Run12.png'))
purple_man_run = [purple_man_run_1, purple_man_run_2, purple_man_run_3, purple_man_run_4, purple_man_run_5,
                  purple_man_run_6, purple_man_run_7, purple_man_run_8, purple_man_run_9, purple_man_run_10,
                  purple_man_run_11, purple_man_run_12]
purple_man_jump = pygame.image.load(os.path.join(purple_man_dir, 'Jump.png'))
purple_man_fall = pygame.image.load(os.path.join(purple_man_dir, 'Fall.png'))
purple_man_files = [purple_man_run, purple_man_jump, purple_man_fall]

# Enemy files:
turtle_idle_type_1_1 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_1.png'))
turtle_idle_type_1_2 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_2.png'))
turtle_idle_type_1_3 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_3.png'))
turtle_idle_type_1_4 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_4.png'))
turtle_idle_type_1_5 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_5.png'))
turtle_idle_type_1_6 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_6.png'))
turtle_idle_type_1_7 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_7.png'))
turtle_idle_type_1_8 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_8.png'))
turtle_idle_type_1_9 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_9.png'))
turtle_idle_type_1_10 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_10.png'))
turtle_idle_type_1_11 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_11.png'))
turtle_idle_type_1_12 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_12.png'))
turtle_idle_type_1_13 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_13.png'))
turtle_idle_type_1_14 = pygame.image.load(os.path.join(turtle_dir, 'Idle_type_1_14.png'))

Spikes_out_1 = pygame.image.load(os.path.join(turtle_dir, 'Spikes_out_1.png'))
Spikes_out_2 = pygame.image.load(os.path.join(turtle_dir, 'Spikes_out_2.png'))
Spikes_out_3 = pygame.image.load(os.path.join(turtle_dir, 'Spikes_out_3.png'))
Spikes_out_4 = pygame.image.load(os.path.join(turtle_dir, 'Spikes_out_4.png'))
Spikes_out_5 = pygame.image.load(os.path.join(turtle_dir, 'Spikes_out_5.png'))
Spikes_out_6 = pygame.image.load(os.path.join(turtle_dir, 'Spikes_out_6.png'))
Spikes_out_7 = pygame.image.load(os.path.join(turtle_dir, 'Spikes_out_7.png'))
Spikes_out_8 = pygame.image.load(os.path.join(turtle_dir, 'Spikes_out_8.png'))
turtle_files = [[turtle_idle_type_1_1, turtle_idle_type_1_2, turtle_idle_type_1_3, turtle_idle_type_1_4,
                 turtle_idle_type_1_5, turtle_idle_type_1_6, turtle_idle_type_1_7, turtle_idle_type_1_8,
                 turtle_idle_type_1_9, turtle_idle_type_1_10, turtle_idle_type_1_11, turtle_idle_type_1_12,
                 turtle_idle_type_1_13, turtle_idle_type_1_14], [Spikes_out_1, Spikes_out_2, Spikes_out_3, Spikes_out_4,
                                                                 Spikes_out_5, Spikes_out_6, Spikes_out_7,
                                                                 Spikes_out_8]]

bird_fly_1 = pygame.image.load(os.path.join(bird_dir, 'Flying1.png'))
bird_fly_2 = pygame.image.load(os.path.join(bird_dir, 'Flying2.png'))
bird_fly_3 = pygame.image.load(os.path.join(bird_dir, 'Flying3.png'))
bird_fly_4 = pygame.image.load(os.path.join(bird_dir, 'Flying4.png'))
bird_fly_5 = pygame.image.load(os.path.join(bird_dir, 'Flying5.png'))
bird_fly_6 = pygame.image.load(os.path.join(bird_dir, 'Flying6.png'))
bird_fly_7 = pygame.image.load(os.path.join(bird_dir, 'Flying7.png'))
bird_fly_8 = pygame.image.load(os.path.join(bird_dir, 'Flying8.png'))
bird_fly_9 = pygame.image.load(os.path.join(bird_dir, 'Flying9.png'))
bird_files = [bird_fly_1, bird_fly_2, bird_fly_3, bird_fly_4, bird_fly_5, bird_fly_6, bird_fly_7, bird_fly_8,
              bird_fly_9]

chameleon_run_1 = pygame.image.load(os.path.join(chameleon_dir, 'Run1.png'))
chameleon_run_2 = pygame.image.load(os.path.join(chameleon_dir, 'Run2.png'))
chameleon_run_3 = pygame.image.load(os.path.join(chameleon_dir, 'Run3.png'))
chameleon_run_4 = pygame.image.load(os.path.join(chameleon_dir, 'Run4.png'))
chameleon_run_5 = pygame.image.load(os.path.join(chameleon_dir, 'Run5.png'))
chameleon_run_6 = pygame.image.load(os.path.join(chameleon_dir, 'Run6.png'))
chameleon_run_7 = pygame.image.load(os.path.join(chameleon_dir, 'Run7.png'))
chameleon_run_8 = pygame.image.load(os.path.join(chameleon_dir, 'Run8.png'))
chameleon_files = [chameleon_run_1, chameleon_run_2, chameleon_run_3, chameleon_run_4, chameleon_run_5, chameleon_run_6,
                   chameleon_run_7, chameleon_run_8]

mushroom_run_1 = pygame.image.load(os.path.join(mushroom_dir, 'Run1.png'))
mushroom_run_2 = pygame.image.load(os.path.join(mushroom_dir, 'Run2.png'))
mushroom_run_3 = pygame.image.load(os.path.join(mushroom_dir, 'Run3.png'))
mushroom_run_4 = pygame.image.load(os.path.join(mushroom_dir, 'Run4.png'))
mushroom_run_5 = pygame.image.load(os.path.join(mushroom_dir, 'Run5.png'))
mushroom_run_6 = pygame.image.load(os.path.join(mushroom_dir, 'Run6.png'))
mushroom_run_7 = pygame.image.load(os.path.join(mushroom_dir, 'Run7.png'))
mushroom_run_8 = pygame.image.load(os.path.join(mushroom_dir, 'Run8.png'))
mushroom_run_9 = pygame.image.load(os.path.join(mushroom_dir, 'Run9.png'))
mushroom_run_10 = pygame.image.load(os.path.join(mushroom_dir, 'Run10.png'))
mushroom_run_11 = pygame.image.load(os.path.join(mushroom_dir, 'Run11.png'))
mushroom_run_12 = pygame.image.load(os.path.join(mushroom_dir, 'Run12.png'))
mushroom_run_13 = pygame.image.load(os.path.join(mushroom_dir, 'Run13.png'))
mushroom_run_14 = pygame.image.load(os.path.join(mushroom_dir, 'Run14.png'))
mushroom_run_15 = pygame.image.load(os.path.join(mushroom_dir, 'Run15.png'))
mushroom_run_16 = pygame.image.load(os.path.join(mushroom_dir, 'Run16.png'))
mushroom_files = [mushroom_run_1, mushroom_run_2, mushroom_run_3, mushroom_run_4, mushroom_run_5, mushroom_run_6,
                  mushroom_run_7, mushroom_run_8, mushroom_run_9, mushroom_run_10, mushroom_run_12, mushroom_run_13,
                  mushroom_run_14, mushroom_run_15, mushroom_run_16]

chicken_run_1 = pygame.image.load(os.path.join(chicken_dir, 'Run1.png'))
chicken_run_2 = pygame.image.load(os.path.join(chicken_dir, 'Run2.png'))
chicken_run_3 = pygame.image.load(os.path.join(chicken_dir, 'Run3.png'))
chicken_run_4 = pygame.image.load(os.path.join(chicken_dir, 'Run4.png'))
chicken_run_5 = pygame.image.load(os.path.join(chicken_dir, 'Run5.png'))
chicken_run_6 = pygame.image.load(os.path.join(chicken_dir, 'Run6.png'))
chicken_run_7 = pygame.image.load(os.path.join(chicken_dir, 'Run7.png'))
chicken_run_8 = pygame.image.load(os.path.join(chicken_dir, 'Run8.png'))
chicken_run_9 = pygame.image.load(os.path.join(chicken_dir, 'Run9.png'))
chicken_run_10 = pygame.image.load(os.path.join(chicken_dir, 'Run10.png'))
chicken_run_11 = pygame.image.load(os.path.join(chicken_dir, 'Run11.png'))
chicken_run_12 = pygame.image.load(os.path.join(chicken_dir, 'Run12.png'))
chicken_run_13 = pygame.image.load(os.path.join(chicken_dir, 'Run13.png'))
chicken_run_14 = pygame.image.load(os.path.join(chicken_dir, 'Run14.png'))
chicken_files = [chicken_run_1, chicken_run_2, chicken_run_3, chicken_run_4, chicken_run_5, chicken_run_6,
                 chicken_run_7, chicken_run_8, chicken_run_9, chicken_run_10, chicken_run_12, chicken_run_13,
                 chicken_run_14]

radish_fly_1 = pygame.image.load(os.path.join(radish_dir, 'Idle_1_1.png'))
radish_fly_2 = pygame.image.load(os.path.join(radish_dir, 'Idle_1_2.png'))
radish_fly_3 = pygame.image.load(os.path.join(radish_dir, 'Idle_1_3.png'))
radish_fly_4 = pygame.image.load(os.path.join(radish_dir, 'Idle_1_4.png'))
radish_fly_5 = pygame.image.load(os.path.join(radish_dir, 'Idle_1_5.png'))
radish_fly_6 = pygame.image.load(os.path.join(radish_dir, 'Idle_1_6.png'))
radish_files = [radish_fly_1, radish_fly_2, radish_fly_3, radish_fly_4, radish_fly_5, radish_fly_6]

ghost_idle_1 = pygame.image.load(os.path.join(ghost_dir, 'Idle1.png'))
ghost_idle_2 = pygame.image.load(os.path.join(ghost_dir, 'Idle2.png'))
ghost_idle_3 = pygame.image.load(os.path.join(ghost_dir, 'Idle3.png'))
ghost_idle_4 = pygame.image.load(os.path.join(ghost_dir, 'Idle4.png'))
ghost_idle_5 = pygame.image.load(os.path.join(ghost_dir, 'Idle5.png'))
ghost_idle_6 = pygame.image.load(os.path.join(ghost_dir, 'Idle6.png'))
ghost_idle_7 = pygame.image.load(os.path.join(ghost_dir, 'Idle7.png'))
ghost_idle_8 = pygame.image.load(os.path.join(ghost_dir, 'Idle8.png'))
ghost_idle_9 = pygame.image.load(os.path.join(ghost_dir, 'Idle9.png'))
ghost_files = [ghost_idle_1, ghost_idle_2, ghost_idle_3, ghost_idle_4, ghost_idle_5, ghost_idle_6,
               ghost_idle_7, ghost_idle_8, ghost_idle_9]

bat_fly_1 = pygame.image.load(os.path.join(bat_dir, 'Flying1.png'))
bat_fly_2 = pygame.image.load(os.path.join(bat_dir, 'Flying2.png'))
bat_fly_3 = pygame.image.load(os.path.join(bat_dir, 'Flying3.png'))
bat_fly_4 = pygame.image.load(os.path.join(bat_dir, 'Flying4.png'))
bat_fly_5 = pygame.image.load(os.path.join(bat_dir, 'Flying5.png'))
bat_fly_6 = pygame.image.load(os.path.join(bat_dir, 'Flying6.png'))
bat_fly_7 = pygame.image.load(os.path.join(bat_dir, 'Flying7.png'))
bat_files = [bat_fly_1, bat_fly_2, bat_fly_3, bat_fly_4, bat_fly_5, bat_fly_6,
             bat_fly_7]

# Coin animation files
coin_1 = pygame.image.load(os.path.join(coin_dir, 'Coin_1.png'))
coin_2 = pygame.image.load(os.path.join(coin_dir, 'Coin_2.png'))
coin_3 = pygame.image.load(os.path.join(coin_dir, 'Coin_3.png'))
coin_4 = pygame.image.load(os.path.join(coin_dir, 'Coin_4.png'))
coin_files = [coin_1, coin_2, coin_3, coin_4]

# Coin icon file
coin_icon = pygame.image.load(os.path.join(coin_dir, 'Coin_icon.png'))
# Collect animation files
collected_1 = pygame.image.load(os.path.join(collected_dir, 'Collected_1.png'))
collected_2 = pygame.image.load(os.path.join(collected_dir, 'Collected_2.png'))
collected_3 = pygame.image.load(os.path.join(collected_dir, 'Collected_3.png'))
collected_4 = pygame.image.load(os.path.join(collected_dir, 'Collected_4.png'))
collected_5 = pygame.image.load(os.path.join(collected_dir, 'Collected_5.png'))
collected_6 = pygame.image.load(os.path.join(collected_dir, 'Collected_6.png'))
collected_files = [collected_1, collected_2, collected_3, collected_4, collected_5, collected_6]


# Create functions so these files are accessible
def save_data(data):
    with open(os.path.join(save_dir, 's.bin'), 'w') as save_file:
        json.dump(data, save_file)


def get_save_data(data_layout):
    try:
        with open(os.path.join(save_dir, 's.bin')) as save_file:
            try:
                print("attempting to load file...")
                json.load(save_file)
                return json.load(save_file)
            except JSONDecodeError:
                print("JSON can't decode...")
                with open(os.path.join(save_dir, 's.bin'), 'a') as save_file_2:
                    json.dump(data_layout, save_file_2)
                    return data_layout
    except FileNotFoundError:
        print("file not found...")
        with open(os.path.join(save_dir, 's.bin'), 'w') as save_file_3:
            json.dump(data_layout, save_file_3)
            return data_layout


def get_appear_animation():
    return appear


def get_disappear_animation():
    return disappear


def get_vr_guy_files():
    return vr_guy_files


def get_ninja_frog_files():
    return ninja_frog_files


def get_mask_dude_files():
    return mask_dude_files


def get_purple_man_files():
    return purple_man_files


def get_turtle_files():
    return turtle_files


def get_bird_files():
    return bird_files


def get_chameleon_files():
    return chameleon_files


def get_mushroom_files():
    return mushroom_files


def get_chicken_files():
    return chicken_files


def get_radish_files():
    return radish_files


def get_ghost_files():
    return ghost_files


def get_bat_files():
    return bat_files


def get_grass_floor_file():
    return grass_floor


def get_mythic_floor_file():
    return mythic_floor


def get_hay_floor_file():
    return hay_floor


def get_stone_floor_file():
    return stone_floor


def get_green_sky():
    return green_sky


def get_purple_sky():
    return purple_sky


def get_brown_sky():
    return brown_sky


def get_mint_sky():
    return mint_sky


def get_blue_purple_sky():
    return blue_purple_sky


def get_blue_purple_2_sky():
    return blue_purple_2_sky


def get_cursor_files():
    return cursor_files


def get_icon_file():
    return icon


def get_font_default():
    return font_default


def get_font_big():
    return font_big


def get_font_small():
    return font_small


def get_music():
    return music


def get_jump_sound():
    return jump_sound


def get_game_over_sound():
    return game_over_sound


def get_collect_sound():
    return collect_sound


def get_hover_sound():
    return hover_sound


def get_click_sound():
    return click_sound


def get_pause_sound():
    return pause_sound


def get_directional_buttons():
    return directional_buttons


def get_button_states():
    return button_states


def get_coin_files():
    return coin_files


def get_coin_icon():
    return coin_icon


def get_collected_files():
    return collected_files
