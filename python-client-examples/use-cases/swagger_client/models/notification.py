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

class Notification(object):
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
        'message': 'str',
        'target_uri': 'str',
        'target_url': 'str',
        'notification_rule': 'NotificationRule'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'message': 'message',
        'target_uri': 'target_uri',
        'target_url': 'target_url',
        'notification_rule': 'notification_rule'
    }

    def __init__(self, id=None, created=None, message=None, target_uri=None, target_url=None, notification_rule=None):  # noqa: E501
        """Notification - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created = None
        self._message = None
        self._target_uri = None
        self._target_url = None
        self._notification_rule = None
        self.discriminator = None
        self.id = id
        self.created = created
        self.message = message
        self.target_uri = target_uri
        self.target_url = target_url
        self.notification_rule = notification_rule

    @property
    def id(self):
        """Gets the id of this Notification.  # noqa: E501


        :return: The id of this Notification.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Notification.


        :param id: The id of this Notification.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this Notification.  # noqa: E501


        :return: The created of this Notification.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Notification.


        :param created: The created of this Notification.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def message(self):
        """Gets the message of this Notification.  # noqa: E501


        :return: The message of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Notification.


        :param message: The message of this Notification.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def target_uri(self):
        """Gets the target_uri of this Notification.  # noqa: E501


        :return: The target_uri of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._target_uri

    @target_uri.setter
    def target_uri(self, target_uri):
        """Sets the target_uri of this Notification.


        :param target_uri: The target_uri of this Notification.  # noqa: E501
        :type: str
        """
        if target_uri is None:
            raise ValueError("Invalid value for `target_uri`, must not be `None`")  # noqa: E501

        self._target_uri = target_uri

    @property
    def target_url(self):
        """Gets the target_url of this Notification.  # noqa: E501


        :return: The target_url of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._target_url

    @target_url.setter
    def target_url(self, target_url):
        """Sets the target_url of this Notification.


        :param target_url: The target_url of this Notification.  # noqa: E501
        :type: str
        """
        if target_url is None:
            raise ValueError("Invalid value for `target_url`, must not be `None`")  # noqa: E501

        self._target_url = target_url

    @property
    def notification_rule(self):
        """Gets the notification_rule of this Notification.  # noqa: E501


        :return: The notification_rule of this Notification.  # noqa: E501
        :rtype: NotificationRule
        """
        return self._notification_rule

    @notification_rule.setter
    def notification_rule(self, notification_rule):
        """Sets the notification_rule of this Notification.


        :param notification_rule: The notification_rule of this Notification.  # noqa: E501
        :type: NotificationRule
        """
        if notification_rule is None:
            raise ValueError("Invalid value for `notification_rule`, must not be `None`")  # noqa: E501

        self._notification_rule = notification_rule

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
        if issubclass(Notification, dict):
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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
