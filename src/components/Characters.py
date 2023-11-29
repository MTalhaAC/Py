import random

class Characters:
  def __init__(self, name,health=100, score=0, ability=100):
    self.name = name
    self.health = health
    self.score = score
    self.ability = ability
    self.damage = random.randint(1,20)
  
  def calculate_damage(self):
        self.damage = random.randint(1, 20)
  def attack(self, other):
    self.calculate_damage()
    other.health -= self.damage
    self.score += self.damage
    print(f"{self.name} attacks {other.name} and deals {self.damage} self.damage.")

    if other.health <= 0:
      print(f"{other.name} has been defeated!")
      other.health = 0
    else:
      print(f"{other.name} has {other.health} health remaining.")
    return self.damage
  def getInfo(self):
    print(f"{self.name} has the health {self.health}, score {self.score} and ability {self.ability}")


# Player1 = Characters("Player1")
  # Player2 = Characters("Player2")

  # while Player1.health > 0 and Player2.health > 0:
    
  #   Player1.getInfo()
  #   Player2.getInfo()
  #   # first round Player1 attacks Player2
  #   Player1.attack(Player2)

  #   if Player2.health <= 0:
  #     break

  #   Player2.attack(Player1)
  # print("Game over")

  # if Player1.health > 0:
  #   print(f"Player win {Player1.name} has score {Player1.score}")
  # elif Player2.health > 0:
  #   print(f"Player win {Player2.name} has score {Player2.score}")
