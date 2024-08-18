from abc import ABC
from enums import SpellType

class Equipment(ABC):
    def __init__(self, name, desc, image, weight):
        self.name = name
        self.desc = desc
        self.image = image
        self.weight = weight

    # def to_dict(self):
    #     return {
    #         'name': self.name,
    #         'desc': self.desc,
    #         'image': self.image,
    #         'weight': self.weight
    #     }

class Armor(Equipment):
    def __init__(self, name, desc, image, weight, defenses): # where defenses is a placeholder for all defenses an armor has
        super().__init__(name, desc, image, weight)
        self.defenses = defenses

class Weapon(Equipment):
    def __init__(self, name, desc, image, weight, str_req, dex_req, int_req, faith_req):
        super().__init__(name, desc, image, weight)
        self.str_req = str_req
        self.dex_req = dex_req
        self.int_req = int_req
        self.faith_req = faith_req

class Spell(Equipment):
    def __init__(self, name, desc, image, int_req, faith_req, attunement, type, fp):
        super().__init__(name, desc, image, 0)
        self.int_req = int_req
        self.faith_req = faith_req
        self.attunement = attunement
        self.type = type
        self.fp = fp


# class Ring