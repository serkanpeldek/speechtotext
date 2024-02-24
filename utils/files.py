import os

def save_text_to_file(text, save_dir, file_name):
    # Create the full path to the file
    file_path = os.path.join(save_dir, file_name)

    # Check if the file already exists
    counter = 1
    while os.path.exists(file_path):
        # If file exists, add a counter to the file name
        new_file_name = f"{file_name}_{counter}.txt"
        file_path = os.path.join(save_dir, new_file_name)
        counter += 1

    # Write the text to the file
    with open(file_path, 'w') as file:
        file.write(text)

    print(f"Text saved to: {file_path}")