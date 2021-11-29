# coding: utf-8

"""
    SimScale API

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from simscale_sdk.configuration import Configuration


class Cylinder(object):
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
        'type': 'str',
        'id': 'str',
        'name': 'str',
        'reference': 'DimensionalVectorLength',
        'axis': 'DimensionalVectorLength',
        'radius': 'DimensionalLength'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'name': 'name',
        'reference': 'reference',
        'axis': 'axis',
        'radius': 'radius'
    }

    def __init__(self, type='CYLINDER', id=None, name=None, reference=None, axis=None, radius=None, local_vars_configuration=None):  # noqa: E501
        """Cylinder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._id = None
        self._name = None
        self._reference = None
        self._axis = None
        self._radius = None
        self.discriminator = None

        self.type = type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if reference is not None:
            self.reference = reference
        if axis is not None:
            self.axis = axis
        if radius is not None:
            self.radius = radius

    @property
    def type(self):
        """Gets the type of this Cylinder.  # noqa: E501

        Schema name: Cylinder  # noqa: E501

        :return: The type of this Cylinder.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Cylinder.

        Schema name: Cylinder  # noqa: E501

        :param type: The type of this Cylinder.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def id(self):
        """Gets the id of this Cylinder.  # noqa: E501


        :return: The id of this Cylinder.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Cylinder.


        :param id: The id of this Cylinder.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Cylinder.  # noqa: E501


        :return: The name of this Cylinder.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Cylinder.


        :param name: The name of this Cylinder.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def reference(self):
        """Gets the reference of this Cylinder.  # noqa: E501


        :return: The reference of this Cylinder.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Cylinder.


        :param reference: The reference of this Cylinder.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._reference = reference

    @property
    def axis(self):
        """Gets the axis of this Cylinder.  # noqa: E501


        :return: The axis of this Cylinder.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._axis

    @axis.setter
    def axis(self, axis):
        """Sets the axis of this Cylinder.


        :param axis: The axis of this Cylinder.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._axis = axis

    @property
    def radius(self):
        """Gets the radius of this Cylinder.  # noqa: E501


        :return: The radius of this Cylinder.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Sets the radius of this Cylinder.


        :param radius: The radius of this Cylinder.  # noqa: E501
        :type: DimensionalLength
        """

        self._radius = radius

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
        if not isinstance(other, Cylinder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Cylinder):
            return True

        return self.to_dict() != other.to_dict()