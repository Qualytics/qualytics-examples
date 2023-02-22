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

class CreateNotificationRule(object):
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
        'name': 'str',
        'description': 'str',
        'trigger_type': 'AllOfCreateNotificationRuleTriggerType',
        'tokenized_message': 'str',
        'receivers': 'list[CreateNotificationReceiver]',
        'team_ids': 'list[int]',
        'tags': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'trigger_type': 'trigger_type',
        'tokenized_message': 'tokenized_message',
        'receivers': 'receivers',
        'team_ids': 'team_ids',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, trigger_type=None, tokenized_message=None, receivers=None, team_ids=None, tags=None):  # noqa: E501
        """CreateNotificationRule - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._trigger_type = None
        self._tokenized_message = None
        self._receivers = None
        self._team_ids = None
        self._tags = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        self.trigger_type = trigger_type
        self.tokenized_message = tokenized_message
        if receivers is not None:
            self.receivers = receivers
        if team_ids is not None:
            self.team_ids = team_ids
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreateNotificationRule.  # noqa: E501

        Notification rule name  # noqa: E501

        :return: The name of this CreateNotificationRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateNotificationRule.

        Notification rule name  # noqa: E501

        :param name: The name of this CreateNotificationRule.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateNotificationRule.  # noqa: E501

        Notification rule description  # noqa: E501

        :return: The description of this CreateNotificationRule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateNotificationRule.

        Notification rule description  # noqa: E501

        :param description: The description of this CreateNotificationRule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def trigger_type(self):
        """Gets the trigger_type of this CreateNotificationRule.  # noqa: E501

        Notification rule trigger type  # noqa: E501

        :return: The trigger_type of this CreateNotificationRule.  # noqa: E501
        :rtype: AllOfCreateNotificationRuleTriggerType
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this CreateNotificationRule.

        Notification rule trigger type  # noqa: E501

        :param trigger_type: The trigger_type of this CreateNotificationRule.  # noqa: E501
        :type: AllOfCreateNotificationRuleTriggerType
        """
        if trigger_type is None:
            raise ValueError("Invalid value for `trigger_type`, must not be `None`")  # noqa: E501

        self._trigger_type = trigger_type

    @property
    def tokenized_message(self):
        """Gets the tokenized_message of this CreateNotificationRule.  # noqa: E501

        The custom message of notification rule  # noqa: E501

        :return: The tokenized_message of this CreateNotificationRule.  # noqa: E501
        :rtype: str
        """
        return self._tokenized_message

    @tokenized_message.setter
    def tokenized_message(self, tokenized_message):
        """Sets the tokenized_message of this CreateNotificationRule.

        The custom message of notification rule  # noqa: E501

        :param tokenized_message: The tokenized_message of this CreateNotificationRule.  # noqa: E501
        :type: str
        """
        if tokenized_message is None:
            raise ValueError("Invalid value for `tokenized_message`, must not be `None`")  # noqa: E501

        self._tokenized_message = tokenized_message

    @property
    def receivers(self):
        """Gets the receivers of this CreateNotificationRule.  # noqa: E501

        The Notification rule receivers  # noqa: E501

        :return: The receivers of this CreateNotificationRule.  # noqa: E501
        :rtype: list[CreateNotificationReceiver]
        """
        return self._receivers

    @receivers.setter
    def receivers(self, receivers):
        """Sets the receivers of this CreateNotificationRule.

        The Notification rule receivers  # noqa: E501

        :param receivers: The receivers of this CreateNotificationRule.  # noqa: E501
        :type: list[CreateNotificationReceiver]
        """

        self._receivers = receivers

    @property
    def team_ids(self):
        """Gets the team_ids of this CreateNotificationRule.  # noqa: E501

        The ids of the related team  # noqa: E501

        :return: The team_ids of this CreateNotificationRule.  # noqa: E501
        :rtype: list[int]
        """
        return self._team_ids

    @team_ids.setter
    def team_ids(self, team_ids):
        """Sets the team_ids of this CreateNotificationRule.

        The ids of the related team  # noqa: E501

        :param team_ids: The team_ids of this CreateNotificationRule.  # noqa: E501
        :type: list[int]
        """

        self._team_ids = team_ids

    @property
    def tags(self):
        """Gets the tags of this CreateNotificationRule.  # noqa: E501

        The tags of the notification rule  # noqa: E501

        :return: The tags of this CreateNotificationRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateNotificationRule.

        The tags of the notification rule  # noqa: E501

        :param tags: The tags of this CreateNotificationRule.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if issubclass(CreateNotificationRule, dict):
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
        if not isinstance(other, CreateNotificationRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
