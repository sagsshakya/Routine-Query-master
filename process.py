import json
from inputs import get_input

# Prompt for input.
day, absentees = get_input(verbose = False)

# Access the database.
df = json.load(open('result.json'))    

#if __name__ == '__main__':
#    print(main())