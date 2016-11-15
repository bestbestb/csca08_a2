# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:

listA = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]


def clean_message(message):
    ''' (str) -> str
    Return a copy of the message that includes only its alphabetical
    characters, where each of those characters has been converted to uppercase.
    >>> clean_message("waij12")
    'WAIJ'
    >>> clean_message("AWj12")
    'AWJ'
    >>> clean_message("11212")
    ''
    >>> clean_message("ABC")
    'ABC'
    
    '''
    # make an empty string for use
    result = ''
    # loop once for each character in the message
    for character in message:
        # if the character is alphabetical
        if character.isalpha():
            # add the character
            result += character
    return result.upper()


def encrypt_letter(character, value):
    '''(str, int) -> str
    The first parameter is a single character and the second represents a
    keystream value.  Apply the keystream value to the character to
    encrypt the character,
    and return the result.
    REQ: character must be uppercase
    >>> encrypt_letter('A', 1)
    'B'
    >>> encrypt_letter('B', 27)
    'C'
    >>> encrypt_letter('A', 15)
    'P'
    >>> encrypt_letter('G', 15)
    'V'
    
    '''

    # find the index of the character in the list
    character_index = listA.index(character)
    # index of the result is the sum of the character index and the keystream
    # value mod 26
    index_result = (character_index + value) % 26
    # find the result using the index
    result = listA[index_result]

    return result


def decrypt_letter(character, value):
    ''' (str, int) -> str
    The first parameter is a single uppercase character and the second
    represents a keystream value.  Apply the keystream value to the character
    to decrypt the character, and return the result.

    >>> decrypt_letter('B', 1)
    'A'
    >>> decrypt_letter('C', 27)
    'B'
    >>> decrypt_letter('C', 12)
    'Q'
    >>> decrypt_letter('Z', 10)
    'P'

    '''
    # find the index of the character
    character_index = listA.index(character)
    # index of the result is the sum of the character index and the keystream
    # index mod 26
    index_result = (character_index - value) % 26
    # find the result using index
    result = listA[index_result]
    return result


def swap_cards(deck, index):
    ''' (list of int, int) -> NoneType
    The first parameter represents a deck of cards and the second represents
    an index into the deck.  Swap the card at the index with the card that
    follows it. Treat the deck as circular: if the card at the index is on
    the bottom of the deck, swap that card with the top card.
    >>> deck = [1, 2, 3, 4, 5]
    >>> swap_cards(deck, 2)
    >>> deck
    [1, 2, 4, 3, 5]

    >>> deck = [1, 3, 4, 5]
    >>> swap_cards(deck, 3)
    >>> deckB
    [5, 3, 4, 1]
    
    >>> deck = [1, 2, 3, 4, 5, 7, 8]
    >>> swap_cards(deck, 5)
    >>> deck
    [1, 2, 3, 4, 5, 8, 7]
    
    >>> deck = [1, 2, 3, 4, 11, 7, 8]
    >>> swap_cards(deck, 1)
    >>> deck
    [1, 3, 2, 4, 11, 7, 8]

    '''

    # find the card using the given index
    card_a = deck[index]
    # find the index of the card that follows the chosen card
    follow_index = (index+1) % len(deck)
    # name the follow card
    follow_num = deck[follow_index]
    # replace the follow card with the chosen card
    deck[follow_index] = card_a
    # replace the chosen card with the follow card
    deck[index] = follow_num


def move_joker_1(deck):
    ''' (list of int) -> NoneType
    The parameter represents a deck of cards.  This is step 1 of the algorithm.
    Find JOKER1 and swap it with the card that follows it.
    Treat the deck as circular.
    >>> deck = [1, 2, JOKER1, 4, 5]
    >>> move_joker_1(deck)
    >>> deck
    [1, 2, 4, 27, 5]

    >>> deck = [1, 2, 3, JOKER1]
    >>> move_joker_1(deckB)
    >>> deck
    [27, 2, 3, 1]


    '''
    # get the index of joker1
    JOKER1_index = deck.index(JOKER1)
    # use the swap function to swap the joker
    swap_cards(deck, JOKER1_index)


def move_joker_2(deck):
    ''' (list of int) -> NoneType
    The parameter represents a deck of cards.  This is step 2 of the algorithm.
    Find JOKER2 and move it two cards down. Treat the deck as circular.

    >>> deck = [1, 2, JOKER2, 4, 5]
    >>> move_joker_2(deck)
    >>> deck
    [1, 2, 4, 5, 28]

    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, JOKER1, JOKER2, 26]
    >>> move_joker_2(deck)
    >>> deck
    [28, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 27, 26]


    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, JOKER1, 26, JOKER2]
    >>> move_joker_2(deck)
    >>> deck
    [1, 28, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 27, 26]
    
    >>> deck = [JOKER1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
   19, 20, 21, 22, 23, 24, 25, 26, JOKER2]
    >>> move_joker_2(deck)
    >>> deck
    [27, 28, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

    '''
    # get the length of the deck
    deck_length = len(deck)
    # get the index of the bottom card
    bot_card_index = len(deck) - 1
    # case 1, if joker2 is at the bottom of the deck
    if deck[bot_card_index] == JOKER2:
        # remove joker2
        deck.remove(JOKER2)
        # name the first card
        first_card = deck[0]
        # replace the first card by joker2
        deck[0] = JOKER2
        # reverse the deck
        deck.reverse()
        # append the first card back
        deck.append(first_card)
        # reverse the deck back
        deck.reverse()
    #  case 2, if joker1 is one card before the bottom of the deck
    elif deck[bot_card_index - 1] == JOKER2:
        # remove joker2
        deck.remove(JOKER2)
        # reverse the deck
        deck.reverse()
        # append joker2 to the deck
        deck.append(JOKER2)
        # reverse the deck back
        deck.reverse()
    # third case, if joker2 is elsewhere in the deck
    else:
        # find the index of joker2
        joker_index = deck.index(JOKER2)
        # use the swap function to swap with the card that follows it
        swap_cards(deck, joker_index)
        # repeat the process so that joker2 is moved 2 cards down
        joker_index = deck.index(JOKER2)
        swap_cards(deck, joker_index)


def triple_cut(deck):
    '''(list of int) -> NoneType
    The parameter represents a deck of cards.  This is step 3 of the algorithm.
    Find the two jokers and do a triple cut.
    REQ: both jokers must be in the deck
    >>> deck = [27, 28, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    >>> triple_cut(deck)
    >>> deck
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    
    >>> deck = [1, 27, 4, 5, 28]
    >>> triple_cut(deck)
    >>> deck
    [27, 4, 5, 28, 1]
    
    >>> deck = [1, 27, 4, 5, 28, 11, 12, 13]
    >>> triple_cut(deck)
    >>> deck
    [11, 12, 13, 27, 4, 5, 28, 1]
    
    >>> deck = [3, 4, 5, 28, 11, 12, 13, 27]
    >>> triple_cut(deck)
    >>> deck
    [28, 11, 12, 13, 27, 3, 4, 5]

    '''

    # find index of joker1 and joker 2
    index_JOKER1 = deck.index(JOKER1)
    index_JOKER2 = deck.index(JOKER2)
    # case 1, if joker1 index is smaller than joker2 index
    if index_JOKER1 < index_JOKER2:
        # front index is joker1 index and bottom index is joker2 index
        front_index = index_JOKER1
        bot_index = index_JOKER2
    # case 2, if joker 2 index is smaller than joker1 index
    elif index_JOKER2 < index_JOKER1:
        # front index is joerk2 index and bottom index is joker1 index
        front_index = index_JOKER2
        bot_index = index_JOKER1
    # create the middle part index
    middle_index = deck[front_index:(bot_index + 1)]
    # add the middle part to the original deck
    deck.extend(middle_index)
    # add the lower part
    deck.extend(deck[:front_index])
    # delete the first part
    del(deck[:bot_index + 1])


def insert_top_to_bottom(deck):
    '''(list of int) -> NoneType
    The parameter represents a deck(pile) of cards.  This is step 4 of the algorithm.
    Look at the bottom card of the deck; move that many cards from the top of
    the deck to the bottom, inserting them just above the bottom card. Special
    case: if the bottom card is JOKER2, use JOKER1 as the number of cards.

   
    >>> deck = [2, 6, 4, 5, 3]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [5, 2, 6, 4, 3]
    
    >>> deck = [28, 11, 12, 13, 27, 3, 4, 5]
    >>> insert_top_to_bottom(deck)
    >>> deck
    >>> [3, 4, 28, 11, 12, 13, 27, 5]

    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28]
    
    >>> deck = [1, 2, 3, 4, 5, 27, 28, 6]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [28, 1, 2, 3, 4, 5, 27, 6]
    

    '''
    # find the index of the bottom card
    bot_index = len(deck) - 1
    # number of cards to be moved is the value of the bottom card
    num_cards = deck[bot_index]
    # special case, if the bottom card is JOKER2
    if num_cards == JOKER2:
        # then number of cards to be moved is joker1
        num_cards = JOKER1
    # find the bottom card
    bot_card = deck[bot_index]
    # delete the bottom card
    del(deck[bot_index])
    # add the cards from the top cards to the number of cards to be removed
    deck.extend(deck[:num_cards])
    # add the bottom card of the original deck
    deck.extend([bot_card])
    # delete from the top card, total euqal to number of cards in total
    del(deck[:num_cards])
    # ignore, for logic purpose only
    # 2, 6, 4, 5, 3 -> 2,6,4,5 -> 2,6,4,5,2,6,4 -> 2,6,4,5,2,6,4,3 -> 5,2,6,4,3


def get_card_at_top_index(deck):
    ''' (list of int) -> int
    The parameter represents a deck of cards.  This is step 5 of the algorithm.
    Look at the top card. Using that value as an index, return the card in that
    deck at that index. Special case: if the top card is JOKER2, use JOKER1 as
    the index.


    >>> get_card_at_top_index([1, 3, 5, 11, 17])
    3
    
    >>> get_card_at_top_index([28, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])
    27
   
    >>> get_card_at_top_index([4, 1, 3, 5, 8, 11, 17])
    8
    
    >>> get_card_at_top_index([7, 2, 4, 1, 3, 5, 8, 11, 17])
    11

    '''
    # top card is index 0 in deck
    top_card = deck[0]
    # if the top card in deck is joker2
    if deck[0] == JOKER2:
        # use joker1 as the index and find the card
        card = deck[JOKER1]
    # otherwise use top card as the index
    else:
        card = deck[top_card]
    return card


def get_next_value(deck):

    ''' (list of int) -> int
    The parameter represents a deck of cards.  This is the function that does
    all five steps of the algorithm. Return the next potential keystream value.
    >>> deck = [28, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
    18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    >>> get_next_value(deck)
    2
    
    >>> get_next_value([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 27, 28])
    27
    
    >>> get_next_value([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 1, 2, 3, 4])
    23
    
    >>> get_next_value([28, 27, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 1, 2, 3, 4])
    22



    '''
    # perform the previous four functions
    move_joker_1(deck)
    move_joker_2(deck)
    triple_cut(deck)
    insert_top_to_bottom(deck)
    # return the 5th function
    return get_card_at_top_index(deck)


def get_next_keystream_value(deck):
    '''(list of int) -> int
    The parameter represents a deck of cards.  This is the function that
    repeats all five steps of the algorithm (call get_next_value to get
    potential keystream values!) until a valid keystream value (a number in the
    range 1-26) is produced.
    
    >>> get_next_keystream_value([28, 27, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 1, 2, 3, 4])
    22
    
    >>> get_next_keystream_value([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 1, 2, 3, 4, 27, 28])
    10
    
    >>> get_next_keystream_value([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 27, 28])
    2
    
    >>> get_next_keystream_value([2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 28, 27])
    3
    

    '''
    

    # use the get_next_value function to obtain the next value
    next_value = get_next_value(deck)
    # while next_value is joker1 or joker2, keep repeating the process
    while (next_value == JOKER1) or (next_value == JOKER2):
        next_value = get_next_value(deck)

    return next_value


def process_message(deck, msg, crypt):
    '''
    (list of int, str, str) -> str
    The first parameter represents a deck of cards. The second represents a
    message to encrypt or decrypt based on the third parameter, which is either
    'e' (to encrypt) or 'd' (to decrypt).  return the encrypted or decrypted
    message. Note that the message might contain non-letters.
    
    >>> process_message([2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 28, 27], 'A', 'd')
    'X'
    
    >>> process_message([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 28, 27], '2A', 'd')
    'W'
    
    >>> process_message([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 28, 27], '2A', 'e')
    'E'
    
    >>> process_message([28, 27, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 2, 1], '2A', 'e')
    'O'
    

    
    '''
    # obtain the key by the get_next_keystream_value function
    key = get_next_keystream_value(deck)
    # obtain the cleaned_msg by the clean_message funtion
    cleaned_msg = clean_message(msg)
    # e means encrypt
    if crypt == 'e':
        result = encrypt_letter(cleaned_msg, key)
    # d means decrypt
    elif crypt == 'd':
        result = decrypt_letter(cleaned_msg, key)
    return result


def process_messages(deck, msg_list, crypt):
    '''(list of int, list of str, str) -> list of str
    The first parameter represents a deck of cards. The second represents a
    list of messages to encrypt or decrypt based on the third parameter, which
    is either 'e' (to encrypt) or 'd' (to decrypt).  Return the list of
    encrypted or decrypted messages.
    
    >>> process_messages([28, 27, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 2, 1], ['2A', 'D3', '111T'], 'e')
    ['O', 'L', 'T']
    
    >>> process_messages([27, 28, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 2, 1], ['2A', 'D3'], 'e')
    ['I', 'T']
    
    >>> process_messages([27, 28, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 2, 1], ['2X', 'd3'], 'd')
    ['P', 'N']
    
    >>> process_messages([27, 28, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 2, 1], ['2X', 'd3', '1111Y'], 'd')
    ['P', 'N', 'V']
    
    '''
    # make an empty new list for use
    new_list = []
    # loop each message
    for msg in msg_list:
        # get result by using the process_message function
        result = process_message(deck, msg, crypt)
        # append the result obtained
        new_list.append(result)
    return new_list


def read_messages(file):
    '''(file open for reading) -> list of str
    The parameter represents an open message file, which contains one message
    per line.  Read and return the contents of the file as a list of messages.
    Strip the newline from each line.
    '''
    result = []
    # loop each line
    for line in file:
        # remove the newline
        line.strip("\n")
        # append the line with newline removed
        result.append(line)
    return result


def read_deck(deck_file):
    '''(file open for reading) -> list of int
    The parameter represents an open deck file, which contains the numbers 1
    through 28 in some order.  Read and return the contents of the file. Do not
    hard-code the number 28 anywhere; just read all of the integers from the
    deck file.

.
    '''
    # make an empty list for use
    deck_list = []
    # loop each line
    for line in deck_file:
        # remove the newline
        new_line = line.strip("\n")
        # remove space
        new_line2 = line.split()
        # loop each number in line
        for num in line:
            # make the number integer class
            result_num = int(num)
            # append the number to the empty list
            deck_list.append(result_num)
    return deck_list
