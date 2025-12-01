#!/usr/bin/python3
""""""

def check_permission(user_permission, required_permission):
    """
    Check if the user has the required permission using bitwise operators.
    
    Parameters:
    user_permission (int): The permission value assigned to the user.
    required_permission (int): The permission value required for access.
    
    Returns:
    str: "Access granted" if the user has the required permission, otherwise "Access denied".
    """
    if user_permission & required_permission == required_permission:
        return "Access granted"
    else:
        return "Access denied"


# Example usage:
print(check_permission(6, 2))  # Output: Access granted
print(check_permission(4, 2))  # Output: Access denied