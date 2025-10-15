# Basic structure without actual implementation
students_data = []

# Read CSV file line by line
with open('StudentData.csv', 'r') as file:
    # Skip header or use it for column names
    header = file.readline().strip().split(',')
    
    for line in file:
        # Split each line by comma
        values = line.strip().split(',')
        
        # Create dictionary for each student
        student = {
            'age': int(values[0]),
            'gender': values[1],
            'name': values[2],
            'course': values[3],
            'roll': int(values[4]),
            'marks': int(values[5]),
            'email': values[6]
        }
        
        students_data.append(student)

# Now analyze using collections, operators, and conditions
