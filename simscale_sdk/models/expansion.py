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


class Expansion(object):
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
        'expansion_coefficient': 'DimensionalFunctionThermalExpansionRate',
        'reference_temperature': 'DimensionalTemperature'
    }

    attribute_map = {
        'type': 'type',
        'expansion_coefficient': 'expansionCoefficient',
        'reference_temperature': 'referenceTemperature'
    }

    def __init__(self, type=None, expansion_coefficient=None, reference_temperature=None, local_vars_configuration=None):  # noqa: E501
        """Expansion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._expansion_coefficient = None
        self._reference_temperature = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if expansion_coefficient is not None:
            self.expansion_coefficient = expansion_coefficient
        if reference_temperature is not None:
            self.reference_temperature = reference_temperature

    @property
    def type(self):
        """Gets the type of this Expansion.  # noqa: E501


        :return: The type of this Expansion.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Expansion.


        :param type: The type of this Expansion.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def expansion_coefficient(self):
        """Gets the expansion_coefficient of this Expansion.  # noqa: E501


        :return: The expansion_coefficient of this Expansion.  # noqa: E501
        :rtype: DimensionalFunctionThermalExpansionRate
        """
        return self._expansion_coefficient

    @expansion_coefficient.setter
    def expansion_coefficient(self, expansion_coefficient):
        """Sets the expansion_coefficient of this Expansion.


        :param expansion_coefficient: The expansion_coefficient of this Expansion.  # noqa: E501
        :type: DimensionalFunctionThermalExpansionRate
        """

        self._expansion_coefficient = expansion_coefficient

    @property
    def reference_temperature(self):
        """Gets the reference_temperature of this Expansion.  # noqa: E501


        :return: The reference_temperature of this Expansion.  # noqa: E501
        :rtype: DimensionalTemperature
        """
        return self._reference_temperature

    @reference_temperature.setter
    def reference_temperature(self, reference_temperature):
        """Sets the reference_temperature of this Expansion.


        :param reference_temperature: The reference_temperature of this Expansion.  # noqa: E501
        :type: DimensionalTemperature
        """

        self._reference_temperature = reference_temperature

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
        if not isinstance(other, Expansion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Expansion):
            return True

        return self.to_dict() != other.to_dict()