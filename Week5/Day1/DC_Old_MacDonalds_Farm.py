class farm:
    def __init__(self, farm_name):
        self.farm_name=farm_name
        self.farm_dic = {}
    def update_farm (self,name,amount):
        self.farm_dic.update({name:amount})
    def print_name(self):
        print(self.farm_name)
    def print_dic(self):
        for key in self.farm_dic:
            print(f'{key} : {self.farm_dic[key]}')
    def get_animal_types(self):
        animal_types_list = []
        for name in self.farm_dic:
            animal_types_list.append(name)
        return animal_types_list
        print(animal_types_list)
    def get_short_info(self):
        sentance = " and ".join(self.get_animal_types())
        print(f'McDonalds farm has {sentance}')


old_Macs=farm("Old MacDonalds Farm")
old_Macs.update_farm("cow",5)
old_Macs.update_farm("sheep",2)
old_Macs.update_farm("goat",12)
old_Macs.print_name()
old_Macs.print_dic()
old_Macs.get_animal_types()
old_Macs.get_short_info()