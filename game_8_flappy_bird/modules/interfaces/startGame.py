import pygame
import sys
import itertools

def startGame(screen,sounds,bird_images,other_images, background_image,cfg):
    base_pos = [0,cfg.SCREEN_HEIGHT*0.79]
    base_diff_bg = other_images["base"].get_width()-background_image.get_width()
    msg_pos = [(cfg.SCREENWIDTH-other_images['message'].get_width())/2, cfg.SCREENHEIGHT*0.12]
    bird_idx = 0
    bird_idx_change_count = 0
    bird_idx_cycle = itertools.cycle([0,1,2,1])
    bird_pos = [cfg.SCREEN_WIDTH*0.2,cfg.SCREEN_HEIGHT- list(bird_images.values())[0].get_height()/2]
    bird_y_shift_count = 0
    bird_y_shift_max = 9
    shift = 1
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    return {"bird pos": bird_pos,'base pos':base_pos, 'bird_idx':bird_idx}

        bird_idx_change_count += 1

        if bird_idx_change_count % 5 == 0:
            bird_idx = next(bird_idx_cycle)
            bird_idx_change_count = 0
        base_pos[0] =  -((-base_pos[0]+4)%base_diff_bg)
        bird_y_shift_count += 1

        if bird_y_shift_count == bird_y_shift_max:
            bird_y_shift_max = 16
            shift = -1*shift
            bird_y_shift_max = 0
        bird_pos[-1] = min([368,max([10,bird_pos[-1] + shift])])
        screen.blit(background_image,(0,0))
        screen.blit(list(bird_images.values())[bird_idx],bird_pos)
        screen.blit(other_images['message'],msg_pos)
        screen.blit(other_images['base'],base_pos)
        pygame.display.update()
        clock.tick(cfg.FPS)