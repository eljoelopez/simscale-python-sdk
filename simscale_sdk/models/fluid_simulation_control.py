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


class FluidSimulationControl(object):
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
        'end_time': 'DimensionalTime',
        'adjoint_end_time': 'DimensionalTime',
        'number_of_iterations': 'int',
        'delta_t': 'DimensionalTime',
        'adjustable_timestep': 'OneOfFluidSimulationControlAdjustableTimestep',
        'write_control': 'OneOfFluidSimulationControlWriteControl',
        'num_processors': 'int',
        'max_run_time': 'DimensionalTime',
        'velocity_scaling': 'float',
        'potential_foam_initialization': 'bool',
        'decompose_algorithm': 'OneOfFluidSimulationControlDecomposeAlgorithm',
        'relative_convergence_criteria': 'float'
    }

    attribute_map = {
        'end_time': 'endTime',
        'adjoint_end_time': 'adjointEndTime',
        'number_of_iterations': 'numberOfIterations',
        'delta_t': 'deltaT',
        'adjustable_timestep': 'adjustableTimestep',
        'write_control': 'writeControl',
        'num_processors': 'numProcessors',
        'max_run_time': 'maxRunTime',
        'velocity_scaling': 'velocityScaling',
        'potential_foam_initialization': 'potentialFoamInitialization',
        'decompose_algorithm': 'decomposeAlgorithm',
        'relative_convergence_criteria': 'relativeConvergenceCriteria'
    }

    def __init__(self, end_time=None, adjoint_end_time=None, number_of_iterations=None, delta_t=None, adjustable_timestep=None, write_control=None, num_processors=None, max_run_time=None, velocity_scaling=None, potential_foam_initialization=None, decompose_algorithm=None, relative_convergence_criteria=None, local_vars_configuration=None):  # noqa: E501
        """FluidSimulationControl - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._end_time = None
        self._adjoint_end_time = None
        self._number_of_iterations = None
        self._delta_t = None
        self._adjustable_timestep = None
        self._write_control = None
        self._num_processors = None
        self._max_run_time = None
        self._velocity_scaling = None
        self._potential_foam_initialization = None
        self._decompose_algorithm = None
        self._relative_convergence_criteria = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        if adjoint_end_time is not None:
            self.adjoint_end_time = adjoint_end_time
        if number_of_iterations is not None:
            self.number_of_iterations = number_of_iterations
        if delta_t is not None:
            self.delta_t = delta_t
        if adjustable_timestep is not None:
            self.adjustable_timestep = adjustable_timestep
        if write_control is not None:
            self.write_control = write_control
        if num_processors is not None:
            self.num_processors = num_processors
        if max_run_time is not None:
            self.max_run_time = max_run_time
        if velocity_scaling is not None:
            self.velocity_scaling = velocity_scaling
        if potential_foam_initialization is not None:
            self.potential_foam_initialization = potential_foam_initialization
        if decompose_algorithm is not None:
            self.decompose_algorithm = decompose_algorithm
        if relative_convergence_criteria is not None:
            self.relative_convergence_criteria = relative_convergence_criteria

    @property
    def end_time(self):
        """Gets the end_time of this FluidSimulationControl.  # noqa: E501


        :return: The end_time of this FluidSimulationControl.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this FluidSimulationControl.


        :param end_time: The end_time of this FluidSimulationControl.  # noqa: E501
        :type: DimensionalTime
        """

        self._end_time = end_time

    @property
    def adjoint_end_time(self):
        """Gets the adjoint_end_time of this FluidSimulationControl.  # noqa: E501


        :return: The adjoint_end_time of this FluidSimulationControl.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._adjoint_end_time

    @adjoint_end_time.setter
    def adjoint_end_time(self, adjoint_end_time):
        """Sets the adjoint_end_time of this FluidSimulationControl.


        :param adjoint_end_time: The adjoint_end_time of this FluidSimulationControl.  # noqa: E501
        :type: DimensionalTime
        """

        self._adjoint_end_time = adjoint_end_time

    @property
    def number_of_iterations(self):
        """Gets the number_of_iterations of this FluidSimulationControl.  # noqa: E501

        <b>Steady-state simulation:</b> This represents the number of total iterations at which the termination of simulation happens. No more iterations will be executed beyond that. <a href='https://www.simscale.com/docs/simulation-setup/simulation-control/' target='_blank'>Learn more</a>.<br> <b>Transient simulation:</b> This represents the number of iterations per time step. The recommended value is 25. The larger the <i>Delta t</i> value is, the larger the <i>Number of iterations</i> has to be, in order to obtain more stable, converged solution. The simulation will terminate only when the <i>End time</i> is reached.</br>  # noqa: E501

        :return: The number_of_iterations of this FluidSimulationControl.  # noqa: E501
        :rtype: int
        """
        return self._number_of_iterations

    @number_of_iterations.setter
    def number_of_iterations(self, number_of_iterations):
        """Sets the number_of_iterations of this FluidSimulationControl.

        <b>Steady-state simulation:</b> This represents the number of total iterations at which the termination of simulation happens. No more iterations will be executed beyond that. <a href='https://www.simscale.com/docs/simulation-setup/simulation-control/' target='_blank'>Learn more</a>.<br> <b>Transient simulation:</b> This represents the number of iterations per time step. The recommended value is 25. The larger the <i>Delta t</i> value is, the larger the <i>Number of iterations</i> has to be, in order to obtain more stable, converged solution. The simulation will terminate only when the <i>End time</i> is reached.</br>  # noqa: E501

        :param number_of_iterations: The number_of_iterations of this FluidSimulationControl.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                number_of_iterations is not None and number_of_iterations < 1):  # noqa: E501
            raise ValueError("Invalid value for `number_of_iterations`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_of_iterations = number_of_iterations

    @property
    def delta_t(self):
        """Gets the delta_t of this FluidSimulationControl.  # noqa: E501


        :return: The delta_t of this FluidSimulationControl.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._delta_t

    @delta_t.setter
    def delta_t(self, delta_t):
        """Sets the delta_t of this FluidSimulationControl.


        :param delta_t: The delta_t of this FluidSimulationControl.  # noqa: E501
        :type: DimensionalTime
        """

        self._delta_t = delta_t

    @property
    def adjustable_timestep(self):
        """Gets the adjustable_timestep of this FluidSimulationControl.  # noqa: E501


        :return: The adjustable_timestep of this FluidSimulationControl.  # noqa: E501
        :rtype: OneOfFluidSimulationControlAdjustableTimestep
        """
        return self._adjustable_timestep

    @adjustable_timestep.setter
    def adjustable_timestep(self, adjustable_timestep):
        """Sets the adjustable_timestep of this FluidSimulationControl.


        :param adjustable_timestep: The adjustable_timestep of this FluidSimulationControl.  # noqa: E501
        :type: OneOfFluidSimulationControlAdjustableTimestep
        """

        self._adjustable_timestep = adjustable_timestep

    @property
    def write_control(self):
        """Gets the write_control of this FluidSimulationControl.  # noqa: E501


        :return: The write_control of this FluidSimulationControl.  # noqa: E501
        :rtype: OneOfFluidSimulationControlWriteControl
        """
        return self._write_control

    @write_control.setter
    def write_control(self, write_control):
        """Sets the write_control of this FluidSimulationControl.


        :param write_control: The write_control of this FluidSimulationControl.  # noqa: E501
        :type: OneOfFluidSimulationControlWriteControl
        """

        self._write_control = write_control

    @property
    def num_processors(self):
        """Gets the num_processors of this FluidSimulationControl.  # noqa: E501

        <p>Selecting more processor cores will speed up the simulation process. Choosing a smaller computation instance will save core hours. <a href='https://www.simscale.com/docs/simulation-setup/simulation-control-fluid/#number-of-processors' target='_blank'>Learn more</a>.</p>  # noqa: E501

        :return: The num_processors of this FluidSimulationControl.  # noqa: E501
        :rtype: int
        """
        return self._num_processors

    @num_processors.setter
    def num_processors(self, num_processors):
        """Sets the num_processors of this FluidSimulationControl.

        <p>Selecting more processor cores will speed up the simulation process. Choosing a smaller computation instance will save core hours. <a href='https://www.simscale.com/docs/simulation-setup/simulation-control-fluid/#number-of-processors' target='_blank'>Learn more</a>.</p>  # noqa: E501

        :param num_processors: The num_processors of this FluidSimulationControl.  # noqa: E501
        :type: int
        """
        allowed_values = [-1, 1, 2, 4, 8, 16, 32, 64, 96]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and num_processors not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `num_processors` ({0}), must be one of {1}"  # noqa: E501
                .format(num_processors, allowed_values)
            )

        self._num_processors = num_processors

    @property
    def max_run_time(self):
        """Gets the max_run_time of this FluidSimulationControl.  # noqa: E501


        :return: The max_run_time of this FluidSimulationControl.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._max_run_time

    @max_run_time.setter
    def max_run_time(self, max_run_time):
        """Sets the max_run_time of this FluidSimulationControl.


        :param max_run_time: The max_run_time of this FluidSimulationControl.  # noqa: E501
        :type: DimensionalTime
        """

        self._max_run_time = max_run_time

    @property
    def velocity_scaling(self):
        """Gets the velocity_scaling of this FluidSimulationControl.  # noqa: E501

        <p>It affects the stability of the simulation. The default value of 0.1 is a good compromise between accuracy and computational requirements. Lower values of this parameter might increase the stability of the simulation at the cost of higher computational time.</p>  # noqa: E501

        :return: The velocity_scaling of this FluidSimulationControl.  # noqa: E501
        :rtype: float
        """
        return self._velocity_scaling

    @velocity_scaling.setter
    def velocity_scaling(self, velocity_scaling):
        """Sets the velocity_scaling of this FluidSimulationControl.

        <p>It affects the stability of the simulation. The default value of 0.1 is a good compromise between accuracy and computational requirements. Lower values of this parameter might increase the stability of the simulation at the cost of higher computational time.</p>  # noqa: E501

        :param velocity_scaling: The velocity_scaling of this FluidSimulationControl.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                velocity_scaling is not None and velocity_scaling > 0.25):  # noqa: E501
            raise ValueError("Invalid value for `velocity_scaling`, must be a value less than or equal to `0.25`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                velocity_scaling is not None and velocity_scaling < 0.025):  # noqa: E501
            raise ValueError("Invalid value for `velocity_scaling`, must be a value greater than or equal to `0.025`")  # noqa: E501

        self._velocity_scaling = velocity_scaling

    @property
    def potential_foam_initialization(self):
        """Gets the potential_foam_initialization of this FluidSimulationControl.  # noqa: E501

        This setting activates the solution of a potential flow field. The potential flow is used as initial condition for the actual simulation. This can accelerate convergence and improve stability during the first time steps. If you experience stability problems, this setting may bring some improvement.  # noqa: E501

        :return: The potential_foam_initialization of this FluidSimulationControl.  # noqa: E501
        :rtype: bool
        """
        return self._potential_foam_initialization

    @potential_foam_initialization.setter
    def potential_foam_initialization(self, potential_foam_initialization):
        """Sets the potential_foam_initialization of this FluidSimulationControl.

        This setting activates the solution of a potential flow field. The potential flow is used as initial condition for the actual simulation. This can accelerate convergence and improve stability during the first time steps. If you experience stability problems, this setting may bring some improvement.  # noqa: E501

        :param potential_foam_initialization: The potential_foam_initialization of this FluidSimulationControl.  # noqa: E501
        :type: bool
        """

        self._potential_foam_initialization = potential_foam_initialization

    @property
    def decompose_algorithm(self):
        """Gets the decompose_algorithm of this FluidSimulationControl.  # noqa: E501


        :return: The decompose_algorithm of this FluidSimulationControl.  # noqa: E501
        :rtype: OneOfFluidSimulationControlDecomposeAlgorithm
        """
        return self._decompose_algorithm

    @decompose_algorithm.setter
    def decompose_algorithm(self, decompose_algorithm):
        """Sets the decompose_algorithm of this FluidSimulationControl.


        :param decompose_algorithm: The decompose_algorithm of this FluidSimulationControl.  # noqa: E501
        :type: OneOfFluidSimulationControlDecomposeAlgorithm
        """

        self._decompose_algorithm = decompose_algorithm

    @property
    def relative_convergence_criteria(self):
        """Gets the relative_convergence_criteria of this FluidSimulationControl.  # noqa: E501

        <b>Steady-state simulation:</b> This represents the relative error residuals that once attained by the solver the simulation is considered to be converged and will stop. The recommended value is 0.001.<br> <b>Transient simulation:</b> This represents the relative error residuals that once attained by the solver the simulation will move to the next time-step regardless of the <i>Number of iterations</i>. The recommended value is 0.1.</br> <br> <b>Please note: </b>Relative residual is defined as the residual in the current iteration divided by the initial residual.</br> <br> <b>Please note: </b>Lower convergence criterion is demanded for <b>Steady-state simulations</b> because the initial guess is typically farther from the correct solution.</br>  # noqa: E501

        :return: The relative_convergence_criteria of this FluidSimulationControl.  # noqa: E501
        :rtype: float
        """
        return self._relative_convergence_criteria

    @relative_convergence_criteria.setter
    def relative_convergence_criteria(self, relative_convergence_criteria):
        """Sets the relative_convergence_criteria of this FluidSimulationControl.

        <b>Steady-state simulation:</b> This represents the relative error residuals that once attained by the solver the simulation is considered to be converged and will stop. The recommended value is 0.001.<br> <b>Transient simulation:</b> This represents the relative error residuals that once attained by the solver the simulation will move to the next time-step regardless of the <i>Number of iterations</i>. The recommended value is 0.1.</br> <br> <b>Please note: </b>Relative residual is defined as the residual in the current iteration divided by the initial residual.</br> <br> <b>Please note: </b>Lower convergence criterion is demanded for <b>Steady-state simulations</b> because the initial guess is typically farther from the correct solution.</br>  # noqa: E501

        :param relative_convergence_criteria: The relative_convergence_criteria of this FluidSimulationControl.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                relative_convergence_criteria is not None and relative_convergence_criteria > 1):  # noqa: E501
            raise ValueError("Invalid value for `relative_convergence_criteria`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                relative_convergence_criteria is not None and relative_convergence_criteria < 0):  # noqa: E501
            raise ValueError("Invalid value for `relative_convergence_criteria`, must be a value greater than or equal to `0`")  # noqa: E501

        self._relative_convergence_criteria = relative_convergence_criteria

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
        if not isinstance(other, FluidSimulationControl):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FluidSimulationControl):
            return True

        return self.to_dict() != other.to_dict()
