# from races.race_factory import * # Import de race et transformation aussi
# from attacks.attack_factory import * # Import attack aussi
# from objects.object_factory import * # Import object aussi
# from entities.deck.deck_builder import *
# from entities.warrior.warrior import Warrior

from managers.team_manager import TeamManager

def test_race_transformation():
    saiyan = Saiyan()
    saiyan.super_saiyan()
    saiyan.super_saiyan_2()
    saiyan.base_form()

def test_attack_factory():
    kame = AttackFactory.create_attack('Kamehameha')
    print(kame.name)

def test_deck_builder():
    deck_builder = DeckBuilder()
    deck_builder.addCard(AttackFactory.create_attack('Kamehameha'))
    deck_builder.addCard(AttackFactory.create_attack('Kamehameha'))
    deck_builder.addCard(ObjectFactory.create_object('SenzuBean'))
    deck_builder.addCard(ObjectFactory.create_object('SenzuBean'))
    deck = deck_builder.build()
    for card in deck.cards:
        # card.use("", "")
        pass

def test_race_factory():
    race = RaceFactory.create_race("Saiyan")
    print(race.get_name())

def test_warrior():
    warrior = Warrior("Son Goku", "Saiyan")
    print(warrior.get_race_name())

def test_fight():
    goku = Warrior("Son Goku", "Saiyan")
    vegeta = Warrior("Vegeta", "Saiyan")

    piccolo = Warrior("Piccolo", "Namekian")

    player_team = TeamManager.get_instance("player")
    enemy_team = TeamManager.get_instance("enemy")

    player_team.set_warrior(goku)
    player_team.set_warrior(vegeta)

    enemy_team.set_warrior(piccolo)

    player_active_warrior = player_team.get_active_warrior()
    enemy_active_warrior = enemy_team.get_active_warrior()

    # NOW FIGHT
    print(f"{player_active_warrior.get_name()} possède {player_active_warrior.get_life()} points de vie")
    load_kick_card = CardFactory.create_card(AttackFactory.create_attack("LoadKick"))
    enemy_active_warrior.use_card(load_kick_card, player_active_warrior)
    print(f"{player_active_warrior.get_name()} possède {player_active_warrior.get_life()} points de vie")

    senzu_card = CardFactory.create_card(ObjectFactory.create_object("SenzuBean"))
    player_active_warrior.use_card(senzu_card, enemy_active_warrior)
    print(f"{player_active_warrior.get_name()} possède {player_active_warrior.get_life()} points de vie")






# test_race_transformation() # Test OK
# test_attack_factory() # Test OK
# test_deck_builder() # Cards use correctly
# test_race_factory() # Test OK
# test_warrior() # Test OK
# test_fight() # Test OK
