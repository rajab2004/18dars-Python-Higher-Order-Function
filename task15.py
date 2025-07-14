ovozlar = [
  {"variant": "A", "ovoz_soni": 123},
  {"variant": "B", "ovoz_soni": 145},
  {"variant": "C", "ovoz_soni": 97}
]

eng_kop_ovoz = max(ovozlar, key=lambda ovoz: ovoz["ovoz_soni"])

print(eng_kop_ovoz)
