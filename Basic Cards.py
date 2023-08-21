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
    global dealer, player
    dealer = []
    player = []

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
dealer_frame.grid(row = 0, column = 0, padx = 50, ipadx = 20, ipady = 5)

player_frame = LabelFrame(my_frame, text = "Player", bd = 0, font = ("Helvetica bold", 18))
player_frame.grid(row = 0, column = 1, ipadx = 20, ipady = 5)

# Put cards in frame
dealer_label = Label(dealer_frame, text = '')
dealer_label.pack(pady = 20)

player_label = Label(player_frame, text = '')
player_label.pack(pady = 20)

# Create a couple buttonsS
shuffle_button = Button(root, text = "Suffle Deck", font = ("Helvetica bold", 14), command = shuffle)
shuffle_button.pack(pady = 20)

deal_button = Button(root, text = "Deal Card", font = ("Helvetica bold", 14), command = deal_cards)
deal_button.pack(pady = 20)

# Start game
shuffle()

root.mainloop()