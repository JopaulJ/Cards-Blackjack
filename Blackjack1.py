from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title('My Card Game')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("1200x800")
root.configure(background = "green")


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
    global dealer, player, dealer_spot, player_spot
    dealer = []
    player = []
    dealer_spot = 0
    player_spot = 0

    # Grab a random card for dealer, remove that card from deck and add to dealer list and output to screen
    card = random.choice(deck)
    deck.remove(card)
    dealer.append(card)
    global dealer_image
    dealer_image = resize_cards(f'Cards_images/{card}.png')
    dealer_label.config(image = dealer_image)

    # Grab a random card for player
    card = random.choice(deck)
    deck.remove(card)
    player.append(card)
    global player_image
    player_image = resize_cards(f'Cards_images/{card}.png')
    player_label.config(image = player_image)

    # Put remaining cards in title bar
    root.title(f"My Card Game - {len(deck)} Cards left")

def dealer_hit():
    pass

def player_hit():
    pass

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

deal_button = Button(button_frame, text = "Hit", font = ("Helvetica bold", 14), command = deal_cards)
deal_button.grid(row = 0, column = 1, padx = 10)

stand_button = Button(button_frame, text = "Stand", font = ("Helvetica bold", 14))
stand_button.grid(row = 0, column = 2)

# Start game
shuffle()

root.mainloop()