# -*- coding: utf-8 -*-

from mongoengine import Document, SequenceField, StringField, DictField, \
    DateTimeField, IntField, BooleanField, ListField, DecimalField, \
    ImageField, EmailField, GeoPointField, EmbeddedDocument, \
    EmbeddedDocumentField, URLField

from mongoengine import signals
from datetime import datetime


# Some nice to have collections/sets/lists
CURRENCIES = ["SEK", "EUR", "USD", "BBD"]

def update_timestamp(sender, document, **kwargs):
    """ Update the document field 'updated_at' with the current date and time.

    :param sender:
    :param document: Document updated
    :param kwargs: Any extra key value arguments
    :return: None
    """
    document.updated_at = datetime.now()


class FooContact(EmbeddedDocument):
    """ Contact information for someone, a person.
    """

    # Might be a significant piece of information
    title = StringField()

    # The contact is a person and as such has a name
    name = StringField(required=True)

    # and an email
    email = EmailField(required=True)

    # and a phone
    phone = StringField(verbose_name="Phone")


class FooPartner(Document):
    """ A Foo Café Partner

    """

    # Generated unique key
    id = SequenceField(required=True)

    # Partner name
    name = StringField(required=True)

    # What is there to know about this partner
    description = StringField()

    # URL to partner
    url = URLField()

    # NOTE! This bastard requires PIL to be installed
    logo = ImageField()

    #
    social = DictField()

    # Contact(s), embedded documents of FooContact
    contacts = ListField(field=EmbeddedDocumentField(document_type=FooContact))



class FooEvent(Document):
    """
    This is what it's all about; Events.

    Notes:

        A field that is marked required false, i.e. required=False, is actually
        going to be required=True later on. A field is not required by default.
        It has been marked False just out of laziness. I want to create model
        instances without typing myself to death...

    """

    # Category choices, see field category
    CATEGORY_CHOICES = ["Code", "Cutting Edge", "Innovation", "People", "Business"]

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
    id = SequenceField(required=True, unique=True, primary_key=True)

    # The event title
    title = StringField(required=True, max_length=255,
                        verbose_name="Event Title")

    # Event subtitle, if any
    sub_title = StringField(required=False, max_length=255)

    # A long and meaty description of the event
    description = StringField(required=False, max_length=255)

    # A name that types the event
    event_type = StringField(required=False, max_length=50)

    # An event category, might not be necessary. Is tags enough for
    # categorization. This is mainly use for filtering and organizing
    # events in the presentation, e.g. Code, People, Business, Innovation
    #category = DictField(required=False)
    category = StringField(required=True, choices=CATEGORY_CHOICES,
                           default=CATEGORY_CHOICES[0])

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

    # Date and time the event ends
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


# Register signal handler for FooEvent saves
signals.pre_save.connect(update_timestamp, sender=FooEvent)


class FooTicketInventory(Document):
    """ Ticket inventory
    """

    @staticmethod
    def create(event_id, **kwargs):
        """
        Basic factory method for creating a Ticket inventory.
        :param event_id: Id for the event, mandatory.
        :param kwargs:
        :return:
        """
        pass

    # The event
    event_id = IntField(required=True)

    # What?
    name = StringField(required=True)

    # What?
    description = StringField(required=True)

    # Price of this ticket
    price = DecimalField(default=0.0, verbose_name="Price")

    # SEK, EUR, USD etc
    currency = DictField(required=True, verbose_name="Currency",
                         choices=CURRENCIES)

    # The number of tickets available
    quantity_available = IntField(required=True)

    # Ticket sell/reservation start date, i.e.
    # date and time when tickets starts to sell
    ticket_start = DateTimeField(required=True)

    # Ticket sell/reservation end date, i.e
    # date and time when tickets should not be available anymore
    ticket_end = DateTimeField(required=True)

    # Min number of tickets that can be ...
    ticket_min = IntField(required=True)

    # Max number of tickets that can be ...
    ticket_max = IntField(required=True)

    # Constraint for attenders/users when acquiring/issuing tickets
    issuing_constraint = ListField(field=StringField())


class FooTicket(Document):
    """ Intersection between a user and a event. Records ticket
    reservations... Is it?

    Reservation == Buy ?
    """

    # Id of the event
    event_id = IntField(required=True)

    # Id of the user/attender
    user_id = IntField(required=True)

    # The amount of tickets reserved
    amount = IntField(required=True, default=1)

    # Date and time the ticket(s) was reserved/issued/bought
    created_at = DateTimeField(required=True, default=datetime.now)



class FooVenue(Document):
    """ Where it's at, the FooEvent.

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
    # better if we also know the company
    company_name = StringField()

    # Dictionary of provider name and auth token
    # e.g. github => token_github, linkedin => token_linked
    oauth_token = DictField()


# class FooUser(Document):
#   user_id = SequenceField(required=True)
#   name = StringField()
#   email = StringField()
#   oauth_data = DictField()
    
  
  