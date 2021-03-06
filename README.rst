Django Onesignal
=============

A Python client library for `OneSignal <https://onesignal.com/>`__ REST API. Supports **async/await**.

Table of Contents
-----------------

-  `Installation <#installation>`__

-  `Example Usage <#example-usage>`__

-  `Example Usage Future Notification <#example-usage-future-notification>`__

Installation
------------

::

    pip install onesignal-django

Example Usage
-------------

You can think this library as a wrapper around OneSignal REST API. It is fairly simple to use:

- Create an instance of **OnesignalClient():**. 
- Setup your credentianl with the **set_app_id()** method (`rest_api_key` is not required but necessary for some API calls).
- Build your request body with the **create_message()** method.
- Once ready send the push notification with the **send_message()** method.

.. code:: python

    from django_onesignal.client import OnesignalClient

    client = OnesignalClient()

    # set up your credentials. rest_api_key is not required for all API calls
    client.set_app_id( app_id=APP_ID , rest_api_key=REST_API_KEY):


    # Pass the TITLE the CONTENT of the push notificaiton
    # Pass 1 or more ids in a **List** objet
    client.create_message(self, title=TITLE, cont=CONTENT, ids:[ID]):
    

    # Check on Onesignal documentation if the notification you are sending requires the `rest_api_key`
    response = client.send_message(requires_rest_api_key=BOOL)

    print(response.status)
    print(response.body)


Example Usage Future Notification
---------------------------------


In this example we use the **create_future_message()** methond. It requires the date on which the message will be sent

.. code:: python

    from django_onesignal.client import OnesignalClient

    client = OnesignalClient()

    # set up your credentials. rest_api_key is not required for all API calls
    client.set_app_id( app_id=APP_ID , rest_api_key=REST_API_KEY):


    # Pass the TITLE the CONTENT of the push notificaiton
    # Pass 1 or more ids in a **List** objet
    # Pass a DATE | Eg. datetime.datetime(2021, 10, 5, 18, 00)
    client.create_future_message(self, title=TITLE, cont=CONTENT, ids:[ID], date=DATE):
    

    # Check on Onesignal documentation if the notification you are sending requires the `rest_api_key`
    response = client.send_message(requires_rest_api_key=BOOL)

    print(response.status)
    print(response.body)
