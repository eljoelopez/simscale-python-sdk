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


class RemoteForceLoadBC(object):
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
        'name': 'str',
        'force': 'DimensionalVectorFunctionForce',
        'moment': 'DimensionalVectorFunctionTorque',
        'scaling': 'DimensionalFunctionDimensionless',
        'phase_angle': 'DimensionalAngle',
        'remote_point': 'DimensionalVectorLength',
        'deformation_behavior': 'str',
        'topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'force': 'force',
        'moment': 'moment',
        'scaling': 'scaling',
        'phase_angle': 'phaseAngle',
        'remote_point': 'remotePoint',
        'deformation_behavior': 'deformationBehavior',
        'topological_reference': 'topologicalReference'
    }

    def __init__(self, type='REMOTE_FORCE_LOAD', name=None, force=None, moment=None, scaling=None, phase_angle=None, remote_point=None, deformation_behavior=None, topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """RemoteForceLoadBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._force = None
        self._moment = None
        self._scaling = None
        self._phase_angle = None
        self._remote_point = None
        self._deformation_behavior = None
        self._topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if force is not None:
            self.force = force
        if moment is not None:
            self.moment = moment
        if scaling is not None:
            self.scaling = scaling
        if phase_angle is not None:
            self.phase_angle = phase_angle
        if remote_point is not None:
            self.remote_point = remote_point
        if deformation_behavior is not None:
            self.deformation_behavior = deformation_behavior
        if topological_reference is not None:
            self.topological_reference = topological_reference

    @property
    def type(self):
        """Gets the type of this RemoteForceLoadBC.  # noqa: E501


        :return: The type of this RemoteForceLoadBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RemoteForceLoadBC.


        :param type: The type of this RemoteForceLoadBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this RemoteForceLoadBC.  # noqa: E501


        :return: The name of this RemoteForceLoadBC.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RemoteForceLoadBC.


        :param name: The name of this RemoteForceLoadBC.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def force(self):
        """Gets the force of this RemoteForceLoadBC.  # noqa: E501


        :return: The force of this RemoteForceLoadBC.  # noqa: E501
        :rtype: DimensionalVectorFunctionForce
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this RemoteForceLoadBC.


        :param force: The force of this RemoteForceLoadBC.  # noqa: E501
        :type: DimensionalVectorFunctionForce
        """

        self._force = force

    @property
    def moment(self):
        """Gets the moment of this RemoteForceLoadBC.  # noqa: E501


        :return: The moment of this RemoteForceLoadBC.  # noqa: E501
        :rtype: DimensionalVectorFunctionTorque
        """
        return self._moment

    @moment.setter
    def moment(self, moment):
        """Sets the moment of this RemoteForceLoadBC.


        :param moment: The moment of this RemoteForceLoadBC.  # noqa: E501
        :type: DimensionalVectorFunctionTorque
        """

        self._moment = moment

    @property
    def scaling(self):
        """Gets the scaling of this RemoteForceLoadBC.  # noqa: E501


        :return: The scaling of this RemoteForceLoadBC.  # noqa: E501
        :rtype: DimensionalFunctionDimensionless
        """
        return self._scaling

    @scaling.setter
    def scaling(self, scaling):
        """Sets the scaling of this RemoteForceLoadBC.


        :param scaling: The scaling of this RemoteForceLoadBC.  # noqa: E501
        :type: DimensionalFunctionDimensionless
        """

        self._scaling = scaling

    @property
    def phase_angle(self):
        """Gets the phase_angle of this RemoteForceLoadBC.  # noqa: E501


        :return: The phase_angle of this RemoteForceLoadBC.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._phase_angle

    @phase_angle.setter
    def phase_angle(self, phase_angle):
        """Sets the phase_angle of this RemoteForceLoadBC.


        :param phase_angle: The phase_angle of this RemoteForceLoadBC.  # noqa: E501
        :type: DimensionalAngle
        """

        self._phase_angle = phase_angle

    @property
    def remote_point(self):
        """Gets the remote_point of this RemoteForceLoadBC.  # noqa: E501


        :return: The remote_point of this RemoteForceLoadBC.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._remote_point

    @remote_point.setter
    def remote_point(self, remote_point):
        """Sets the remote_point of this RemoteForceLoadBC.


        :param remote_point: The remote_point of this RemoteForceLoadBC.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._remote_point = remote_point

    @property
    def deformation_behavior(self):
        """Gets the deformation_behavior of this RemoteForceLoadBC.  # noqa: E501

        <p>Choose the deformation behavior of the assigned entity. If <b>deformable</b> is selected, the entitiy is allowed to deform without applying additional stiffness, selecting <b>undeformable</b> leads to a rigid entity.</p>  # noqa: E501

        :return: The deformation_behavior of this RemoteForceLoadBC.  # noqa: E501
        :rtype: str
        """
        return self._deformation_behavior

    @deformation_behavior.setter
    def deformation_behavior(self, deformation_behavior):
        """Sets the deformation_behavior of this RemoteForceLoadBC.

        <p>Choose the deformation behavior of the assigned entity. If <b>deformable</b> is selected, the entitiy is allowed to deform without applying additional stiffness, selecting <b>undeformable</b> leads to a rigid entity.</p>  # noqa: E501

        :param deformation_behavior: The deformation_behavior of this RemoteForceLoadBC.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEFORMABLE", "UNDEFORMABLE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and deformation_behavior not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `deformation_behavior` ({0}), must be one of {1}"  # noqa: E501
                .format(deformation_behavior, allowed_values)
            )

        self._deformation_behavior = deformation_behavior

    @property
    def topological_reference(self):
        """Gets the topological_reference of this RemoteForceLoadBC.  # noqa: E501


        :return: The topological_reference of this RemoteForceLoadBC.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this RemoteForceLoadBC.


        :param topological_reference: The topological_reference of this RemoteForceLoadBC.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

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
        if not isinstance(other, RemoteForceLoadBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoteForceLoadBC):
            return True

        return self.to_dict() != other.to_dict()