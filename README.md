# json-documentor

This project provides Python scripts, for generating MD and XLS documentation out of provided JSON objects.

## JSON to MD usage

1. In repo root, execute `python json-to-md.py``
2. Specify the path of the input json
3. When prompted, specify a description for each property in provided JSON
4. The generated MD file is dumped into the `output-md` dir

## MD to XLS

1. In repo root, execute `python md-to-xls.py`
2. Specify the name of the previously output MD file (note: MD file is expected to reside in `output-md` dir)
3. The generated XLS file is dumped into the `output-xls` dir
