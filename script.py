import os

directory = 'textfiles'  # Define the directory name

def create(directory, file_name, content):
    # Construct the full path where the file will be saved
    full_path = os.path.join(directory, file_name)

    # Ensure the directory exists; if not, create it
    os.makedirs(directory, exist_ok=True)

    # Check if the file already exists
    if not os.path.exists(full_path):
        # Open the file in write mode and write the content
        with open(full_path, 'w') as file:
            file.write(content)
        return True  # Return True if file was created
    return False  # Return False if file already exists

# Read the email template from 'template.txt'
with open('template.txt', 'r') as file:
    template = file.read()

# Open the CSV file and process entries
with open('namelist.csv', 'r') as file:
    next(file)  # Skip the header line
    for index, line in enumerate(file):
        line = line.strip()
        fields = line.split(';')
        # Map the data to the template placeholders
        custom_content = template.replace('[First Name]', fields[0])
        custom_content = custom_content.replace('[Last Name]', fields[1])
        custom_content = custom_content.replace('[Position]', fields[2])
        custom_content = custom_content.replace('[Limehome Email Address]', fields[3])
        custom_content = custom_content.replace('[Company Phone Number]', fields[4])
        
        # Create a filename using the person's first and last name
        filename = f"{fields[0]}{fields[1]}.txt".replace(' ', '').lower()
        full_path = os.path.join(directory, filename)
        
        # Attempt to create the file and check if it was actually created
        if create(directory, filename, custom_content):
            print(f"File '{filename}' has been created.")
            # Only append to 'done.csv' if the file was newly created
            with open('done.csv', 'a', newline='') as done_file:
                # Write the email and filename to the new line in the CSV
                done_file.write(f"{fields[3]};{filename}\n")
        else:
            print(f"File '{filename}' already exists. No new file was created.")
