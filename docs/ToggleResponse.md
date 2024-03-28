# ToggleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **int** | Device state 1 - ON / 0 - OFF | [optional] 
**brightness** | **int** | Only for lights and fans 0-100 [ for fans value is 33, 66 and 100 only ] | [optional] 

## Example

```python
from tinxy_client.models.toggle_response import ToggleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleResponse from a JSON string
toggle_response_instance = ToggleResponse.from_json(json)
# print the JSON string representation of the object
print(ToggleResponse.to_json())

# convert the object into a dict
toggle_response_dict = toggle_response_instance.to_dict()
# create an instance of ToggleResponse from a dict
toggle_response_form_dict = toggle_response.from_dict(toggle_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


