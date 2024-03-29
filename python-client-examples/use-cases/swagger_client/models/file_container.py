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

class FileContainer(object):
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
        'relative_path': 'str',
        'file_name': 'str',
        'extension': 'str',
        'format': 'str',
        'escape_character': 'str',
        'has_header': 'bool',
        'last_modified': 'datetime',
        'line_identifier_field': 'str'
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
        'relative_path': 'relative_path',
        'file_name': 'file_name',
        'extension': 'extension',
        'format': 'format',
        'escape_character': 'escape_character',
        'has_header': 'has_header',
        'last_modified': 'last_modified',
        'line_identifier_field': 'line_identifier_field'
    }

    def __init__(self, id=None, created=None, store_type=None, datastore=None, name=None, exclude_fields=None, status=None, global_tags=None, active_freshness_sla=None, freshness_tracking_enabled=None, latest_freshness_measurement=None, relative_path=None, file_name=None, extension=None, format=None, escape_character=None, has_header=None, last_modified=None, line_identifier_field=None):  # noqa: E501
        """FileContainer - a model defined in Swagger"""  # noqa: E501
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
        self._relative_path = None
        self._file_name = None
        self._extension = None
        self._format = None
        self._escape_character = None
        self._has_header = None
        self._last_modified = None
        self._line_identifier_field = None
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
        self.relative_path = relative_path
        self.file_name = file_name
        self.extension = extension
        if format is not None:
            self.format = format
        if escape_character is not None:
            self.escape_character = escape_character
        if has_header is not None:
            self.has_header = has_header
        self.last_modified = last_modified
        if line_identifier_field is not None:
            self.line_identifier_field = line_identifier_field

    @property
    def id(self):
        """Gets the id of this FileContainer.  # noqa: E501


        :return: The id of this FileContainer.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileContainer.


        :param id: The id of this FileContainer.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this FileContainer.  # noqa: E501


        :return: The created of this FileContainer.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this FileContainer.


        :param created: The created of this FileContainer.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def store_type(self):
        """Gets the store_type of this FileContainer.  # noqa: E501


        :return: The store_type of this FileContainer.  # noqa: E501
        :rtype: str
        """
        return self._store_type

    @store_type.setter
    def store_type(self, store_type):
        """Sets the store_type of this FileContainer.


        :param store_type: The store_type of this FileContainer.  # noqa: E501
        :type: str
        """
        if store_type is None:
            raise ValueError("Invalid value for `store_type`, must not be `None`")  # noqa: E501
        allowed_values = ["file"]  # noqa: E501
        if store_type not in allowed_values:
            raise ValueError(
                "Invalid value for `store_type` ({0}), must be one of {1}"  # noqa: E501
                .format(store_type, allowed_values)
            )

        self._store_type = store_type

    @property
    def datastore(self):
        """Gets the datastore of this FileContainer.  # noqa: E501


        :return: The datastore of this FileContainer.  # noqa: E501
        :rtype: DatastoreStub
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this FileContainer.


        :param datastore: The datastore of this FileContainer.  # noqa: E501
        :type: DatastoreStub
        """
        if datastore is None:
            raise ValueError("Invalid value for `datastore`, must not be `None`")  # noqa: E501

        self._datastore = datastore

    @property
    def name(self):
        """Gets the name of this FileContainer.  # noqa: E501


        :return: The name of this FileContainer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileContainer.


        :param name: The name of this FileContainer.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def exclude_fields(self):
        """Gets the exclude_fields of this FileContainer.  # noqa: E501


        :return: The exclude_fields of this FileContainer.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude_fields

    @exclude_fields.setter
    def exclude_fields(self, exclude_fields):
        """Sets the exclude_fields of this FileContainer.


        :param exclude_fields: The exclude_fields of this FileContainer.  # noqa: E501
        :type: list[str]
        """

        self._exclude_fields = exclude_fields

    @property
    def status(self):
        """Gets the status of this FileContainer.  # noqa: E501


        :return: The status of this FileContainer.  # noqa: E501
        :rtype: ContainerStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FileContainer.


        :param status: The status of this FileContainer.  # noqa: E501
        :type: ContainerStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def global_tags(self):
        """Gets the global_tags of this FileContainer.  # noqa: E501


        :return: The global_tags of this FileContainer.  # noqa: E501
        :rtype: list[GlobalTag]
        """
        return self._global_tags

    @global_tags.setter
    def global_tags(self, global_tags):
        """Sets the global_tags of this FileContainer.


        :param global_tags: The global_tags of this FileContainer.  # noqa: E501
        :type: list[GlobalTag]
        """

        self._global_tags = global_tags

    @property
    def active_freshness_sla(self):
        """Gets the active_freshness_sla of this FileContainer.  # noqa: E501


        :return: The active_freshness_sla of this FileContainer.  # noqa: E501
        :rtype: FreshnessSla
        """
        return self._active_freshness_sla

    @active_freshness_sla.setter
    def active_freshness_sla(self, active_freshness_sla):
        """Sets the active_freshness_sla of this FileContainer.


        :param active_freshness_sla: The active_freshness_sla of this FileContainer.  # noqa: E501
        :type: FreshnessSla
        """

        self._active_freshness_sla = active_freshness_sla

    @property
    def freshness_tracking_enabled(self):
        """Gets the freshness_tracking_enabled of this FileContainer.  # noqa: E501


        :return: The freshness_tracking_enabled of this FileContainer.  # noqa: E501
        :rtype: bool
        """
        return self._freshness_tracking_enabled

    @freshness_tracking_enabled.setter
    def freshness_tracking_enabled(self, freshness_tracking_enabled):
        """Sets the freshness_tracking_enabled of this FileContainer.


        :param freshness_tracking_enabled: The freshness_tracking_enabled of this FileContainer.  # noqa: E501
        :type: bool
        """
        if freshness_tracking_enabled is None:
            raise ValueError("Invalid value for `freshness_tracking_enabled`, must not be `None`")  # noqa: E501

        self._freshness_tracking_enabled = freshness_tracking_enabled

    @property
    def latest_freshness_measurement(self):
        """Gets the latest_freshness_measurement of this FileContainer.  # noqa: E501


        :return: The latest_freshness_measurement of this FileContainer.  # noqa: E501
        :rtype: FreshnessMeasurement
        """
        return self._latest_freshness_measurement

    @latest_freshness_measurement.setter
    def latest_freshness_measurement(self, latest_freshness_measurement):
        """Sets the latest_freshness_measurement of this FileContainer.


        :param latest_freshness_measurement: The latest_freshness_measurement of this FileContainer.  # noqa: E501
        :type: FreshnessMeasurement
        """

        self._latest_freshness_measurement = latest_freshness_measurement

    @property
    def relative_path(self):
        """Gets the relative_path of this FileContainer.  # noqa: E501


        :return: The relative_path of this FileContainer.  # noqa: E501
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this FileContainer.


        :param relative_path: The relative_path of this FileContainer.  # noqa: E501
        :type: str
        """
        if relative_path is None:
            raise ValueError("Invalid value for `relative_path`, must not be `None`")  # noqa: E501

        self._relative_path = relative_path

    @property
    def file_name(self):
        """Gets the file_name of this FileContainer.  # noqa: E501


        :return: The file_name of this FileContainer.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FileContainer.


        :param file_name: The file_name of this FileContainer.  # noqa: E501
        :type: str
        """
        if file_name is None:
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501

        self._file_name = file_name

    @property
    def extension(self):
        """Gets the extension of this FileContainer.  # noqa: E501


        :return: The extension of this FileContainer.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this FileContainer.


        :param extension: The extension of this FileContainer.  # noqa: E501
        :type: str
        """
        if extension is None:
            raise ValueError("Invalid value for `extension`, must not be `None`")  # noqa: E501

        self._extension = extension

    @property
    def format(self):
        """Gets the format of this FileContainer.  # noqa: E501


        :return: The format of this FileContainer.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this FileContainer.


        :param format: The format of this FileContainer.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def escape_character(self):
        """Gets the escape_character of this FileContainer.  # noqa: E501


        :return: The escape_character of this FileContainer.  # noqa: E501
        :rtype: str
        """
        return self._escape_character

    @escape_character.setter
    def escape_character(self, escape_character):
        """Sets the escape_character of this FileContainer.


        :param escape_character: The escape_character of this FileContainer.  # noqa: E501
        :type: str
        """

        self._escape_character = escape_character

    @property
    def has_header(self):
        """Gets the has_header of this FileContainer.  # noqa: E501


        :return: The has_header of this FileContainer.  # noqa: E501
        :rtype: bool
        """
        return self._has_header

    @has_header.setter
    def has_header(self, has_header):
        """Sets the has_header of this FileContainer.


        :param has_header: The has_header of this FileContainer.  # noqa: E501
        :type: bool
        """

        self._has_header = has_header

    @property
    def last_modified(self):
        """Gets the last_modified of this FileContainer.  # noqa: E501


        :return: The last_modified of this FileContainer.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this FileContainer.


        :param last_modified: The last_modified of this FileContainer.  # noqa: E501
        :type: datetime
        """
        if last_modified is None:
            raise ValueError("Invalid value for `last_modified`, must not be `None`")  # noqa: E501

        self._last_modified = last_modified

    @property
    def line_identifier_field(self):
        """Gets the line_identifier_field of this FileContainer.  # noqa: E501


        :return: The line_identifier_field of this FileContainer.  # noqa: E501
        :rtype: str
        """
        return self._line_identifier_field

    @line_identifier_field.setter
    def line_identifier_field(self, line_identifier_field):
        """Sets the line_identifier_field of this FileContainer.


        :param line_identifier_field: The line_identifier_field of this FileContainer.  # noqa: E501
        :type: str
        """

        self._line_identifier_field = line_identifier_field

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
        if issubclass(FileContainer, dict):
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
        if not isinstance(other, FileContainer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
