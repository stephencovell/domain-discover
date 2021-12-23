# ========================================================
#  
# Created by Stephen Covell on 21/12/21 @ 12:00 Hrs
#
# Project Title: Domain Discover
# Project Description:
#   To discover sub-domains and domains on a given domain.
#
# ========================================================
import os

from resolver import * 

class Menu:
    def askForDomain(self):
        domain = input("Please enter a domain name: ")
        return domain

    def displauMenuOpt(self):
        user_input = ""
        while str(user_input) != "Q" or str(user_input) != "q":
            self.showMenuOpt(self)
            user_input = input("Please input 'q' to quit or any other key to continue: ")

    def showMenuOpt(self, errormsg = ""):
        # Clear the screen
        os.system('cls')

        # Display any errors
        if str(errormsg) != "":
            print (str(errormsg) + "error")

        # Menu properties
        min_menu_option = 1
        max_menu_option = 6

        # Displaying the menu
        print (""""
        Domain Discover
        Discover sub-domains and domains on a given domain

        Options:
        (1) Full Scan
        (2) Resolve NS
        (3) Resolve MX
        (4) Resolve A Records
        (5) Reverse IP Lookup
        (6) Search the WWW
        """)

        # Getting user input
        user_input = input("Please enter an option between " + str(min_menu_option) + " and " + str(max_menu_option) + ": ")
        self.selectUserMenuOpt(user_input, min_menu_option, max_menu_option)

    def selectUserMenuOpt(self, user_input, min_menu_option, max_menu_option):
        # Lets check input

        # converting user input into a string
        # need to refactor this a bit
        try:
            ui_int = int(user_input)
        except:
            self.showMenuOpt("Invalid input")

        if min_menu_option > ui_int: # if the option is less than the minimum
            self.showMenuOpt("Error: Option can not be less than " + str(min_menu_option) + ". Please enter a higher value.")
        elif max_menu_option < ui_int: # if the option is more than the maximum
            self.showMenuOpt("Error: Option can not be more than " + str(max_menu_option) + ". Please enter a lower value.")
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
                case _: 
                    print ("Something went wrong. Sorry.")

