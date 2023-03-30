# DBMS interface

DBMS interface. The implementation is not important for this tutorial.

## Overview

| **model_name** | **Implementation**         |
| -------------- | -------------------------- |
| dict_db        | Python dictionary          |
| json_db        | File System (Json Format)  |

## Usage

```python
from dbms.model_name.model import Model
model = Model()

value = model.method(args)
```

## Method

### Create

```python
def create(self, key: str, value: dict) -> bool:
    '''
    key = "1"
    value = {"firstName": "Sergey", "lastName": "Mikhaylov"}
    return = True when succeed
             False when faild
    '''
```

### Read
```python
def read(self, key: str) -> dict:
    '''
    key = "1"
    reutrn = {"firstName": "Sergey", "lastName": "Mikhaylov"}
             None when key does not exist
    '''
```

### Update

```python
def update(self, key: str, value: dict) -> bool:
    '''
    key = "1"
    value = {"firstName": "Sergey", "lastName": "Mikhaylov"}
    return = True when succeed
             False when faild
    '''
```

### Delete

```python
def delete(self, key: str) -> bool:
    '''
    key = "1"
    return = True when succeed
             False when key does not exist
    '''
```

### Debug

```python
def debug(self) -> dict:
    '''
    return = database if implemented
             None if not implemented
    '''
```