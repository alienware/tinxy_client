# tinxy_client.DefaultApi

All URIs are relative to *https://backend.tinxy.in*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_devices_device_id_state_get**](DefaultApi.md#v2_devices_device_id_state_get) | **GET** /v2/devices/{deviceId}/state | 
[**v2_devices_device_id_toggle_post**](DefaultApi.md#v2_devices_device_id_toggle_post) | **POST** /v2/devices/{deviceId}/toggle | 
[**v2_devices_get**](DefaultApi.md#v2_devices_get) | **GET** /v2/devices/ | 


# **v2_devices_device_id_state_get**
> DeviceState v2_devices_device_id_state_get(device_id)



Get device state

### Example

* Bearer Authentication (bearerAuth):

```python
import tinxy_client
from tinxy_client.models.device_state import DeviceState
from tinxy_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://backend.tinxy.in
# See configuration.py for a list of all supported configuration parameters.
configuration = tinxy_client.Configuration(
    host = "https://backend.tinxy.in"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = tinxy_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tinxy_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tinxy_client.DefaultApi(api_client)
    device_id = 'device_id_example' # str | Device Id

    try:
        api_response = api_instance.v2_devices_device_id_state_get(device_id)
        print("The response of DefaultApi->v2_devices_device_id_state_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_devices_device_id_state_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id | 

### Return type

[**DeviceState**](DeviceState.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrived status of given device |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_devices_device_id_toggle_post**
> DeviceState v2_devices_device_id_toggle_post(device_id, toggle)



Set device state

### Example

* Bearer Authentication (bearerAuth):

```python
import tinxy_client
from tinxy_client.models.device_state import DeviceState
from tinxy_client.models.toggle import Toggle
from tinxy_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://backend.tinxy.in
# See configuration.py for a list of all supported configuration parameters.
configuration = tinxy_client.Configuration(
    host = "https://backend.tinxy.in"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = tinxy_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tinxy_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tinxy_client.DefaultApi(api_client)
    device_id = 'device_id_example' # str | Device Number
    toggle = tinxy_client.Toggle() # Toggle | Optional description in *Markdown*

    try:
        api_response = api_instance.v2_devices_device_id_toggle_post(device_id, toggle)
        print("The response of DefaultApi->v2_devices_device_id_toggle_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_devices_device_id_toggle_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Number | 
 **toggle** | [**Toggle**](Toggle.md)| Optional description in *Markdown* | 

### Return type

[**DeviceState**](DeviceState.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrived status of given device |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_devices_get**
> List[Device] v2_devices_get()



Get all devices connected top your account

### Example

* Bearer Authentication (bearerAuth):

```python
import tinxy_client
from tinxy_client.models.device import Device
from tinxy_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://backend.tinxy.in
# See configuration.py for a list of all supported configuration parameters.
configuration = tinxy_client.Configuration(
    host = "https://backend.tinxy.in"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = tinxy_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tinxy_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tinxy_client.DefaultApi(api_client)

    try:
        api_response = api_instance.v2_devices_get()
        print("The response of DefaultApi->v2_devices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_devices_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Device]**](Device.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lists all devices connected top your account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

