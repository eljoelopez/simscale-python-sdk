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


class OneOfImplicitTimeIntegrationTypeScheme(object):
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
        'alpha': 'float',
        'method': 'str',
        'beta': 'float',
        'gamma': 'float'
    }

    attribute_map = {
        'type': 'type',
        'alpha': 'alpha',
        'method': 'method',
        'beta': 'beta',
        'gamma': 'gamma'
    }

    discriminator_value_class_map = {
        'HHT': 'HhtTimeIntegrationScheme',
        'NEWMARK': 'NewmarkTimeIntegrationScheme'
    }

    def __init__(self, type='NEWMARK', alpha=None, method=None, beta=None, gamma=None, local_vars_configuration=None):  # noqa: E501
        """OneOfImplicitTimeIntegrationTypeScheme - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._alpha = None
        self._method = None
        self._beta = None
        self._gamma = None
        self.discriminator = 'type'

        self.type = type
        if alpha is not None:
            self.alpha = alpha
        if method is not None:
            self.method = method
        if beta is not None:
            self.beta = beta
        if gamma is not None:
            self.gamma = gamma

    @property
    def type(self):
        """Gets the type of this OneOfImplicitTimeIntegrationTypeScheme.  # noqa: E501

        Schema name: NewmarkTimeIntegrationScheme  # noqa: E501

        :return: The type of this OneOfImplicitTimeIntegrationTypeScheme.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfImplicitTimeIntegrationTypeScheme.

        Schema name: NewmarkTimeIntegrationScheme  # noqa: E501

        :param type: The type of this OneOfImplicitTimeIntegrationTypeScheme.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def alpha(self):
        """Gets the alpha of this OneOfImplicitTimeIntegrationTypeScheme.  # noqa: E501

        The parameter <b>&alpha;</b> is given by a negative value. The larger |<b>&alpha;</b>| is, the more numerical damping is induced.  # noqa: E501

        :return: The alpha of this OneOfImplicitTimeIntegrationTypeScheme.  # noqa: E501
        :rtype: float
        """
        return self._alpha

    @alpha.setter
    def alpha(self, alpha):
        """Sets the alpha of this OneOfImplicitTimeIntegrationTypeScheme.

        The parameter <b>&alpha;</b> is given by a negative value. The larger |<b>&alpha;</b>| is, the more numerical damping is induced.  # noqa: E501

        :param alpha: The alpha of this OneOfImplicitTimeIntegrationTypeScheme.  # noqa: E501
        :type: float
        """

        self._alpha = alpha

    @property
    def method(self):
        """Gets the method of this OneOfImplicitTimeIntegrationTypeScheme.  # noqa: E501

        Choose the mode of the HHT method. Compared to the <b>average acceleration</b> scheme the induced numerical damping of the <b>alpha method</b> is more selective: it is weaker for low frequencies and it will increase with the frequencies.  # noqa: E501

        :return: The method of this OneOfImplicitTimeIntegrationTypeScheme.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this OneOfImplicitTimeIntegrationTypeScheme.

        Choose the mode of the HHT method. Compared to the <b>average acceleration</b> scheme the induced numerical damping of the <b>alpha method</b> is more selective: it is weaker for low frequencies and it will increase with the frequencies.  # noqa: E501

        :param method: The method of this OneOfImplicitTimeIntegrationTypeScheme.  # noqa: E501
        :type: str
        """
        allowed_values = ["AVERAGE_ACCELERATION", "ALPHA_METHOD"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def beta(self):
        """Gets the beta of this OneOfImplicitTimeIntegrationTypeScheme.  # noqa: E501

        <p>The choice of the values for the parameters <b>&alpha;</b> and <b>&beta;</b> influences the stability, accuracy and numerical damping of the <i>Newmark Sheme</i>.</v>  # noqa: E501

        :return: The beta of this OneOfImplicitTimeIntegrationTypeScheme.  # noqa: E501
        :rtype: float
        """
        return self._beta

    @beta.setter
    def beta(self, beta):
        """Sets the beta of this OneOfImplicitTimeIntegrationTypeScheme.

        <p>The choice of the values for the parameters <b>&alpha;</b> and <b>&beta;</b> influences the stability, accuracy and numerical damping of the <i>Newmark Sheme</i>.</v>  # noqa: E501

        :param beta: The beta of this OneOfImplicitTimeIntegrationTypeScheme.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                beta is not None and beta > 1):  # noqa: E501
            raise ValueError("Invalid value for `beta`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                beta is not None and beta < 0):  # noqa: E501
            raise ValueError("Invalid value for `beta`, must be a value greater than or equal to `0`")  # noqa: E501

        self._beta = beta

    @property
    def gamma(self):
        """Gets the gamma of this OneOfImplicitTimeIntegrationTypeScheme.  # noqa: E501

        <p>The choice of the values for the parameters <b>&alpha;</b> and <b>&beta;</b> influences the stability, accuracy and numerical damping of the <i>Newmark Sheme</i>.</v>  # noqa: E501

        :return: The gamma of this OneOfImplicitTimeIntegrationTypeScheme.  # noqa: E501
        :rtype: float
        """
        return self._gamma

    @gamma.setter
    def gamma(self, gamma):
        """Sets the gamma of this OneOfImplicitTimeIntegrationTypeScheme.

        <p>The choice of the values for the parameters <b>&alpha;</b> and <b>&beta;</b> influences the stability, accuracy and numerical damping of the <i>Newmark Sheme</i>.</v>  # noqa: E501

        :param gamma: The gamma of this OneOfImplicitTimeIntegrationTypeScheme.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                gamma is not None and gamma > 1):  # noqa: E501
            raise ValueError("Invalid value for `gamma`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                gamma is not None and gamma < 0):  # noqa: E501
            raise ValueError("Invalid value for `gamma`, must be a value greater than or equal to `0`")  # noqa: E501

        self._gamma = gamma

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
        if not isinstance(other, OneOfImplicitTimeIntegrationTypeScheme):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfImplicitTimeIntegrationTypeScheme):
            return True

        return self.to_dict() != other.to_dict()