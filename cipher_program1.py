"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message1.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main(DECK_FILENAME, MSG_FILENAME, mode):
    """ (file open for reading, file open for reading, str) -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """
    deck = read_deck(DECK_FILENAME)
    
    msg_list = read_messages(MSG_FILENAME)
    
    process_messages(deck, msg_list, mode)

    

main()
