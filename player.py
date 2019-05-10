class Player:
  def __init__(self):
    self.gold_coins = 0
    self.health_points = 10
    self.lives = 5

  def __str__(self):
    return f"Gold Coins: {self.gold_coins}\nHealth Points: {self.health_points}\nLives: {self.lives}"

  def level_up(self):
    self.lives += 1
    print(f"You have leveled up! Your lives are now at: {self.lives}")
    print(player1)

  def collect_treasure(self):
    self.gold_coins += 1
    print(f"+1 coin! You now have {self.gold_coins} coins!")
    if self.gold_coins % 10 == 0:
      self.level_up()

  def do_battle(self, damage):
    self.health_points -= damage
    print(f"You have taken {damage} damage")
    if self.health_points < 1:
      self.lives -= 1
      self.health_points = 10
      print(f"You have lost a life point! Your lives are now at {self.lives}")
      print(player1)
    if self.lives < 1:
      self.restart()

  def restart(self): 
    self.gold_coins = 0
    self.health_points = 10
    self.lives = 5
    print("You are out of lives! Restarting...")
    print(player1)

player1 = Player()

print(player1)

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
player1.collect_treasure()
player1.collect_treasure()

player1.do_battle(3)
player1.do_battle(5)
player1.do_battle(6)
player1.do_battle(7)
player1.do_battle(8)
player1.do_battle(10)
player1.do_battle(7)
player1.do_battle(7)
player1.do_battle(8)
player1.do_battle(10)
player1.do_battle(7)
player1.do_battle(5)
