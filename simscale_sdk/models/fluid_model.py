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


class FluidModel(object):
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
        'turbulent_schmidt_number': 'float',
        'diffusion_coefficients': 'list[DimensionalKinematicViscosity]',
        'delta_coefficient': 'OneOfFluidModelDeltaCoefficient',
        'gravity': 'DimensionalVectorAcceleration',
        'surface_tension': 'DimensionalSurfaceTension'
    }

    attribute_map = {
        'turbulent_schmidt_number': 'turbulentSchmidtNumber',
        'diffusion_coefficients': 'diffusionCoefficients',
        'delta_coefficient': 'deltaCoefficient',
        'gravity': 'gravity',
        'surface_tension': 'surfaceTension'
    }

    def __init__(self, turbulent_schmidt_number=None, diffusion_coefficients=None, delta_coefficient=None, gravity=None, surface_tension=None, local_vars_configuration=None):  # noqa: E501
        """FluidModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._turbulent_schmidt_number = None
        self._diffusion_coefficients = None
        self._delta_coefficient = None
        self._gravity = None
        self._surface_tension = None
        self.discriminator = None

        if turbulent_schmidt_number is not None:
            self.turbulent_schmidt_number = turbulent_schmidt_number
        if diffusion_coefficients is not None:
            self.diffusion_coefficients = diffusion_coefficients
        if delta_coefficient is not None:
            self.delta_coefficient = delta_coefficient
        if gravity is not None:
            self.gravity = gravity
        if surface_tension is not None:
            self.surface_tension = surface_tension

    @property
    def turbulent_schmidt_number(self):
        """Gets the turbulent_schmidt_number of this FluidModel.  # noqa: E501


        :return: The turbulent_schmidt_number of this FluidModel.  # noqa: E501
        :rtype: float
        """
        return self._turbulent_schmidt_number

    @turbulent_schmidt_number.setter
    def turbulent_schmidt_number(self, turbulent_schmidt_number):
        """Sets the turbulent_schmidt_number of this FluidModel.


        :param turbulent_schmidt_number: The turbulent_schmidt_number of this FluidModel.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                turbulent_schmidt_number is not None and turbulent_schmidt_number < 0):  # noqa: E501
            raise ValueError("Invalid value for `turbulent_schmidt_number`, must be a value greater than or equal to `0`")  # noqa: E501

        self._turbulent_schmidt_number = turbulent_schmidt_number

    @property
    def diffusion_coefficients(self):
        """Gets the diffusion_coefficients of this FluidModel.  # noqa: E501


        :return: The diffusion_coefficients of this FluidModel.  # noqa: E501
        :rtype: list[DimensionalKinematicViscosity]
        """
        return self._diffusion_coefficients

    @diffusion_coefficients.setter
    def diffusion_coefficients(self, diffusion_coefficients):
        """Sets the diffusion_coefficients of this FluidModel.


        :param diffusion_coefficients: The diffusion_coefficients of this FluidModel.  # noqa: E501
        :type: list[DimensionalKinematicViscosity]
        """

        self._diffusion_coefficients = diffusion_coefficients

    @property
    def delta_coefficient(self):
        """Gets the delta_coefficient of this FluidModel.  # noqa: E501


        :return: The delta_coefficient of this FluidModel.  # noqa: E501
        :rtype: OneOfFluidModelDeltaCoefficient
        """
        return self._delta_coefficient

    @delta_coefficient.setter
    def delta_coefficient(self, delta_coefficient):
        """Sets the delta_coefficient of this FluidModel.


        :param delta_coefficient: The delta_coefficient of this FluidModel.  # noqa: E501
        :type: OneOfFluidModelDeltaCoefficient
        """

        self._delta_coefficient = delta_coefficient

    @property
    def gravity(self):
        """Gets the gravity of this FluidModel.  # noqa: E501


        :return: The gravity of this FluidModel.  # noqa: E501
        :rtype: DimensionalVectorAcceleration
        """
        return self._gravity

    @gravity.setter
    def gravity(self, gravity):
        """Sets the gravity of this FluidModel.


        :param gravity: The gravity of this FluidModel.  # noqa: E501
        :type: DimensionalVectorAcceleration
        """

        self._gravity = gravity

    @property
    def surface_tension(self):
        """Gets the surface_tension of this FluidModel.  # noqa: E501


        :return: The surface_tension of this FluidModel.  # noqa: E501
        :rtype: DimensionalSurfaceTension
        """
        return self._surface_tension

    @surface_tension.setter
    def surface_tension(self, surface_tension):
        """Sets the surface_tension of this FluidModel.


        :param surface_tension: The surface_tension of this FluidModel.  # noqa: E501
        :type: DimensionalSurfaceTension
        """

        self._surface_tension = surface_tension

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
        if not isinstance(other, FluidModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FluidModel):
            return True

        return self.to_dict() != other.to_dict()