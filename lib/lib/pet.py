class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")

        self.name = name
        self.pet_type = pet_type
        self.owner = None

        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of Owner class")
            self.owner = owner

        Pet.all.append(self)
