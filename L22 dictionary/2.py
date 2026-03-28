student_data = {
    "id1":{"name":"Embreigh","class":"V","subject_integration":"english,math,sience"},
    "id2":{"name":"Elijah","class":"V","subject_integration":"english,math,sience"},
    "id3":{"name":"Noah","class":"V","subject_integration":"english,math,sience"},
    "id4":{"name":"Paislee","class":"V","subject_integration":"english,math,sience"}
}

result = {}
seen_keys = [] #Using a list insteadof set 

for student_id, details in student_data.items():
    unique_key = {details["name"],details["class"],details["subject_integration"]}

    if unique_key not in seen_keys: 
        seen_keys.append(unique_key)
        result[student_id] = details

#Print output line by line
for k, v in result.items():
    print(k,":",v)