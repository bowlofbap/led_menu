import .MFRC522
import signal
import RPi.GPIO as GPIO
from .SnakeWebHandler import SnakeWebHandler
from .TetrisWebHandler import TetrisWebHandler

#  Main program logic follows:
if __name__ == '__main__':
    snakeWebHandler = SnakeWebHandler(processHandler)
    tetrisWebHandler = TetrisWebHandler(processHandler)
    MIFAREReader = MFRC522.MFRC522(dev_num=1)
    continue_reading = True
    while continue_reading:
        
        # Scan for cards    
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        if status == MIFAREReader.MI_OK:
            print("Card detected")
        
        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:

            # Print UID
            print("Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3]))
        
            # This is the default key for authentication
            key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
            
            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)

            # Authenticate
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                continue_reading = False
                output = MIFAREReader.MFRC522_Read(8)
                MIFAREReader.MFRC522_StopCrypto1()
                if output == "snake":
                    snakeWebHandler.play_snake_game(True, False)
                elif output == "tetris":
                    tetrisWebHandler.play_tetris_game()
            else:
                print("Authentication error")
