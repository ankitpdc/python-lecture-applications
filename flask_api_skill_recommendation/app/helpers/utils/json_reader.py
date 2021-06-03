
def read_json_file(file_path):
    import json
    
    # Opening JSON file
    f = open(file_path,)
    
    # returns JSON object as a dictionary
    final_list = json.load(f)
    return final_list


def get_json_file_data(input_data_filepath):
    try:
        input_data = read_json_file(input_data_filepath)
        return input_data
    except Exception as e:
        raise ValueError('file_reading Failed!!!! and error is: ', e) 

# try-except is handling file reading failure, and raise will raise the error and stop the code here itself