# ========================================================
#  
# Created by Stephen Covell on 21/12/21 @ 12:00 Hrs
#
# Project Title: Domain Discovery
# Project Description:
#   To discover sub-domains and domains on a given domain.
#
# ========================================================

import sys

# import the menu
sys.path.append("src/")
from menu import *

def main():
    m = Menu()
    m.displayMenuOpt()

if __name__ == "__main__":
    main()