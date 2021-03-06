# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class DBRPs(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'notification_endpoints': 'list[DBRP]',
        'links': 'Links'
    }

    attribute_map = {
        'notification_endpoints': 'notificationEndpoints',
        'links': 'links'
    }

    def __init__(self, notification_endpoints=None, links=None):  # noqa: E501
        """DBRPs - a model defined in OpenAPI"""  # noqa: E501

        self._notification_endpoints = None
        self._links = None
        self.discriminator = None

        if notification_endpoints is not None:
            self.notification_endpoints = notification_endpoints
        if links is not None:
            self.links = links

    @property
    def notification_endpoints(self):
        """Gets the notification_endpoints of this DBRPs.  # noqa: E501


        :return: The notification_endpoints of this DBRPs.  # noqa: E501
        :rtype: list[DBRP]
        """
        return self._notification_endpoints

    @notification_endpoints.setter
    def notification_endpoints(self, notification_endpoints):
        """Sets the notification_endpoints of this DBRPs.


        :param notification_endpoints: The notification_endpoints of this DBRPs.  # noqa: E501
        :type: list[DBRP]
        """

        self._notification_endpoints = notification_endpoints

    @property
    def links(self):
        """Gets the links of this DBRPs.  # noqa: E501


        :return: The links of this DBRPs.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DBRPs.


        :param links: The links of this DBRPs.  # noqa: E501
        :type: Links
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DBRPs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
