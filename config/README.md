# Data Parser

A lightweight and efficient library for parsing various data formats.

## Supported Formats

*   CSV (Comma Separated Values)
*   JSON (JavaScript Object Notation)
*   TXT (Plain Text)
*   INI (Initialization File)

## Installation

```bash
pip install data-parser
```

## Usage

### CSV

```python
from data_parser import CSVParser

parser = CSVParser(filepath='data.csv', delimiter=',', header=True)
data = parser.parse()

for row in data:
    print(row)
```

### JSON

```python
from data_parser import JSONParser

parser = JSONParser(filepath='data.json')
data = parser.parse()

print(data)
```

### TXT

```python
from data_parser import TXTParser

parser = TXTParser(filepath='data.txt')
data = parser.parse()

for line in data:
    print(line)
```

### INI

```python
from data_parser import INIParser

parser = INIParser(filepath='data.ini')
data = parser.parse()

for section, values in data.items():
    print(f"Section: {section}")
    for key, value in values.items():
        print(f"  {key}: {value}")
```

## Contributing

We welcome contributions! Please fork the repository and submit a pull request with your changes.

## License

MIT License

Copyright (c) 2023 [Your Name/Organization]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.