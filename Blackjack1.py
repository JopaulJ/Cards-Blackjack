from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('My Card Game')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("1200x800")
root.configure(background = "green")


# Test for blackjack on shuffle
def blackjack_suffle(player):
    if player == "dealer":
        if len(dealer_score) == 2:
            if dealer_score[0] + dealer_score[1] == 21:
                messagebox.showinfo("Dealer Wins!", "Blackjack! Dealer Wins")
                # Disable buttons
                hit_button.config(state = "disabled")
                stand_button.config(state = "disabled")

    if player == "player":
        if len(player_score) == 2:
            if player_score[0] + player_score[1] == 21:
                messagebox.showinfo("Player Wins!", "Blackjack! Player Wins")
                # Disable buttons
                hit_button.config(state = "disabled")
                stand_button.config(state = "disabled")


# Resize Cards
def resize_cards(card):
    # Open the image
    our_card_img = Image.open(card)
    # Resize the image
    our_card_resize_image =  our_card_img.resize((128, 176))
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)
    return our_card_image


# Shuffle the cards
def shuffle():

    # Enable buttons
    hit_button.config(state = "normal")
    stand_button.config(state = "normal")

    # Clear all old cards from prev games
    dealer_label_1.config(image = '')
    dealer_label_2.config(image = '')
    dealer_label_3.config(image = '')
    dealer_label_4.config(image = '')
    dealer_label_5.config(image = '')

    player_label_1.config(image = '')
    player_label_2.config(image = '')
    player_label_3.config(image = '')
    player_label_4.config(image = '')
    player_label_5.config(image = '')

    # Define deck
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2, 15)
    # 11 = Jack, 12 = Queen, 13 = King, 14 = Ace

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    # Create our players
    global dealer, player, dealer_spot, player_spot, dealer_score, player_score
    dealer = []
    player = []
    dealer_score = []
    player_score = []
    dealer_spot = 0
    player_spot = 0

    # Shuffle Two cards for player and dealer
    dealer_hit()
    dealer_hit()

    player_hit()
    player_hit()

    # Put remaining cards in title bar
    root.title(f"My Card Game - {len(deck)} Cards left")


def dealer_hit():
    global dealer_spot
    if dealer_spot < 5:
        try:
            # Grab a random card for dealer
            dealer_card = random.choice(deck)
            deck.remove(dealer_card)
            dealer.append(dealer_card)
            
            # Append to dealer score list and convert face cards to 10 or 11
            dcard = int(dealer_card.split("_", 1)[0])
            if dcard == 14:
                dealer_score.append(11)
            elif dcard == 11 or dcard == 12 or dcard == 13:
                dealer_score.append(10)
            else:
                dealer_score.append(dcard)

            # Outputing image
            global dealer_image1, dealer_image2, dealer_image3, dealer_image4, dealer_image5

            if dealer_spot == 0:
                dealer_image1 = resize_cards(f'Cards_images/{dealer_card}.png')
                dealer_label_1.config(image = dealer_image1)
                # Increment dealer spot counter
                dealer_spot += 1
            elif dealer_spot == 1:
                dealer_image2 = resize_cards(f'Cards_images/{dealer_card}.png')
                dealer_label_2.config(image = dealer_image2)
                # Increment dealer spot counter
                dealer_spot += 1
            elif dealer_spot == 2:
                dealer_image3 = resize_cards(f'Cards_images/{dealer_card}.png')
                dealer_label_3.config(image = dealer_image3)
                # Increment dealer spot counter
                dealer_spot += 1
            elif dealer_spot == 3:
                dealer_image4 = resize_cards(f'Cards_images/{dealer_card}.png')
                dealer_label_4.config(image = dealer_image4)
                # Increment dealer spot counter
                dealer_spot += 1
            elif dealer_spot == 4:
                dealer_image5 = resize_cards(f'Cards_images/{dealer_card}.png')
                dealer_label_5.config(image = dealer_image5)
                # Increment dealer spot counter
                dealer_spot += 1

            # Put remaining cards in title bar
            root.title(f"My Card Game - {len(deck)} Cards left")

        except:
           root.title('My Card Game - No cards in deck')

        # Check for blackjack
        blackjack_suffle("dealer")


def player_hit():
    global player_spot
    if player_spot < 5:
        try:
            # Grab a random card for player
            player_card = random.choice(deck)
            deck.remove(player_card)
            player.append(player_card)

            # Append to player score list and convert face cards to 10 or 11
            pcard = int(player_card.split("_", 1)[0])
            if pcard == 14:
                player_score.append(11)
            elif pcard == 11 or pcard == 12 or pcard == 13:
                player_score.append(10)
            else:
                player_score.append(pcard)

            # Outputing image
            global player_image1, player_image2, player_image3, player_image4, player_image5

            if player_spot == 0:
                player_image1 = resize_cards(f'Cards_images/{player_card}.png')
                player_label_1.config(image = player_image1)
                # Increment player spot counter
                player_spot += 1
            elif player_spot == 1:
                player_image2 = resize_cards(f'Cards_images/{player_card}.png')
                player_label_2.config(image = player_image2)
                # Increment player spot counter
                player_spot += 1
            elif player_spot == 2:
                player_image3 = resize_cards(f'Cards_images/{player_card}.png')
                player_label_3.config(image = player_image3)
                # Increment player spot counter
                player_spot += 1
            elif player_spot == 3:
                player_image4 = resize_cards(f'Cards_images/{player_card}.png')
                player_label_4.config(image = player_image4)
                # Increment player spot counter
                player_spot += 1
            elif player_spot == 4:
                player_image5 = resize_cards(f'Cards_images/{player_card}.png')
                player_label_5.config(image = player_image5)
                # Increment player spot counter
                player_spot += 1

            # Put remaining cards in title bar
            root.title(f"My Card Game - {len(deck)} Cards left")

        except:
            root.title('My Card Game - No cards in deck')

        # Check for blackjack
        blackjack_suffle("player")

"""
# Deal out the cards
def deal_cards():
    try:
        # Grab card etc etc... same as above shuffle function
        card = random.choice(deck)
        deck.remove(card)
        dealer.append(card)

        # Outputing image
        global dealer_image
        dealer_image = resize_cards(f'Cards_images/{card}.png')
        dealer_label.config(image = dealer_image)

        # Grab a random card for player
        card = random.choice(deck)
        deck.remove(card)
        player.append(card)

        # Outputing image
        global player_image
        player_image = resize_cards(f'Cards_images/{card}.png')
        player_label.config(image = player_image)

        # Put remaining cards in title bar
        root.title(f"My Card Game - {len(deck)} Cards left")

    except:
        root.title('My Card Game - No cards in deck')
"""

#####################################################################################
my_frame = Frame(root, bg = "green")
my_frame.pack(pady = 50)

# Creates frames for cards
dealer_frame = LabelFrame(my_frame, text = "Dealer", bd = 0, font = ("Helvetica bold", 18))
dealer_frame.pack(pady = 20, ipadx = 20, ipady = 5)

player_frame = LabelFrame(my_frame, text = "Player", bd = 0, font = ("Helvetica bold", 18))
player_frame.pack(ipadx = 20, ipady = 5)


# Put dealer cards in frame
dealer_label_1 = Label(dealer_frame, text = '')
dealer_label_1.grid(row = 0, column = 0, pady = 10, padx = 20)

dealer_label_2 = Label(dealer_frame, text = '')
dealer_label_2.grid(row = 0, column = 1, pady = 10, padx = 20)

dealer_label_3 = Label(dealer_frame, text = '')
dealer_label_3.grid(row = 0, column = 2, pady = 10, padx = 20)

dealer_label_4 = Label(dealer_frame, text = '')
dealer_label_4.grid(row = 0, column = 3, pady = 10, padx = 20)

dealer_label_5 = Label(dealer_frame, text = '')
dealer_label_5.grid(row = 0, column = 4, pady = 10, padx = 20)

# Put player cards in frame
player_label_1 = Label(player_frame, text = '')
player_label_1.grid(row = 1, column = 0, pady = 10, padx = 20)

player_label_2 = Label(player_frame, text = '')
player_label_2.grid(row = 1, column = 1, pady = 10, padx = 20)

player_label_3 = Label(player_frame, text = '')
player_label_3.grid(row = 1, column = 2, pady = 10, padx = 20)

player_label_4 = Label(player_frame, text = '')
player_label_4.grid(row = 1, column = 3, pady = 10, padx = 20)

player_label_5 = Label(player_frame, text = '')
player_label_5.grid(row = 1, column = 4, pady = 10, padx = 20)


# Create button frame
button_frame = Frame(root, bg = "green")
button_frame.pack(pady = 10)

# Create a couple buttonsS
shuffle_button = Button(button_frame, text = "Suffle Deck", font = ("Helvetica bold", 14), command = shuffle)
shuffle_button.grid(row = 0, column = 0)

hit_button = Button(button_frame, text = "Hit", font = ("Helvetica bold", 14), command = player_hit)
hit_button.grid(row = 0, column = 1, padx = 10)

stand_button = Button(button_frame, text = "Stand", font = ("Helvetica bold", 14))
stand_button.grid(row = 0, column = 2)

# Start game
shuffle()

root.mainloop()