import os
import csv

directory = 'textfiles'  # Define the directory name

def create_or_update(directory, file_name, content, update_all):
    # Construct the full path where the file will be saved
    full_path = os.path.join(directory, file_name)

    # Ensure the directory exists; if not, create it
    os.makedirs(directory, exist_ok=True)

    # Check if the file already exists
    if os.path.exists(full_path):
        if update_all or input(f"File '{file_name}' already exists. Do you want to update it? (yes/no): ").strip().lower() == 'yes':
            with open(full_path, 'w') as file:
                file.write(content)
            print(f"File '{file_name}' has been updated.")
            return True
        else:
            # No update and no deletion, just return False
            print(f"File '{file_name}' was not updated.")
            return False
    else:
        # Open the file in write mode and write the content
        with open(full_path, 'w') as file:
            file.write(content)
        print(f"New file '{file_name}' has been created.")  # Notify when a new file is created
        return True  # Return True if file was created


# Get user decision on updating all files at once
update_all = input("Do you want to automatically update all existing files? (yes/no): ").strip().lower() == 'yes'

# Read the email template from 'template.txt'
with open('template.txt', 'r') as file:
    template = file.read()

# Open the CSV file and process entries
with open('namelist.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)  # Skip the header line
    for fields in reader:
        # Map the data to the template placeholders
        custom_content = template
        placeholders = ['[First Name]', '[Last Name]', '[Position]', '[Limehome Email Address]', '[Company Phone Number]']
        for placeholder, field in zip(placeholders, fields):
            custom_content = custom_content.replace(placeholder, field)
        
        # Create a filename using the person's first and last name
        filename = f"{fields[0]}{fields[1]}.txt".replace(' ', '').lower()
        
        # Attempt to create or update the file and check if it was actually created or updated
        if create_or_update(directory, filename, custom_content, update_all):
            # Only append to 'done.csv' if the file was newly created or updated
            with open('done.csv', 'a', newline='') as done_file:
                csv_writer = csv.writer(done_file, delimiter=';')
                # Write the email and filename to the new line in the CSV
                csv_writer.writerow([fields[3], filename])
        else:
            print(f"No action taken for '{filename}'.")
