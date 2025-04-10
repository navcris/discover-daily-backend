import json 

"""
Combines json files into one larger json to parse

Args: N/A 

Returns: N/A
"""
def combiner():
    json_files = ['snex_articles.json']

    combined_data = []

    for json_file in json_files:
        with open (json_file, 'r') as f:
            data = json.load(f)
            combined_data.extend(data)

    with open("combined.json", 'w') as f:
        json.dump(combined_data, f, indent=4)
