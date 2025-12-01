#!/usr/bin/python3
"""a module that convert tempreture scale"""

def convert_temperature(temp, scale):
    """
    Convert temperature between Celsius and Fahrenheit.
    
    Parameters:
    temp (float): The temperature value to convert.
    scale (str): Target scale - "C" for Celsius, "F" for Fahrenheit.
    
    Returns:
    float: Converted temperature.
    """
    if scale == "C":
        # Convert Fahrenheit to Celsius
        converted = (temp - 32) * 5/9
    elif scale == "F":
        # Convert Celsius to Fahrenheit
        converted = (temp * 9/5) + 32
    else:
        raise ValueError("Scale must be 'C' or 'F'")
    
    return round(converted, 2)