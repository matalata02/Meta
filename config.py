from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS


# Go to my.telegram.org then Enter your Phone Number with your country code.
# After, you are logged in click on API Development Tools.
# Enter Anything as App name and App short name, Enter my.telegram.org in url section
# That’s it, You”ll get your API_ID and API_HASH
API_ID = int(getenv("API_ID", "9634859"))
API_HASH = getenv("API_HASH", "0fcd865bdac0fb0ec5cffcde87e0126e")

# Assistant Prefix needed to trigger your assistant accounts in User mode to execute your command. This can be only set as one Symbol (Special Character)
# Example:- . or , or ! or * etc etc
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())

# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 10 mins.
# Remember to give value in Minutes
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "500"))

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "5583236615:AAFxMEINKdbT0wfJfykn-LNLHJNRi44MP08")

## MONGO DB
# HOW TO GEN :-  https://telegra.ph/How-To-get-Mongodb-URI-04-06
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://caca:caca111@cluster0.qlwoq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


## PRIVATE START MESSAGE.. IMAGE
# Please use telegraph link for this

START_IMG_URL = getenv("START_IMG_URL", None)

# To work some Heroku compatible modules, this var value required to Access your account to use `get_log`, `usage`, `update` etc etc commands.
# You can fill this var using your API key or Authorization token.
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# To use your Yukki as default with all regular Updates and Patches.
# Also without customizing or modifying as your own choice, this must be
# filled with Yukki Music Bot Main Repository URL in value.
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/matalata02/Meta"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

# If you have a Support for your Music Bot, You can set this var
# Only  Links formats can be accepted for this Var value.
# Example:- https://t.me/YukkiSupport
# Don’t use @

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL", "https://t.me/sadnesstalk"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP", "https://t.me/sadnesstalk"))


# You'll need a Private Group for this.
# Add @MissRose_Bot in your Private Group from Add Member > Search "@MissRose_Bot" and then Add.

# After added, Just type "/id" in the chat.
# You'll get the ID of your group.

# Remember to add your Music Bot , Assistant Accounts and Logger Id in Group and Promote them Admin with Full Rights.

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001733995304"))


# A name for your Music bot.
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "MEGABAS")

## Bot SUDO USERS AND DEVS

# Sudo Users ID(not username) for Bot. (For multiple users seperate IDs with space)
# Input type must be interger.
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5372468167").split()))

# Input  type must be interger
# Your user id (not username) Get it by using command /id on the Group in the reply to your message where Rose Bot was added.
OWNER_ID = list(map(int, getenv("OWNER_ID", "5372468167").split())) + [5372468167]

## String Session Vars ...
# You'll need a Pyrogram String Session for these vars.
# Generate String from our session generator bot 
# WHAT IS MULTI ASSISTANT MODE?
# One Telegram Account can join upto 500 chats.
# If your bot is running in higher number of chats it will create a problem for assistant to join and leave chat everytime giving invite link exportation floods too
# You can use upto 5 Assistant Clients ( allowing your bot to atleast work in 2000-2500 chats at a time )

if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1", "AgC5Ag7kFy02dxEuUP6iwkeOXG70gqmaOIvpGcMMCaYjoRsxQO1Z_CMP4HyrXVb1-F5jnh66zLrt94ZYzdKoe6aBLCHiLoGHPFBYT3axfSOYOS2giCX5L9Tj2zR5SER4RMo8pruFja22l3-RgO8TCkv9binUNV01C0oxqzYmK-6Z34xKYHprs3yyaLj-AbgbNSW8jSmMEWQCPWLDhkBtcrbwX5nzfiQVdSQsNRcLYiDa_Stvp9_nUrwCi92HlQJPVa6Cc1Oles3YnT4L1wEjapisTUXrPTQ8LIXgnQTKzkvOAD8mW6xOQ8q_HpGDHg3PM7t4mH30ud_2FZ2iy5zvlbCLAAAAAUA5W8cA"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2", "AgBXTWb3YhSsGiI5rscy-ZN4ehJNLEo8afkpPd1U_ZxM65lC_B3irQPxui1Qfs0RFeHzkCevnA1jqtQugKmKu3CDKx__PcuDZy3iLqUSW_oAZucrkVcLdJqXVd42G-tS34xg3IFDdkrXWgULijbNPsJ2uK2aqrmi2wa_3Rt52RQr4N_CBeCEpdXdQrjheHioyZ4dilz2dwl_jwhIiZlA74EzNFUcdjU-TU9zMKmTLqm40L-M5f76DOpHr8cmD_d7Rkg7P8mHAI0rc2v1kez1B2icDsDXvcj9iHzy2EubomQbaoRj8tX5AuW1-yMdUzbEZBHtwRTm6MhKEPZQHfFcv-idAAAAATTlaVcA"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3", "AgB4CKEb5GJ9kHMuwoifJKkGjuN_nR5HfHkAPb55ATfkgp4kTd7Y7FY-QWl0WuOvkBwt7_HZjh-QX7YyakaHLvCc6nkLV4PiiNEu2XKpZMu-3RIEhDBtBkZ-4MM43gROYtPgsuq84BnfHJi28FQLtxwm0Ykqu6zuvZHPM2IBxiJCeay06Zaj3zrWzPXOoTAEVJt_V6WTTF8ypFJU_RkAbjNenOqgaAxwO1STYm_NLMS4WwOTJ6lwNT3afno78eeg5S8DVFp5t7B20_VejuVYAQ4UjNL8oeRIzfdSMrFDeHXnXCqHBaCNZgH8iW5-PT8f0403C09xhe34B0z17_pHjvrIAAAAAT6jBRkA"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4", "AgANMKmfcSjTy1DE6ZKwij86dqRbetiiBUOA9dIoJpEzVn2w9c4GE29FQI-AUk92TzYwfPSnjlnb6m1mGzbUX4FwubGHEGdNgCxnzC8gsqpE9hLfhF4MfuCNYAztOIWU9rNHsnYIJgqLw-1gvJaBbBkc3KWP9vEBg-pcIjT5xbjsyF4MZd5sggAaK-JLu9KyToIallUBCpsSdP0c1YtuBOYkvxZN0rP5_WkNRphzhS9o65VzuMq_Do4emTKtysHBhV-ifDbEdenQIh5YG_oi2oJ-58FzWqK7bQ94U7RHc8uIeyoJf5h5SgRwOAC0_jl4SFXev3btlPb4FhcBnWSThQlBAAAAATs0UUwA"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5", "AgC0CzIyn_QimX1h5_21otiRiH-AVxIN1rLaAf2Na0TOjlJXO0Mp3s0FpYeIle5GazUCHeJFucjF9OVEzrupY8ZlSYY1mfERiiTEo5FsxozK7wHlZoBmPWuVFheHP9PJaDLZAsx8IwBOC0aOCf-1ODSzHbO1cJL1lrhRWM4ZE2cuJjO2zAmSg8sYkOiOONiL2WFRoLrGQat-qunnvTlHuUNaeEgPyPGtUBWGlNaj47qP7z8Gci2XpCt4HQvqL_2WPOhgdYMnA2VuOX7kjleRRRWohNjyxUIwDR09tKaUh43EU8jkV_llXllj6bVK7N5Kx3LzKSmqt5-Qp9SFPXr26dVNAAAAATZu6NsA"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION", "AgC5Ag7kFy02dxEuUP6iwkeOXG70gqmaOIvpGcMMCaYjoRsxQO1Z_CMP4HyrXVb1-F5jnh66zLrt94ZYzdKoe6aBLCHiLoGHPFBYT3axfSOYOS2giCX5L9Tj2zR5SER4RMo8pruFja22l3-RgO8TCkv9binUNV01C0oxqzYmK-6Z34xKYHprs3yyaLj-AbgbNSW8jSmMEWQCPWLDhkBtcrbwX5nzfiQVdSQsNRcLYiDa_Stvp9_nUrwCi92HlQJPVa6Cc1Oles3YnT4L1wEjapisTUXrPTQ8LIXgnQTKzkvOAD8mW6xOQ8q_HpGDHg3PM7t4mH30ud_2FZ2iy5zvlbCLAAAAAUA5W8cA"))


## Dont Change

get_queue = {}
