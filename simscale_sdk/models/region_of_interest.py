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


class RegionOfInterest(object):
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
        'disc_radius': 'DimensionalLength',
        'center_point': 'DimensionalVector2dLength',
        'ground_height': 'DimensionalLength',
        'north_angle': 'DimensionalAngle',
        'advanced_settings': 'AdvancedROISettings'
    }

    attribute_map = {
        'disc_radius': 'discRadius',
        'center_point': 'centerPoint',
        'ground_height': 'groundHeight',
        'north_angle': 'northAngle',
        'advanced_settings': 'advancedSettings'
    }

    def __init__(self, disc_radius=None, center_point=None, ground_height=None, north_angle=None, advanced_settings=None, local_vars_configuration=None):  # noqa: E501
        """RegionOfInterest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._disc_radius = None
        self._center_point = None
        self._ground_height = None
        self._north_angle = None
        self._advanced_settings = None
        self.discriminator = None

        if disc_radius is not None:
            self.disc_radius = disc_radius
        if center_point is not None:
            self.center_point = center_point
        if ground_height is not None:
            self.ground_height = ground_height
        if north_angle is not None:
            self.north_angle = north_angle
        if advanced_settings is not None:
            self.advanced_settings = advanced_settings

    @property
    def disc_radius(self):
        """Gets the disc_radius of this RegionOfInterest.  # noqa: E501


        :return: The disc_radius of this RegionOfInterest.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._disc_radius

    @disc_radius.setter
    def disc_radius(self, disc_radius):
        """Sets the disc_radius of this RegionOfInterest.


        :param disc_radius: The disc_radius of this RegionOfInterest.  # noqa: E501
        :type: DimensionalLength
        """

        self._disc_radius = disc_radius

    @property
    def center_point(self):
        """Gets the center_point of this RegionOfInterest.  # noqa: E501


        :return: The center_point of this RegionOfInterest.  # noqa: E501
        :rtype: DimensionalVector2dLength
        """
        return self._center_point

    @center_point.setter
    def center_point(self, center_point):
        """Sets the center_point of this RegionOfInterest.


        :param center_point: The center_point of this RegionOfInterest.  # noqa: E501
        :type: DimensionalVector2dLength
        """

        self._center_point = center_point

    @property
    def ground_height(self):
        """Gets the ground_height of this RegionOfInterest.  # noqa: E501


        :return: The ground_height of this RegionOfInterest.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._ground_height

    @ground_height.setter
    def ground_height(self, ground_height):
        """Sets the ground_height of this RegionOfInterest.


        :param ground_height: The ground_height of this RegionOfInterest.  # noqa: E501
        :type: DimensionalLength
        """

        self._ground_height = ground_height

    @property
    def north_angle(self):
        """Gets the north_angle of this RegionOfInterest.  # noqa: E501


        :return: The north_angle of this RegionOfInterest.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._north_angle

    @north_angle.setter
    def north_angle(self, north_angle):
        """Sets the north_angle of this RegionOfInterest.


        :param north_angle: The north_angle of this RegionOfInterest.  # noqa: E501
        :type: DimensionalAngle
        """

        self._north_angle = north_angle

    @property
    def advanced_settings(self):
        """Gets the advanced_settings of this RegionOfInterest.  # noqa: E501


        :return: The advanced_settings of this RegionOfInterest.  # noqa: E501
        :rtype: AdvancedROISettings
        """
        return self._advanced_settings

    @advanced_settings.setter
    def advanced_settings(self, advanced_settings):
        """Sets the advanced_settings of this RegionOfInterest.


        :param advanced_settings: The advanced_settings of this RegionOfInterest.  # noqa: E501
        :type: AdvancedROISettings
        """

        self._advanced_settings = advanced_settings

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
        if not isinstance(other, RegionOfInterest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegionOfInterest):
            return True

        return self.to_dict() != other.to_dict()