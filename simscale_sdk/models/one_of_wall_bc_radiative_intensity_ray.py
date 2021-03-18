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


class OneOfWallBCRadiativeIntensityRay(object):
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
        'emissivity': 'float',
        'farfield_black_body_temperature': 'DimensionalTemperature',
        'transmissivity': 'float'
    }

    attribute_map = {
        'type': 'type',
        'emissivity': 'emissivity',
        'farfield_black_body_temperature': 'farfieldBlackBodyTemperature',
        'transmissivity': 'transmissivity'
    }

    discriminator_value_class_map = {
        'GREYBODY_DIFFUSIVE_RAY': 'GreybodyDiffusiveRayBC',
        'OPEN_BOUNDARY_RAY': 'OpenBoundaryRayBC',
        'SEMI_OPEN_BOUNDARY_RAY': 'SemiOpenBoundaryRayBC'
    }

    def __init__(self, type='SEMI_OPEN_BOUNDARY_RAY', emissivity=None, farfield_black_body_temperature=None, transmissivity=None, local_vars_configuration=None):  # noqa: E501
        """OneOfWallBCRadiativeIntensityRay - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._emissivity = None
        self._farfield_black_body_temperature = None
        self._transmissivity = None
        self.discriminator = 'type'

        self.type = type
        if emissivity is not None:
            self.emissivity = emissivity
        if farfield_black_body_temperature is not None:
            self.farfield_black_body_temperature = farfield_black_body_temperature
        if transmissivity is not None:
            self.transmissivity = transmissivity

    @property
    def type(self):
        """Gets the type of this OneOfWallBCRadiativeIntensityRay.  # noqa: E501


        :return: The type of this OneOfWallBCRadiativeIntensityRay.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfWallBCRadiativeIntensityRay.


        :param type: The type of this OneOfWallBCRadiativeIntensityRay.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def emissivity(self):
        """Gets the emissivity of this OneOfWallBCRadiativeIntensityRay.  # noqa: E501


        :return: The emissivity of this OneOfWallBCRadiativeIntensityRay.  # noqa: E501
        :rtype: float
        """
        return self._emissivity

    @emissivity.setter
    def emissivity(self, emissivity):
        """Sets the emissivity of this OneOfWallBCRadiativeIntensityRay.


        :param emissivity: The emissivity of this OneOfWallBCRadiativeIntensityRay.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                emissivity is not None and emissivity > 1):  # noqa: E501
            raise ValueError("Invalid value for `emissivity`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                emissivity is not None and emissivity < 0):  # noqa: E501
            raise ValueError("Invalid value for `emissivity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._emissivity = emissivity

    @property
    def farfield_black_body_temperature(self):
        """Gets the farfield_black_body_temperature of this OneOfWallBCRadiativeIntensityRay.  # noqa: E501


        :return: The farfield_black_body_temperature of this OneOfWallBCRadiativeIntensityRay.  # noqa: E501
        :rtype: DimensionalTemperature
        """
        return self._farfield_black_body_temperature

    @farfield_black_body_temperature.setter
    def farfield_black_body_temperature(self, farfield_black_body_temperature):
        """Sets the farfield_black_body_temperature of this OneOfWallBCRadiativeIntensityRay.


        :param farfield_black_body_temperature: The farfield_black_body_temperature of this OneOfWallBCRadiativeIntensityRay.  # noqa: E501
        :type: DimensionalTemperature
        """

        self._farfield_black_body_temperature = farfield_black_body_temperature

    @property
    def transmissivity(self):
        """Gets the transmissivity of this OneOfWallBCRadiativeIntensityRay.  # noqa: E501


        :return: The transmissivity of this OneOfWallBCRadiativeIntensityRay.  # noqa: E501
        :rtype: float
        """
        return self._transmissivity

    @transmissivity.setter
    def transmissivity(self, transmissivity):
        """Sets the transmissivity of this OneOfWallBCRadiativeIntensityRay.


        :param transmissivity: The transmissivity of this OneOfWallBCRadiativeIntensityRay.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                transmissivity is not None and transmissivity > 1):  # noqa: E501
            raise ValueError("Invalid value for `transmissivity`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transmissivity is not None and transmissivity < 0):  # noqa: E501
            raise ValueError("Invalid value for `transmissivity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._transmissivity = transmissivity

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
        if not isinstance(other, OneOfWallBCRadiativeIntensityRay):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfWallBCRadiativeIntensityRay):
            return True

        return self.to_dict() != other.to_dict()
