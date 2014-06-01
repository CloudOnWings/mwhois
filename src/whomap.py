#!/usr/bin/env python

import const as CONST

#domain whois server info found at http://www.iana.org/domains/root/db
#gtld launch dates http://www.sedo.com/us/new-gtlds/gtld-launch-dates/
#Wiki with info about domain names tld's https://wiki.rrpproxy.net/Main_Page

"""
Still to Add
.uno	unodominio.com x
.ceo	peoplebrowsr.com x
.berlin	whois.nic.berlin
.ruhr	whois.nic.ruhr


"""


class WhoisServerMap(object):

    def __init__(self):
        self.list_of_emails = r'[w.-]+@[w.-]+'

        """
        Structure
        ['first_server', 'second _server', 'status', 'exceeded', 'tld_type']
        """

        self.all_server_map = {'ac': ['whois.nic.ac', '', 'is available', '', CONST.CCTLD_STANDARD],
                               'aero': ['whois.aero', '', 'NOT FOUND', '', CONST.STLD_STANDARD],
                               'af': ['whois.nic.af', '', 'No Object Found', '', CONST.CCTLD_STANDARD],
                               'ag': ['whois.nic.ag', '', 'NOT FOUND', '', CONST.CCTLD_STANDARD],
                               'am': ['whois.nic.am', '', 'No match', '', CONST.CCTLD_STANDARD],
                               'as': ['whois.nic.as', '', 'Not Registered', '', CONST.CCTLD_STANDARD],
                               'at': ['whois.nic.at', '', 'nothing found', '', CONST.CCTLD_STANDARD],
                               'au': ['whois.aunic.net', 'whois-check.ausregistry.net.au', 'No Data Found',
                                      'BLACKLISTED', CONST.CCTLD_STANDARD],
                               'be': ['whois.dns.be', '', 'Status:    AVAILABLE', '', CONST.CCTLD_STANDARD],
                               'biz': ['whois.biz', '', 'Not found', '', CONST.TLD_STANDARD],
                               'bj': ['whois.nic.bj', '', '', '', CONST.CCTLD_STANDARD],
                               'br': ['whois.registro.br', '', 'No match for', '', CONST.CCTLD_STANDARD],
                               'bz': ['whois.belizenic.bz', '', 'No Match', '', CONST.CCTLD_STANDARD],
                               'ca': ['whois.cira.ca', 'whois.domainpeople.com', 'Domain status: .*available', '',
                                      CONST.CCTLD_STANDARD],
                               'cat': ['whois.cat', '', '', '', CONST.STLD_STANDARD],
                               'cc': ['whois.nic.cc', '', 'No match', '', CONST.CCTLD_STANDARD],
                               'cd': ['whois.nic.cd', '', 'Domain Status: Available', '', CONST.CCTLD_STANDARD],
                               'ch': ['whois.nic.ch', '', 'not have an entry', '', CONST.CCTLD_STANDARD],
                               'ci': ['whois.nic.ci', '', '', '', CONST.CCTLD_STANDARD],
                               'cl': ['whois.nic.cl', '', 'no existe', '', CONST.CCTLD_STANDARD],
                               'cn': ['whois.cnnic.net.cn', '', 'no matching record', '', CONST.CCTLD_STANDARD],
                               'com': ['whois.verisign-grs.com', 'whois.domain.com', 'No match for',
                                       'You have exceeded your quota of queries', CONST.TLD_STANDARD],
                               'coop': ['whois.nic.coop', '', '', '', CONST.GTLD_STANDARD],
                               'cx': ['whois.nic.cx', '', 'No Object Found', '', CONST.CCTLD_STANDARD],
                               'cz': ['whois.nic.cz', '', 'No data found', '', CONST.CCTLD_STANDARD],
                               'de': ['whois.denic.de', '', 'Status: free', 'access control limit exceeded',
                                      CONST.CCTLD_STANDARD],
                               'dk': ['whois.dk-hostmaster.dk', '', 'No entries found', '', CONST.CCTLD_STANDARD],
                               'edu': ['whois.educause.edu', '', 'No Match', '', CONST.TLD_STANDARD],
                               'ee': ['whois.eenet.ee', '', '', '', CONST.CCTLD_STANDARD],
                               'es': ['whois.nic.es', '', '', '', CONST.CCTLD_STANDARD],
                               'eu': ['whois.eu', '', 'AVAILABLE', '', CONST.CCTLD_STANDARD],
                               'fi': ['whois.ficora.fi', '', '', '', CONST.CCTLD_STANDARD],
                               'fr': ['whois.nic.fr', '', 'No entries found', '', CONST.CCTLD_STANDARD],
                               'gf': ['whois.internic.net', '', 'No match for domain', '', CONST.CCTLD_STANDARD],
                               'gg': ['whois.channelisles.net', '', '', '', CONST.CCTLD_STANDARD],
                               'gov': ['whois.dotgov.gov', '', 'No match', '', CONST.TLD_STANDARD],
                               'gr': ['whois.ripe.net', '', 'no entries found', '', CONST.CCTLD_STANDARD],
                               'graphics': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                               'guru': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                               'hk': ['whois.hkirc.net.hk', '', 'The domain has not been registered.', '',
                                      CONST.CCTLD_STANDARD],
                               'hn': ['whois2.afilias-grs.net', '', '', '', CONST.CCTLD_STANDARD],
                               'hu': ['whois.nic.hu', '', '', '', '', CONST.CCTLD_STANDARD],
                               'ie': ['whois.domainregistry.ie', '', 'Not Registered ', '', CONST.CCTLD_STANDARD],
                               'il': ['whois.isoc.org.il', '', '% No data was found', '', CONST.CCTLD_STANDARD],
                               'in': ['whois.inregistry.net', '', '', '', CONST.CCTLD_STANDARD],
                               'info': ['whois.afilias.info', '', 'NOT FOUND', 'WHOIS LIMIT EXCEEDED',
                                        CONST.TLD_STANDARD],
                               'int': ['whois.iana.org', '', '', '', CONST.STLD_STANDARD],
                               'io': ['whois.nic.io', '', 'is available', '', CONST.CCTLD_STANDARD],
                               'is': ['whois.isnic.is', '', 'No entries found', '', CONST.CCTLD_STANDARD],
                               'it': ['whois.nic.it', '', 'AVAILABLE', '', CONST.CCTLD_STANDARD],
                               'jp': ['whois.jprs.jp', '', 'No match!!', '', CONST.CCTLD_STANDARD],
                               'ke': ['whois.kenic.or.ke', '', '', '', CONST.CCTLD_STANDARD],
                               'kr': ['whois.nic.or.kr', '', 'is not registered', '', CONST.CCTLD_STANDARD],
                               'kz': ['whois.nic.kz', '', 'Nothing found for this query', '', CONST.CCTLD_STANDARD],
                               'li': ['whois.nic.li', '', 'not have an entry', '', CONST.CCTLD_STANDARD],
                               'lt': ['whois.domreg.lt', '', '', '', CONST.CCTLD_STANDARD],
                               'lu': ['whois.dns.lu', '', '% No such domain', '', CONST.CCTLD_STANDARD],
                               'lv': ['whois.nic.lv', '', '', '', CONST.CCTLD_STANDARD],
                               'me': ['me.whois-servers.net', '', '', '', CONST.CCTLD_STANDARD],
                               'mg': ['whois.nic.mg', '', '', '', CONST.CCTLD_STANDARD],
                               'mil': ['whois.nic.mil', '', '', '', CONST.STLD_STANDARD],
                               'mn': ['whois.nic.mn', '', '', '', CONST.CCTLD_STANDARD],
                               'ms': ['whois.adamsnames.tc', '', 'is not registered', '', CONST.CCTLD_STANDARD],
                               'museum': ['whois.museum', '', '', '', CONST.GTLD_STANDARD],
                               'mx': ['whois.nic.mx', '', 'Object_Not_Found', '', CONST.CCTLD_STANDARD],
                               'my': ['whois.mynic.net.my', '', '', '', CONST.CCTLD_STANDARD],
                               'na': ['whois.na-nic.com.na', '', '', '', CONST.CCTLD_STANDARD],
                               'name': ['whois.nic.name', '', 'No match', '', CONST.GTLD_STANDARD],
                               'net': ['whois.internic.net', 'whois.markmonitor.com', 'No match for', '',
                                       CONST.TLD_STANDARD],
                               'nl': ['whois.domain-registry.nl', '', 'is free', '', CONST.CCTLD_STANDARD],
                               'no': ['whois.norid.no', '', '% No match', '', CONST.CCTLD_STANDARD],
                               'nu': ['whois.nic.nu', '', 'not found', '', CONST.CCTLD_STANDARD],
                               'nz': ['whois.srs.net.nz', '', '220 Available', '', CONST.CCTLD_STANDARD],
                               'org': ['whois.publicinterestregistry.net', 'whois.domain.com', 'NOT FOUND',
                                       'WHOIS LIMIT EXCEEDED', CONST.TLD_STANDARD],
                               'pl': ['whois.dns.pl', '', 'No information available', '', CONST.CCTLD_STANDARD],
                               'pm': ['whois.nic.pm', '', '', '', CONST.CCTLD_STANDARD],
                               'pr': ['whois.uprr.pr', '', '', '', CONST.CCTLD_STANDARD],
                               'pro': ['whois.registrypro.pro', '', 'NOT FOUND', '', CONST.GTLD_STANDARD],
                               're': ['whois.nic.re', '', '', '', CONST.CCTLD_STANDARD],
                               'ro': ['whois.rotld.ro', '', 'No entries found', '', CONST.CCTLD_STANDARD],
                               'ru': ['whois.ripn.net', '', 'No entries found', '', CONST.CCTLD_STANDARD],
                               'se': ['whois.iis.se', '', 'not found', '', CONST.CCTLD_STANDARD],
                               'sg': ['whois.nic.net.sg', '', 'Domain Not Found', '', CONST.CCTLD_STANDARD],
                               'sh': ['whois.nic.sh', '', 'is available', '', CONST.CCTLD_STANDARD],
                               'si': ['whois.arnes.si', '', 'No entries found', '', CONST.CCTLD_STANDARD],
                               'st': ['whois.nic.st', '', 'No entries found', '', CONST.CCTLD_STANDARD],
                               'technology': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                               'tf': ['whois.nic.tf', '', '', '', CONST.CCTLD_STANDARD],
                               'tj': ['whois.nic.tj', '', 'no match', '', CONST.CCTLD_STANDARD],
                               'tk': ['whois.dot.tk', '', 'domain name not known', '', CONST.CCTLD_STANDARD],
                               'tl': ['whois.nic.tl', '', '', '', CONST.CCTLD_STANDARD],
                               'tm': ['whois.nic.tm', '', 'is available', '', CONST.CCTLD_STANDARD],
                               'to': ['monarch.tonic.to', '', 'No match for', '', CONST.CCTLD_STANDARD],
                               'today': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                               'tr': ['whois.nic.tr', '', '', '', CONST.CCTLD_STANDARD],
                               'tv': ['whois.nic.tv', '', 'No match for', '', CONST.CCTLD_STANDARD],
                               'tw': ['whois.twnic.net.tw', '', '', '', CONST.CCTLD_STANDARD],
                               'ua': ['whois.net.ua', '', 'No entries found', '', CONST.CCTLD_STANDARD],
                               'ug': ['whois.co.ug', '', 'No entries found', '', CONST.CCTLD_STANDARD],
                               'uk': ['whois.nic.uk', '', 'No match', '', CONST.CCTLD_STANDARD],
                               'us': ['whois.nic.us', '', 'Not found', '', CONST.CCTLD_STANDARD],
                               'uz': ['whois.cctld.uz', '', '', '', CONST.CCTLD_STANDARD],
                               've': ['whois.nic.ve', '', '', '', CONST.CCTLD_STANDARD],
                               'wf': ['whois.nic.wf', '', '', '', CONST.CCTLD_STANDARD],
                               'ws': ['whois.nic.ws', '', 'No match for', '', CONST.CCTLD_STANDARD],
                               'yt': ['whois.nic.yt', '', 'No entries found', '', CONST.CCTLD_STANDARD],
                               'xxx': ['whois.nic.xxx', 'whois.internic.net', 'NOT FOUND', '', CONST.GTLD_STANDARD],

                                #Add Extra gTLD's
                                'academy': ['whois.donuts.co', '', 'Domain not found',
                                            'Your request is being rate limited', CONST.GTLD_DONUTS],
                                'bike': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'builders': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'camera': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'camp': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'cab': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'careers': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'center': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'clothing': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'construction': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'contractors': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'company': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'computer': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'diamonds': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'directory': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'domains': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'education': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'enterprises': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'email': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'equipment': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'estate': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'gallery': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'glass': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'holdings': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'kicthen': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'land': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'lighting': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'limo': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                #'ninja': ['whois.unitedtld.com', '', 'Domain not found', '', CONST.GTLD_UNITED],
                                'institute': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'management': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],

                                #TODO: Server not responding
                                #'menu': ['whois.nic.menu', '', 'No Data Found', '', CONST.GTLD_STANDARD],

                                'photography': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'photos': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'plumbing': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'recipes': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'rentals': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'repair': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'sexy': ['whois.uniregistry.net', '', 'is available for registration', '',
                                         CONST.GTLD_UNIREG],
                                'shoes': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'singles': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'systems': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'support': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'soultions': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'tips': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'training': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'ventures': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'voyage': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'tattoo': ['whois.uniregistry.net', '', 'is available for registration', '',
                                           CONST.GTLD_STANDARD],
                                #'uno': ['unodominio.com', '', '', '', CONST.GTLD_STANDARD]

                                #More gTLDs
                                'agency': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'bargains': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'boutique': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'build': ['whois.nic.build', '', 'No Data Found', '', CONST.GTLD_STANDARD],
                                'buzz': ['whois.nic.buzz', '', 'Not found', '', CONST.GTLD_STANDARD],
                                'cheap': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'club': ['whois.nic.club', '', 'Not found', '',  CONST.GTLD_STANDARD],
                                'codes': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'coffee': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'cool': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'dance': ['whois.unitedtld.com', '', 'Domain not found', '', CONST.GTLD_UNITED],
                                'democrat': ['whois.unitedtld.com', '', 'Domain not found', '', CONST.GTLD_UNITED],
                                'expert': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'exposed': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'farm': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'florist': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'foundation': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_UNIREG],
                                'gift': ['whois.uniregistry.net', '', 'is available for registration', '',
                                         CONST.GTLD_UNIREG],
                                'guitars': ['whois.uniregistry.net', '', 'is available for registration', '',
                                            CONST.GTLD_DONUTS],
                                'holiday': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'house': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'international': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_STANDARD],
                                'kiwi': ['whois.dot-kiwi.com', '', 'Not Registered', '', CONST.GTLD_STANDARD],
                                'link': ['whois.uniregistry.net', '', 'is available for registration', '',
                                         CONST.GTLD_UNIREG],

                                #TODO: Server not responding
                                #'luxury': ['whois.nic.luxury', '', 'No Data Found', '', CONST.GTLD_STANDARD],

                                'marketing': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'onl': ['whois.afilias-srs.net', '', 'NOT FOUND', '', CONST.GTLD_STANDARD],
                                'pics': ['whois.uniregistry.net', '', 'is available for registration', '',
                                         CONST.GTLD_UNIREG],
                                'properties': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'qpon': ['whois.nic.qpon', '', 'Not found', '', CONST.GTLD_STANDARD],
                                'solar': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'viajes': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'watch': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'works': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS],
                                'zone': ['whois.donuts.co', '', 'Domain not found', '', CONST.GTLD_DONUTS]
                                }

        self.all_info_map = {'ac': ['N/A', 'Expiry :s*(.+)', 'N/A', 'N/A', 'N/A'],
                             'aero': ['N/A', 'Expires On:s*(.+)', 'Updated On:s*(.+)', 'Registrants*(.+)',
                                      'Name Server:s*(.+)'],
                             'af': ['Creation Dates*(.+)', 'Registry Expiry Dates*(.+)', 'Updated Date:s*(.+)',
                                    'Registrants*(.+)', 'Name Server:s*(.+)'],
                             'ag': ['Created Ons*(.+)', 'Expiration Date:s*(.+)', 'Last Updated On:s*(.+)',
                                    'Registrants*(.+)', 'Name Server:s*(.+)'],
                             'am': ['Registered:s*(.+)', 'Expires:s*(.+)', 'Last modified:s*(.+)', 'Registrant:s*(.+)',
                                    'N/A'],
                             'as': ['Created:s*(.+)', 'Expires:s*(.+)', 'N/A', 'Registrant:s*(.+)',
                                    'Name Servers:s*(.+)'],
                             'at': ['N/A', 'N/A', 'N/A', 'registrant:s*(.+)', 'N/A'],
                             'au': ['N/A', 'N/A', 'N/A', 'Registrants*(.+)', 'N/A'],
                             'be': ['N/A', 'N/A', 'N/A', 'Registrant:s*(.+)', 'Nameservers:s*(.+)'],
                             'biz': ['Createds*(.+)', 'Expiration Date:s*(.+)', 'Last Updated Date:s*(.+)',
                                     'Registrants*(.+)', 'Name Server:s*(.+)'],
                             'bj': ['N/A', 'N/A', 'Last Updated:s*(.+)', 'N/A', 'N/A'],
                             'br': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'bz': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'ca': ['Creation date:s*(.+)', 'Expiry date:s*(.+)', 'Updated date:s*(.+)',
                                    'Registrant:s*(.+)', 'Name servers:s*(.+)'],
                             'cat': ['Created Ons*(.+)', 'Expiration Date:s*(.+)', 'Last Updated On:s*(.+)',
                                     'Registrants*(.+)', 'Name Servers*(.+)'],
                             'cc': ['Creation Dates*(.+)', 'N/A', 'N/A', 'N/A', 'Name Server:s*(.+)'],
                             'cd': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'ch': ['N/A', 'N/A', 'N/A', 'N/A', 'Name servers:s*(.+)'],
                             'ci': ['N/A', 'Expiration date:s*(.+)', 'N/A', 'N/A', 'Nameserver:s*(.+)'],
                             'cl': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'cn': ['N/A', 'Expiration Date:s*(.+)', 'N/A', 'Registrants*(.+)', 'Name Server:s*(.+)'],
                             'com': ['Creation Date:s*(.+)', ' Expiration Date:s*(.+)', 'Updated Date:s*(.+)',
                                     'Registrants*(.+)', 'Name Server:s*(.+)'],
                             'coop': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'cx': ['Creation Dates*(.+)', 'Registry Expiry Dates*(.+)', 'Updated Date:s*(.+)',
                                    'Registrants*(.+)', 'Name Server:s*(.+)'],
                             'cz': ['created:s*(.+)', 'N/A', 'N/A', 'registrant:s*(.+)', 'N/A'],
                             'de': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'dk': ['N/A', 'Expires:s*(.+)', 'N/A', 'N/A', 'Nameserverss*(.+)'],
                             'edu': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'ee': ['created:s*(.+)', 'N/A', 'N/A', 'registrant:s*(.+)', 'N/A'],
                             'eu': ['N/A', 'N/A', 'N/A', 'N/A', 'Name servers:s*(.+)'],
                             'fi': ['created:s*(.+)', 'expires:s*(.+)', 'N/A', 'N/A', 'N/A'],
                             'fr': ['created:s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'gf': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'gg': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'gov': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'gr': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'hk': ['N/A', 'Expiry Date:s*(.+)', 'N/A', 'N/A', 'Name Server:s*(.+)'],
                             'hn': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'hu': ['record createds*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'ie': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'il': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'in': ['Created Ons*(.+)', 'Expiration Date:s*(.+)', 'Last Updated On:s*(.+)',
                                    'Registrants*(.+)', 'Name Server:s*(.+)'],
                             'info': ['Created Ons*(.+)', 'Expiration Date:s*(.+)', 'Last Updated On:s*(.+)',
                                      'Registrants*(.+)', 'Name Server:s*(.+)'],
                             'int': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'io': ['N/A', 'Expires :s*(.+)', 'Last Updated :s*(.+)', 'N/A', 'N/A'],
                             'is': ['created:s*(.+)', 'expires:s*(.+)', 'N/A', 'N/A', 'N/A'],
                             'it': ['Created:s*(.+)', 'N/A', 'N/A', 'N/A', 'Nameserverss*(.+)'],
                             'jp': ['Created ons*(.+)', 'Expires ons*(.+)', 'Last Updateds*(.+)', 'N/A',
                                    'Name Servers*(.+)'],
                             'ke': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'kr': ['N/A', 'Expiration Date             :s*(.+)', 'Last Updated Date           :s*(.+)',
                                    'Registrants*(.+)', 'Name Servers*(.+)'],
                             'kz': ['Domain createds*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'li': ['N/A', 'N/A', 'N/A', 'N/A', 'Name servers:s*(.+)'],
                             'lt': ['N/A', 'N/A', 'N/A', 'N/A', 'Nameserver:s*(.+)'],
                             'lu': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'lv': ['N/A', 'N/A', 'Updated:s*(.+)', 'N/A', 'N/A'],
                             'me': ['Create Date:s*(.+)', 'Expiration Date:s*(.+)', 'Updated Date:s*(.+)',
                                    'Registrant s*(.+)', 'Nameservers:s*(.+)'],
                             'mg': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'mil': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'mn': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'ms': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'museum': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'mx': ['Created Ons*(.+)', 'Expiration Date:   s*(.+)', 'Last Updated On:   s*(.+)', 'N/A',
                                    'Name Servers:s*(.+)'],
                             'my': ['Record Createds*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'na': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'name': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'net': ['Creation Date:s*(.+)', 'Expiration Date:s*(.+)', 'Updated Date:s*(.+)',
                                     'Registrants*(.+)', 'Name Server:s*(.+)'],
                             'nl': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'no': ['N/A', 'N/A', 'Last updated:s*(.+)', 'N/A', 'N/A'],
                             'nu': ['N/A', 'expires:s*(.+)', 'N/A', 'N/A', 'N/A'],
                             'nz': ['domain_date registered:s*(.+)', 'domain_datebilleduntil:s*(.+)',
                                    'domain_datelastmodified:s*(.+)', 'registrant_contact_name:s*(.+)',
                                    'ns_name_01:s*(.+)'],
                             'org': ['Creation Date:s*(.+)', 'Expiry Date:s*(.+)', 'Updated Date:s*(.+)',
                                     'Registrants*(.+)', 'Name Server:s*(.+)'],
                             'pl': ['option created:s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'pm': ['created:s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'pr': ['N/A', 'expiration date:       s*(.+)', 'N/A', 'N/A', 'N/A'],
                             'pro': ['created:s*(.+)', 'Expiration Date:s*(.+)', 'Last Updated On:s*(.+)',
                                     'Registrants*(.+)', 'Name Server:s*(.+)'],
                             're': ['created:s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'ro': ['Registered On:s*(.+)', 'N/A', 'N/A', 'N/A', 'Nameserver:s*(.+)'],
                             'ru': ['created:s*(.+)', 'N/A', 'Last updated ons*(.+)', 'N/A', 'N/A'],
                             'se': ['created:s*(.+)', 'expires:s*(.+)', 'N/A', 'N/A', 'N/A'],
                             'sg': ['Creation Dates*(.+)', 'Expiration Date:s*(.+)', 'N/A', 'N/A',
                                    'Name Servers:s*(.+)'],
                             'sh': ['N/A', 'Expiry :s*(.+)', 'N/A', 'N/A', 'N/A'],
                             'si': ['created:s*(.+)', 'N/A', 'N/A', 'N/A', 'nameserver:s*(.+)'],
                             'st': ['created-date:s*(.+)', 'expiration-date:s*(.+)', 'updated-date:s*(.+)',
                                    'registrant-s*(.+)', 'Name Server:s*(.+)'],
                             'tf': ['created:s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'tj': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'tk': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'tl': ['Creation Dates*(.+)', 'Expiry Date:s*(.+)', 'Updated Date:s*(.+)',
                                    'Registrants*(.+)', 'Name Server:s*(.+)'],
                             'tm': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'to': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'tr': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'tv': ['Creation Date:s*(.+)', 'N/A', 'Updated Date:s*(.+)', 'N/A', 'Name Server:s*(.+)'],
                             'tw': ['Record created ons*(.+)', 'expires ons*(.+)', 'N/A', 'Registrants*(.+)', 'N/A'],
                             'ua': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'ug': ['Registered:s*(.+)', 'Expiry:             s*(.+)', 'Updated:s*(.+)', 'N/A',
                                    'Nameserver:s*(.+)'],
                             'uk': ['Registered on:s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'us': ['Last Transferred Date:s*(.+)', 'Expiration Date:s*(.+)',
                                    'Domain Last Updated Date:s*(.+)', 'Registrants*(.+)', 'Name Server:s*(.+)'],
                             'uz': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             've': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'wf': ['created:s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'ws': ['Creation Dates*(.+)', 'Expiration Date:s*(.+)', 'Updated Date:s*(.+)',
                                    'Registrants*(.+)', 'Name Server:s*(.+)'],
                             'yt': ['created:s*(.+)', 'anniversary:s*(.+)', 'last-update:s*(.+)', 'N/A', 'N/A'],
                             'xxx': ['Creation Date:s*(.+)', 'Updated Date:s*(.+)', 'Expiry Date:s*(.+)',
                                     'Registrants*(.+)', 'Name Server:s*(.+)'],

                             #Standard gtld's
                             'menu': ['Creation Date:s*(.+)', 'Registry Expiry Date:s*(.+)', 'Updated Date:s*(.+)',
                                      'Registrant:s*(.+)', 'N/A'],
                             'buzz': ['Registration Date:s*(.+)', 'Expiration Date:s*(.+)', 'Last Updated Date:s*(.+)',
                                      'Updated by Registrar:s*(.+)', 'Name Server:s*(.+)'],
                             'build': ['Creation Date:s*(.+)', 'Registry Expiry Date:s*(.+)', 'Updated Date::s*(.+)',
                                       'Registrant Name:s*(.+)', 'N/A'],
                             'club': ['Domain Registration Date:s*(.+)', 'Domain Expiration Date::s*(.+)',
                                      'Domain Last Updated Date::s*(.+)', 'Last Updated by Registrar: :s*(.+)', 'N/A'],
                             'kiwi': ['Creation Date:s*(.+)', 'Registry Expiry Date:s*(.+)', 'Updated Date:s*(.+)',
                                      'Registrant ID:', 'Name Server:s*(.+)'],
                             'luxury': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             'onl': ['Creation Date:s*(.+)', 'Registry Expiry Date: ', 'Updated Date:s*(.+)',
                                     'Registrant ID:', 'Name Server:s*(.+)'],
                             'qpon': ['Domain Registration Date:s*(.+)', 'Domain Expiration Date: s*(.+)',
                                      'Domain Last Updated Date: s*(.+)', 'Last Updated by Registrar:s*(.+)', 'N/A'],
                             'tattoo': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
                             #'uno': ['', '', '', '', ''],

                             #Used for all whois.donuts.co gtld's whois server
                             CONST.GTLD_DONUTS: ['Creation Date:s*(.+)', 'Expiry Date:s*(.+)', 'Updated Date:s*(.+)',
                                                 'Registrants*(.+)', 'Name Server:s*(.+)'],

                             #Used for all whois.unitedtld.com gtld's whois server
                             CONST.GTLD_UNITED: ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'],

                             #Used for all whois.uniregistry.net  gtld's whois server
                             CONST.GTLD_UNIREG: ['N/A', 'N/A', 'N/A', 'N/A', 'N/A']
                             }
