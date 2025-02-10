# question
number_question = 2135

# a .binner
biner_formatter_symbol = "{:b}"
print(f"biner :{biner_formatter_symbol.format(number_question)}")

# b.octal
octal_formatter_symbol = "{:o}"
print(f"octal :{octal_formatter_symbol.format(number_question)}")

hexadecimal_formatter_symbol = "{:x}"
print(f"octal :{hexadecimal_formatter_symbol.format(number_question)}")

# d. 4 angka dibelakang coma 
print(f"4 angka dibelakang coma: {number_question:.4f}")

# pemisahan ribuan /currency
thousands_formatter_symbol = "{:,}"
print(f"octal :{thousands_formatter_symbol.format(number_question)}")



