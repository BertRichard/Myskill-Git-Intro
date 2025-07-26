def setup_level():
    # Define the layout of the level
    level_layout = [
        "##########",
        "#        #",
        "#  M     #",
        "#        #",
        "##########"
    ]
    
    return level_layout

def create_obstacles():
    # Define obstacles in the level
    obstacles = [
        {"type": "block", "position": (2, 2)},
        {"type": "enemy", "position": (3, 3)}
    ]
    
    return obstacles

def initialize_level():
    layout = setup_level()
    obstacles = create_obstacles()
    
    # Initialize the level with layout and obstacles
    level_data = {
        "layout": layout,
        "obstacles": obstacles
    }
    
    return level_data

if __name__ == "__main__":
    level = initialize_level()
    print("Level initialized:", level)