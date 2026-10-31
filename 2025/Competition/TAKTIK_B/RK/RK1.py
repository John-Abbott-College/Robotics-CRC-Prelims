class Unit:
    def __init__(self, name: str, attack_value: int, defense_value: int, priority: int, health: int):
        self.name = name
        self.attack_value = attack_value
        self.defense_value = defense_value
        self.health = health
        self.priority = priority
        self.is_alive = True
    
    def attack(self, target: "Unit") -> None:
        #TODO: complete attack
        pass
    def defend(self, attack: int) -> None:
        #TODO: Complete defense
        pass

def combat(army1: list[Unit], army2: list[Unit]) -> list[Unit]:
    ### Vous devez implementer la logique du combat tour par tour ###
    ### You need to implement the turn based combat logic ###
    pass

def ragnarok(combats: list[tuple[str]], armies: dict[list[Unit]]) -> list[str]:
    ### Vous devez implementer les combats du ragnarok ###
    ### You have to implement the combats of the ragnarok ###
    pass