#!/usr/bin/python3
""""""

def calculate_bonus(salary, performance_rating):
    """
    Calculate total salary including bonus based on performance rating.
    
    Parameters:
    salary (float): Employee's base salary
    performance_rating (str): Performance rating ("Excellent", "Good", "Average")
    
    Returns:
    float: Total salary including bonus
    """
    # Assign bonus percentage based on rating
    if performance_rating == "Excellent":
        bonus_percent = 20
    elif performance_rating == "Good":
        bonus_percent = 10
    elif performance_rating == "Average":
        bonus_percent = 5
    else:
        raise ValueError("Performance rating must be 'Excellent', 'Good', or 'Average'")
    
    # Calculate bonus amount
    bonus_amount = salary * (bonus_percent / 100)
    
    # Calculate total salary including bonus
    total_salary = salary + bonus_amount
    
    return total_salary