class Player:
  def __init__(self):
    self.gold_coins = 0
    self.health_points = 10
    self.lives = 5

  def __str__(self):
    return f"Gold Coins: {self.gold_coins}\nHealth Points: {self.health_points}\nLives: {self.lives}"

  def level_up(self):
    self.lives += 1

player1 = Player()

print(player1)

print()
print("Level up!")
player1.level_up()
print(player1)

