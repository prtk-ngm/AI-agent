from tools import(get_current_time, roll_dice, generate_password)

def execute_tool( user_input):
    """executes tool based on input and"""
    if "time" in user_input.lower():
        return get_current_time()
    elif "dice" in user_input.lower():
        return roll_dice()
    elif "password" in user_input.lower():
        return generate_password()
    else:
        return None
    
