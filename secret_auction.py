import random

items_list = ['four Wheeler', 'week cruise vacation', 'new MAC laptop', 'surfing class' ]

print('Welcome to the secret auction program.')
bidding_item = random.choice(items_list)
print(f'Next up, you will be bidding for a {bidding_item}')

bidder_auctions = {}

bid_on = True
while bid_on:

    bidder_name = input('What is your name?: ').lower()
    bid_amount = int(input('What\'s your bid?: $'))

    other_bidders = input('Are there any other bidders? Type "yes" or "no"').lower()

    bidder_auctions[bidder_name] = bid_amount
    if other_bidders == 'yes':
        print('\n' * 20)
        continue
    else:
        break

highest_bid = 0
highest_bidder = ''
for bids in bidder_auctions:
    if bidder_auctions[bids] > highest_bid:
        highest_bid = bidder_auctions[bids]
        highest_bidder = bids

print(f'{highest_bidder} wins the auction!')