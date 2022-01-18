# ========================================================
#  
# Created by Stephen Covell on 21/12/21 @ 12:00 Hrs
#
# Project Title: Domain Discover
# Project Description:
#   To discover sub-domains and domains on a given domain.
#
# ========================================================

from settings import *
from resolver import *
from xls import *
from data_append import *
class Bruteforce:
    def __init__(self, p_workbook, p_worksheet, p_domain):
        """"
        __init__()

        Gathers the list to use from settings and determines the workbook
        """

        # Getting settings from config file
        settings = read_config()
        self._brutelist = settings['APP']['DEFAULT_SUBBRUTE']
        print(self._brutelist)

        # worksheet
        self._workbook = p_workbook
        self._ws = p_worksheet

        # target domain
        self._domain = p_domain

        # append data
        self._ad = DataAppend(self._workbook)

    def scanDomain(self):

        # We can use resolver
        reso = Resolver()

        # list of records/DNS types we can try
        records = [
            'NONE',
            'A',
            'NS',
            'MD',
            'MF',
            'CNAME',
            'SOA',
            'MB',
            'MG',
            'MR',
            'NULL',
            'WKS',
            'PTR',
            'HINFO',
            'MINFO',
            'MX',
            'TXT',
            'RP',
            'AFSDB',
            'X25',
            'ISDN',
            'RT',
            'NSAP',
            'NSAP-PTR',
            'SIG',
            'KEY',
            'PX',
            'GPOS',
            'AAAA',
            'LOC',
            'NXT',
            'SRV',
            'NAPTR',
            'KX',
            'CERT',
            'A6',
            'DNAME',
            'OPT',
            'APL',
            'DS',
            'SSHFP',
            'IPSECKEY',
            'RRSIG',
            'NSEC',
            'DNSKEY',
            'DHCID',
            'NSEC3',
            'NSEC3PARAM',
            'TLSA',
            'HIP',
            'CDS',
            'CDNSKEY',
            'CSYNC',
            'SPF',
            'UNSPEC',
            'EUI48',
            'EUI64',
            'TKEY',
            'TSIG',
            'IXFR',
            'AXFR',
            'MAILB',
            'MAILA',
            'ANY',
            'URI',
            'CAA',
            'TA',
            'DLV',
        ]

        try:
            file = open(str(self._brutelist))
        except:
            print("There was an error opening the file.")
            return False

        for lines in file:
            target = lines.rstrip('\n') + '.' + self._domain

            for dnstype in records:
                res = reso.resolveDNS(target, dnstype)

                # if there is a result, lets log it
                if (res != ""):
                    for ipval in res:
                        #(self, sheet, targetdomain="", hostname="", ipaddr="", type="", reversedns="", netblockowner="", country="", source="")
                        self._ad.d_append(self._ws, self._domain, target, ipval, dnstype, source="Subdomain Brute Force")

        # closing the file after we are done
        file.close()

