class Player:
    def __init__(self, speed, power, accuracy, stamina):
        self.speed = speed
        self.power = power
        self.accuracy = accuracy
        self.stamina = stamina

class Attacher(Player):
    def __init__(self, speed, power, accuracy, stamina):
        super.__init__(speed, power, accuracy, stamina)

    def attack(self):
        print('Attack')


class Defender(Player):
    def __init__(self, speed, power, accuracy, stamina):
        super.__init__(speed, power, accuracy, stamina)

    def defend(self):
        print('Defend')


class SemiDefender(Player):
    def __init__(self, speed, power, accuracy, stamina):
        super.__init__(speed, power, accuracy, stamina)

    def semiDefend(self):
        print('semiDefend')


class GoalKeeper(Player):
    def __init__(self, speed, power, accuracy, stamina):
        super.__init__(speed, power, accuracy, stamina)

    def goalKeep(self):
        print('Keeped the goal')
