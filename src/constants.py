"""
Mr. Do! Modern - Constants and Configuration
"""
import pygame

# Screen / Display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
TILE_SIZE = 20  # Pixels per grid tile (good balance for visibility + detail)

# Grid dimensions (playable area)
GRID_COLS = 36  # ~720px wide playable
GRID_ROWS = 26  # ~520px tall playable
# Centered play area
PLAY_AREA_OFFSET_X = (SCREEN_WIDTH - (GRID_COLS * TILE_SIZE)) // 2
PLAY_AREA_OFFSET_Y = 40  # Leave room for UI at top

# Colors (vibrant retro-modern palette)
COLOR_BG = (20, 15, 35)          # Dark underground purple-blue
COLOR_DIRT_BASE = (139, 90, 43)  # Warm brown dirt
COLOR_DIRT_HIGHLIGHT = (160, 110, 60)
COLOR_DIRT_SHADOW = (100, 65, 30)
COLOR_TUNNEL = (30, 25, 45)      # Darker tunnel color
COLOR_CHERRY = (220, 40, 60)     # Bright red cherries
COLOR_APPLE = (200, 50, 50)      # Apple red
COLOR_POWERBALL = (255, 200, 50) # Glowing yellow-orange
COLOR_PLAYER = (255, 80, 120)    # Pinkish clown accents (temp)
COLOR_TEXT = (255, 255, 255)
COLOR_UI_BG = (40, 30, 60)

# Game settings
START_LIVES = 3
CHERRIES_TO_COLLECT = 20  # For this prototype level

# Player
PLAYER_SPEED = 3.5  # Pixels per frame (smooth movement)
DIG_COOLDOWN = 80     # ms between digs (prevents spam, feels weighty)

# Powerball (stub values for v0.1)
POWERBALL_SPEED = 6
POWERBALL_COOLDOWN = 400  # ms
