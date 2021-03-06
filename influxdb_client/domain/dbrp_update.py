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


class DBRPUpdate(object):
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
        'database': 'str',
        'retention_policy': 'str',
        'default': 'bool',
        'links': 'Links'
    }

    attribute_map = {
        'database': 'database',
        'retention_policy': 'retention_policy',
        'default': 'default',
        'links': 'links'
    }

    def __init__(self, database=None, retention_policy=None, default=None, links=None):  # noqa: E501
        """DBRPUpdate - a model defined in OpenAPI"""  # noqa: E501

        self._database = None
        self._retention_policy = None
        self._default = None
        self._links = None
        self.discriminator = None

        if database is not None:
            self.database = database
        if retention_policy is not None:
            self.retention_policy = retention_policy
        if default is not None:
            self.default = default
        if links is not None:
            self.links = links

    @property
    def database(self):
        """Gets the database of this DBRPUpdate.  # noqa: E501

        InfluxDB v1 database  # noqa: E501

        :return: The database of this DBRPUpdate.  # noqa: E501
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this DBRPUpdate.

        InfluxDB v1 database  # noqa: E501

        :param database: The database of this DBRPUpdate.  # noqa: E501
        :type: str
        """

        self._database = database

    @property
    def retention_policy(self):
        """Gets the retention_policy of this DBRPUpdate.  # noqa: E501

        InfluxDB v1 retention policy  # noqa: E501

        :return: The retention_policy of this DBRPUpdate.  # noqa: E501
        :rtype: str
        """
        return self._retention_policy

    @retention_policy.setter
    def retention_policy(self, retention_policy):
        """Sets the retention_policy of this DBRPUpdate.

        InfluxDB v1 retention policy  # noqa: E501

        :param retention_policy: The retention_policy of this DBRPUpdate.  # noqa: E501
        :type: str
        """

        self._retention_policy = retention_policy

    @property
    def default(self):
        """Gets the default of this DBRPUpdate.  # noqa: E501


        :return: The default of this DBRPUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this DBRPUpdate.


        :param default: The default of this DBRPUpdate.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def links(self):
        """Gets the links of this DBRPUpdate.  # noqa: E501


        :return: The links of this DBRPUpdate.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DBRPUpdate.


        :param links: The links of this DBRPUpdate.  # noqa: E501
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
        if not isinstance(other, DBRPUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
