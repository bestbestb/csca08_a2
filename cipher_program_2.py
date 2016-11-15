"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'secret2.txt'
MODE = 'd'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """
    
    
    
    deck_file_handle = open(DECK_FILENAME, 'r')      
    deck = cipher_functions.read_deck(deck_file_handle)
    deck_file_handle.close()
    
    msg_file_handle = open(MSG_FILENAME, 'r')
    msg_list = cipher_functions.read_messages(msg_file_handle)
    
    msg_file_handle.close()
    
    
   
        
    msg_oneline = cipher_functions.process_messages(deck, msg_list, MODE)
    
    for msg in msg_oneline:
        print(msg)
    
    
    
main()

