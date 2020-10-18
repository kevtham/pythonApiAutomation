from pykson import JsonObject, IntegerField, StringField, ObjectListField, FloatField, ObjectField

class Codes(JsonObject):
    admin_district = StringField()
    admin_county = StringField()

# Reference https://pypi.org/project/pykson/
class PostCode(JsonObject):
    postcode = StringField()
    nhs_ha = StringField()
    quality = IntegerField()
    longitude = FloatField()
    codes = ObjectField(Codes)