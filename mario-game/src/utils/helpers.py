def load_image(file_path):
    """Load an image from the specified file path."""
    import pygame
    try:
        image = pygame.image.load(file_path)
        return image
    except pygame.error as e:
        print(f"Unable to load image at {file_path}: {e}")
        return None

def play_sound(file_path):
    """Play a sound from the specified file path."""
    import pygame
    try:
        sound = pygame.mixer.Sound(file_path)
        sound.play()
    except pygame.error as e:
        print(f"Unable to play sound at {file_path}: {e}")

def check_collision(rect1, rect2):
    """Check for collision between two rectangles."""
    return rect1.colliderect(rect2)