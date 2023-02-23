# coding: utf-8

"""
    Surveillance Hub

    Qualytics API  # noqa: E501

    OpenAPI spec version: 5ca80d8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class FreshnessMeasurementsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def execute_measurement_run(self, body, **kwargs):  # noqa: E501
        """Execute Measurement Run  # noqa: E501

        Initiates a freshness synchronization run for the specified event loop priority.   This endpoint is meant to be invoked by the Hub Command service which has two scheduled jobs configured by default: - a priority event loop job that fires every 5 minutes - a standard event loop job that fires every 48 minutes  The priority event loop collects freshness measurements for any SLAs that are in a violation state and any that will enter a violation state within 60 minutes.   The standard event loop collects freshness measurements for any containers where freshness monitoring is enabled and  that are excluded from the priority even loop.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.execute_measurement_run(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FreshnessMeasurementRun body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.execute_measurement_run_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.execute_measurement_run_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def execute_measurement_run_with_http_info(self, body, **kwargs):  # noqa: E501
        """Execute Measurement Run  # noqa: E501

        Initiates a freshness synchronization run for the specified event loop priority.   This endpoint is meant to be invoked by the Hub Command service which has two scheduled jobs configured by default: - a priority event loop job that fires every 5 minutes - a standard event loop job that fires every 48 minutes  The priority event loop collects freshness measurements for any SLAs that are in a violation state and any that will enter a violation state within 60 minutes.   The standard event loop collects freshness measurements for any containers where freshness monitoring is enabled and  that are excluded from the priority even loop.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.execute_measurement_run_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FreshnessMeasurementRun body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method execute_measurement_run" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `execute_measurement_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Auth0HTTPBearer', 'Auth0ImplicitBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/freshness-measurement/run', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
