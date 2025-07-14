gap = "Functional programming in Python is very powerful and elegant"
sozlar = gap.split()

sozlar = sorted(
    sozlar,
    key=lambda soz: len(soz)
)

print(sozlar[-3:])
