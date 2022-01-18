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
#import whois
class DataAppend:
    def __init__(self, workbook):
        self._workbook = workbook

    def d_append(self, sheet, targetdomain="", hostname="", ipaddr="", type="", reversedns="", netblockowner="", country="", source=""):
        """
        d_append(self, targetdomain="", hostname="", ipaddr="", type="", reversedns="", netblockowner="", country="", source="")
        Paramters:
            All paramters are fields for the excel spreadsheet document.
            Missing paramters can be researched. The essential paramter is ipaddr.
        """

        # Resolve Reverse DNS
        if (str(reversedns) == ""):  
            print(ipaddr)
            rn = Resolver()
            result = rn.reverseNameLookup(str(ipaddr))
            reversedns = ' '.join(str(v) for v in result)
            #reversedns, alias, addresslist = rn.reverseIpLookup(ipaddr)

            if (type == ""):
                type = "PTR"

        # added ti resolve netblockowner/country, not working as expected
        #if (netblockowner == "" and not type == 'txt'):
        #    w = whois.whois(str(ipaddr))
        #    print (w)

            #if ('NetName' in w):
            #    netblockowner = w['NetName']

            #if (country == ""):
            #    if ('country' in w):
            #        country = w['country']

        #if (country == ""):

        #    if (country == ""):
        #        if ('country' in w):
        #            country = w['country']

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
        self._workbook.addTargetSheetEntry(sheet, p_target, p_hostname, p_ipaddr, p_type, p_reversedns, p_netblockowner, p_country, p_source)

    def nmap_append(self, sheet, target="", hostname="", state="", protocol="", name="", product="", extrainfo="", reason="", version="", conf="", port="", os=""):
       
        p_target = str(target)
        p_hostname = str(hostname)
        p_protocol = str(protocol)
        p_name = str(name)
        p_product = str(product)
        p_state = str(state)
        p_extrainfo = str(extrainfo) 
        p_reason = str(reason)
        p_version = str(version)
        p_conf = str(conf)
        p_port = int(port)
        p_os = str(os)

        self._workbook.addNMAPSheetEntry(sheet, p_target, p_hostname, p_state, p_protocol, p_name, p_product, p_extrainfo, p_reason, p_version, p_conf, p_port, p_os)
