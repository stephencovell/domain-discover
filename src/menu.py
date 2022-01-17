# ========================================================
#  
# Created by Stephen Covell on 21/12/21 @ 12:00 Hrs
#
# Project Title: Domain Discovery
# Project Description:
#   To discover sub-domains and domains on a given domain.
#
# ========================================================
# import os

# Lets import other classes
from resolver import * 
from censys import * 
from scan import * 
from xls import *
class Menu:
    def __init__(self):
        self._exc = Excel()

    def askForDomain(self):
        """
        askForDomain()
        Returns input

        Asks a user for domain name
        """
        domain = input("Please enter a domain name: ")
        return domain

    def displayMenuOpt(self):
        """
        displayMenuOpt()

        A loop to show the menu. User can input 'Q/q' to exit the program
        """
        user_input = ""
        while (user_input.upper() != "Q"):
            self.showMenuOpt(self)
            user_input = input("Please input 'q' to quit or any other key to continue: ")

    def showMenuOpt(self, errormsg = ""):
        """
        showMenuOpt(errormsg)
        Paramter: String of an error message to be displayed

        Shows all menu options. An error message is displayed
        if string isn't null/empty. Options can be expanded.
        """
        # Clear the screen
        # os.system('cls')

        # Display any errors
        if str(errormsg) != "":
            print (str(errormsg) + "error")

        # Menu properties
        min_menu_option = 1
        max_menu_option = 9

        # Displaying the menu
        # !!!! BE SURE TO UPDATE MENU PROPERTIES WHEN ADDING OPTIONS !!!
        print (""""
        Domain Discover
        Discover sub-domains and domains on a given domain

        Options:
        (1) Full Scan (writes output to /saves/)
        (2) Resolve NS
        (3) Resolve MX
        (4) Resolve A Records
        (5) Reverse IP Lookup (Under Development)
        (6) Search the WWW (Under Development)
        (7) Subdomain Bruteforce (Under Development)
        (8) Censys (writes output to /saves/)
        (9) NMAP Scan
        """)

        # Getting user input
        user_input = input("Please enter an option between " + str(min_menu_option) + " and " + str(max_menu_option) + ": ")
        self.selectUserMenuOpt(user_input, min_menu_option, max_menu_option)

    def selectUserMenuOpt(self, user_input, min_menu_option, max_menu_option):
        """
        selectUserMenuOpt(user_input, min_menu_option, max_menu_option)
        Paramters:
            user_input - User input must be an integer
            min_menu_option - Minimum option displayed on the menu
            max_menu_option - Maximum option displayed on the menu

        Inputs are all checked. An error is shown if user_input is not integer.
        min_menu_option and max_menu options are checked.
        Code is executed for each case of Options.
        """

        # Lets check input

        # converting user input into a string
        # need to refactor this a bit
        try:
            ui_int = int(user_input)
        except:
            return self.showMenuOpt("Invalid input") # Lets return this, stop the program running any further

        if min_menu_option > ui_int: # if the option is less than the minimum
            return self.showMenuOpt("Error: Option can not be less than " + str(min_menu_option) + ". Please enter a higher value.")
        elif max_menu_option < ui_int: # if the option is more than the maximum
            return self.showMenuOpt("Error: Option can not be more than " + str(max_menu_option) + ". Please enter a lower value.")
        else:
            match ui_int:
                case 1: # Full scan
                    # Lets ask the user for domain to target
                    domain = self.askForDomain() # this causes an error, will investiage later

                    # Lets lookup the NS
                    resolve = Resolver()
                    resolve.resolveNS(domain)
                    resolve.resolveMX(domain)
                    resolve.resolveA(domain)

                     # perform the API request
                    c = Censys(domain)
                    result = c.peformAPIRequest()
                case 2: # Resolve NS
                    # Lets ask the user for domain to target
                    domain = self.askForDomain()

                    # Lets lookup the NS
                    resolve = Resolver()
                    resolve.resolveNS(domain)
                case 3: # Resolve MX
                    # Lets ask the user for domain to target
                    domain = self.askForDomain()

                    # Lets lookup the NS
                    resolve = Resolver()
                    resolve.resolveMX(domain)
                case 4: # Resolve A
                    # Lets ask the user for domain to target
                    domain = self.askForDomain()

                    # Lets lookup the A
                    resolve = Resolver()
                    resolve.resolveA(domain)
                case 5: # Ip Lookup
                    print ("Feature under development.")
                case 6: # Search WWWW
                    print ("Feature under development.")
                case 7: # Subdomain bruteforce
                    print ("Feature under development.")
                    # Lets ask the user for domain to target
                    #domain = self.askForDomain()

                    # And the magic
                    #sub_bf = Bruteforce()
                case 8:
                    # Lets ask the user for domain to target
                    domain = self.askForDomain()

                    # perform the API request
                    c = Censys(self._exc, domain)
                    result = c.peformAPIRequest()
                case 9:
                    # NMAP scan
                    scn = Scan(self._exc)
                    scn.simpleScan()
                case _: 
                    print ("Something went wrong. Sorry.")

