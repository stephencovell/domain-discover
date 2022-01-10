# ========================================================
#  
# Created by Stephen Covell on 21/12/21 @ 12:00 Hrs
#
# Project Title: Domain Discovery
# Project Description:
#   To discover sub-domains and domains on a given domain.
#
# ========================================================

# THIS FILE DOES WONDEFUL MAGJIC
# SO...
# THERE ARE MANY METHODOLOGIES:
# - SUBDOMAIN BRUTE FORCE
# - SEARCH THE WORLD WIDE WEB
# - CALLING APIs
# ALL THSE METHODS RETRIVE DIFFERENT DATA.
# THIS FILE FILLS IN THE GAPS
from resolver import * 
from xls import * 

class DataAppend:
    def d_append(self, targetdomain="", hostname="", ipaddr="", type="", reversedns="", netblockowner="", country="", source=""):
        """
        d_append(self, targetdomain="", hostname="", ipaddr="", type="", reversedns="", netblockowner="", country="", source="")
        Paramters:
            All paramters are fields for the excel spreadsheet document.
            Missing paramters can be researched. The essential paramter is ipaddr.
        """

        # Resolve Reverse DNS
        if (str(reversedns) == ""):  
            rn = Resolver()
            result = rn.reverseNameLookup(ipaddr)
            reversedns = ' '.join(str(v) for v in result)
            type = "PTR"

        # to avoid any funny results, lets convert all passed paramters into strings
        p_target = str(targetdomain)
        p_hostname = str(hostname)
        p_ipaddr = str(ipaddr)
        p_type = str(type)
        p_reversedns = str(reversedns)
        p_netblockowner = str(netblockowner)
        p_country = str(country)
        p_source = str(source)

        # using our Excel class to create an object
        e = Excel()
        ws = e.createTargetSheet()
        e.addTargetSheetEntry(ws, p_target, p_hostname, p_ipaddr, p_type, p_reversedns, p_netblockowner, p_country, p_source)
