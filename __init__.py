from Econ import Economy
from Production import TerranProduction, Barracks, Factory, Starport
import pprint

def protoss():
    econ = Economy(2, 3, 1)

    production = [
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.REACTOR).produce_marines(),
        Factory(TerranProduction.TECH_LAB).produce_tanks(),
        Starport(TerranProduction.REACTOR).produce_medivacs(),
    ]

    print("Two bases, three gas, one of the OCs mule-ing\n")
    output = econ.calculate(production)
    pprint.pprint(output)

    econ = Economy(3, 4, 3)

    production = [
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_ghosts(),
        #Barracks(TerranProduction.REACTOR).produce_marines(),
        Barracks(TerranProduction.REACTOR).produce_marines(),
        Barracks(TerranProduction.REACTOR).produce_marines(),
        Starport(TerranProduction.REACTOR).produce_medivacs(),
    ]

    print("\nThree bases, 4gas, three of the OCs mule-ing\n")

    scvs = 3*16 + 4*3

    print(f"Need {scvs} scvs")

    output = econ.calculate(production)
    pprint.pprint(output)

    econ = Economy(4, 6, 2)

    production = [
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_ghosts(),
        Barracks(TerranProduction.TECH_LAB).produce_ghosts(),
        #Barracks(TerranProduction.REACTOR).produce_marines(),
        Barracks(TerranProduction.REACTOR).produce_marines(),
        Barracks(TerranProduction.REACTOR).produce_marines(),
        Starport(TerranProduction.REACTOR).produce_medivacs(),
        Starport(TerranProduction.REACTOR).produce_liberators(),
        Starport().produce_liberators(),
    ]

    print("\nFour bases, 6gas, two of the OCs mule-ing\n")

    scvs = 4*16 + 6*3

    print(f"Need {scvs} scvs")

    output = econ.calculate(production)
    pprint.pprint(output)

def zerg():
    econ = Economy(2, 2, 2)

    production = [
        Barracks(TerranProduction.TECH_LAB).produce_marines(),
        Barracks(TerranProduction.REACTOR).produce_marines(),
        Barracks(TerranProduction.REACTOR).produce_marines(),
        Factory(TerranProduction.TECH_LAB).produce_tanks(),
        Starport(TerranProduction.REACTOR).produce_medivacs(),
    ]

    print("Two bases, two gas, both of the OCs mule-ing\n")
    output = econ.calculate(production)
    pprint.pprint(output)

    econ = Economy(3, 4, 3)

    production = [
        Barracks(TerranProduction.REACTOR).produce_marines(),
        Barracks(TerranProduction.REACTOR).produce_marines(),
        Barracks(TerranProduction.REACTOR).produce_marines(),
        Barracks(TerranProduction.REACTOR).produce_marines(),
        Barracks(TerranProduction.TECH_LAB).produce_marines(),
        Barracks().produce_marines(),
        Barracks().produce_marines(),
        Barracks().produce_marines(),
        Factory(TerranProduction.TECH_LAB).produce_tanks(),
        Starport(TerranProduction.REACTOR).produce_medivacs(),
    ]

    print("\nThree bases, 4gas, three of the OCs mule-ing\n")

    scvs = 3*16 + 4*3

    print(f"Need {scvs} scvs")

    output = econ.calculate(production)
    pprint.pprint(output)

    econ = Economy(4, 6, 2)

    production = [
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_marauders(),
        Barracks(TerranProduction.TECH_LAB).produce_ghosts(),
        Barracks(TerranProduction.TECH_LAB).produce_ghosts(),
        #Barracks(TerranProduction.REACTOR).produce_marines(),
        Barracks(TerranProduction.REACTOR).produce_marines(),
        Barracks(TerranProduction.REACTOR).produce_marines(),
        Starport(TerranProduction.REACTOR).produce_medivacs(),
        Starport(TerranProduction.REACTOR).produce_liberators(),
        Starport().produce_liberators(),
    ]

    print("\nFour bases, 6gas, two of the OCs mule-ing\n")

    scvs = 4*16 + 6*3

    print(f"Need {scvs} scvs")

    output = econ.calculate(production)
    pprint.pprint(output)

if __name__ == "__main__":
    zerg()