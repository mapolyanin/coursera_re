def calculate(data, findall):
    matches = findall(r"([abc])([-+]?)=([abc]?)([+-]?\d*)")  # Если придумать хорошую регулярку, будет просто
    #print(matches, "\n")
    for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        # Если бы могло быть только =, вообще одной строкой все считалось бы, вот так:
        data[v1] = (-data.get(v2, 0) if s=="-" else data.get(v2, 0))   + int(n or 0)
        print (v1, s, v2, n, "\n")
    return data
