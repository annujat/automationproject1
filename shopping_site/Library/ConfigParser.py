import configparser


def parse_driver(section, key):
    parse = configparser.ConfigParser()
    parse.read(".\\ConfigFile\\config.cfg")
    data = parse.get(section, key)
    return data


def parse_details(section, key):
    parse = configparser.ConfigParser()
    parse.read(".\\ConfigFile\\details.cfg")
    return parse.get(section, key)


def parse_payment_card(section, key):
    parse = configparser.ConfigParser()
    parse.read(".\\ConfigFile\\payment_card.cfg")
    return parse.get(section, key)
