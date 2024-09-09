from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet()
fonts = figlet.getFonts()

# zero command-line arguments
if len(sys.argv) == 1:
    str = input("Input: ")
    figlet.setFont(font = choice(fonts))
    print(figlet.renderText(str))

# two command-line arguments
elif len(sys.argv) == 3:
    if  sys.argv[1] != '-f' and sys.argv[1] != '--font' :
        sys.exit("Invalid usage")
    elif not sys.argv[2] in fonts:
        sys.exit("Invalid usage")
    else:
        str = input("Input: ")
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(str))
else:
    sys.exit("Invalid usage")
