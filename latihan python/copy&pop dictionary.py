#copy dictionary
teman_teman = {
    "ucup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung suruput",
    "asep":"asep si kasyep",
    "cuy": "ucuy surucuy"
}

friends = teman_teman.copy()

print(f"teman_teman:{teman_teman}")
print(f"friends:{friends}\n")

teman_teman ["ucup"]= "ucup sikeren"
print(f"teman_teman:{teman_teman}")
print(f"friends:{friends}\n")

# pop dictionary
dataaseep = friends.pop("asep")
print(f"data asep = {dataaseep}\n")
print(f"friends = {friends}\n")
