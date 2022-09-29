# Apkg to Csv

Converts .apkg Anki deck SRS file to .csv

## Requirements

- Python 3

## Installation

## Usage

copy .apkg file to project's root and run

```python
python src/run.py {filename}.apkg
```

it will output {filename}.csv

If you want to convert all .apkg files in specific directory please run:
```python
python src/manage.py {directory}
```

## Tests

```python
python -m unittest tests.TestFile
```

## Contributions

Contributions are welcome and will be fully credited.

## License

This project is open-sourced software licensed under the MIT license.
