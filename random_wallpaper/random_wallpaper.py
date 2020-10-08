import ctypes
import random
import os

PATH = "C:\\Users\\your\\path\\to\\wallpaper"
SPI_SETDESKWALLPAPER = 20  # 0x0014
SPIF_SENDCHANGE = 3  # 0x0003

pic = random.choice(os.listdir(PATH))

new_wallpaper = PATH + "\\" + pic

ctypes.windll.user32.SystemParametersInfoW(
    SPI_SETDESKWALLPAPER,
    0,
    new_wallpaper,
    SPIF_SENDCHANGE
)
