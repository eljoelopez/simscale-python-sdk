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


class OneOfMaterialProperty(object):
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
        'name': 'str',
        'unit': 'str',
        'value_type': 'str',
        'data_type': 'PropertyDataType',
        'value': 'object',
        'parameters': 'list[MaterialPropertyParameter]',
        'parametric_values': 'list[dict(str, object)]'
    }

    attribute_map = {
        'name': 'name',
        'unit': 'unit',
        'value_type': 'valueType',
        'data_type': 'dataType',
        'value': 'value',
        'parameters': 'parameters',
        'parametric_values': 'parametricValues'
    }

    discriminator_value_class_map = {
        'fixed': 'FixedMaterialProperty',
        'parametric': 'ParametricMaterialProperty'
    }

    def __init__(self, name=None, unit=None, value_type='parametric', data_type=None, value=None, parameters=None, parametric_values=None, local_vars_configuration=None):  # noqa: E501
        """OneOfMaterialProperty - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._unit = None
        self._value_type = None
        self._data_type = None
        self._value = None
        self._parameters = None
        self._parametric_values = None
        self.discriminator = 'value_type'

        if name is not None:
            self.name = name
        if unit is not None:
            self.unit = unit
        self.value_type = value_type
        if data_type is not None:
            self.data_type = data_type
        self.value = value
        self.parameters = parameters
        if parametric_values is not None:
            self.parametric_values = parametric_values

    @property
    def name(self):
        """Gets the name of this OneOfMaterialProperty.  # noqa: E501

        The material property name  # noqa: E501

        :return: The name of this OneOfMaterialProperty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfMaterialProperty.

        The material property name  # noqa: E501

        :param name: The name of this OneOfMaterialProperty.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def unit(self):
        """Gets the unit of this OneOfMaterialProperty.  # noqa: E501

        The material property unit  # noqa: E501

        :return: The unit of this OneOfMaterialProperty.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this OneOfMaterialProperty.

        The material property unit  # noqa: E501

        :param unit: The unit of this OneOfMaterialProperty.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def value_type(self):
        """Gets the value_type of this OneOfMaterialProperty.  # noqa: E501


        :return: The value_type of this OneOfMaterialProperty.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this OneOfMaterialProperty.


        :param value_type: The value_type of this OneOfMaterialProperty.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value_type is None:  # noqa: E501
            raise ValueError("Invalid value for `value_type`, must not be `None`")  # noqa: E501

        self._value_type = value_type

    @property
    def data_type(self):
        """Gets the data_type of this OneOfMaterialProperty.  # noqa: E501


        :return: The data_type of this OneOfMaterialProperty.  # noqa: E501
        :rtype: PropertyDataType
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this OneOfMaterialProperty.


        :param data_type: The data_type of this OneOfMaterialProperty.  # noqa: E501
        :type: PropertyDataType
        """

        self._data_type = data_type

    @property
    def value(self):
        """Gets the value of this OneOfMaterialProperty.  # noqa: E501

        The property value  # noqa: E501

        :return: The value of this OneOfMaterialProperty.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OneOfMaterialProperty.

        The property value  # noqa: E501

        :param value: The value of this OneOfMaterialProperty.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def parameters(self):
        """Gets the parameters of this OneOfMaterialProperty.  # noqa: E501

        Parameter properties of the material  # noqa: E501

        :return: The parameters of this OneOfMaterialProperty.  # noqa: E501
        :rtype: list[MaterialPropertyParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this OneOfMaterialProperty.

        Parameter properties of the material  # noqa: E501

        :param parameters: The parameters of this OneOfMaterialProperty.  # noqa: E501
        :type: list[MaterialPropertyParameter]
        """
        if self.local_vars_configuration.client_side_validation and parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

    @property
    def parametric_values(self):
        """Gets the parametric_values of this OneOfMaterialProperty.  # noqa: E501


        :return: The parametric_values of this OneOfMaterialProperty.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._parametric_values

    @parametric_values.setter
    def parametric_values(self, parametric_values):
        """Sets the parametric_values of this OneOfMaterialProperty.


        :param parametric_values: The parametric_values of this OneOfMaterialProperty.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._parametric_values = parametric_values

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, OneOfMaterialProperty):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfMaterialProperty):
            return True

        return self.to_dict() != other.to_dict()
