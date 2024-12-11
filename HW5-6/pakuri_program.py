#Patrick Leimer HW5-6 4/2/2024
from pakudex import *
from pakuri import *

if __name__ == '__main__':
    firstRun = False
    while True:
        if firstRun == False: #Checks for first run
            print("Welcome to Pakudex: Tracker Extraordinaire!")
            while True:
                aMaxCap = input('Enter max capacity of the Pakudex: ')
                if aMaxCap.isnumeric():
                    aMaxCap = int(aMaxCap)
                    break
                print('Please enter a valid size.')
            pakudex = Pakudex(aMaxCap)
            print(f'The Pakudex can hold {pakudex.get_capacity()} species of Pakuri.\n')
            firstRun = True
        print("Pakudex Main Menu\n-----------------\n1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit\n")
        choice = input('What would you like to do? ')
        if choice.isnumeric():
            choice = int(choice)
            if choice not in range(1, 7):
                print('Unrecognized menu selection!\n')
                continue
        else:
            print('Unrecognized menu selection!\n')
            continue

        if choice == 1: #Listing Pokedex
            if pakudex.get_species_array() != None:
                print('Pakuri In Pakudex: ')
                for species in pakudex.get_species_array():
                    print(f"{pakudex.get_species_array().index(species) + 1}. {species}")
            else:
                print('No Pakuri in Pakudex yet!\n')
            print()
        elif choice == 2: #Showing a Pokemon
            speciesToDisplay = input('Enter the name of the species to display: ')
            if pakudex.get_species_array() != None:
                for species in pakudex.get_species_array():
                    if speciesToDisplay == species:
                        stats = pakudex.get_stats(speciesToDisplay)
                        print(f'Species: {speciesToDisplay}\nAttack: {stats[0]}\nDefense: {stats[1]}\nSpeed: {stats[2]}')
                        print()
                        break
                else:
                    print('Error: No such Pakuri!\n')
            else:
                print('Error: No such Pakuri!\n')
        elif choice == 3: #Add a Pokemon
            notInPakudex = True
            pakudexName = None
            if pakudex.get_species_array() != None:
                if (pakudex.get_capacity() <= len(pakudex.get_species_array())):
                    print('Error: Pakudex is full!\n')
                else:
                    pakudexName = input('Enter the name of the species to add: ')
                    for species in pakudex.get_species_array():
                        if species == pakudexName:
                            notInPakudex = False
                    if (notInPakudex == True):
                        pakudex.add_pakuri(pakudexName)
                        print(f'Pakuri species {pakudexName} successfully added!\n')
                    elif pakudex.get_species_array() != None:
                        if len(pakudex.get_species_array()) >= pakudex.get_capacity():
                            print('Error: Pakudex is full!\n')
                    else:
                        print('Error: Pakudex already contains this species!\n')
            else:
                pakudexName = input('Enter the name of the species to add: ')
                pakudex.add_pakuri(pakudexName)
                print(f'Pakuri species {pakudexName} successfully added!\n')

        elif choice == 4: #evolve pokemon
            speciesToEvolve = input('Enter the name of the species to evolve: ')
            notInPakudex = True
            if pakudex.get_species_array() != None:
                for species in pakudex.get_species_array():
                    if species == speciesToEvolve:
                        notInPakudex = False
                    if notInPakudex == False:
                        evolved = pakudex.evolve_species(species)
                        if evolved == True:
                            print(f'{species} has evolved!\n')
                            break
            if notInPakudex == True:
                print('Error: No such Pakuri!\n')

        elif choice == 5: #Sort Pokedex
            pakudex.sort_pakuri()
            print('Pakuri have been sorted!\n')
        elif choice == 6:
            print('Thanks for using Pakudex! Bye!')
            break