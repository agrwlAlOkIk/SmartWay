import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Traffic Light Management System Simulation")

# Define colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Default green light times (in seconds)
green_time_ns = 30
green_time_ew = 30
yellow_time = 5

# Minimum green time to avoid starving any direction
min_green_time = 15

# Simulated vehicle count for each direction
vehicle_count_ns = random.randint(5, 20)  # Simulate vehicles in North-South direction
vehicle_count_ew = random.randint(5, 20)  # Simulate vehicles in East-West direction


# Function to dynamically adjust green light times
def adjust_green_times():
    
    global green_time_ns, green_time_ew

    # Adjust based on vehicle counts
    if vehicle_count_ns > vehicle_count_ew:
        green_time_ns += (vehicle_count_ns - vehicle_count_ew) * 2
        green_time_ew -= (vehicle_count_ns - vehicle_count_ew) * 2
    elif vehicle_count_ew > vehicle_count_ns:
        green_time_ew += (vehicle_count_ew - vehicle_count_ns) * 2
        green_time_ns -= (vehicle_count_ew - vehicle_count_ns) * 2

    # Ensure that green times don't drop below the minimum threshold
    green_time_ns = max(green_time_ns, min_green_time)
    green_time_ew = max(green_time_ew, min_green_time)


# Draw traffic lights on the window
def draw_traffic_lights(ns_color, ew_color):
    window.fill(BLACK)

    # North-South traffic lights (vertical)
    pygame.draw.rect(window, WHITE, (250, 50, 50, 100))  # Light box
    pygame.draw.circle(window, ns_color, (275, 100), 20)  # Traffic light

    # East-West traffic lights (horizontal)
    pygame.draw.rect(window, WHITE, (100, 175, 100, 50))  # Light box
    pygame.draw.circle(window, ew_color, (150, 200), 20)  # Traffic light

    # Display the vehicle counts for both directions
    font = pygame.font.SysFont(None, 35)
    text_ns = font.render(f"NS Vehicles: {vehicle_count_ns}", True, WHITE)
    text_ew = font.render(f"EW Vehicles: {vehicle_count_ew}", True, WHITE)
    window.blit(text_ns, (50, 300))
    window.blit(text_ew, (350, 300))

    pygame.display.update()


# Timer variables
start_time = time.time()
ns_light_state = "GREEN"  # Start with North-South green light
ew_light_state = "RED"

# Simulation loop
running = True
while running:
    current_time = time.time() - start_time

    # Adjust green light times at the start of the simulation
    adjust_green_times()

    # North-South light logic
    if ns_light_state == "GREEN" and current_time >= green_time_ns:
        ns_light_state = "YELLOW"
        start_time = time.time()
    elif ns_light_state == "YELLOW" and current_time >= yellow_time:
        ns_light_state = "RED"
        ew_light_state = "GREEN"
        start_time = time.time()

    # East-West light logic
    elif ew_light_state == "GREEN" and current_time >= green_time_ew:
        ew_light_state = "YELLOW"
        start_time = time.time()
    elif ew_light_state == "YELLOW" and current_time >= yellow_time:
        ew_light_state = "RED"
        ns_light_state = "GREEN"
        start_time = time.time()

    # Set the traffic light colors based on the current state
    ns_color = GREEN if ns_light_state == "GREEN" else (YELLOW if ns_light_state == "YELLOW" else RED)
    ew_color = GREEN if ew_light_state == "GREEN" else (YELLOW if ew_light_state == "YELLOW" else RED)

    # Draw the traffic lights on the screen
    draw_traffic_lights(ns_color, ew_color)

    # Handle events (e.g., close the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
