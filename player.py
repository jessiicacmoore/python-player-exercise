class Player:
  def __init__(self):
    self.gold_coins = 0
    self.health_points = 10
    self.lives = 5

  def __str__(self):
    return f"Gold Coins: {self.gold_coins}\nHealth Points: {self.health_points}\nLives: {self.lives}"

  def level_up(self):
    self.lives += 1

  def collect_treasure(self):
    self.gold_coins += 1
    if self.gold_coins % 10 == 0:
      self.level_up()

  def do_battle(self, damage):
    self.health_points -= damage
    if self.health_points < 1:
      self.lives -= 1
      self.health_points = 10
    if self.lives < 1:
      self.restart()

  def restart(self): 
    self.gold_coins = 0
    self.health_points = 10
    self.lives = 5

player1 = Player()

print(player1)

print()
print("Level up!")
player1.level_up()
print(player1)

print()
print("Collect treasure!")
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()

print(player1)

print()
print("Go to battle! ... Oh no, you've taken 11 damage!")
player1.do_battle(11)
print(player1)

player1.do_battle(11)
player1.do_battle(11)
player1.do_battle(11)
player1.do_battle(11)
player1.do_battle(11)
player1.do_battle(11)

print("Wow, you're really bad at this game. -1 life")
print(player1)