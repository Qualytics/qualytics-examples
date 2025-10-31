"""
Custom API Client wrapper that extends the generated swagger_client.ApiClient
to support both old-style Swagger models and new Pydantic models.

This file is NOT auto-generated and can be safely modified.
"""

import datetime
import six
from swagger_client.api_client import ApiClient as GeneratedApiClient


class CustomApiClient(GeneratedApiClient):
    """
    Custom API Client that extends the generated ApiClient to handle
    both old Swagger models (with swagger_types) and new Pydantic models.
    """

    def sanitize_for_serialization(self, obj):
        """
        Builds a JSON POST object with support for both Pydantic and Swagger models.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is Pydantic model, use model_dump() or dict() method.
        If obj is swagger model instance, return the properties as a dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj)
                    for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj)
                         for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        if isinstance(obj, dict):
            obj_dict = obj
        else:
            # Check if this is a Pydantic model (new style)
            if hasattr(obj, 'model_dump'):
                # Pydantic v2 model
                obj_dict = obj.model_dump(by_alias=True, exclude_none=True)
            elif hasattr(obj, 'dict'):
                # Pydantic v1 model
                obj_dict = obj.dict(by_alias=True, exclude_none=True)
            elif hasattr(obj, 'swagger_types'):
                # Old-style Swagger model
                # Convert model obj to dict except
                # attributes `swagger_types`, `attribute_map`
                # and attributes which value is not None.
                # Convert attribute name to json key in
                # model definition for request.
                obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
                            for attr, _ in six.iteritems(obj.swagger_types)
                            if getattr(obj, attr) is not None}
            else:
                # Fallback: try to convert object to dict
                obj_dict = obj.__dict__

        return {key: self.sanitize_for_serialization(val)
                for key, val in six.iteritems(obj_dict)}

    def deserialize(self, response, response_type):
        """
        Deserializes response into an object with lenient error handling.

        Overrides the parent deserialize method to gracefully handle
        deserialization failures with old Swagger models.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for deserialized object, or string of class name.
        :return: deserialized object, or raw dict if deserialization fails.
        """
        try:
            # Try the parent's deserialization first
            return super().deserialize(response, response_type)
        except (ValueError, TypeError, AttributeError) as e:
            # If deserialization fails, return the raw response data as dict
            print(f"Warning: Deserialization failed: {e}")
            print("Returning raw response data as dict instead.")
            try:
                import json
                data = json.loads(response.data)
                return data
            except Exception:
                # If we can't even parse JSON, return the response object
                return response
