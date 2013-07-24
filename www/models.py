class FooEvent(Document):
  event_id = SequenceField(required=True)
  title = StringField(required=True, max_length=255)
  sub_title = StringField(required=True, max_length=255)
  description = StringField(required=True, max_length=255)
  event_type = StringField(required=True, max_length=50)
  category = DictField(required=True)
  event_start = DateField(required=True)
  event_end = DateField(required=True)
  event_cutoff = DateField(required=True)
  status = IntField()
  timezone = StringField()
  privacy = BoolField()
  venue_id = IntField(Required=True)
  partner_ids = DictField()
  capacity = IntField(Required=True)
  email_html = BlobField()
  email_plaintext = BlobField()

class FooTicket(Document):
  event_id = IntField(required=True)
  name = StringField(required=True)
  description = StringField(required=True)
  price = DecimalField()
  currancy = DictField(required=True)
  quantity_available = IntField(required=True)
  ticket_start = DateField(required=True)
  ticket_end = DateField(required=True)
  ticket_min = IntField(required=True)
  ticket_max = IntField(required=True)

class FooVenue(Document):
  venue_id = SequenceField(required=True)
  name = StringField()
  address = StringField()
  address2 = StringField()
  postal_code = StringField()
  city = StringField()
  coude_code = StringField()

class FooPartner(Document):
  partner_id = SequenceField(required=True)
  name = StringField()
  description = StringField()
  email = StringField()
  url = StringField()
  logo = ImageField()
  social = DictField()

class FooUser(Document):
  user_id = SequenceField(required=True)
  name = StringField()
  email = StringField()
  oauth_data = DictField()
    
  
  