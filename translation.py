class Translation(object):
    START_TEXT = """Hi!
Thank you for using me 😬
Enter your Telegram Phone Number, to get the APP-ID from my.telegram.org

/start at any stage to re-enter your details"""
    AFTER_RECVD_CODE_TEXT = """I see!
now please send the Telegram code that you received from Telegram!

this code is only used for the purpose of getting the APP ID from my.telegram.org

/start at any stage to re-enter your details"""
    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."
    ERRED_PAGE = "something wrongings. failed to get app id. \n\n@FZBOTS"
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = "sorry, but the input does not seem to be a valid Telegram Web-Login code"
    IN_VALID_PHNO_PVDED = "sorry, but the input does not seem to be a valid phone number"
