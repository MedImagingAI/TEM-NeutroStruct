import json

# Paths to the input and output JSON files
input_json_path = './7classes_version/train/annotations/annotations_7classes.json'  # Update as needed
output_json_path = './7classes_version/train/annotations/annotations_7classes_updated.json'  # Update as needed

# Define the new class IDs and names
CLASSES = {
    'Specific granules': 1,
    'Non-specific primary granules': 2,
    'Non-specific tertiary granules': 3,
    'Non-specific secondary granules': 4,
    'Empty vesicles': 5,
    'Emptying vesicles': 6,
    'Vacuoles': 7
}

# Load the JSON data
with open(input_json_path, 'r') as f:
    data = json.load(f)

# Create a dictionary to map old category IDs to new ones based on their names
category_mapping = {cat['name']: CLASSES[cat['name']] for cat in data['categories'] if cat['name'] in CLASSES}

# Update the category IDs in the annotations
for annotation in data['annotations']:
    # Find the category name using the old category ID
    old_category_name = next((cat['name'] for cat in data['categories'] if cat['id'] == annotation['category_id']), None)
    if old_category_name and old_category_name in category_mapping:
        # Update the category_id to the new one
        annotation['category_id'] = category_mapping[old_category_name]

# Update the categories section with the new IDs and remove old ones
data['categories'] = [{'id': id, 'name': name, 'supercategory': 'granule/vesicle'} for name, id in CLASSES.items()]

# Save the updated JSON file
with open(output_json_path, 'w') as f:
    json.dump(data, f, indent=4)

print(f"Updated JSON file created at: {output_json_path}")
