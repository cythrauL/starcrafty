from Econ import Economy
from Production import TerranProduction, Barracks, Factory, Starport
import pprint

if __name__ == "__main__":
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
        Barracks(TerranProduction.TECH_LAB).produce_ghosts(),
        Barracks(TerranProduction.REACTOR).produce_marines(),
        Barracks(TerranProduction.REACTOR).produce_marines(),
        Barracks(TerranProduction.REACTOR).produce_marines(),
        Starport().produce_medivacs(), #not reactored, or just don't constant produce
        Starport(TerranProduction.REACTOR).produce_liberators()
    ]

    print("\nThree bases, 4gas, two of the OCs mule-ing\n")

    scvs = 3*16 + 4*3

    print(f"Need {scvs} scvs")

    output = econ.calculate(production)
    pprint.pprint(output)
