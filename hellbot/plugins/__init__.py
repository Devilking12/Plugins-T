from hellbot import *
from hellbot.config import Config
from hellbot.helpers import *
from hellbot.utils import *


DEVLIST = ["1748056101", "1432756163", "1777340882", "816517310"]
HELL_USER = Config.YOUR_NAME or "Hêll"
ForGo10God = bot.uid
hell_mention = f"[{HELL_USER}](tg://user?id={ForGo10God})"
hell_logo = "./hellbot/resources/hellbot_logo.jpg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER


sudos = Config.SUDO_USERS

if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

chnl_link = "https://t.me/its_hellbot"
hell_channel = f"[†hê Hêllẞø†]({chnl_link})"
grp_link = "https://t.me/HellBot_Chat"
hell_grp = f"[Hêllẞø† Group]({grp_link})"

# will add more soon

# hellbot
