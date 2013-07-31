# -*- coding: utf-8 -*-

__author__ = 'H Svalin'
__version__ = '0.1.0'

import unittest

from mongoengine import *
from biz.models import FooEvent, FooPartner, FooContact


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

        event_id = event.event_id

        #event.delete()

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

        p = FooPartner(name="A Partner")
        p.description = "This partner is nice, really nice!"
        p.url = "http://www.foocafe.org"


        c  = FooContact(title="Sir", name="Hakan Svalin",
                        email="hakan.svalin@gmail.com", phone="+46 735 237494")

        p.contacts.append(c)

        p.save()
