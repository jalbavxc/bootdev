import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "green", self.triangle(), 0)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        super().update(dt)
        self.shoot_timer -= dt

    # Move the player (you might already have this)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    #Player shoots
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Update the position based on velocity
        self.position += self.velocity * dt

    # Clamp the player position to the screen boundaries
        self.position.x = max(0, min(self.position.x, SCREEN_WIDTH))
        self.position.y = max(0, min(self.position.y, SCREEN_HEIGHT))


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x,self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_SHOOT_SPEED



