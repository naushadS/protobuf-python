# Protobuf-Python

## What is Protobuf?
1. Protobuf, short for 'Protocol buffers' are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data – think XML/JSON, but smaller, faster, and simpler.
2. You define how you want your data to be structured once, then you can use special generated source code to easily write and read your structured data to and from a variety of data streams and using a variety of languages.

## What is this repo about?
1. See how a sample `.proto` file which contains the schema definition, looks like. 
2. See how the proto compiler generated python code(for the purpose of serializing/deserializing the data) looks like.To generate the Java, Python, or C++ code you need to work with the message types defined in a `.proto` file, you need to run the protocol buffer compiler `protoc` on the `.proto`.)
3. See how you can generate a sample data as per your defined schema and serialize it to its binary form, all using the python data access classes.
4. See how you can deserialize the sample data from its binary form, back to its original form.
5. See how efficient it is, in terms of the size that it takes to store the data/send across the network, as compared to JSON.

## Setup Mini/Conda Environment

RUN Following:
1. ```conda env create -f conda-environment.yml```
2. ```conda activate protobuf-python```

## Setup pip virtual environment

RUN Following:
1. ```python -m venv ./protobuf-python```
2. ```source ./protobuf-python/bin/activate```
3. ```pip install -r requirements.txt```

## (Optional) To generate python code for serializing/deserializing the data using proto

- from the project root, RUN
    ```
    protoc protos/person.proto --proto_path generated=protos/ --python_out=protos/
    ```

## proto_serializer.py output

```
########################################################################################################################
Encoding -> person
########################################################################################################################
    

'person in python-dictionary form' representation:
------------------------------------------------------------------------------------------------------------------------
{'firstName': 'Naushad', 'lastName': 'Shukoor', 'age': 25, 'email': 'naushadshukoor@gmail.com'}
------------------------------------------------------------------------------------------------------------------------


'person in json form' representation:
------------------------------------------------------------------------------------------------------------------------
{"firstName": "Naushad", "lastName": "Shukoor", "age": 25, "email": "naushadshukoor@gmail.com"}
------------------------------------------------------------------------------------------------------------------------

    
Took 95 bytes to store json data in json format


'person in proto form' representation:
------------------------------------------------------------------------------------------------------------------------
firstName: "Naushad"
lastName: "Shukoor"
age: 25
email: "naushadshukoor@gmail.com"

------------------------------------------------------------------------------------------------------------------------


'person in binary form' representation:
------------------------------------------------------------------------------------------------------------------------
b'\n\x07Naushad\x12\x07Shukoor\x18\x19"\x18naushadshukoor@gmail.com'
------------------------------------------------------------------------------------------------------------------------

    
Took 46 bytes to store serialized data(using protobuf) in binary format


########################################################################################################################
Encoding -> persons (person array)
########################################################################################################################
    

'persons in python-list form' representation:
------------------------------------------------------------------------------------------------------------------------
[{'firstName': 'Naushad', 'lastName': 'Shukoor', 'age': 25, 'email': 'naushadshukoor@gmail.com'}, {'firstName': 'John', 'lastName': 'Doe', 'age': 26, 'email': 'johndoe@mail.com'}, {'firstName': 'Bruce', 'lastName': 'Wayne', 'age': 27, 'email': 'brucewayne@mail.com'}, {'firstName': 'Clark', 'lastName': 'Kent', 'age': 28, 'email': 'clarkkent@mail.com'}, {'firstName': 'Peter', 'lastName': 'Parker', 'age': 29, 'email': 'peterparker@mail.com'}]
------------------------------------------------------------------------------------------------------------------------


'persons in JSON form' representation:
------------------------------------------------------------------------------------------------------------------------
[{"firstName": "Naushad", "lastName": "Shukoor", "age": 25, "email": "naushadshukoor@gmail.com"}, {"firstName": "John", "lastName": "Doe", "age": 26, "email": "johndoe@mail.com"}, {"firstName": "Bruce", "lastName": "Wayne", "age": 27, "email": "brucewayne@mail.com"}, {"firstName": "Clark", "lastName": "Kent", "age": 28, "email": "clarkkent@mail.com"}, {"firstName": "Peter", "lastName": "Parker", "age": 29, "email": "peterparker@mail.com"}]
------------------------------------------------------------------------------------------------------------------------

    
Took 443 bytes to store json data in json format


'persons in proto form' representation:
------------------------------------------------------------------------------------------------------------------------
persons {
  firstName: "Naushad"
  lastName: "Shukoor"
  age: 25
  email: "naushadshukoor@gmail.com"
}
persons {
  firstName: "John"
  lastName: "Doe"
  age: 26
  email: "johndoe@mail.com"
}
persons {
  firstName: "Bruce"
  lastName: "Wayne"
  age: 27
  email: "brucewayne@mail.com"
}
persons {
  firstName: "Clark"
  lastName: "Kent"
  age: 28
  email: "clarkkent@mail.com"
}
persons {
  firstName: "Peter"
  lastName: "Parker"
  age: 29
  email: "peterparker@mail.com"
}

------------------------------------------------------------------------------------------------------------------------


'persons in binary form' representation:
------------------------------------------------------------------------------------------------------------------------
b'\n.\n\x07Naushad\x12\x07Shukoor\x18\x19"\x18naushadshukoor@gmail.com\n\x1f\n\x04John\x12\x03Doe\x18\x1a"\x10johndoe@mail.com\n%\n\x05Bruce\x12\x05Wayne\x18\x1b"\x13brucewayne@mail.com\n#\n\x05Clark\x12\x04Kent\x18\x1c"\x12clarkkent@mail.com\n\'\n\x05Peter\x12\x06Parker\x18\x1d"\x14peterparker@mail.com'
------------------------------------------------------------------------------------------------------------------------

    
Took 198 bytes to store serialized data(using protobuf) (5 records)  in binary format

Took 9988890 bytes(9.99 MB) to store data (100k records) in JSON format

Took 4983486 bytes(4.98 MB) to store serialized data(using protobuf) (100k records) in binary format


########################################################################################################################
Summary
########################################################################################################################

person(json):95 bytes, person(binary):46 bytes ------> (0.48% reduction in storage size)

persons_5_records(json):443 bytes, persons_5_records(binary):198 bytes ------> (0.45% reduction in storage size)

persons_100k_records(json):9988890 bytes (9.99 MB), persons_100k_records(binary):4983486 bytes (4.98 MB) ------> (0.5% reduction in storage size)
```

## proto_deserializer.py output

```
########################################################################################################################
Decoding -> person
########################################################################################################################
    

person(in binary) deserialized:
------------------------------------------------------------------------------------------------------------------------
firstName: "Naushad"
lastName: "Shukoor"
age: 25
email: "naushadshukoor@gmail.com"

------------------------------------------------------------------------------------------------------------------------
type -> <class 'generated.person_pb2.Person'>
    

convert person to Dict using MessageToDict(from google.protobuf.json_format):
------------------------------------------------------------------------------------------------------------------------
{'firstName': 'Naushad', 'lastName': 'Shukoor', 'age': 25, 'email': 'naushadshukoor@gmail.com'}
------------------------------------------------------------------------------------------------------------------------
type -> <class 'dict'>
    

convert person to JSON using MessageToJson(from google.protobuf.json_format):
------------------------------------------------------------------------------------------------------------------------
{
  "firstName": "Naushad",
  "lastName": "Shukoor",
  "age": 25,
  "email": "naushadshukoor@gmail.com"
}
------------------------------------------------------------------------------------------------------------------------
type -> <class 'str'>
    

person(in JSON file) read back:
------------------------------------------------------------------------------------------------------------------------
{'firstName': 'Naushad', 'lastName': 'Shukoor', 'age': 25, 'email': 'naushadshukoor@gmail.com'}
------------------------------------------------------------------------------------------------------------------------
type -> <class 'dict'>
    

########################################################################################################################
Decoding -> persons (person array)
########################################################################################################################
    

persons(in binary) deserialized:
------------------------------------------------------------------------------------------------------------------------
persons {
  firstName: "Naushad"
  lastName: "Shukoor"
  age: 25
  email: "naushadshukoor@gmail.com"
}
persons {
  firstName: "John"
  lastName: "Doe"
  age: 26
  email: "johndoe@mail.com"
}
persons {
  firstName: "Bruce"
  lastName: "Wayne"
  age: 27
  email: "brucewayne@mail.com"
}
persons {
  firstName: "Clark"
  lastName: "Kent"
  age: 28
  email: "clarkkent@mail.com"
}
persons {
  firstName: "Peter"
  lastName: "Parker"
  age: 29
  email: "peterparker@mail.com"
}

------------------------------------------------------------------------------------------------------------------------
type -> <class 'generated.person_pb2.Persons'>
    

convert person to Dict using MessageToDict(from google.protobuf.json_format):
------------------------------------------------------------------------------------------------------------------------
{'persons': [{'firstName': 'Naushad', 'lastName': 'Shukoor', 'age': 25, 'email': 'naushadshukoor@gmail.com'}, {'firstName': 'John', 'lastName': 'Doe', 'age': 26, 'email': 'johndoe@mail.com'}, {'firstName': 'Bruce', 'lastName': 'Wayne', 'age': 27, 'email': 'brucewayne@mail.com'}, {'firstName': 'Clark', 'lastName': 'Kent', 'age': 28, 'email': 'clarkkent@mail.com'}, {'firstName': 'Peter', 'lastName': 'Parker', 'age': 29, 'email': 'peterparker@mail.com'}]}
------------------------------------------------------------------------------------------------------------------------
type -> <class 'dict'>
    

convert person to JSON using MessageToJson(from google.protobuf.json_format):
------------------------------------------------------------------------------------------------------------------------
{
  "persons": [
    {
      "firstName": "Naushad",
      "lastName": "Shukoor",
      "age": 25,
      "email": "naushadshukoor@gmail.com"
    },
    {
      "firstName": "John",
      "lastName": "Doe",
      "age": 26,
      "email": "johndoe@mail.com"
    },
    {
      "firstName": "Bruce",
      "lastName": "Wayne",
      "age": 27,
      "email": "brucewayne@mail.com"
    },
    {
      "firstName": "Clark",
      "lastName": "Kent",
      "age": 28,
      "email": "clarkkent@mail.com"
    },
    {
      "firstName": "Peter",
      "lastName": "Parker",
      "age": 29,
      "email": "peterparker@mail.com"
    }
  ]
}
------------------------------------------------------------------------------------------------------------------------
type -> <class 'str'>
    

Printing value of 'persons' key from the Dict:
------------------------------------------------------------------------------------------------------------------------
[{'firstName': 'Naushad', 'lastName': 'Shukoor', 'age': 25, 'email': 'naushadshukoor@gmail.com'}, {'firstName': 'John', 'lastName': 'Doe', 'age': 26, 'email': 'johndoe@mail.com'}, {'firstName': 'Bruce', 'lastName': 'Wayne', 'age': 27, 'email': 'brucewayne@mail.com'}, {'firstName': 'Clark', 'lastName': 'Kent', 'age': 28, 'email': 'clarkkent@mail.com'}, {'firstName': 'Peter', 'lastName': 'Parker', 'age': 29, 'email': 'peterparker@mail.com'}]
------------------------------------------------------------------------------------------------------------------------
type -> <class 'list'>
    

persons(in JSON file) read back:
------------------------------------------------------------------------------------------------------------------------
[{'firstName': 'Naushad', 'lastName': 'Shukoor', 'age': 25, 'email': 'naushadshukoor@gmail.com'}, {'firstName': 'John', 'lastName': 'Doe', 'age': 26, 'email': 'johndoe@mail.com'}, {'firstName': 'Bruce', 'lastName': 'Wayne', 'age': 27, 'email': 'brucewayne@mail.com'}, {'firstName': 'Clark', 'lastName': 'Kent', 'age': 28, 'email': 'clarkkent@mail.com'}, {'firstName': 'Peter', 'lastName': 'Parker', 'age': 29, 'email': 'peterparker@mail.com'}]
------------------------------------------------------------------------------------------------------------------------
type -> <class 'list'>

```
