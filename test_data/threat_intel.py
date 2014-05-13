import datetime

import iocdb.model

evil_domain = iocdb.model.Observable('domain', 'evil.example.com', id=123)
extracted_blog_post = iocdb.model.Document(
    name='some extracted intel', 
    category='osint',
    source='some blog post',
    investigator='Steven Seagal',
    received=datetime.datetime(2014, 04, 11, 16, 30),
    id=777)
feed_msg = iocdb.model.Document(
    name='some feed message',
    category='osint',
    source='some feed',
    investigator='Jackie Chan',
    received=datetime.datetime(2013, 03, 10, 15, 29),
    id=888)
exfil = iocdb.model.TTP(category='exfiltration site', id=22)
proxy = iocdb.model.TTP(category='proxy', id=23)
panda = iocdb.model.Actor(name='KungFuPanda', id=3)
guyfox = iocdb.model.Actor(name='GuyFox', id=4)
ddos_campaign = iocdb.model.Campaign(name='some ddos event', id=7)
breach_campaign = iocdb.model.Campaign(name='some breach event', id=9)

rumors = [
    iocdb.model.Rumor(
        observable=evil_domain, 
        valid=datetime.datetime(2014, 04, 10), 
        document=extracted_blog_post,
        ttp=exfil,
        actor=panda,
        campaign=breach_campaign),
    iocdb.model.Rumor(
        observable=evil_domain,
        valid=datetime.datetime(2013, 03, 10, 15, 29),
        document=feed_msg,
        ttp=proxy,
        actor=guyfox,
        campaign=ddos_campaign)
         ]

import random
import string

CHARCHOICES = string.ascii_uppercase + string.digits

def make_random_string(n=6):
    return ''.join(random.choice(CHARCHOICES) for x in range(n))

MINDATETIME = datetime.datetime(datetime.MINYEAR, 01, 31)
MAXDATETIME = datetime.datetime(datetime.MAXYEAR, 12, 31)

def make_random_date(start=MINDATETIME, end=MAXDATETIME):
    delta_seconds = int((end - start).total_seconds())
    random_second = random.randint(0, delta_seconds)
    random_datetime = start + datetime.timedelta(seconds=random_second)
    return random_datetime

def make_random_rumor():
    rumor = _make_valid_ttp_observable_combo(
        valid=make_random_date(), document=make_random_document(),
        actor=make_random_actor(), campaign=make_random_campaign(),
        description=make_random_string())
    return rumor

def _make_valid_ttp_observable_combo(valid, document, actor, campaign,
                                     description):
    #TODO: do this without brute force
    rumor = None
    while not rumor:
        try:
            ttp = make_random_ttp()
            observable = make_random_observable()
            rumor = iocdb.model.Rumor(
                observable, valid, document, ttp, actor, campaign, description)
        except AttributeError:
            pass #invalid observable ttp combo

    return rumor

def make_random_document():
    document = iocdb.model.Document(
        name=make_random_string(),
        category=random.choice(iocdb.model.DOCUMENT_CATEGORY),
        source=make_random_string(),
        investigator=make_random_string(),
        tlp=random.choice(iocdb.model.TLP),
        noforn=random.choice([True, False]),
        nocomm=random.choice([True, False]),
        received=make_random_date(),
        text=make_random_string())
    return document

def make_random_actor():
    actor = iocdb.model.Actor(name=make_random_string())
    return actor

def make_random_campaign():
    campaign = iocdb.model.Campaign(name=make_random_string())
    return campaign

def make_random_ip():
    #TODO: make more random
    return random.choice(('192.0.2.1', '192.0.2.7', '192.0.2.8', '192.0.2.9'))

def make_random_cidr():
    #TODO: make more random
    return random.choice(('192.0.2.0/24', '198.51.100.0/24', '203.0.113.0/24'))

def make_random_url():
    #TODO: make more random
    return 'evil.example.com/foo'

def make_random_email():
    #TODO: make more random
    return 'evil@example.com'

def make_random_domain():
    #TODO: make more random
    return 'evil.example.com'

HEXCHOICES = ('A', 'B', 'C', 'D', 'E', 'F',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
def make_random_hex(n):
    return ''.join(random.choice(HEXCHOICES) for i in range(n))

CHARCHOICES = string.ascii_uppercase + string.digits

_observable_variety_to_random_fn = {
    'ip':make_random_ip,
    'network':make_random_cidr,
    'asn':make_random_string,
    'url':make_random_url,
    'email':make_random_email,
    'domain':make_random_domain,
    'sha256':lambda: make_random_hex(64),
    'sha1':lambda: make_random_hex(40),
    'md5':lambda: make_random_hex(32)}

def make_random_observable():
    variety = random.choice(iocdb.model.OBSERVABLE_VARIETY)
    value = _observable_variety_to_random_fn[variety]()
    observable = iocdb.model.Observable(variety, value)
    return observable

def make_random_ttp():
    ttp = iocdb.model.TTP(
        category=random.choice(iocdb.model.TTP_CATEGORY),
        actions=make_random_string(),
        malware=make_random_string())
    return ttp
