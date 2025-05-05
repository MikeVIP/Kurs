mitarbeitende = {
    "person1": {
        "Name": "Max Müller",
        "E-Mail": "max.mueller@example.com",
        "Alter": 29,
        "Geschlecht": "männlich"
    },
    "person2": {
        "Name": "Lisa Schmidt",
        "E-Mail": "lisa.schmidt@example.com",
        "Alter": 34,
        "Geschlecht": "weiblich"
    },
    "person3": {
        "Name": "Ali Khan",
        "E-Mail": "ali.khan@example.com",
        "Alter": 41,
        "Geschlecht": "männlich"
    }
}

for k, p in mitarbeitende.items():
    print(f"ID: {k} Name: {p['Name']}")
    print(f"Alter: {p['Alter']} Geschlecht: {p['Geschlecht']}")
    print(f"E-Mail: {p['E-Mail']}")
    print("_"*40)

# lub

print("\n"*4)

for k in mitarbeitende:
    print(f"ID: {k} Name: {mitarbeitende[k]['Name']}")
    print(f"Alter: {mitarbeitende[k]['Alter']} Geschlecht: {mitarbeitende[k]['Geschlecht']}")
    print(f"E-Mail: {mitarbeitende[k]['E-Mail']}")
    print("_"*40)
