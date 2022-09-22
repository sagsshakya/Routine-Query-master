from itertools import chain
import json
import pandas as pd

def load_teachers(dataframe: pd.DataFrame) -> set:
    
    # Teachers' list.
    teachers = dataframe.iloc[:, 1:].values.ravel()
    teachers = set(teachers)
    teachers = [name.split("/") for name in teachers]
    teachers = set(chain.from_iterable(teachers))  
    return teachers  
    
def dump_json(df_dict: dict, filepath: str):
    class JSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if hasattr(obj, 'to_json'):
                return obj.to_json(orient='records')
            return json.JSONEncoder.default(self, obj)    

    with open(filepath, 'w') as fp:
        json.dump(df_dict, fp, cls=JSONEncoder)
        
def load_config() -> dict:
    # Load config.
    with open("config.json") as ff:
        config = json.load(ff)
        
    return config