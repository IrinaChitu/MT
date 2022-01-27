import ast

TRANSL_FILENAME = "results_sample.txt"

f = open(TRANSL_FILENAME, "r")
data = f.read()

transl_dict = ast.literal_eval('(' + data + ')')

# print(transl_dict[0]["bg"])