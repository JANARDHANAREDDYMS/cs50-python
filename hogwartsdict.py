students = [
    {"name": "hermoine","house":"gryffindor","patronus":"otter"},
    {"name": "harry","house":"gryffindor","patronus":"stag"},
    {"name": "ron","house":"gryffindor","patronus":"jack russel terrier"},
    {"name":"draco","house":"slyhterin","patronus":None}
]

for student in students:
    print(student["name"],student["house"],student["patronus"])