import random

card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

cardtype = random.randrange(0, 4)
cardnum = random.randrange(0, 13)
if cardtype == 0:
    print("당신이 뽑은 카드는 하트", )
elif cardtype == 1:
    pass
elif cardtype == 2:
    pass
elif cardtype == 3: