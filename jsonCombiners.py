import json 


def combiner():
    json_files = ['nature_articles.json', 'snex_articles.json', 'yale_articles.json'] 

    combined_data = []

    for json_file in json_files:
        with open (json_file, 'r') as f:
            data = json.load(f)
            combined_data.extend(data)

    with open("combined.json", 'w') as f:
        json.dump(combined_data, f, indent=4)
