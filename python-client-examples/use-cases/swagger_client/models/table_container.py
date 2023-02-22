# coding: utf-8

"""
    Surveillance Hub

    Qualytics API  # noqa: E501

    OpenAPI spec version: 5ca80d8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TableContainer(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'created': 'datetime',
        'store_type': 'str',
        'datastore': 'DatastoreStub',
        'name': 'str',
        'exclude_fields': 'list[str]',
        'status': 'ContainerStatus',
        'global_tags': 'list[GlobalTag]',
        'active_freshness_sla': 'FreshnessSla',
        'freshness_tracking_enabled': 'bool',
        'latest_freshness_measurement': 'FreshnessMeasurement',
        'table_type': 'str',
        'row_identifier_field': 'str',
        'partition_field': 'str',
        'incremental_field_name': 'str',
        'incremental_identifier_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'store_type': 'store_type',
        'datastore': 'datastore',
        'name': 'name',
        'exclude_fields': 'exclude_fields',
        'status': 'status',
        'global_tags': 'global_tags',
        'active_freshness_sla': 'active_freshness_sla',
        'freshness_tracking_enabled': 'freshness_tracking_enabled',
        'latest_freshness_measurement': 'latest_freshness_measurement',
        'table_type': 'table_type',
        'row_identifier_field': 'row_identifier_field',
        'partition_field': 'partition_field',
        'incremental_field_name': 'incremental_field_name',
        'incremental_identifier_type': 'incremental_identifier_type'
    }

    def __init__(self, id=None, created=None, store_type=None, datastore=None, name=None, exclude_fields=None, status=None, global_tags=None, active_freshness_sla=None, freshness_tracking_enabled=None, latest_freshness_measurement=None, table_type=None, row_identifier_field=None, partition_field=None, incremental_field_name=None, incremental_identifier_type=None):  # noqa: E501
        """TableContainer - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created = None
        self._store_type = None
        self._datastore = None
        self._name = None
        self._exclude_fields = None
        self._status = None
        self._global_tags = None
        self._active_freshness_sla = None
        self._freshness_tracking_enabled = None
        self._latest_freshness_measurement = None
        self._table_type = None
        self._row_identifier_field = None
        self._partition_field = None
        self._incremental_field_name = None
        self._incremental_identifier_type = None
        self.discriminator = None
        self.id = id
        self.created = created
        self.store_type = store_type
        self.datastore = datastore
        self.name = name
        if exclude_fields is not None:
            self.exclude_fields = exclude_fields
        self.status = status
        if global_tags is not None:
            self.global_tags = global_tags
        if active_freshness_sla is not None:
            self.active_freshness_sla = active_freshness_sla
        self.freshness_tracking_enabled = freshness_tracking_enabled
        if latest_freshness_measurement is not None:
            self.latest_freshness_measurement = latest_freshness_measurement
        self.table_type = table_type
        if row_identifier_field is not None:
            self.row_identifier_field = row_identifier_field
        if partition_field is not None:
            self.partition_field = partition_field
        if incremental_field_name is not None:
            self.incremental_field_name = incremental_field_name
        if incremental_identifier_type is not None:
            self.incremental_identifier_type = incremental_identifier_type

    @property
    def id(self):
        """Gets the id of this TableContainer.  # noqa: E501


        :return: The id of this TableContainer.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TableContainer.


        :param id: The id of this TableContainer.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this TableContainer.  # noqa: E501


        :return: The created of this TableContainer.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this TableContainer.


        :param created: The created of this TableContainer.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def store_type(self):
        """Gets the store_type of this TableContainer.  # noqa: E501


        :return: The store_type of this TableContainer.  # noqa: E501
        :rtype: str
        """
        return self._store_type

    @store_type.setter
    def store_type(self, store_type):
        """Sets the store_type of this TableContainer.


        :param store_type: The store_type of this TableContainer.  # noqa: E501
        :type: str
        """
        if store_type is None:
            raise ValueError("Invalid value for `store_type`, must not be `None`")  # noqa: E501
        allowed_values = ["table"]  # noqa: E501
        if store_type not in allowed_values:
            raise ValueError(
                "Invalid value for `store_type` ({0}), must be one of {1}"  # noqa: E501
                .format(store_type, allowed_values)
            )

        self._store_type = store_type

    @property
    def datastore(self):
        """Gets the datastore of this TableContainer.  # noqa: E501


        :return: The datastore of this TableContainer.  # noqa: E501
        :rtype: DatastoreStub
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this TableContainer.


        :param datastore: The datastore of this TableContainer.  # noqa: E501
        :type: DatastoreStub
        """
        if datastore is None:
            raise ValueError("Invalid value for `datastore`, must not be `None`")  # noqa: E501

        self._datastore = datastore

    @property
    def name(self):
        """Gets the name of this TableContainer.  # noqa: E501


        :return: The name of this TableContainer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TableContainer.


        :param name: The name of this TableContainer.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def exclude_fields(self):
        """Gets the exclude_fields of this TableContainer.  # noqa: E501


        :return: The exclude_fields of this TableContainer.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude_fields

    @exclude_fields.setter
    def exclude_fields(self, exclude_fields):
        """Sets the exclude_fields of this TableContainer.


        :param exclude_fields: The exclude_fields of this TableContainer.  # noqa: E501
        :type: list[str]
        """

        self._exclude_fields = exclude_fields

    @property
    def status(self):
        """Gets the status of this TableContainer.  # noqa: E501


        :return: The status of this TableContainer.  # noqa: E501
        :rtype: ContainerStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TableContainer.


        :param status: The status of this TableContainer.  # noqa: E501
        :type: ContainerStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def global_tags(self):
        """Gets the global_tags of this TableContainer.  # noqa: E501


        :return: The global_tags of this TableContainer.  # noqa: E501
        :rtype: list[GlobalTag]
        """
        return self._global_tags

    @global_tags.setter
    def global_tags(self, global_tags):
        """Sets the global_tags of this TableContainer.


        :param global_tags: The global_tags of this TableContainer.  # noqa: E501
        :type: list[GlobalTag]
        """

        self._global_tags = global_tags

    @property
    def active_freshness_sla(self):
        """Gets the active_freshness_sla of this TableContainer.  # noqa: E501


        :return: The active_freshness_sla of this TableContainer.  # noqa: E501
        :rtype: FreshnessSla
        """
        return self._active_freshness_sla

    @active_freshness_sla.setter
    def active_freshness_sla(self, active_freshness_sla):
        """Sets the active_freshness_sla of this TableContainer.


        :param active_freshness_sla: The active_freshness_sla of this TableContainer.  # noqa: E501
        :type: FreshnessSla
        """

        self._active_freshness_sla = active_freshness_sla

    @property
    def freshness_tracking_enabled(self):
        """Gets the freshness_tracking_enabled of this TableContainer.  # noqa: E501


        :return: The freshness_tracking_enabled of this TableContainer.  # noqa: E501
        :rtype: bool
        """
        return self._freshness_tracking_enabled

    @freshness_tracking_enabled.setter
    def freshness_tracking_enabled(self, freshness_tracking_enabled):
        """Sets the freshness_tracking_enabled of this TableContainer.


        :param freshness_tracking_enabled: The freshness_tracking_enabled of this TableContainer.  # noqa: E501
        :type: bool
        """
        if freshness_tracking_enabled is None:
            raise ValueError("Invalid value for `freshness_tracking_enabled`, must not be `None`")  # noqa: E501

        self._freshness_tracking_enabled = freshness_tracking_enabled

    @property
    def latest_freshness_measurement(self):
        """Gets the latest_freshness_measurement of this TableContainer.  # noqa: E501


        :return: The latest_freshness_measurement of this TableContainer.  # noqa: E501
        :rtype: FreshnessMeasurement
        """
        return self._latest_freshness_measurement

    @latest_freshness_measurement.setter
    def latest_freshness_measurement(self, latest_freshness_measurement):
        """Sets the latest_freshness_measurement of this TableContainer.


        :param latest_freshness_measurement: The latest_freshness_measurement of this TableContainer.  # noqa: E501
        :type: FreshnessMeasurement
        """

        self._latest_freshness_measurement = latest_freshness_measurement

    @property
    def table_type(self):
        """Gets the table_type of this TableContainer.  # noqa: E501


        :return: The table_type of this TableContainer.  # noqa: E501
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        """Sets the table_type of this TableContainer.


        :param table_type: The table_type of this TableContainer.  # noqa: E501
        :type: str
        """
        if table_type is None:
            raise ValueError("Invalid value for `table_type`, must not be `None`")  # noqa: E501
        allowed_values = ["table", "view"]  # noqa: E501
        if table_type not in allowed_values:
            raise ValueError(
                "Invalid value for `table_type` ({0}), must be one of {1}"  # noqa: E501
                .format(table_type, allowed_values)
            )

        self._table_type = table_type

    @property
    def row_identifier_field(self):
        """Gets the row_identifier_field of this TableContainer.  # noqa: E501


        :return: The row_identifier_field of this TableContainer.  # noqa: E501
        :rtype: str
        """
        return self._row_identifier_field

    @row_identifier_field.setter
    def row_identifier_field(self, row_identifier_field):
        """Sets the row_identifier_field of this TableContainer.


        :param row_identifier_field: The row_identifier_field of this TableContainer.  # noqa: E501
        :type: str
        """

        self._row_identifier_field = row_identifier_field

    @property
    def partition_field(self):
        """Gets the partition_field of this TableContainer.  # noqa: E501


        :return: The partition_field of this TableContainer.  # noqa: E501
        :rtype: str
        """
        return self._partition_field

    @partition_field.setter
    def partition_field(self, partition_field):
        """Sets the partition_field of this TableContainer.


        :param partition_field: The partition_field of this TableContainer.  # noqa: E501
        :type: str
        """

        self._partition_field = partition_field

    @property
    def incremental_field_name(self):
        """Gets the incremental_field_name of this TableContainer.  # noqa: E501


        :return: The incremental_field_name of this TableContainer.  # noqa: E501
        :rtype: str
        """
        return self._incremental_field_name

    @incremental_field_name.setter
    def incremental_field_name(self, incremental_field_name):
        """Sets the incremental_field_name of this TableContainer.


        :param incremental_field_name: The incremental_field_name of this TableContainer.  # noqa: E501
        :type: str
        """

        self._incremental_field_name = incremental_field_name

    @property
    def incremental_identifier_type(self):
        """Gets the incremental_identifier_type of this TableContainer.  # noqa: E501


        :return: The incremental_identifier_type of this TableContainer.  # noqa: E501
        :rtype: str
        """
        return self._incremental_identifier_type

    @incremental_identifier_type.setter
    def incremental_identifier_type(self, incremental_identifier_type):
        """Sets the incremental_identifier_type of this TableContainer.


        :param incremental_identifier_type: The incremental_identifier_type of this TableContainer.  # noqa: E501
        :type: str
        """

        self._incremental_identifier_type = incremental_identifier_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TableContainer, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TableContainer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other