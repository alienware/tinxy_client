# Toggle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**ToggleRequest**](ToggleRequest.md) |  | [optional] 
**device_number** | **int** | Device Number. You can get the device number from the &#x60;devices&#x60; section start from 1 for each item | [optional] 

## Example

```python
from tinxy_client.models.toggle import Toggle

# TODO update the JSON string below
json = "{}"
# create an instance of Toggle from a JSON string
toggle_instance = Toggle.from_json(json)
# print the JSON string representation of the object
print(Toggle.to_json())

# convert the object into a dict
toggle_dict = toggle_instance.to_dict()
# create an instance of Toggle from a dict
toggle_form_dict = toggle.from_dict(toggle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


