from datetime import datetime

def generate_job_number(zone, item_type):
    year = datetime.now().strftime('%y')
    
    if zone == 'SCR' and item_type == 'SG':
        first_digit = '3'
    elif zone == 'SCR' and item_type == 'NSG':
        first_digit = '5'
    elif zone != 'SCR' and item_type == 'SG':
        first_digit = '4'
    else:
        first_digit = '6'

    # Incremental number logic would go here. For now, using a placeholder '001'.
    incremental_number = '001'
    
    return f'{first_digit}{incremental_number}{year}00'