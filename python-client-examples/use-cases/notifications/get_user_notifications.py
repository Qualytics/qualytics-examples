"""
Example script demonstrating how to retrieve user notifications using the Qualytics API swagger client.

This example shows how to fetch notifications for the authenticated user, with options to include
or exclude acknowledged notifications.

This example uses old-style Swagger models since the notification models were generated with
the older Swagger Codegen tool. The CustomApiClient is used to handle lenient deserialization
of responses that may not match model validation.
"""

from __future__ import print_function
import sys
import os
from pprint import pprint

# Add the parent directory to the path so we can import swagger_client
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.custom_api_client import CustomApiClient

# Configure OAuth2 access token for authorization: Auth0ImplicitBearer
configuration = swagger_client.Configuration()

# Create an instance of the API class using CustomApiClient
# The CustomApiClient handles lenient deserialization to avoid validation errors
api_instance = swagger_client.NotificationsApi(CustomApiClient(configuration))


def get_user_notifications_example(include_acknowledged=False):
    """
    Get a list of user notifications.

    Args:
        include_acknowledged (bool): Whether to include acknowledged notifications.
                                     Defaults to False (only unacknowledged notifications).

    Returns:
        list or dict: List of user notifications or paginated response dict
    """
    try:
        # Call the API to get user notifications
        # See the official docs for more details: https://demo.qualytics.io/api/docs#tag/Notifications/operation/get_user_notifications
        api_response = api_instance.get_user_notifications(
            include_acknowledged=include_acknowledged
        )

        # Handle response - the API returns a paginated response (dict with 'items' field)
        # even though the Swagger spec says it returns a list
        if isinstance(api_response, dict):
            # Paginated response
            items = api_response.get('items', [])
            total = api_response.get('total', 0)
            page = api_response.get('page', 1)
            pages = api_response.get('pages', 0)

            print(f"Retrieved {len(items)} notification(s) on page {page} of {pages} (total: {total})")
            if items:
                print("\nNotifications:")
                pprint(items)
            else:
                print("No notifications found.")
            return items
        else:
            # Direct list response (if API changes or spec is correct)
            notification_count = len(api_response) if api_response else 0
            print(f"Retrieved {notification_count} notification(s)")
            pprint(api_response)
            return api_response
    except ApiException as e:
        print("Exception when calling NotificationsApi->get_user_notifications: %s\n" % e)
        return None


def get_user_notification_by_id_example(notification_id):
    """
    Get details of a specific user notification.

    Args:
        notification_id (int): The ID of the notification to retrieve

    Returns:
        UserNotification or dict: The notification details
    """
    try:
        # Call the API to get a specific notification by ID
        api_response = api_instance.get_user_notification(id=notification_id)

        print(f"Retrieved notification {notification_id}")
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling NotificationsApi->get_user_notification: %s\n" % e)
        return None


if __name__ == '__main__':
    # Uncomment the example you want to run:

    # Example 1: Get all unacknowledged notifications (default)
    # get_user_notifications_example()

    # Example 2: Get all notifications including acknowledged ones
    get_user_notifications_example(include_acknowledged=True)

    # Example 3: Get a specific notification by ID
    # get_user_notification_by_id_example(12345)
