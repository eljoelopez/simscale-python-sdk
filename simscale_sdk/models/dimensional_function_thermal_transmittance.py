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


class DimensionalFunctionThermalTransmittance(object):
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
        'value': 'OneOfDimensionalFunctionThermalTransmittanceValue',
        'unit': 'str'
    }

    attribute_map = {
        'value': 'value',
        'unit': 'unit'
    }

    def __init__(self, value=None, unit=None, local_vars_configuration=None):  # noqa: E501
        """DimensionalFunctionThermalTransmittance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._unit = None
        self.discriminator = None

        if value is not None:
            self.value = value
        self.unit = unit

    @property
    def value(self):
        """Gets the value of this DimensionalFunctionThermalTransmittance.  # noqa: E501


        :return: The value of this DimensionalFunctionThermalTransmittance.  # noqa: E501
        :rtype: OneOfDimensionalFunctionThermalTransmittanceValue
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DimensionalFunctionThermalTransmittance.


        :param value: The value of this DimensionalFunctionThermalTransmittance.  # noqa: E501
        :type: OneOfDimensionalFunctionThermalTransmittanceValue
        """

        self._value = value

    @property
    def unit(self):
        """Gets the unit of this DimensionalFunctionThermalTransmittance.  # noqa: E501


        :return: The unit of this DimensionalFunctionThermalTransmittance.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this DimensionalFunctionThermalTransmittance.


        :param unit: The unit of this DimensionalFunctionThermalTransmittance.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and unit is None:  # noqa: E501
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501
        allowed_values = ["W/(K·m²)", "Btu/(s·in²·°F)"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and unit not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}"  # noqa: E501
                .format(unit, allowed_values)
            )

        self._unit = unit

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
        if not isinstance(other, DimensionalFunctionThermalTransmittance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DimensionalFunctionThermalTransmittance):
            return True

        return self.to_dict() != other.to_dict()