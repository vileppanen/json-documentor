# json-documentor

This project provides Python scripts, for generating MD and XLS documentation out of provided JSON objects.

## Limitations

### Objects
- the documentor script does not prompt for additional props that might be missing from the documented json (the props that are present in the json are the props, that will be documented)
- complex, nested objects are documented only two level deep

### Arrays
- the documentor script assumes every item in an array is of similar type and structure and it generates item documentation based on first item in the array
- the documentor script does not support documenting arrays containing arrays (the type will be specified as `NestedArray` and traversing values is skipped)

## JSON to MD usage

1. In repo root, execute `python json-to-md.py`
2. Specify the path of the input json
3. When prompted, specify a description for each property in provided JSON
4. The generated MD file is dumped into the `output-md` dir

## MD to XLS

1. In repo root, execute `python md-to-xls.py`
2. Specify the name of the previously output MD file (note: MD file is expected to reside in `output-md` dir)
3. The generated XLS file is dumped into the `output-xls` dir

## Example

Repo root contains `example.json` you can play with.
