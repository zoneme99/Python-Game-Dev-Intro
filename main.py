import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)
orgimage = pygame.image.load('girl.jpg')
image = pygame.transform.scale(orgimage,(40,60))

morgimage = pygame.image.load('man.png')
mimage = pygame.transform.scale(morgimage,(20,30))

def draw(player, elapsed_time, stars):
    pygame.Surface.blit(image, WIN, player)
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    WIN.blit(image, player)
    #pygame.draw.rect(WIN, "red", player)

    for star in stars:
        WIN.blit(mimage, star)

    pygame.display.update()


def main():
    run = True

    player = WIN.blit(image,(200,HEIGHT - PLAYER_HEIGHT))
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False
    start_text = FONT.render("Akta dig för Dansgalningar! Tryck högerpil för start", 1, "white")
    WIN.blit(start_text, (WIDTH/2 - start_text.get_width()/2, HEIGHT/2 - start_text.get_height()/2))
    pygame.display.update()
    while True:
        e = pygame.event.wait()
        if e.type == pygame.QUIT:
            pygame.quit()
        elif e.type == pygame.KEYDOWN:
            break

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT,
                                   STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("Vill du boka danskurs med mig?", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            while True:
                e = pygame.event.wait()
                if e.type == pygame.QUIT:
                    pygame.quit()
                elif e.type == pygame.KEYDOWN:
                    break
            

        draw(player, elapsed_time, stars)

    pygame.quit()


if __name__ == "__main__":
    main()
