from spaceone.inventory.model.resources.base import ResourceModel
from spaceone.inventory.model.resources.block_storage import VolumeModel


from schematics.types import ModelType, ListType, StringType, IntType, DateTimeType, BooleanType, FloatType, DictType, IPAddressType

class FlavorModel(ResourceModel):

    name = StringType()
    original_name = StringType(serialize_when_none=False)
    disk = IntType()
    ephemeral = IntType(default=0)
    ram = IntType()
    swap = IntType(default=0)
    vcpus = IntType()
    extra_specs = DictType(StringType)

class InstanceModel(ResourceModel):
    id = StringType()
    name = StringType()
    description = StringType()
    instance_name = StringType()
    availability_zone = StringType()
    access_ip_v4 = IPAddressType()
    access_ip_v6 = IPAddressType()
    host_id = StringType()
    compute_host = StringType()
    host_status = StringType()
    region_name = StringType()
    key_name = StringType()
    project_id = StringType()
    project_name = StringType()
    root_device_name = StringType()
    server_groups = StringType(default=None)
    user_data = StringType(default=None)
    user_id = StringType()
    status = StringType()
    attached_volumes = ListType(StringType, default=[])
    addresses = DictType(StringType)
    minimal_addresses = ListType(IPAddressType, default=[])
    security_groups = ListType(StringType, default=[])
    minimal_security_groups = ListType(StringType, default=[])
    created_at = DateTimeType()
    updated_at = DateTimeType()
    launched_at = DateTimeType()
    flavor = ModelType(FlavorModel, serialize_when_none=False)
    volumes = ListType(ModelType(VolumeModel), default=[])
