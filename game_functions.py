'''
Author: taobo
Date: 2020-11-11 19:33:13
LastEditTime: 2020-11-13 09:29:25
'''
import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien

def fire_bullet(ai_setting, screen, ship, bullets):
    """发射子弹到 Group 容器"""
    if len(bullets) < ai_setting.bullets_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(event, ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_play_button(stats, play_button, mouse_x, mouse_y, ai_setting, screen, ship, bullets, aliens):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        ai_setting.initialize_dynamic_settings()
        stats.reset_stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_fleet(ai_setting, screen, aliens, ship)
        ship.center_ship()


def check_events(ai_setting, screen, ship, bullets, aliens, stats, play_button):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, ai_setting, screen, ship, bullets, aliens)


def update_screen(ai_setting, screen, ship, aliens, bullets, stats, play_button):
    """刷新屏幕"""
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def check_bullet_alien_collisions(bullets, ai_setting, screen, aliens, ship):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        ai_setting.increase_speed()
        create_fleet(ai_setting, screen, aliens, ship)


def update_bullets(bullets, ai_setting, screen, aliens, ship):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(bullets, ai_setting, screen, aliens, ship)            


def get_number_aliens_x(ai_setting, alien_width):
    """
    可用于放置外星人的水平空间为屏幕宽度减去外星人宽度的两倍:
        available_space_x = ai_settings.screen_width – (2 * alien_width)
    确定一行可容纳多少个外星人，我们将可用空间除以外星人宽度的两倍:
        number_aliens_x = available_space_x / (2 * alien_width)
    """
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_aliens_y(ai_setting, alien_height, ship_height):
    available_space_y = ai_setting.screen_height - 3 * alien_height - ship_height
    number_aliens_y = int(available_space_y / (2 * alien_height))
    return number_aliens_y


def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * row_number
    aliens.add(alien)


def create_fleet(ai_setting, screen, aliens, ship):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    alien = Alien(ai_setting, screen)
    number_aliens_x = get_number_aliens_x(ai_setting, alien.rect.width)
    number_aliens_y = get_number_aliens_y(ai_setting, alien.rect.height, ship.rect.height)

    for row_number in range(number_aliens_y):
        for alien_number in range(number_aliens_x):
            create_alien(ai_setting, screen, aliens, alien_number, row_number)
        

def check_fleet_edges(ai_setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_direction(ai_setting, aliens)
            break


def change_direction(ai_setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.alien_drop_speed
    ai_setting.fleet_direction *= -1


def ship_hit(ai_setting, stats, screen, aliens, ship, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_setting, screen, aliens, ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_setting, stats, screen, aliens, ship, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting, stats, screen, aliens, ship, bullets)
            break


def update_aliens(ai_setting, stats, screen, aliens, ship, bullets):
    check_fleet_edges(ai_setting, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, stats, screen, aliens, ship, bullets)
    check_aliens_bottom(ai_setting, stats, screen, aliens, ship, bullets)