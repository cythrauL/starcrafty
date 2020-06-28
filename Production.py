class TerranProduction(object):
    NONE = 0
    TECH_LAB = 1
    REACTOR = 2
    def __init__(self, add_on=NONE):
        self.add_on = add_on
    def calculate_cost(self, unit, minerals, gas, supply, time, multiplier = 1):
        time_val = (60.0 / time) * multiplier
        return {
            unit: time_val,
            'minerals_used': minerals*time_val,
            'gas_used': gas*time_val,
            'supply_used': supply*time_val, 
        }

class Barracks(TerranProduction):
    def produce_marines(self):
        if (self.add_on == TerranProduction.REACTOR):
            return self.calculate_cost('marines', 50, 0, 1, 18, 2)
        else:
            return self.calculate_cost('marines', 50, 0, 1, 18)
    
    def produce_marauders(self):
        if(self.add_on != TerranProduction.TECH_LAB):
            raise TypeError("Non tech-labbed rax can't produce marauders")
        else:
            return self.calculate_cost('marauders', 100, 25, 2, 21)
    
    def produce_ghosts(self):
        if(self.add_on != TerranProduction.TECH_LAB):
            raise TypeError("Non tech-labbed rax can't produce ghosts")
        else:
            return self.calculate_cost('ghosts', 150, 125, 2, 29)

class Factory(TerranProduction):
    def produce_tanks(self):
        if (self.add_on != TerranProduction.TECH_LAB):
            raise TypeError("Non tech-labbed fact can't produce tanks")
        else:
            return self.calculate_cost('tanks', 150, 125, 3, 32)
    
    def produce_mines(self):
        if (self.add_on == TerranProduction.REACTOR):
            return self.calculate_cost('widow_mines', 75, 25, 2, 21, 2)
        else:
            return self.calculate_cost('widow_mines', 75, 25, 2, 21)
    
    def produce_hellions(self):
        if(self.add_on == TerranProduction.REACTOR):
            return self.calculate_cost('hellions', 100, 0, 2, 21, 2)
        else:
            return self.calculate_cost('hellions', 100, 0, 2, 21)
    
    def produce_hellbats(self):
        m = self.produce_hellions()
        m['hellbats'] = m['hellions']
        del m.hellions
        return m
    
    def produce_cyclones(self):
        if(self.add_on != TerranProduction.TECH_LAB):
            raise TypeError("Non tech-labbed fact can't produce cyclones")
        else:
            return self.calculate_cost('cyclones', 150, 100, 32, 3)
    
    def produce_thors(self):
        if (self.add_on != TerranProduction.TECH_LAB):
            raise TypeError("Non tech-labbed fact can't produce thors")
        else:
            return self.calculate_cost('thors', 300, 200, 6, 43)

class Starport(TerranProduction):
    def produce_medivacs(self):
        if(self.add_on == TerranProduction.REACTOR):
            return self.calculate_cost('medivacs', 100, 100, 2, 30, 2)
        else:
            return self.calculate_cost('medivacs', 100, 100, 2, 30)
    
    def produce_vikings(self):
        if(self.add_on == TerranProduction.REACTOR):
            return self.calculate_cost('vikings', 150, 75, 2, 30, 2)
        else:
            return self.calculate_cost('vikings', 150, 75, 2, 30)
    
    def produce_liberators(self):
        if(self.add_on == TerranProduction.REACTOR):
            return self.calculate_cost('libs', 150, 150, 3, 43, 2)
        else:
            return self.calculate_cost('libs', 150, 150, 3, 43)

    def produce_ravens(self):
        if (self.add_on != TerranProduction.TECH_LAB):
            raise TypeError("Non tech-labbed port can't produce ravens")
        else:
            return self.calculate_cost('ravens', 100, 200, 2, 43)

    def produce_banshees(self):
        if (self.add_on != TerranProduction.TECH_LAB):
            raise TypeError("Non tech-labbed port can't produce banshees")
        else:
            return self.calculate_cost('banshees', 150, 100, 3, 43)
    
    def produce_battlecruisers(self):
        if (self.add_on != TerranProduction.TECH_LAB):
            raise TypeError("Non tech-labbed port can't produce battlecruisers")
        else:
            return self.calculate_cost('battlecruisers', 400, 300, 6, 64)
       

