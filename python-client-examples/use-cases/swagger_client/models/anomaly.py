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

class Anomaly(object):
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
        'uuid': 'str',
        'type': 'str',
        'is_new': 'bool',
        'archived': 'bool',
        'status': 'AnomalyStatusType',
        'source_enriched': 'bool',
        'failed_checks': 'list[FailedCheck]',
        'global_tags': 'list[GlobalTag]',
        'comments': 'list[Comment]'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'uuid': 'uuid',
        'type': 'type',
        'is_new': 'is_new',
        'archived': 'archived',
        'status': 'status',
        'source_enriched': 'source_enriched',
        'failed_checks': 'failed_checks',
        'global_tags': 'global_tags',
        'comments': 'comments'
    }

    def __init__(self, id=None, created=None, uuid=None, type=None, is_new=None, archived=None, status=None, source_enriched=None, failed_checks=None, global_tags=None, comments=None):  # noqa: E501
        """Anomaly - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created = None
        self._uuid = None
        self._type = None
        self._is_new = None
        self._archived = None
        self._status = None
        self._source_enriched = None
        self._failed_checks = None
        self._global_tags = None
        self._comments = None
        self.discriminator = None
        self.id = id
        self.created = created
        self.uuid = uuid
        self.type = type
        self.is_new = is_new
        self.archived = archived
        self.status = status
        self.source_enriched = source_enriched
        self.failed_checks = failed_checks
        if global_tags is not None:
            self.global_tags = global_tags
        if comments is not None:
            self.comments = comments

    @property
    def id(self):
        """Gets the id of this Anomaly.  # noqa: E501


        :return: The id of this Anomaly.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Anomaly.


        :param id: The id of this Anomaly.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this Anomaly.  # noqa: E501


        :return: The created of this Anomaly.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Anomaly.


        :param created: The created of this Anomaly.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def uuid(self):
        """Gets the uuid of this Anomaly.  # noqa: E501


        :return: The uuid of this Anomaly.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Anomaly.


        :param uuid: The uuid of this Anomaly.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def type(self):
        """Gets the type of this Anomaly.  # noqa: E501


        :return: The type of this Anomaly.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Anomaly.


        :param type: The type of this Anomaly.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["shape", "record"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def is_new(self):
        """Gets the is_new of this Anomaly.  # noqa: E501


        :return: The is_new of this Anomaly.  # noqa: E501
        :rtype: bool
        """
        return self._is_new

    @is_new.setter
    def is_new(self, is_new):
        """Sets the is_new of this Anomaly.


        :param is_new: The is_new of this Anomaly.  # noqa: E501
        :type: bool
        """
        if is_new is None:
            raise ValueError("Invalid value for `is_new`, must not be `None`")  # noqa: E501

        self._is_new = is_new

    @property
    def archived(self):
        """Gets the archived of this Anomaly.  # noqa: E501


        :return: The archived of this Anomaly.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this Anomaly.


        :param archived: The archived of this Anomaly.  # noqa: E501
        :type: bool
        """
        if archived is None:
            raise ValueError("Invalid value for `archived`, must not be `None`")  # noqa: E501

        self._archived = archived

    @property
    def status(self):
        """Gets the status of this Anomaly.  # noqa: E501


        :return: The status of this Anomaly.  # noqa: E501
        :rtype: AnomalyStatusType
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Anomaly.


        :param status: The status of this Anomaly.  # noqa: E501
        :type: AnomalyStatusType
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def source_enriched(self):
        """Gets the source_enriched of this Anomaly.  # noqa: E501


        :return: The source_enriched of this Anomaly.  # noqa: E501
        :rtype: bool
        """
        return self._source_enriched

    @source_enriched.setter
    def source_enriched(self, source_enriched):
        """Sets the source_enriched of this Anomaly.


        :param source_enriched: The source_enriched of this Anomaly.  # noqa: E501
        :type: bool
        """
        if source_enriched is None:
            raise ValueError("Invalid value for `source_enriched`, must not be `None`")  # noqa: E501

        self._source_enriched = source_enriched

    @property
    def failed_checks(self):
        """Gets the failed_checks of this Anomaly.  # noqa: E501


        :return: The failed_checks of this Anomaly.  # noqa: E501
        :rtype: list[FailedCheck]
        """
        return self._failed_checks

    @failed_checks.setter
    def failed_checks(self, failed_checks):
        """Sets the failed_checks of this Anomaly.


        :param failed_checks: The failed_checks of this Anomaly.  # noqa: E501
        :type: list[FailedCheck]
        """
        if failed_checks is None:
            raise ValueError("Invalid value for `failed_checks`, must not be `None`")  # noqa: E501

        self._failed_checks = failed_checks

    @property
    def global_tags(self):
        """Gets the global_tags of this Anomaly.  # noqa: E501


        :return: The global_tags of this Anomaly.  # noqa: E501
        :rtype: list[GlobalTag]
        """
        return self._global_tags

    @global_tags.setter
    def global_tags(self, global_tags):
        """Sets the global_tags of this Anomaly.


        :param global_tags: The global_tags of this Anomaly.  # noqa: E501
        :type: list[GlobalTag]
        """

        self._global_tags = global_tags

    @property
    def comments(self):
        """Gets the comments of this Anomaly.  # noqa: E501


        :return: The comments of this Anomaly.  # noqa: E501
        :rtype: list[Comment]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this Anomaly.


        :param comments: The comments of this Anomaly.  # noqa: E501
        :type: list[Comment]
        """

        self._comments = comments

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
        if issubclass(Anomaly, dict):
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
        if not isinstance(other, Anomaly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other