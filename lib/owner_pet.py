class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self,name, pet_type, owner = None) -> None:
        self.name = name
        self.pet_type = pet_type 
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, val):
        if val not in Pet.PET_TYPES:
            raise ValueError('Pet type not found in our system, the pet type must include {}'.format(','.join(Pet.PET_TYPES)))
        else:
            self._pet_type = val


class Owner:
    
    def __init__(self, name) -> None:
        self.name = name

    def return_all_owner_pets(self):
        return [{'name': pet.name, 'type': pet.type} for pet in Pet.all if pet.owner == self]
    
    def pets(self):
        return Pet.all
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise ValueError("pet must be an instance of class Pet")
        
    def get_sorted_pets(self):
        sorted_list = sorted(Pet.all, key = lambda p: p.name)
        return sorted_list