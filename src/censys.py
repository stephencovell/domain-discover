# ========================================================
#  
# Created by Stephen Covell on 21/12/21 @ 12:00 Hrs
#
# Project Title: Domain Discovery
# Project Description:
#   To discover sub-domains and domains on a given domain.
#
# ========================================================

import requests
import json
import time
import dns.resolver
import dns.reversename

from data_append import *
from settings import *

class Censys:
    """
    Censys consists of a large database of information to query.
    Querying information related to target domain.

    Configuation for Censys can be set in the settings file.
    Registration for a Censys account: https://search.censys.io/api
    """

    def __init__(self, p_workbook, p_worksheet, p_domain):
        """
        __init__(self, p_domain)
        Paramters:
            p_domain - Input of domain to target

        Gets CENSYS USERID and SECRET from Config file.
        Sets the domain to be used for Censys
        """

        # Getting settings from config file
        settings = read_config()
        self._UID = settings['API']['CENSY_APIID']
        self._SECRET = settings['API']['CENSY_SECRET']
        self._DEVENV = settings['APP']['DEVELOPMENT_STATUS']

        # Variables for API request
        self._domain = p_domain
        self._perpage = 100
        self._virtualhosts = "INCLUDE" 

        # workbook
        self._workbook = p_workbook
        self._worksheet = p_worksheet

    def checkCensysConfig(self):
        """
        checkCensysConfig()
        Returns:
            True - UID and SECRET values set
            False - UID and SECRET values invalid/not set
        """

        if (self._UID == "" or self._SECRET == ""):
            return False
        else:
            return True

    def getAPIResponse(self, p_cursor=""):
        """
        getAPIResponse()
        Paramters:
            cursor - Next page string.
        Returns:
            Returns a JSON file

        Runs an API query to Censys using given variables.
        If DEVLOPMENT ENVIRONMENT is activated, a JSON file
        is loaded instead. This is due to a limited amount of
        requests that can be performed on the API query.
        """

        # For testing reasons, lets load a JSON file we have already
        if (self._DEVENV == "DEV_STAT_DEV"):
            try:
                file = open('testing/censys.json')
            except:
                return "invalid"

            data = json.load(file)
            file.close()

            return data

        else: # if production, lets use the actual API call
            if (self.checkCensysConfig()): # lets check we have a UID and Secret set
                params = {
                "q" : self._domain, 
                "per_page" : self._perpage, 
                "virtual_hosts" : self._virtualhosts,
                "cursor" : str(p_cursor) }

                response = requests.get(f"https://search.censys.io/api/v2/hosts/search", auth=(self._UID, self._SECRET), params=params, headers={
        
                })

                data = response.json()
                return data
            else: # no UID or SECRET set
                return "invalid"

    def getAPIResults(self, p_data):
        """
        getAPIResults(p_data)
        Paramters:
            p_data - JSON file/data
        Returns:
            Returns a useful information how the request performed

        If successful, all data gets apended to an excel spreadsheet document.
        If unsuccessful, a useful error is returned
        """

        if (p_data == "invalid"):
            return "Please set UID/SECRET in Config file."
        elif (p_data["code"] == 400): # Code 400 - Bad request
            return "Bad Request. Invalid Search. Your query could not be parsed."
        elif (p_data["code"] == 401): # invalid authentiction
            return "Unauthorised. you must authetnicate with a valid API ID and secret"
        elif (p_data["code"] == 200):# great sucess
            for value in p_data["result"]["hits"]:
                # Declare a new object
                row = DataAppend(self._workbook)

                # Could be an error with no input
                try:
                    t_country = value["location"]["country"]
                except:
                    t_country = ""

                # asn 
                try:
                    t_netblockowner=value["autonomous_system"]["name"]
                except:
                    t_netblockowner=""

                # hostname
                try:
                    t_hostname = value["name"]
                except:
                    t_hostname = ""

                # appending data to spreadsheet :)
                row.d_append(
                    self._worksheet,
                    targetdomain=self._domain,
                    hostname=t_hostname,
                    ipaddr=value["ip"],
                    netblockowner=t_netblockowner, 
                    country=t_country,
                    source="Censys")
            
            # Cursor - performs another API request to get results from next page if results are more than 100
            next = p_data["result"]["links"]["next"]
            if(next != ""):
                d = self.getAPIResponse(next)
                self.getAPIResults(d)
        else:
            return "Something went wrong"

        # The only case that should continue to execute, is the case looking for code 200
        # It may loop so lets return great success here
        return "Successful"

    def peformAPIRequest(self):
        """
        peformAPIRequest()

        Brining it all together
        """

        data = self.getAPIResponse()

        if (data == "invalid"):
            msg = "Invalid"
        else:
            msg = self.getAPIResults(data)

        return msg

    
#c = Censys('bbconsult.co.uk')
#result = c.peformAPIRequest()
#print(result)
