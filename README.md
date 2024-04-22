Sure, here's a README for your script:

---

# Bulk Email Template Generator

This Python script automates the generation of personalized email templates for a list of recipients stored in a CSV file. It reads a template from a text file, replaces placeholders with recipient-specific information, and saves the customized emails as individual text files. Additionally, it maintains a record of generated emails in a CSV file.

## Prerequisites

Before running the script, ensure you have Python installed on your system.

## Usage

1. **Prepare Template and Data**:
   - Create a template text file (`template.txt`) with placeholders for recipient information.
   - Prepare a CSV file (`namelist.csv`) with recipient data. The CSV file should have the following format:
     ```
     First Name;Last Name;Position;Limehome Email Address;Company Phone Number
     John;Doe;Manager;johndoe@example.com;123456789
     ```

2. **Customize Script**:
   - Update the `template.txt` file with your email template containing placeholders like `[First Name]`, `[Last Name]`, etc.
   - Adjust the `directory` variable to specify the directory where the generated email files will be saved.

3. **Run the Script**:
   - Execute the script by running the Python file.
   - Follow the prompts:
     - Decide whether to automatically update all existing files or update each file manually.
     - Confirm whether you want to update each existing file individually.

4. **Review Output**:
   - The script will generate individual email files for each recipient based on the template and data provided.
   - A CSV file named `done.csv` will be created, containing the email addresses and filenames of the generated emails.

## Script Details

- The `create_or_update` function is responsible for creating new files or updating existing ones.
- It reads the template from `template.txt` and processes each entry in the `namelist.csv`.
- Placeholders in the template are replaced with corresponding recipient data.
- Each email file is named using the recipient's first and last name.
- If a file already exists, the script prompts the user to update it or skip the update.

## Note

- Ensure that the CSV file (`namelist.csv`) and the template file (`template.txt`) are in the same directory as the script.
- Make sure to review the generated emails before sending them to recipients.

---
Feel free to adjust this README as needed to provide additional instructions or details specific to your use case.
