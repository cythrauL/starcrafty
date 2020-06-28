class Economy(object):
    '''
    An object to keep track of our income, and the excess we have.
    All quantities are per in-game minute (42.86s on faster)

    900 mins
    320 gas
    225 per mule
    '''
    def __init__(self, saturated_bases, vespene_geysers, mules=0):
        self.mineral_income = 900 * saturated_bases
        self.gas_income = vespene_geysers * 320
        self.mineral_income += mules * 225

    def calculate(self, production):
        prod = {}
        for product in production:
            for key in product:
                if not key in prod:
                    prod[key] = 0
                prod[key] += product[key]
        output = {
            'mineral_surplus' : self.mineral_income - prod['minerals_used'],
            'gas_surplus' : self.gas_income - prod['gas_used'],
            'units' : prod
        }
        return output