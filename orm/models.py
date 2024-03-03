import mongoengine


class IpAddress(mongoengine.Document):
    ip = mongoengine.StringField(max_length=16)


class Access(mongoengine.Document):
    src_ip = mongoengine.ReferenceField(IpAddress, reverse_delete_rule=mongoengine.CASCADE)
    dst_ip = mongoengine.ReferenceField(IpAddress, reverse_delete_rule=mongoengine.CASCADE)
    port = mongoengine.IntField()
    proto = mongoengine.StringField(max_length=32)
    contract = mongoengine.StringField(max_length=256)
