# coding: utf-8

"""
    SimScale API

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from simscale_sdk.api_client import ApiClient
from simscale_sdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class GeometryImportsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_geometry_import(self, project_id, geometry_import_id, **kwargs): # noqa: E501
        """Get information about the geometry import  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_geometry_import(project_id, geometry_import_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: The project ID (required)
        :param str geometry_import_id: The geometry import ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GeometryImportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_geometry_import_with_http_info(project_id, geometry_import_id, **kwargs)  # noqa: E501

    def get_geometry_import_with_http_info(self, project_id, geometry_import_id, **kwargs):  # noqa: E501
        """Get information about the geometry import  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_geometry_import_with_http_info(project_id, geometry_import_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: The project ID (required)
        :param str geometry_import_id: The geometry import ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GeometryImportResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'geometry_import_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_geometry_import" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `get_geometry_import`")  # noqa: E501
        # verify the required parameter 'geometry_import_id' is set
        if self.api_client.client_side_validation and ('geometry_import_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['geometry_import_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `geometry_import_id` when calling `get_geometry_import`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['projectId'] = local_var_params['project_id']  # noqa: E501
        if 'geometry_import_id' in local_var_params:
            path_params['geometryImportId'] = local_var_params['geometry_import_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectId}/geometryimports/{geometryImportId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GeometryImportResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_geometry_import_event_log(self, project_id, geometry_import_id, **kwargs): # noqa: E501
        """Get the geometry import event log  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_geometry_import_event_log(project_id, geometry_import_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: The project ID (required)
        :param str geometry_import_id: The geometry import ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: EventLogResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_geometry_import_event_log_with_http_info(project_id, geometry_import_id, **kwargs)  # noqa: E501

    def get_geometry_import_event_log_with_http_info(self, project_id, geometry_import_id, **kwargs):  # noqa: E501
        """Get the geometry import event log  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_geometry_import_event_log_with_http_info(project_id, geometry_import_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: The project ID (required)
        :param str geometry_import_id: The geometry import ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(EventLogResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'geometry_import_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_geometry_import_event_log" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `get_geometry_import_event_log`")  # noqa: E501
        # verify the required parameter 'geometry_import_id' is set
        if self.api_client.client_side_validation and ('geometry_import_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['geometry_import_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `geometry_import_id` when calling `get_geometry_import_event_log`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['projectId'] = local_var_params['project_id']  # noqa: E501
        if 'geometry_import_id' in local_var_params:
            path_params['geometryImportId'] = local_var_params['geometry_import_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectId}/geometryimports/{geometryImportId}/eventlog', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventLogResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def import_geometry(self, project_id, geometry_import_request, **kwargs): # noqa: E501
        """Import a new geometry  # noqa: E501

        Geometry import requires the following steps: 1. Request a temporary storage location via `POST /storage`. 2. Upload your CAD file using the HTTP `PUT` method to the `url` provided in the temporary storage location response object. 3. Start the import via `POST /projects/{projectId}/geometryimports` and include the `storageId` provided in the temporary storage location response object. 4. Check for the import status via `GET /projects/{projectId}/geometryimports/{geometryImportId}`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_geometry(project_id, geometry_import_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: The project ID (required)
        :param GeometryImportRequest geometry_import_request: Geometry import specification. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GeometryImportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.import_geometry_with_http_info(project_id, geometry_import_request, **kwargs)  # noqa: E501

    def import_geometry_with_http_info(self, project_id, geometry_import_request, **kwargs):  # noqa: E501
        """Import a new geometry  # noqa: E501

        Geometry import requires the following steps: 1. Request a temporary storage location via `POST /storage`. 2. Upload your CAD file using the HTTP `PUT` method to the `url` provided in the temporary storage location response object. 3. Start the import via `POST /projects/{projectId}/geometryimports` and include the `storageId` provided in the temporary storage location response object. 4. Check for the import status via `GET /projects/{projectId}/geometryimports/{geometryImportId}`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_geometry_with_http_info(project_id, geometry_import_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_id: The project ID (required)
        :param GeometryImportRequest geometry_import_request: Geometry import specification. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GeometryImportResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project_id',
            'geometry_import_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_geometry" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_id` when calling `import_geometry`")  # noqa: E501
        # verify the required parameter 'geometry_import_request' is set
        if self.api_client.client_side_validation and ('geometry_import_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['geometry_import_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `geometry_import_request` when calling `import_geometry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['projectId'] = local_var_params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'geometry_import_request' in local_var_params:
            body_params = local_var_params['geometry_import_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectId}/geometryimports', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GeometryImportResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
