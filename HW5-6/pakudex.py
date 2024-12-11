from pakuri import Pakuri as Pak
class Pakudex:
    def __init__(self, capacity = 20):
        self.__capacity = int(capacity)
        self.__pakuriList = []
    def get_size(self):
        return len(self.__pakuriList)
    def get_capacity(self):
        return self.__capacity
    def get_species_array(self):
        if self.get_size() == 0:
            return None
        return [pakur.get_species() for pakur in self.__pakuriList]
    def get_stats(self, species):
        for pakuri in self.__pakuriList:
            if pakuri.get_species() == species:
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        return None
    def sort_pakuri(self):
        self.__pakuriList = sorted(self.__pakuriList)
    def add_pakuri(self, species):
        if self.get_size() < self.__capacity:
            new_pakuri = Pak(species)
            self.__pakuriList.append(new_pakuri)
            return True
        return False
    def evolve_species(self, species):
        for pakuri in self.__pakuriList:
            if pakuri.get_species() == species:
                pakuri.evolve()
                return True
        return False


