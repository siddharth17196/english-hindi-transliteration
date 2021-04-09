# english-hindi-transliteration

A python package for transliterations from english to multiple indian languages


> Transliteration refers to the process of converting text in one script into another. (not translation)

## Installation
Recommended to create a virtual environment and then install.
```bash
pip install git+https://github.com/siddharth17196/english-hindi-transliteration
```


## Usage

``` python
>>>from elt import translit

>>>to_hindi = translit('hindi')
>>>to_hindi.convert(['hello world', 'namaste'])

['हेलो वर्ल्ड', 'नमस्ते']
```

## Supported Languages

| Languages |
|-----------|
| hindi     |
| telegu    |
| bengali   |
| marathi   |
| malayalam |
| odiya     |
| tamil     |
| sanskrit  |
| urdu      |
| kannada   |
| gujarati  |
| punjabi   |


### References

[Google input tools](https://www.google.co.in/inputtools/try/)
