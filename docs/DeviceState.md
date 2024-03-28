# DeviceState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Device state ON / OFF | [optional] 
**brightness** | **int** | Only for lights and fans 0-100 [ for fans value is 33, 66 and 100 only ] | [optional] 
**status** | **int** | 1 - Online 0 - Offline | [optional] 

## Example

```python
from tinxy_client.models.device_state import DeviceState

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceState from a JSON string
device_state_instance = DeviceState.from_json(json)
# print the JSON string representation of the object
print(DeviceState.to_json())

# convert the object into a dict
device_state_dict = device_state_instance.to_dict()
# create an instance of DeviceState from a dict
device_state_form_dict = device_state.from_dict(device_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


