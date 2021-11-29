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


class SnapControls(object):
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
        'mesh_to_geometry_conformation_iterations': 'int',
        'tolerance': 'float',
        'solver_iterations': 'int',
        'relax_iterations': 'int',
        'max_mex_conformation_iterations': 'int',
        'implicit_feature_snap': 'bool',
        'explicit_feature_snap': 'bool',
        'detect_features_between_multiple_surfaces': 'bool'
    }

    attribute_map = {
        'mesh_to_geometry_conformation_iterations': 'meshToGeometryConformationIterations',
        'tolerance': 'tolerance',
        'solver_iterations': 'solverIterations',
        'relax_iterations': 'relaxIterations',
        'max_mex_conformation_iterations': 'maxMexConformationIterations',
        'implicit_feature_snap': 'implicitFeatureSnap',
        'explicit_feature_snap': 'explicitFeatureSnap',
        'detect_features_between_multiple_surfaces': 'detectFeaturesBetweenMultipleSurfaces'
    }

    def __init__(self, mesh_to_geometry_conformation_iterations=None, tolerance=None, solver_iterations=None, relax_iterations=None, max_mex_conformation_iterations=None, implicit_feature_snap=None, explicit_feature_snap=None, detect_features_between_multiple_surfaces=None, local_vars_configuration=None):  # noqa: E501
        """SnapControls - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mesh_to_geometry_conformation_iterations = None
        self._tolerance = None
        self._solver_iterations = None
        self._relax_iterations = None
        self._max_mex_conformation_iterations = None
        self._implicit_feature_snap = None
        self._explicit_feature_snap = None
        self._detect_features_between_multiple_surfaces = None
        self.discriminator = None

        if mesh_to_geometry_conformation_iterations is not None:
            self.mesh_to_geometry_conformation_iterations = mesh_to_geometry_conformation_iterations
        if tolerance is not None:
            self.tolerance = tolerance
        if solver_iterations is not None:
            self.solver_iterations = solver_iterations
        if relax_iterations is not None:
            self.relax_iterations = relax_iterations
        if max_mex_conformation_iterations is not None:
            self.max_mex_conformation_iterations = max_mex_conformation_iterations
        if implicit_feature_snap is not None:
            self.implicit_feature_snap = implicit_feature_snap
        if explicit_feature_snap is not None:
            self.explicit_feature_snap = explicit_feature_snap
        if detect_features_between_multiple_surfaces is not None:
            self.detect_features_between_multiple_surfaces = detect_features_between_multiple_surfaces

    @property
    def mesh_to_geometry_conformation_iterations(self):
        """Gets the mesh_to_geometry_conformation_iterations of this SnapControls.  # noqa: E501

        <p>Define the max number of iterations to ensure that the mesh conforms to the geometry. Higher values lead to a better conforming mesh.</p>  # noqa: E501

        :return: The mesh_to_geometry_conformation_iterations of this SnapControls.  # noqa: E501
        :rtype: int
        """
        return self._mesh_to_geometry_conformation_iterations

    @mesh_to_geometry_conformation_iterations.setter
    def mesh_to_geometry_conformation_iterations(self, mesh_to_geometry_conformation_iterations):
        """Sets the mesh_to_geometry_conformation_iterations of this SnapControls.

        <p>Define the max number of iterations to ensure that the mesh conforms to the geometry. Higher values lead to a better conforming mesh.</p>  # noqa: E501

        :param mesh_to_geometry_conformation_iterations: The mesh_to_geometry_conformation_iterations of this SnapControls.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                mesh_to_geometry_conformation_iterations is not None and mesh_to_geometry_conformation_iterations < 0):  # noqa: E501
            raise ValueError("Invalid value for `mesh_to_geometry_conformation_iterations`, must be a value greater than or equal to `0`")  # noqa: E501

        self._mesh_to_geometry_conformation_iterations = mesh_to_geometry_conformation_iterations

    @property
    def tolerance(self):
        """Gets the tolerance of this SnapControls.  # noqa: E501

        <p>This parameter describes a distance (relative to the local maximum mesh edge length) within which the algorithm looks for a geometry point to snap the mesh to. Higher values lead to better snapping but are costlier.</p>  # noqa: E501

        :return: The tolerance of this SnapControls.  # noqa: E501
        :rtype: float
        """
        return self._tolerance

    @tolerance.setter
    def tolerance(self, tolerance):
        """Sets the tolerance of this SnapControls.

        <p>This parameter describes a distance (relative to the local maximum mesh edge length) within which the algorithm looks for a geometry point to snap the mesh to. Higher values lead to better snapping but are costlier.</p>  # noqa: E501

        :param tolerance: The tolerance of this SnapControls.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                tolerance is not None and tolerance < 0):  # noqa: E501
            raise ValueError("Invalid value for `tolerance`, must be a value greater than or equal to `0`")  # noqa: E501

        self._tolerance = tolerance

    @property
    def solver_iterations(self):
        """Gets the solver_iterations of this SnapControls.  # noqa: E501

        <p>This parameter defines the number of displacement relaxation iterations during the meshing process. Higher values lead to enhanced mesh quality but increase the computing time.</p>  # noqa: E501

        :return: The solver_iterations of this SnapControls.  # noqa: E501
        :rtype: int
        """
        return self._solver_iterations

    @solver_iterations.setter
    def solver_iterations(self, solver_iterations):
        """Sets the solver_iterations of this SnapControls.

        <p>This parameter defines the number of displacement relaxation iterations during the meshing process. Higher values lead to enhanced mesh quality but increase the computing time.</p>  # noqa: E501

        :param solver_iterations: The solver_iterations of this SnapControls.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                solver_iterations is not None and solver_iterations < 0):  # noqa: E501
            raise ValueError("Invalid value for `solver_iterations`, must be a value greater than or equal to `0`")  # noqa: E501

        self._solver_iterations = solver_iterations

    @property
    def relax_iterations(self):
        """Gets the relax_iterations of this SnapControls.  # noqa: E501

        <p>This parameter defines the max number of iterations to remove bad mesh points (see documentation).</p>  # noqa: E501

        :return: The relax_iterations of this SnapControls.  # noqa: E501
        :rtype: int
        """
        return self._relax_iterations

    @relax_iterations.setter
    def relax_iterations(self, relax_iterations):
        """Sets the relax_iterations of this SnapControls.

        <p>This parameter defines the max number of iterations to remove bad mesh points (see documentation).</p>  # noqa: E501

        :param relax_iterations: The relax_iterations of this SnapControls.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                relax_iterations is not None and relax_iterations < 0):  # noqa: E501
            raise ValueError("Invalid value for `relax_iterations`, must be a value greater than or equal to `0`")  # noqa: E501

        self._relax_iterations = relax_iterations

    @property
    def max_mex_conformation_iterations(self):
        """Gets the max_mex_conformation_iterations of this SnapControls.  # noqa: E501

        <p>This parameter defines the max number of iterations done to ensure that the mesh conforms to the geometry.</p>  # noqa: E501

        :return: The max_mex_conformation_iterations of this SnapControls.  # noqa: E501
        :rtype: int
        """
        return self._max_mex_conformation_iterations

    @max_mex_conformation_iterations.setter
    def max_mex_conformation_iterations(self, max_mex_conformation_iterations):
        """Sets the max_mex_conformation_iterations of this SnapControls.

        <p>This parameter defines the max number of iterations done to ensure that the mesh conforms to the geometry.</p>  # noqa: E501

        :param max_mex_conformation_iterations: The max_mex_conformation_iterations of this SnapControls.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_mex_conformation_iterations is not None and max_mex_conformation_iterations < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_mex_conformation_iterations`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_mex_conformation_iterations = max_mex_conformation_iterations

    @property
    def implicit_feature_snap(self):
        """Gets the implicit_feature_snap of this SnapControls.  # noqa: E501

        <p>Activating this makes the snapping algorithm detecting geometrical features by sampling the surface. This might be time-consuming. The other option is to create a feature refinement which also enables feature snapping.</p>  # noqa: E501

        :return: The implicit_feature_snap of this SnapControls.  # noqa: E501
        :rtype: bool
        """
        return self._implicit_feature_snap

    @implicit_feature_snap.setter
    def implicit_feature_snap(self, implicit_feature_snap):
        """Sets the implicit_feature_snap of this SnapControls.

        <p>Activating this makes the snapping algorithm detecting geometrical features by sampling the surface. This might be time-consuming. The other option is to create a feature refinement which also enables feature snapping.</p>  # noqa: E501

        :param implicit_feature_snap: The implicit_feature_snap of this SnapControls.  # noqa: E501
        :type: bool
        """

        self._implicit_feature_snap = implicit_feature_snap

    @property
    def explicit_feature_snap(self):
        """Gets the explicit_feature_snap of this SnapControls.  # noqa: E501

        <p>Use the explicitly given feature refinements for feature snapping. An explicit feature refinement can be added under 'Mesh refinement'. Specifying a feature refinement results in sharp mesh edges even with a refinement level of zero.</p>  # noqa: E501

        :return: The explicit_feature_snap of this SnapControls.  # noqa: E501
        :rtype: bool
        """
        return self._explicit_feature_snap

    @explicit_feature_snap.setter
    def explicit_feature_snap(self, explicit_feature_snap):
        """Sets the explicit_feature_snap of this SnapControls.

        <p>Use the explicitly given feature refinements for feature snapping. An explicit feature refinement can be added under 'Mesh refinement'. Specifying a feature refinement results in sharp mesh edges even with a refinement level of zero.</p>  # noqa: E501

        :param explicit_feature_snap: The explicit_feature_snap of this SnapControls.  # noqa: E501
        :type: bool
        """

        self._explicit_feature_snap = explicit_feature_snap

    @property
    def detect_features_between_multiple_surfaces(self):
        """Gets the detect_features_between_multiple_surfaces of this SnapControls.  # noqa: E501

        <p>Also detect features between multiple surfaces. This is relevant when you want to create a mesh with multiple regions - used for example in the conjugate heat transfer solver. Needs 'Use feature refinement for snapping' turned on!</p>  # noqa: E501

        :return: The detect_features_between_multiple_surfaces of this SnapControls.  # noqa: E501
        :rtype: bool
        """
        return self._detect_features_between_multiple_surfaces

    @detect_features_between_multiple_surfaces.setter
    def detect_features_between_multiple_surfaces(self, detect_features_between_multiple_surfaces):
        """Sets the detect_features_between_multiple_surfaces of this SnapControls.

        <p>Also detect features between multiple surfaces. This is relevant when you want to create a mesh with multiple regions - used for example in the conjugate heat transfer solver. Needs 'Use feature refinement for snapping' turned on!</p>  # noqa: E501

        :param detect_features_between_multiple_surfaces: The detect_features_between_multiple_surfaces of this SnapControls.  # noqa: E501
        :type: bool
        """

        self._detect_features_between_multiple_surfaces = detect_features_between_multiple_surfaces

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
        if not isinstance(other, SnapControls):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapControls):
            return True

        return self.to_dict() != other.to_dict()