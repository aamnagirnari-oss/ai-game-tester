import pygame
import time
from game.grid import Grid
from game.agent import Agent
from game.smart_agent import SmartAgent

# -----------------------------
# SETUP
# -----------------------------
pygame.init()
font = pygame.font.SysFont(None, 30)

cell_size = 80
grid = Grid()

width = grid.cols * cell_size * 2   # double width for comparison
height = grid.rows * cell_size

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("AI Game Tester - Comparison")

# -----------------------------
# AGENTS
# -----------------------------
agent_random = Agent(grid.start)

agent_smart = SmartAgent(grid.start)
agent_smart.bfs(grid)  # precompute shortest path
smart_step_index = 0

running = True

# -----------------------------
# MAIN LOOP
# -----------------------------
while running:
    screen.fill((255, 255, 255))

    offset = grid.cols * cell_size

    # =============================
    # LEFT SIDE → RANDOM AGENT
    # =============================
    for i in range(grid.rows):
        for j in range(grid.cols):
            rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)

            if grid.grid[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 0), rect)
            else:
                pygame.draw.rect(screen, (180, 180, 180), rect, 1)

    # Goal (left)
    gx, gy = grid.goal
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (gy * cell_size, gx * cell_size, cell_size, cell_size)
    )

    # Move random agent
    agent_random.move(grid)

    # Draw random path
    for (px, py) in agent_random.path:
        pygame.draw.rect(
            screen,
            (150, 150, 255),
            (py * cell_size, px * cell_size, cell_size, cell_size)
        )

    # Draw random agent
    x, y = agent_random.position
    pygame.draw.rect(
        screen,
        (0, 0, 255),
        (y * cell_size, x * cell_size, cell_size, cell_size)
    )

    # =============================
    # RIGHT SIDE → SMART AGENT
    # =============================
    for i in range(grid.rows):
        for j in range(grid.cols):
            rect = pygame.Rect(j * cell_size + offset, i * cell_size, cell_size, cell_size)

            if grid.grid[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 0), rect)
            else:
                pygame.draw.rect(screen, (180, 180, 180), rect, 1)

    # Goal (right)
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (gy * cell_size + offset, gx * cell_size, cell_size, cell_size)
    )

    # Smart agent movement (step-by-step)
    if smart_step_index < len(agent_smart.path):
        smart_pos = agent_smart.path[smart_step_index]
        smart_step_index += 1
    else:
        smart_pos = agent_smart.path[-1]

    # Draw smart path
    for (px, py) in agent_smart.path:
        pygame.draw.rect(
            screen,
            (180, 255, 180),
            (py * cell_size + offset, px * cell_size, cell_size, cell_size)
        )

    # Draw smart agent
    sx, sy = smart_pos
    pygame.draw.rect(
        screen,
        (0, 200, 0),
        (sy * cell_size + offset, sx * cell_size, cell_size, cell_size)
    )

    # =============================
    # LABELS + STATS
    # =============================
    left_label = font.render("Random Agent", True, (0, 0, 0))
    screen.blit(left_label, (10, 10))

    right_label = font.render("Smart Agent", True, (0, 0, 0))
    screen.blit(right_label, (offset + 10, 10))

    steps_text = font.render(f"Steps: {len(agent_random.path)}", True, (0, 0, 0))
    screen.blit(steps_text, (10, 40))

    # =============================
    # DISPLAY
    # =============================
    pygame.display.flip()
    time.sleep(0.4)

    # Stop when random reaches goal
    if agent_random.reached_goal(grid.goal):
        print("✅ Random agent reached goal")
        running = False

    # Exit handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()