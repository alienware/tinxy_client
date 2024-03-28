# TypeId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**primary** | **bool** |  | [optional] 
**number_of_relays** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**v** | **int** |  | [optional] 
**gtype** | **str** |  | [optional] 
**traits** | **List[str]** |  | [optional] 
**long_name** | **str** |  | [optional] 
**amazon_review_link** | **str** |  | [optional] 
**features** | **List[str]** |  | [optional] 
**toggle_delay** | **int** | Toggle dealy in ms | [optional] 
**uuid_ref** | **object** |  | [optional] 
**rf_code** | **int** |  | [optional] 
**remote_codes** | **List[object]** |  | [optional] 

## Example

```python
from tinxy_client.models.type_id import TypeId

# TODO update the JSON string below
json = "{}"
# create an instance of TypeId from a JSON string
type_id_instance = TypeId.from_json(json)
# print the JSON string representation of the object
print(TypeId.to_json())

# convert the object into a dict
type_id_dict = type_id_instance.to_dict()
# create an instance of TypeId from a dict
type_id_form_dict = type_id.from_dict(type_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


