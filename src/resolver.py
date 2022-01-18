# ========================================================
#  
# Created by Stephen Covell on 21/12/21 @ 12:00 Hrs
#
# Project Title: Domain Discover
# Project Description:
#   To discover sub-domains and domains on a given domain.
#
# ========================================================

import dns.resolver
import dns.reversename
import socket

class Resolver:
    def resolveNS(self, website):
        self.resolveDNS(website, 'NS')

    def resolveMX(self, website):
        self.resolveDNS(website, 'MX')

    def resolveTXT(self, website):
        self.resolveDNS(website, 'TXT')

    def resolveA(self, website):
        self.resolveDNS(website, 'A')

    def resolveDNS(self, website, type):
        print('Resolving ' + website + ' ' + str(type) + '...')

        try:
            dns_result = dns.resolver.resolve(website, type)
        except:
            dns_result = ""

        for ipval in dns_result:
            print(ipval.to_text())

        return dns_result
        
    def reverseIpLookup(self, addr):
        try:
            name, alias, addresslist = socket.gethostbyaddr(addr)
        except socket.herror:
            return None, None, None

    def reverseNameLookup(self, ip):
        try:
            qname = dns.reversename.from_address(str(ip))
        except:
            answer = ""

        try:
            answer = dns.resolver.query(qname, 'PTR')
        except:
            answer = ""

        #for rr in answer:
        #    print(rr)

        return answer

    


# could come in handy
#for ipval in a_result:
#    print (str(ipval).strip())
#    
#    name, alias, addresslist = lookup(str(ipval).strip())
#    print(name)