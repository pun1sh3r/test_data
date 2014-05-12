from datetime import datetime

from iocdb.model import Rumor, Observable, Document, TTP, Actor, Campaign

evil_domain = Observable('domain', 'evil.example.com', id=123)
extracted_blog_post = Document(
    name='some extracted intel', 
    category='osint',
    source='some blog post',
    investigator='Steven Seagal',
    received=datetime(2014, 04, 11, 16, 30),
    id=777)
feed_msg = Document(
    name='some feed message',
    category='osint',
    source='some feed',
    investigator='Jackie Chan',
    received=datetime(2013, 03, 10, 15, 29),
    id=888)
exfil = TTP(category='exfiltration site', id=22)
proxy = TTP(category='proxy', id=23)
panda = Actor(name='KungFuPanda', id=3)
guyfox = Actor(name='GuyFox', id=4)
ddos_campaign = Campaign(name='some ddos event', id=7)
breach_campaign = Campaign(name='some breach event', id=9)

rumors = [
    Rumor(
        observable=evil_domain, 
        valid=datetime(2014, 04, 10), 
        document=extracted_blog_post,
        ttp=exfil,
        actor=panda,
        campaign=breach_campaign),
    Rumor(
        observable=evil_domain,
        valid=datetime(2013, 03, 10, 15, 29),
        document=feed_msg,
        ttp=proxy,
        actor=guyfox,
        campaign=ddos_campaign)
         ]
