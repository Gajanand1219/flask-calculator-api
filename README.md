# flask-calculator-api




https://github.com/user-attachments/assets/dd46d298-fd9e-443d-9635-8f4845425b62













# Simple Python Flask API

This repository contains a simple **Python Flask API** that provides the following functionalities:

### Functionalities:
1. **Age Calculator**: Calculate a person's age based on the provided birthdate.
2. **Mathematical Operations**: Perform basic math operations like square root and cube.
3. **Unit Conversions**: Convert between various units of measurement:
   - **Weight**: Kilograms to grams and grams to kilograms.
   - **Length**: Centimeters to meters and meters to centimeters.

## API Endpoints:

### 1. Age Calculator
- **URL**: `/calculate_age`
- **Method**: `GET`
- **Parameters**: 
  - `birthdate` (format: YYYY-MM-DD)
- **Description**: Takes a birthdate as input and returns the current age in years.

#### Example:
- **Request**: `GET /calculate_age?birthdate=1990-01-01`
- **Response**: 
  ```json
  {
    "age": 34
  }

### 2. Math Operations
- **URL**: `/math_operations`
- **Method**: `GET`
- **Parameters**:
  - `number`: The number to perform the operation on.
  - `operation`: The operation to perform (`sqrt` for square root, `cube` for cube).
- **Description**: Performs either a square root or cube operation on the provided number.

#### Example:
- **Request**: `GET /math_operations?number=16&operation=sqrt`
- **Response**: 
  ```json
  {
    "result": 4.0
  }

### 3. Weight Conversion
- **URL**: `/convert_weight`
- **Method**: `GET`
- **Parameters**:
  - `value`: The numerical value of the weight.
  - `unit`: The unit of the provided value (`kg` for kilograms or `gram` for grams).
- **Description**: Converts between kilograms and grams.

#### Example:
- **Request**: `GET /convert_weight?value=1&unit=kg`
- **Response**: 
  ```json
  {
    "result": "1 kg is 1000 grams"
  }

### 4. Length Conversion
- **URL**: `/convert_length`
- **Method**: `GET`
- **Parameters**:
  - `value`: The numerical value of the length.
  - `unit`: The unit of the provided value (`cm` for centimeters or `m` for meters).
- **Description**: Converts between centimeters and meters.

#### Example:
- **Request**: `GET /convert_length?value=200&unit=cm`
- **Response**: 
  ```json
  {
    "result": "200 cm is 2.0 m"
  }



This snippet outlines how to use the **Length Conversion** endpoint, with the URL, method, parameters, description, and a practical example of the request and response.






