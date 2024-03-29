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

class CreateTableContainer(object):
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
        'store_type': 'str',
        'name': 'str',
        'field_names': 'list[str]',
        'table_type': 'str',
        'partition_field': 'str',
        'row_identifier_field': 'str',
        'incremental_identifier': 'IncrementalIdentifier'
    }

    attribute_map = {
        'store_type': 'store_type',
        'name': 'name',
        'field_names': 'field_names',
        'table_type': 'table_type',
        'partition_field': 'partition_field',
        'row_identifier_field': 'row_identifier_field',
        'incremental_identifier': 'incremental_identifier'
    }

    def __init__(self, store_type='table', name=None, field_names=None, table_type=None, partition_field=None, row_identifier_field=None, incremental_identifier=None):  # noqa: E501
        """CreateTableContainer - a model defined in Swagger"""  # noqa: E501
        self._store_type = None
        self._name = None
        self._field_names = None
        self._table_type = None
        self._partition_field = None
        self._row_identifier_field = None
        self._incremental_identifier = None
        self.discriminator = None
        if store_type is not None:
            self.store_type = store_type
        self.name = name
        if field_names is not None:
            self.field_names = field_names
        self.table_type = table_type
        if partition_field is not None:
            self.partition_field = partition_field
        if row_identifier_field is not None:
            self.row_identifier_field = row_identifier_field
        if incremental_identifier is not None:
            self.incremental_identifier = incremental_identifier

    @property
    def store_type(self):
        """Gets the store_type of this CreateTableContainer.  # noqa: E501


        :return: The store_type of this CreateTableContainer.  # noqa: E501
        :rtype: str
        """
        return self._store_type

    @store_type.setter
    def store_type(self, store_type):
        """Sets the store_type of this CreateTableContainer.


        :param store_type: The store_type of this CreateTableContainer.  # noqa: E501
        :type: str
        """
        allowed_values = ["table"]  # noqa: E501
        if store_type not in allowed_values:
            raise ValueError(
                "Invalid value for `store_type` ({0}), must be one of {1}"  # noqa: E501
                .format(store_type, allowed_values)
            )

        self._store_type = store_type

    @property
    def name(self):
        """Gets the name of this CreateTableContainer.  # noqa: E501


        :return: The name of this CreateTableContainer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTableContainer.


        :param name: The name of this CreateTableContainer.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def field_names(self):
        """Gets the field_names of this CreateTableContainer.  # noqa: E501


        :return: The field_names of this CreateTableContainer.  # noqa: E501
        :rtype: list[str]
        """
        return self._field_names

    @field_names.setter
    def field_names(self, field_names):
        """Sets the field_names of this CreateTableContainer.


        :param field_names: The field_names of this CreateTableContainer.  # noqa: E501
        :type: list[str]
        """

        self._field_names = field_names

    @property
    def table_type(self):
        """Gets the table_type of this CreateTableContainer.  # noqa: E501


        :return: The table_type of this CreateTableContainer.  # noqa: E501
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        """Sets the table_type of this CreateTableContainer.


        :param table_type: The table_type of this CreateTableContainer.  # noqa: E501
        :type: str
        """
        if table_type is None:
            raise ValueError("Invalid value for `table_type`, must not be `None`")  # noqa: E501

        self._table_type = table_type

    @property
    def partition_field(self):
        """Gets the partition_field of this CreateTableContainer.  # noqa: E501


        :return: The partition_field of this CreateTableContainer.  # noqa: E501
        :rtype: str
        """
        return self._partition_field

    @partition_field.setter
    def partition_field(self, partition_field):
        """Sets the partition_field of this CreateTableContainer.


        :param partition_field: The partition_field of this CreateTableContainer.  # noqa: E501
        :type: str
        """

        self._partition_field = partition_field

    @property
    def row_identifier_field(self):
        """Gets the row_identifier_field of this CreateTableContainer.  # noqa: E501


        :return: The row_identifier_field of this CreateTableContainer.  # noqa: E501
        :rtype: str
        """
        return self._row_identifier_field

    @row_identifier_field.setter
    def row_identifier_field(self, row_identifier_field):
        """Sets the row_identifier_field of this CreateTableContainer.


        :param row_identifier_field: The row_identifier_field of this CreateTableContainer.  # noqa: E501
        :type: str
        """

        self._row_identifier_field = row_identifier_field

    @property
    def incremental_identifier(self):
        """Gets the incremental_identifier of this CreateTableContainer.  # noqa: E501


        :return: The incremental_identifier of this CreateTableContainer.  # noqa: E501
        :rtype: IncrementalIdentifier
        """
        return self._incremental_identifier

    @incremental_identifier.setter
    def incremental_identifier(self, incremental_identifier):
        """Sets the incremental_identifier of this CreateTableContainer.


        :param incremental_identifier: The incremental_identifier of this CreateTableContainer.  # noqa: E501
        :type: IncrementalIdentifier
        """

        self._incremental_identifier = incremental_identifier

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
        if issubclass(CreateTableContainer, dict):
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
        if not isinstance(other, CreateTableContainer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
