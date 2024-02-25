import json
import math
with open('./dataset.jsonl', 'r') as json_file:
    dataset = json.load(json_file)
length = len(dataset["messages"])
train_portion = math.ceil(80/100 * length)
train_set = []
valid_set = []
for i in range(0, train_portion, 2):
    dct = {"messages": dataset["messages"][i:i + 2]}
    train_set.append(dct)

# Loop through the remaining part of the dataset to create the validation set
for j in range(train_portion, length, 2):
    dct = {"messages": dataset["messages"][j:j + 2]}
    valid_set.append(dct)

    
with open('./train_set.jsonl', 'w') as json_out:
    for item in train_set:
        json_out.write(json.dumps(item) + '\n')
with open('./val_set.jsonl', 'w') as json_out:
    for item in valid_set:
        json_out.write(json.dumps(item) + '\n')

