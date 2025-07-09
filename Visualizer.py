import pygame
import sys
import time

# === SETTINGS ===
WIDTH, HEIGHT = 800, 600
BG_COLOR = (10, 10, 30)
PULSE_COLOR = (255, 0, 150)
FPS = 60

# === VISUALIZER CLASS ===
class PhonkVisualizer:
    def __init__(self, beat_times):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Phonk Beat Visualizer")
        self.clock = pygame.time.Clock()
        self.beat_times = beat_times
        self.start_time = time.time()

    def draw_pulse(self, intensity):
        radius = int(50 + intensity * 100)
        pygame.draw.circle(
            self.screen, PULSE_COLOR, (WIDTH // 2, HEIGHT // 2), radius, 4
        )

    def run(self):
        running = True
        beat_index = 0

        while running:
            self.screen.fill(BG_COLOR)
            current_time = time.time() - self.start_time

            # Check for beat trigger
            if beat_index < len(self.beat_times) and current_time >= self.beat_times[beat_index]:
                self.draw_pulse(1.0)  # Full pulse
                beat_index += 1
            else:
                self.draw_pulse(0.2)  # Subtle pulse

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()
