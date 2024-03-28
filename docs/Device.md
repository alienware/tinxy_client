# Device


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**hub_id** | **str** | Only for devices with hub | [optional] 
**user_id** | **str** | Id of the user who owns the device | [optional] 
**enabled** | **bool** |  | [optional] 
**devices** | **List[str]** |  | [optional] 
**device_types** | **List[str]** |  | [optional] 
**switch_type** | **str** |  | [optional] 
**name** | **str** | The Name we set in App | [optional] 
**toggle_delay** | **int** | Toggle dealy in ms | [optional] 
**mqtt_password** | **str** |  | [optional] 
**type_id** | [**TypeId**](TypeId.md) |  | [optional] 
**registration_date** | **str** |  | [optional] 
**firmware_version** | **int** |  | [optional] 
**pairing_code** | **int** |  | [optional] 

## Example

```python
from tinxy_client.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print(Device.to_json())

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_form_dict = device.from_dict(device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


