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


class TagsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_global_tag(self, body, **kwargs):  # noqa: E501
        """Create Global Tag  # noqa: E501

        Create a new Tag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_global_tag(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateGlobalTag body: (required)
        :return: GetGlobalTag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_global_tag_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_global_tag_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_global_tag_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Global Tag  # noqa: E501

        Create a new Tag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_global_tag_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateGlobalTag body: (required)
        :return: GetGlobalTag
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
                    " to method create_global_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_global_tag`")  # noqa: E501

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
            '/api/global-tags', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetGlobalTag',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_global_tag(self, name, **kwargs):  # noqa: E501
        """Delete Global Tag  # noqa: E501

        Deletes a Tag. Supply the tag `name` and the tag will be deleted  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_global_tag(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: GlobalTag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_global_tag_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_global_tag_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def delete_global_tag_with_http_info(self, name, **kwargs):  # noqa: E501
        """Delete Global Tag  # noqa: E501

        Deletes a Tag. Supply the tag `name` and the tag will be deleted  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_global_tag_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: GlobalTag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_global_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `delete_global_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

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
            '/api/global-tags/{name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GlobalTag',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_global_tag(self, name, **kwargs):  # noqa: E501
        """Get Global Tag  # noqa: E501

        Retrieves the detail of a Tag. Supply the unique Tag `name` and the Tag values will be returned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_tag(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Tag name (required)
        :return: GetGlobalTag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_global_tag_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_global_tag_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_global_tag_with_http_info(self, name, **kwargs):  # noqa: E501
        """Get Global Tag  # noqa: E501

        Retrieves the detail of a Tag. Supply the unique Tag `name` and the Tag values will be returned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_tag_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Tag name (required)
        :return: GetGlobalTag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_global_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_global_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

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
            '/api/global-tags/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetGlobalTag',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_global_tags(self, **kwargs):  # noqa: E501
        """Get Global Tags  # noqa: E501

        Returns a list of all your Tags.  The Tags are returned sorted by ascending tag name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_tags(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page:
        :param int size:
        :return: PageGetGlobalTag_
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_global_tags_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_global_tags_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_global_tags_with_http_info(self, **kwargs):  # noqa: E501
        """Get Global Tags  # noqa: E501

        Returns a list of all your Tags.  The Tags are returned sorted by ascending tag name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_tags_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page:
        :param int size:
        :return: PageGetGlobalTag_
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_global_tags" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
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
            '/api/global-tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageGetGlobalTag_',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_global_tags_listing(self, **kwargs):  # noqa: E501
        """Get Global Tags Listing  # noqa: E501

        Returns a list of all your Tags.  The Tags are returned sorted by ascending tag name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_tags_listing(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[GetGlobalTag]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_global_tags_listing_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_global_tags_listing_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_global_tags_listing_with_http_info(self, **kwargs):  # noqa: E501
        """Get Global Tags Listing  # noqa: E501

        Returns a list of all your Tags.  The Tags are returned sorted by ascending tag name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_tags_listing_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[GetGlobalTag]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_global_tags_listing" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/global-tags/listing', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetGlobalTag]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_global_tag(self, body, name, **kwargs):  # noqa: E501
        """Update Global Tag  # noqa: E501

        Updates the specific Tag by setting the values of the parameters passed.  Any parameters not provided will be left unchanged  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_global_tag(body, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateGlobalTag body: (required)
        :param str name: (required)
        :return: GetGlobalTag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_global_tag_with_http_info(body, name, **kwargs)  # noqa: E501
        else:
            (data) = self.update_global_tag_with_http_info(body, name, **kwargs)  # noqa: E501
            return data

    def update_global_tag_with_http_info(self, body, name, **kwargs):  # noqa: E501
        """Update Global Tag  # noqa: E501

        Updates the specific Tag by setting the values of the parameters passed.  Any parameters not provided will be left unchanged  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_global_tag_with_http_info(body, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateGlobalTag body: (required)
        :param str name: (required)
        :return: GetGlobalTag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_global_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_global_tag`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `update_global_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

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
            '/api/global-tags/{name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetGlobalTag',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
