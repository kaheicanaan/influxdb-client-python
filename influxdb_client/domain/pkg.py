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


class Pkg(object):
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
        'api_version': 'str',
        'kind': 'str',
        'meta': 'PkgMeta',
        'spec': 'PkgSpec'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'meta': 'meta',
        'spec': 'spec'
    }

    def __init__(self, api_version=None, kind=None, meta=None, spec=None):  # noqa: E501
        """Pkg - a model defined in OpenAPI"""  # noqa: E501

        self._api_version = None
        self._kind = None
        self._meta = None
        self._spec = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if meta is not None:
            self.meta = meta
        if spec is not None:
            self.spec = spec

    @property
    def api_version(self):
        """Gets the api_version of this Pkg.  # noqa: E501


        :return: The api_version of this Pkg.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this Pkg.


        :param api_version: The api_version of this Pkg.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this Pkg.  # noqa: E501


        :return: The kind of this Pkg.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Pkg.


        :param kind: The kind of this Pkg.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def meta(self):
        """Gets the meta of this Pkg.  # noqa: E501


        :return: The meta of this Pkg.  # noqa: E501
        :rtype: PkgMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Pkg.


        :param meta: The meta of this Pkg.  # noqa: E501
        :type: PkgMeta
        """

        self._meta = meta

    @property
    def spec(self):
        """Gets the spec of this Pkg.  # noqa: E501


        :return: The spec of this Pkg.  # noqa: E501
        :rtype: PkgSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this Pkg.


        :param spec: The spec of this Pkg.  # noqa: E501
        :type: PkgSpec
        """

        self._spec = spec

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
        if not isinstance(other, Pkg):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
