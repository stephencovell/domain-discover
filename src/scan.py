# ========================================================
#  
# Created by Stephen Covell on 21/12/21 @ 12:00 Hrs
#
# Project Title: Domain Discover
# Project Description:
#   To discover sub-domains and domains on a given domain.
#
# ========================================================

# Libaries
import nmap
import pandas as pd
import requests

# From this project
from settings import *
from xls import * 
from data_append import * 

#workbook = Excel()
#workbook.openWB()
#ws = workbook.createNMAPSheet()

class Scan:
    """
    Scan

    Performs a network map scan using the tool NMAP
    Results are written to an excel spreadsheet document
    """

    def __init__(self, p_workbook):
        """
        Ininitiates all relevant varaibles
        """

        # Lets get the development status
        settings = read_config()
        self._DEVENV = settings['APP']['DEVELOPMENT_STATUS']

        # Sorting out the workbook.. For testing reasons, I'm going to use an
        # excel spreadsheet document filled with data
        if(self._DEVENV == "DEV_STAT_DEV"):
            self._df = pd.read_excel('saves/10-01-2022 21-21-49.xlsx', sheet_name='Target')
            self._workbook = Excel()
            self._workbook.openWB()
        else:
            self._workbook = p_workbook
            self.df = pd.read_excel(self._workbook, sheet_name='Target')
    
        # Opening the workbook:
        self._ws = self._workbook.createNMAPSheet()
            
        # Grabbing a unique set of IPs from the Target spreadsheet document
        # Future development:
        # - Write contents to a file, and iterate contents from file
        # - Stops all variables being stored in memory, helpful when dealing with big datasets
        self._uniquevalues = self._df['IP'].unique()

        # Need a way to append data...
        self._apendnmap = DataAppend(self._workbook)

    def simpleScan(self):
        """
        simpleScan()

        Scans all ports using default nmap settings
        """
        nmScan = nmap.PortScanner()

        for address in self._uniquevalues:

            # the scan
            try:
                #  '-v -sS -sV -sC -sU -A -O' root privilegs needed
                res = nmScan.scan(address, '21-1024')
            except:
                print("Error")

            for host in nmScan.all_hosts():

                # function from data append
                # def addNMAPSheetEntry(sheet, target="", state="", extrainfo="", reason="", version="", conf="")
                for proto in nmScan[host].all_protocols():

                    lport = nmScan[host][proto].keys()

                    for port in lport:
                        
                        # this doesnt appear to be working as expected
                        httpheader = ""
                        if (nmScan[host][proto][port]['name'] == 'https' or nmScan[host][proto][port]['name'] == 'http'):
                            url = str(address) + ":" + str(port)
                            try:
                                r = requests.get(url)
                            except:
                                httpheader = "continue"
                            
                            if (httpheader == "continue"):
                                httpheader = ""
                            else:
                                httpheader = r.request.headers

                        self._apendnmap.nmap_append(self._ws, address,
                        nmScan[host].hostname(),
                        nmScan[host].state(),
                        proto,
                        nmScan[host][proto][port]['name'],
                        nmScan[host][proto][port]['product'],
                        nmScan[host][proto][port]['extrainfo'],
                        nmScan[host][proto][port]['reason'],
                        nmScan[host][proto][port]['version'],
                        nmScan[host][proto][port]['conf'],
                        port,
                        httpheader)
        

