"""Writing for loops practice"""

pets: list[str] = ["Louie", "Bo", "Bear"]

for pet_name in pets:
    print(f"Good boy, {pet_name}!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]
#print each index name
for idx in range(0,len(names)):
    print(f"{idx}: {names{idx}}")