# Created by Stephen Covell on 21/12/21 @ 12:00 Hrs
# Project Title: Domain Discover
# Project Description:
#   To discover sub-domains and domains on a given domain.

import dns.resolver
import dns.reversename
import socket

# DEFINE THE WEBSITE
website = 'bbconsult.co.uk'

# RESOLVE DNS Servers type NS
print('DNS')
ns_result = dns.resolver.resolve(website, 'NS')
for ipval in ns_result:
    print(ipval.to_text())
print('\n')

# RESOLVE DNS Servers type MX
print('MX')
mx_result = dns.resolver.resolve(website, 'MX')
for ipval in mx_result:
    print(ipval.to_text())
print('\n')

# RESOLVE DNS Servers type MX
print('TXT')
mx_result = dns.resolver.resolve(website, 'TXT')
for ipval in mx_result:
    print(ipval.to_text())
print('\n')

# RESOLVE CNAME RECORDS
#print('CNAME RECORDS')
#cn_result = dns.resolver.resolve(website, 'CNAME')
#if (cn_result):
#    for ipval in cn_result:
#        print(ipval.to_text())
#    print('\n')


# FIND A RECORDS
print('A RECORDS')
a_result = dns.resolver.resolve(website, 'A')
for ipval in a_result:
    print(ipval.to_text())
print('\n')

# REVERSE IP LOOKUP
print('REVERSE IP LOOKUP')

#qname = dns.reversename.from_address('104.26.9.35')
#answer = dns.resolver.resolve(qname)
#for rr in qname:
#    print(rr)
#print(ipval.to_text())

def lookup(addr):
    try:
        name, alias, addresslist = socket.gethostbyaddr('104.26.8.35')
    except socket.herror:
        return None, None, None

for ipval in a_result:
    print (str(ipval).strip())
    
    name, alias, addresslist = lookup(str(ipval).strip())
    print(name)

print('\n')
