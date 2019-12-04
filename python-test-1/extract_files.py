import os
import uuid

source_directory = os.path.join(os.getcwd(), "source")

for filename in os.listdir(source_directory):
    file, extension = os.path.splitext(filename)
    unique_filename = str(uuid.uuid4()) + extension
    os.rename(os.path.join(source_directory,  filename), os.path.join(source_directory, unique_filename))


training_directory = os.path.join(os.getcwd(), "training_data")

for process_file in os.listdir(source_directory):
    print(process_file)
    file, extension = os.path.splitext(process_file)

    # We create a new text file name by concatenating the .txt extension to file UUID
    dest_file_path = "myfile" + '.txt'

    # extract text from the file
    content = textract.process(os.path.join(source_directory, process_file))

    # We create and open the new and we prepare to write the Binary Data which is represented by the wb - Write Binary
    write_text_file = open(os.path.join(training_directory, dest_file_path), "wb")

    # write the content and close the newly created file
    write_text_file.write(content)
    write_text_file.close()