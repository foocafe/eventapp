# -*- coding: utf-8 -*-

__author__ = 'H Svalin'
__version__ = '0.1.0'

import unittest
import os

from mongoengine import *
from biz.models import FooEvent, FooPartner, FooContact, FooAddress, Base64Content, \
    FooSocial

TEST_PNG = os.path.abspath(os.path.join(os.path.dirname(__file__),'../static/images/foo-logo-small.png'))

# Base64 encode the content of the specified path and return the result
def encode(path):
    with open(path, "rb") as f:
        data = f.read()
        result = data.encode("base64")
        return result

    return None



class FooEventTest(unittest.TestCase):
    """ Sloppy and simple test case for FooEvent, might want to
    elaborate on this... but isn't testing for weaklings

    """
    def setUp(self):
        self.connection = connect("fooTest")

    def tearDown(self):
        self.connection.disconnect()

    def testBasicCrud(self):

        event = FooEvent.create(title="Test title")
        event.sub_title = "A nice sub title"
        event.tags = ['coding', 'sap', 'larry_ellison']

        event.save()

        event_id = event.id

        event.delete()

        #try:
        #    FooEvent.objects.get(event_id=event_id)
        #    self.fail("This should not be here")
        #except:
        #    pass


class FooPartnerTest(unittest.TestCase):

    def setUp(self):
        self.connection = connect("fooTest")

    def tearDown(self):
        self.connection.disconnect()


    def testBasicCrud(self):

        p = FooPartner(name="Mjukvarudepartementet")
        p.url = "http://www.mjukvarudepartementet.org"


        c  = FooContact(title="VP", name="Hakan Svalin",
                        email="hakan.svalin@gmail.com", phone="+46 735 237494")

        p.contacts.append(c)

        a = FooAddress(address_1="Korsgatan 11B", postal_code="22353", city="Lund", country="SE")
        p.address = a

        s = encode(TEST_PNG)
        logo = Base64Content(name="logo.png", mime="image/png", data=s)
        p.logo = logo

        fb = FooSocial(kind=FooSocial.KINDS_MAP['facebook'], value="some-link-to-fb")
        tw = FooSocial(kind=FooSocial.KINDS_MAP['twitter'], value="some-link-to-twitter")

        p.social.append(fb)
        p.social.append(tw)

        p.save()
