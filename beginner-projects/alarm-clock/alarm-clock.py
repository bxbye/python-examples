"""
Author: Kadir KAYA
Date: 3.7.2023
Description: Pygame is a game library for python. mixer and display methods were used for creeating alarm app.
Before writing the program you should know that you also need an alarm tone which will ring at the time of the alarm. So you can download an alarm tune from https://pixabay.com/
"""


import pygame
import datetime

pygame.init()

# Set the alarm time
alarm_time = datetime.datetime.now() + datetime.timedelta(seconds=3)  # 10 seconds from now

# Load the alarm sound file
sound_file = "cardinal-37075.mp3"
pygame.mixer.music.load(sound_file)

# Set up the display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Alarm App")

# Main Loop for Alarm
running = True
while running:
    current_time = datetime.datetime.now()
    # Check if the alarm time is reached
    if current_time >= alarm_time:
        pygame.mixer.music.play()  # Play the alarm sound
        running = False  # Exit the loop and end the app
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('QUIT')
            running = False  # Exit the loop and end the app
    # Refresh the display with RGB colors
    screen.fill((102, 122, 122))
    pygame.display.flip()

# Wait for the sound to finish playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.quit()

