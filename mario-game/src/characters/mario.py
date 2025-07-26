class Mario:
    def __init__(self, position=(0, 0), lives=3):
        self.position = position
        self.lives = lives
        self.coins = 0

    def jump(self):
        # Logic for jumping
        print("Mario jumps!")

    def run(self):
        # Logic for running
        print("Mario runs!")

    def collect_coin(self):
        self.coins += 1
        print(f"Coins collected: {self.coins}")