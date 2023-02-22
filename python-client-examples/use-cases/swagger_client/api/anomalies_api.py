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


class AnomaliesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def bulk_update_anomalies(self, body, **kwargs):  # noqa: E501
        """Bulk Update Anomalies  # noqa: E501

        Bulk update multiple Anomalies by setting the values of the parameters passed.  Any parameters not provided will be left unchanged  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_update_anomalies(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[BulkUpdateAnomaly] body: (required)
        :return: list[GetAnomaly]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bulk_update_anomalies_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.bulk_update_anomalies_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def bulk_update_anomalies_with_http_info(self, body, **kwargs):  # noqa: E501
        """Bulk Update Anomalies  # noqa: E501

        Bulk update multiple Anomalies by setting the values of the parameters passed.  Any parameters not provided will be left unchanged  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_update_anomalies_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[BulkUpdateAnomaly] body: (required)
        :return: list[GetAnomaly]
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
                    " to method bulk_update_anomalies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `bulk_update_anomalies`")  # noqa: E501

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
            '/api/anomalies', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetAnomaly]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_anomalies(self, **kwargs):  # noqa: E501
        """Get Anomalies  # noqa: E501

        Returns a list of your Anomalies. The anomalies are returned sorted by creation timestamp and importance score  with the most recent anomalies appearing first  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_anomalies(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The unique identifier
        :param list[AnomalyStatusType] status: The `status` of the `Anomaly`
        :param str anomaly_type: The `type` of the created `Anomaly`
        :param int datastore: The `Datastore` id
        :param list[int] container: The `Container` ids
        :param list[str] field: The `Anomaly` fields 
        :param int container_scan: The `Container` ids
        :param int partition_scan: The `Partition` ids
        :param list[RuleType] rule_type: The type of the rule of `Quality Check`
        :param list[int] quality_check: The `Quality Check` ids
        :param list[str] tag: The name of the `Tag`
        :param date created_date: The created date of the `Anomaly`
        :param date start_date: The start date of the `Anomaly`
        :param date end_date: The end date of the `Anomaly`
        :param int timeframe: The time frame of the created date of the `Anomaly`, it is used for a time frame
        :param int page:
        :param int size:
        :return: PageAnomalyListing_
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_anomalies_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_anomalies_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_anomalies_with_http_info(self, **kwargs):  # noqa: E501
        """Get Anomalies  # noqa: E501

        Returns a list of your Anomalies. The anomalies are returned sorted by creation timestamp and importance score  with the most recent anomalies appearing first  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_anomalies_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The unique identifier
        :param list[AnomalyStatusType] status: The `status` of the `Anomaly`
        :param str anomaly_type: The `type` of the created `Anomaly`
        :param int datastore: The `Datastore` id
        :param list[int] container: The `Container` ids
        :param list[str] field: The `Anomaly` fields 
        :param int container_scan: The `Container` ids
        :param int partition_scan: The `Partition` ids
        :param list[RuleType] rule_type: The type of the rule of `Quality Check`
        :param list[int] quality_check: The `Quality Check` ids
        :param list[str] tag: The name of the `Tag`
        :param date created_date: The created date of the `Anomaly`
        :param date start_date: The start date of the `Anomaly`
        :param date end_date: The end date of the `Anomaly`
        :param int timeframe: The time frame of the created date of the `Anomaly`, it is used for a time frame
        :param int page:
        :param int size:
        :return: PageAnomalyListing_
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'status', 'anomaly_type', 'datastore', 'container', 'field', 'container_scan', 'partition_scan', 'rule_type', 'quality_check', 'tag', 'created_date', 'start_date', 'end_date', 'timeframe', 'page', 'size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_anomalies" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
            collection_formats['status'] = 'multi'  # noqa: E501
        if 'anomaly_type' in params:
            query_params.append(('anomaly_type', params['anomaly_type']))  # noqa: E501
        if 'datastore' in params:
            query_params.append(('datastore', params['datastore']))  # noqa: E501
        if 'container' in params:
            query_params.append(('container', params['container']))  # noqa: E501
            collection_formats['container'] = 'multi'  # noqa: E501
        if 'field' in params:
            query_params.append(('field', params['field']))  # noqa: E501
            collection_formats['field'] = 'multi'  # noqa: E501
        if 'container_scan' in params:
            query_params.append(('container_scan', params['container_scan']))  # noqa: E501
        if 'partition_scan' in params:
            query_params.append(('partition_scan', params['partition_scan']))  # noqa: E501
        if 'rule_type' in params:
            query_params.append(('rule_type', params['rule_type']))  # noqa: E501
            collection_formats['rule_type'] = 'multi'  # noqa: E501
        if 'quality_check' in params:
            query_params.append(('quality_check', params['quality_check']))  # noqa: E501
            collection_formats['quality_check'] = 'multi'  # noqa: E501
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501
            collection_formats['tag'] = 'multi'  # noqa: E501
        if 'created_date' in params:
            query_params.append(('created_date', params['created_date']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'timeframe' in params:
            query_params.append(('timeframe', params['timeframe']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Auth0HTTPBearer', 'Auth0ImplicitBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/anomalies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageAnomalyListing_',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_anomaly_by_id(self, id, **kwargs):  # noqa: E501
        """Get Anomaly By Id  # noqa: E501

        Retrieves the details of an existing Anomaly.  Supply the unique Anomaly `ID` or `UUID` from either an Anomaly creation request or the Anomaly list,  and the corresponding Anomaly information will be returned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_anomaly_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Id id: (required)
        :return: GetAnomaly
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_anomaly_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_anomaly_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_anomaly_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Anomaly By Id  # noqa: E501

        Retrieves the details of an existing Anomaly.  Supply the unique Anomaly `ID` or `UUID` from either an Anomaly creation request or the Anomaly list,  and the corresponding Anomaly information will be returned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_anomaly_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Id id: (required)
        :return: GetAnomaly
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_anomaly_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_anomaly_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Auth0HTTPBearer', 'Auth0ImplicitBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/anomalies/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAnomaly',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_anomaly_source_record(self, id, **kwargs):  # noqa: E501
        """Get Anomaly Source Record  # noqa: E501

        Retrieves the details of the anomalous record.  Supply the unique Anomaly `ID` or `UUID` and the anomalous values that triggered the creation of that Anomaly will be returned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_anomaly_source_record(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Id2 id: (required)
        :return: GetSourceRecord
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_anomaly_source_record_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_anomaly_source_record_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_anomaly_source_record_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Anomaly Source Record  # noqa: E501

        Retrieves the details of the anomalous record.  Supply the unique Anomaly `ID` or `UUID` and the anomalous values that triggered the creation of that Anomaly will be returned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_anomaly_source_record_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Id2 id: (required)
        :return: GetSourceRecord
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_anomaly_source_record" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_anomaly_source_record`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Auth0HTTPBearer', 'Auth0ImplicitBearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/anomalies/{id}/source-record', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetSourceRecord',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_anomaly(self, body, id, **kwargs):  # noqa: E501
        """Update Anomaly  # noqa: E501

        Updates the specific Anomaly by setting the values of the parameters passed.  Any parameters not provided will be left unchanged  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_anomaly(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateAnomaly body: (required)
        :param Id1 id: (required)
        :return: GetAnomaly
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_anomaly_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_anomaly_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def update_anomaly_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Update Anomaly  # noqa: E501

        Updates the specific Anomaly by setting the values of the parameters passed.  Any parameters not provided will be left unchanged  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_anomaly_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateAnomaly body: (required)
        :param Id1 id: (required)
        :return: GetAnomaly
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_anomaly" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_anomaly`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_anomaly`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/api/anomalies/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAnomaly',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)