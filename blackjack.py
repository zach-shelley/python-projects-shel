import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

want_to_play = True
while want_to_play:
    play_game = input('Do you want to play a game of Blackjack? Type "y" or "n"').lower()
    if play_game == 'y':
        want_to_play = False
    elif play_game == 'n':
        print('Next time')
        continue

player_card = random.choice(cards)
player_card2 = random.choice(cards)
computer_card = random.choice(cards)

computer_cards = [computer_card]
player_cards = [player_card, player_card2]

def hit():

    print(f'Player total = {sum(player_cards)} Computer total = {sum(computer_cards)}')

    while sum(player_cards) < 21:
            hit_or_stay = input('Type "y" to hit, type "n" to stay: ')
            if hit_or_stay == 'y':
                new_player_card = random.choice(cards)
                player_cards.append(new_player_card)
                player_total = adjust_for_ace(player_cards)
                print(f'Player drew a {new_player_card}')
                print(f'Player total: {sum(player_cards)}')
            elif hit_or_stay == 'n':
                computer_second_card = random.choice(cards)
                computer_cards.append(computer_second_card)
                computer_total = adjust_for_ace(computer_cards)
                print(f'Computer reveals second card: {computer_second_card}')
                print(f'Computer total: {sum(computer_cards)}')
                while sum(computer_cards) <= 16:
                    new_computer_card = random.choice(cards)
                    computer_cards.append(new_computer_card)
                    computer_total = adjust_for_ace(computer_cards)
                    print(f'Computer drew a {new_computer_card}')

                    if sum(computer_cards) == 21:
                        print(f'Player has {sum(player_cards)}, Computer has {sum(computer_cards)}.')
                        break

                    elif sum(computer_cards) > 21:
                        print(f'Computer has {sum(computer_cards)}.')
                        break
                    elif sum(computer_cards) < 21 and sum(computer_cards) > 16:
                        print(f'Computer has {sum(computer_cards)}.')
                        break
                break

def adjust_for_ace(hand):
    total = sum(hand)
    # While we're busting AND we have an ace worth 11, convert it to 1
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1  # Find first 11 and change it to 1
        total = sum(hand)
    return total

def compare():
    if sum(player_cards) > 21:

        print(f'You are at {sum(player_cards)} - Bust! You lose')

    elif sum(computer_cards) > 21:

        print(f'Computer busts! You win!')

    elif sum(computer_cards) == sum(player_cards):

        print('It\'s a tie!')

    elif sum(computer_cards) == 21:

        print(f'Computer Blackjack! Computer wins.')

    elif sum(player_cards) > sum(computer_cards):

        print(f'Player has {sum(player_cards)}, Computer has {sum(computer_cards)} - Player wins!')

    elif sum(player_cards) < sum(computer_cards):

        print(f'Player has {sum(player_cards)}, Computer has {sum(computer_cards)} - Computer wins!')

game_on = True
while game_on:
    print(f'Your cards: {[player_card, player_card2]}, current score: {player_card + player_card2}')
    print(f'Computer\'s first card: {computer_card}')

    hit()
    compare()

    play_again = input('Would you like to play again? y/n').lower()
    if play_again == 'y':

        player_cards = []
        computer_cards = []
        player_card = random.choice(cards)
        player_card2 = random.choice(cards)
        computer_card = random.choice(cards)

        computer_cards = [computer_card]
        player_cards = [player_card, player_card2]
        continue
    if play_again == 'n':
        print('Thanks for playing!')
        game_on = False
