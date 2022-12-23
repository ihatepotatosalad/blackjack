
import random



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def play_blackjack():
    def calculate_total(hand):
        total = 0
        for i in hand:           
            total += i
        if 11 in hand and total > 21:
                hand.remove(11)
                hand.append(1)
                return calculate_total(hand)
        else:
            return total


    def user_draw():
        user_hand.append(random.choice(cards))
        


    def computer_draw():
        computer_hand.append(random.choice(cards))
    user_hand=[]
    computer_hand = []


    user_draw()
    user_draw()
    computer_draw()
    computer_draw()

    user_total= calculate_total(user_hand)
    computer_total = calculate_total(computer_hand)

    

    print(f'your cards {user_hand}, total: {calculate_total(user_hand)}')
    print(f'computers first card is {computer_hand[0]}')
    in_session =True
    while in_session:

        next_draw = input('WOuld you like to draw again or pass type y or n: ')

        if next_draw == 'y':
            if calculate_total(computer_hand) < 17:
                computer_draw()

            computer_total = calculate_total(computer_hand)
            user_draw()
            user_total= calculate_total(user_hand)
            if user_total > 21:
                print('YOU LOSE you hve gone over 21')
                print(f'user final hand {user_hand} total: {user_total}')
                print(f'computer final hand: {computer_hand} total: {computer_total}')
                in_session = False
            elif computer_total > 21:
                print('YOU WIN computer went over 21')
                print(f'user final hand {user_hand} total: {user_total}')
                print(f'computer final hand: {computer_hand} total: {computer_total}')
                in_session = False
            else:
                print(f'your cards {user_hand}, total: {calculate_total(user_hand)}')
        else:
            if user_total > computer_total:
                print(f'YOU WON user final hand {user_hand} total: {user_total}')
                print(f'computer final hand: {computer_hand} total: {computer_total}')
                in_session = False
            elif user_total == computer_total:
                print(f'DRAW user final hand {user_hand} total: {user_total}')
                print(f'computer final hand: {computer_hand} total: {computer_total}')
                in_session = False

            else:
                print(f'YOU LOST user final hand {user_hand} total: {user_total}')
                print(f'computer final hand: {computer_hand} total: {computer_total}')
                in_session = False


    

    

    


start_game = input('Do you wanna ply Blackjack? y or n: ')

if start_game == 'y':
    play_blackjack()

