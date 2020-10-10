#!/usr/bin/python3
# code: utf-8
import json
import sys
from collections import OrderedDict

import dns.resolver


def dac(dns_val=None) -> OrderedDict:
    """
    Domain Availability Checker (DNS lookup)

    :param _dns: URL string
    :return: Availability [True, False]
    """
    ip_values = None
    avail = False

    if dns_val is None:
        raise ValueError("Sorry, DNS is needed")
    if isinstance(dns_val, str) is False:
        raise TypeError("Sorry, \'DNS\' must be type \'str\'")
    try:
        output = dns.resolver.resolve(dns_val, 'A')
        ip_values = [ipval.to_text() for ipval in output]
    except dns.resolver.NXDOMAIN:
        avail = True

    return OrderedDict([
        ("DNS", dns_val),
        ("IP", ip_values),
        ("AVAIL", avail),
    ])


if __name__ == '__main__':
    dns_val = None
    option = None

    if len(sys.argv) > 1:
        if '--dns' in sys.argv:
            d_index = sys.argv.index('--dns')
            if d_index == sys.argv.index(sys.argv[-1:][0]):
                print("Sorry, DNS was not specified")
                sys.exit(1)
            dns_val = sys.argv[sys.argv.index('--dns') + 1]
        else:
            print("help:\nuse \'--dns\' for DNS specification")
            sys.exit(1)
    try:
        response = dac(dns_val=dns_val)
    except Exception as err:
        print(f"error: {err}")
        sys.exit(1)

    print(json.dumps(response, indent=4))
    sys.exit(0)
