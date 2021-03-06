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


class DBRP(object):
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
        'id': 'str',
        'org_id': 'str',
        'org': 'str',
        'bucket_id': 'str',
        'database': 'str',
        'retention_policy': 'str',
        'default': 'bool',
        'links': 'Links'
    }

    attribute_map = {
        'id': 'id',
        'org_id': 'orgID',
        'org': 'org',
        'bucket_id': 'bucketID',
        'database': 'database',
        'retention_policy': 'retention_policy',
        'default': 'default',
        'links': 'links'
    }

    def __init__(self, id=None, org_id=None, org=None, bucket_id=None, database=None, retention_policy=None, default=None, links=None):  # noqa: E501
        """DBRP - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._org_id = None
        self._org = None
        self._bucket_id = None
        self._database = None
        self._retention_policy = None
        self._default = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.org_id = org_id
        self.org = org
        self.bucket_id = bucket_id
        self.database = database
        self.retention_policy = retention_policy
        if default is not None:
            self.default = default
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this DBRP.  # noqa: E501

        the mapping identifier  # noqa: E501

        :return: The id of this DBRP.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DBRP.

        the mapping identifier  # noqa: E501

        :param id: The id of this DBRP.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def org_id(self):
        """Gets the org_id of this DBRP.  # noqa: E501

        the organization ID that owns this mapping.  # noqa: E501

        :return: The org_id of this DBRP.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this DBRP.

        the organization ID that owns this mapping.  # noqa: E501

        :param org_id: The org_id of this DBRP.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def org(self):
        """Gets the org of this DBRP.  # noqa: E501

        the organization that owns this mapping.  # noqa: E501

        :return: The org of this DBRP.  # noqa: E501
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this DBRP.

        the organization that owns this mapping.  # noqa: E501

        :param org: The org of this DBRP.  # noqa: E501
        :type: str
        """
        if org is None:
            raise ValueError("Invalid value for `org`, must not be `None`")  # noqa: E501

        self._org = org

    @property
    def bucket_id(self):
        """Gets the bucket_id of this DBRP.  # noqa: E501

        the bucket ID used as target for the translation.  # noqa: E501

        :return: The bucket_id of this DBRP.  # noqa: E501
        :rtype: str
        """
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, bucket_id):
        """Sets the bucket_id of this DBRP.

        the bucket ID used as target for the translation.  # noqa: E501

        :param bucket_id: The bucket_id of this DBRP.  # noqa: E501
        :type: str
        """
        if bucket_id is None:
            raise ValueError("Invalid value for `bucket_id`, must not be `None`")  # noqa: E501

        self._bucket_id = bucket_id

    @property
    def database(self):
        """Gets the database of this DBRP.  # noqa: E501

        InfluxDB v1 database  # noqa: E501

        :return: The database of this DBRP.  # noqa: E501
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this DBRP.

        InfluxDB v1 database  # noqa: E501

        :param database: The database of this DBRP.  # noqa: E501
        :type: str
        """
        if database is None:
            raise ValueError("Invalid value for `database`, must not be `None`")  # noqa: E501

        self._database = database

    @property
    def retention_policy(self):
        """Gets the retention_policy of this DBRP.  # noqa: E501

        InfluxDB v1 retention policy  # noqa: E501

        :return: The retention_policy of this DBRP.  # noqa: E501
        :rtype: str
        """
        return self._retention_policy

    @retention_policy.setter
    def retention_policy(self, retention_policy):
        """Sets the retention_policy of this DBRP.

        InfluxDB v1 retention policy  # noqa: E501

        :param retention_policy: The retention_policy of this DBRP.  # noqa: E501
        :type: str
        """
        if retention_policy is None:
            raise ValueError("Invalid value for `retention_policy`, must not be `None`")  # noqa: E501

        self._retention_policy = retention_policy

    @property
    def default(self):
        """Gets the default of this DBRP.  # noqa: E501

        Specify if this mapping represents the default retention policy for the database specificed.  # noqa: E501

        :return: The default of this DBRP.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this DBRP.

        Specify if this mapping represents the default retention policy for the database specificed.  # noqa: E501

        :param default: The default of this DBRP.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def links(self):
        """Gets the links of this DBRP.  # noqa: E501


        :return: The links of this DBRP.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DBRP.


        :param links: The links of this DBRP.  # noqa: E501
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
        if not isinstance(other, DBRP):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
