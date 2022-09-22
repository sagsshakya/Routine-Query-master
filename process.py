import json
import os

from inputs import get_input
from utils import load_config

# Load Configuration file.
config = load_config()

# Prompt for input.
day, absentees = get_input(verbose = False)

# Access the database.
save_dir = config['database_path']['root']
routine_filename = config['database_path']['routine_db_path']

routine_filename = os.path.join(save_dir, routine_filename)

df = json.load(open(routine_filename))    

print(df)
#if __name__ == '__main__':
#    print(main())