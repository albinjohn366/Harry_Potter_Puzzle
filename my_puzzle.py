# HARRY POTTER PUZZLE

from my_logic_of_knowledge import *

people = ['Gilderoy', 'Minerva', 'Pomona', 'Horace']
houses = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclow']

symbols = []
knowledge = And(Or(Symbol('GilderoyGryffindor'), Symbol('GilderoyRavenclow')),
                Not(Symbol('PomonaSlytherin')), Symbol('MinervaGryffindor'))

# Person should belong to any of the 4 houses
for person in people:
    knowledge.add(Or(Symbol('{}Gryffindor'.format(person)),
                     Symbol('{}Slytherin'.format(person)),
                     Symbol('{}Hufflepuff'.format(person)),
                     Symbol('{}Ravenclow'.format(person))))

# Adding symbols to the list of symbols
for person in people:
    for house in houses:
        symbols.append(Symbol('{}{}'.format(person, house)))

# Same person can't have different houses
for person in people:
    for house_1 in houses:
        for house_2 in houses:
            if house_1 != house_2:
                knowledge.add(Implication(Symbol('{}{}'.format(person,
                                                               house_1)),
                                          Not(Symbol('{}{}'.format(person,
                                                                   house_2)))))

# Same house can't be occupied by more than one person among the 4
for house in houses:
    for p1 in people:
        for p2 in people:
            if p1 != p2:
                knowledge.add(Implication(Symbol('{}{}'.format(p1, house)),
                                          Not(Symbol('{}{}'.format(p2,
                                                                   house)))))

# Doing model check for each symbol
for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol.symbols())
