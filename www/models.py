# -*- coding: utf-8 -*-

from mongoengine import Document, SequenceField, StringField, DictField, \
    DateTimeField, IntField, BooleanField, ListField, DecimalField, \
    ImageField, EmailField, GeoPointField

from mongoengine import signals
from datetime import datetime


def update_timestamp(sender, document, **kwargs):
    """ Update the document field 'updated_at' with the current date and time.

    :param sender:
    :param document: Document updated
    :param kwargs: Any extra key value arguments
    :return: None
    """
    document.updated_at = datetime.now()

class FooEvent(Document):
    """
    This is what it's all about; Events.

    Notes:

        A field that is marked required false, i.e. required=False, is actually
        going to be required=True later on. A field is not required by default.
        It has been marked False just out of laziness. I want to create model
        instances without typing myself to death...

    """

    @staticmethod
    def create(title, **kwargs):
        """
        Basic factory method for creating a new instance of a FooEvent with
        sane initial values.

        :param title: The title of the event
        :param kwargs:
        :return: A FooEvent instance
        """

        result = FooEvent(title=title)
        result.sub_title = "Give me a sub title!"
        result.description = "And a description too..."

        now = datetime.now() # Timezone!!

        result.event_start = datetime(now.year, now.month, now.day, 8)
        result.event_end = datetime(now.year, now.month, now.day, 17)

        return result


    def __str__(self):
        return "FooEvent: [%d] %s" % (self.event_id, self.title)

    # Unique id for this event. Auto incremented
    event_id = SequenceField(required=True, unique=True, primary_key=True)

    # The event title
    title = StringField(required=True, max_length=255,
                        verbose_name="Event Title")

    # Event subtitle, if any
    sub_title = StringField(required=False, max_length=255)

    # A long and meaty description of the event
    description = StringField(required=False, max_length=255)

    # A name that types the event
    event_type = StringField(required=False, max_length=50)

    # An event category
    category = DictField(required=False)

    # Tags assigned to this event
    tags = ListField(StringField(max_length=30))

    # Event creation bookkeeping
    created_at = DateTimeField(required=True, verbose_name="Event created at",
                               default=datetime.now)

    # Event updated bookkeeping
    updated_at = DateTimeField(required=True, verbose_name="Event updated at",
                               default=None)

    # Date and time with minute accuracy the event starts
    event_start = DateTimeField(required=False, verbose_name="Start Date")

    #
    event_end = DateTimeField(required=False, verbose_name="End Date")

    #
    event_cutoff = DateTimeField(required=False, verbose_name="Cutoff Date")

    # The status of this event. An event can have any of the following:
    #   0   Tentative
    #   1   Ready to go
    status = IntField(default=0)

    # In what timezone is this event taking place, e.g. UTC, CET, GMT etc
    timezone = StringField()

    # What was this?
    privacy = BooleanField(default=False, verbose_name="")

    # Id of the the venue, see FooVenue
    venue_id = IntField(required=False, verbose_name="Venue")

    # The partners for this event and their partnership engagement,
    # Sponsoring etc
    partner_ids = DictField(verbose_name="Partners")

    # The capacity of the event, usually number of attenders
    capacity = IntField(required=False, default=20, verbose_name="Event Capacity")

    # Changed this to a StringField from 'Blob' like field
    email_html = StringField(verbose_name="Response email in HTML")

    # Changed this to a StringField from 'Blob' like field
    email_plaintext = StringField(verbose_name="Response email in plain text")


# Register signal handler for FooEvent
signals.pre_save.connect(update_timestamp, sender=FooEvent)


# class FooTicket(Document):
#   event_id = IntField(required=True)
#   name = StringField(required=True)
#   description = StringField(required=True)
#   price = DecimalField()
#   currancy = DictField(required=True)
#   quantity_available = IntField(required=True)
#   ticket_start = DateTimeField(required=True)
#   ticket_end = DateTimeField(required=True)
#   ticket_min = IntField(required=True)
#   ticket_max = IntField(required=True)
#

class FooVenue(Document):
    """ Where it's at

    """

    def __str__(self):
        return "FooVenue: %s" % (self.name,)

    venue_id = SequenceField(required=True, unique=True, primary_key=True)

    # The name of this venue, e.g. Foo Café Malmö
    name = StringField()

    # Address line 1
    address = StringField()

    # Addressl line 2
    address2 = StringField()

    # Postal code, e.g. 222 12,
    postal_code = StringField()

    # City e.g. Malmö
    city = StringField(required=True)

    # ISO country code of the country where this venue is located, e.g SE, BB
    country_code = StringField(required=True, default="SE")

    # GEO location of this venue
    geo_location = GeoPointField()


# class FooPartner(Document):
#   partner_id = SequenceField(required=True)
#   name = StringField()
#   description = StringField()
#   email = StringField()
#   url = StringField()
#
#   # NOTE! This bastard requires PIL to be installed
#   logo = ImageField()
#
#   social = DictField()

class FooAttender(Document):
    """ A FooAttender is a person (usually) who attends any FooEvent

    """

    # Generated unique key for a FooAttender
    attender_id = SequenceField(required=True, unique=True)

    # Name, moniker of the attender, e.g. first and last name
    name = StringField(required=True, max_length=255)

    # Email address where the attender can be contacted, in most cases
    # to receive an invoice (We want your money...)
    email = EmailField(required=True)

    # Name of company the attender represents and/or works for. Even
    # better if we now the company
    company_name = StringField()



# class FooUser(Document):
#   user_id = SequenceField(required=True)
#   name = StringField()
#   email = StringField()
#   oauth_data = DictField()
    
  
  