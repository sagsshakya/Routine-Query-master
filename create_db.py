import os
import pandas as pd

from utils import dump_json, load_config, load_teachers

def create_database(config: dict):
    root_dir = config["intermidiate_path"]           #'data\\intermidiate'
    input_filenames = os.listdir(root_dir)
    input_filepaths = [os.path.join(root_dir, NAME)  for NAME in input_filenames]

    keys = [item.split(".")[0][-2:] for item in input_filenames]

    # Save format.
        ## key_grade : dict(routine)
    df_dict = {KK: pd.read_csv(FILEPATH, delimiter = "\t").to_dict() for KK, FILEPATH in zip(keys, input_filepaths)}

    # Serialize to JSON.
    save_dir = config['database_path']['root']
    routine_filename = config['database_path']['routine_db_path']
    
    routine_filename = os.path.join(save_dir, routine_filename)
    dump_json(df_dict, routine_filename)

    # Update teachers - universal.
    teachers_coll = set()
    for dictionary in df_dict.values():
        teachers_set = load_teachers(pd.DataFrame(dictionary))
        teachers_coll = teachers_coll.union(teachers_set)

    teachers_coll = sorted(teachers_coll.difference({'void'}))

    # Dump the file to TXT.
    teachers_filename = config['database_path']['teachers_list_path']
    teachers_filename = os.path.join(save_dir, teachers_filename)
    
    with open(teachers_filename, 'w') as f:
        for name in teachers_coll:
            f.write(f"{name}\n")
            
if __name__ == '__main__':
    config = load_config()
    create_database(config)