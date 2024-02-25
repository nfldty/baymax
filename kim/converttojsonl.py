import json

# Read the iCliniq.json file
with open('./iCliniq.json', 'r') as json_file:
    iCliniq_data = json.load(json_file)

# New list to hold transformed data
transformed_data = {"messages": []}

# Loop through each object in the iCliniq_data list
for item in iCliniq_data:
    # Extract the input to User and answer_icliniq to Chatbot
    input_message = item["input"].replace("Welcome to Chat Doctor", "").replace("Welcome to ChatDoctor", "")
    answer_icliniq = item["answer_icliniq"].replace("Welcome to Chat Doctor", "Welcome to BayMax").replace("Welcome to ChatDoctor", "Welcome to BayMax").replace("ChatDoctor", "")
    # Add the transformed data to the new list
    transformed_data["messages"].append({
        "role": "User",
        "content": input_message
    })
    transformed_data["messages"].append({
        "role": "Chatbot",
        "content": answer_icliniq
    })

# Write the transformed data to a new JSON file
with open('./dataset.jsonl', 'w') as json_out:
    json.dump(transformed_data, json_out, indent=2)

