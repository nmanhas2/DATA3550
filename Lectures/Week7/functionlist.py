values = [12,34,590,100]
scores = [32,54,67.5,29,35]

def sum(values) :
    total = 0.0
    for element in values:
        total = total + element
    return total

def multiply(values, factor) :
    for i in range(len(values)):
        values[i] = values[i] * factor
    print(values)

def squares(n) :
    result = []
    for i in range(n) :
        result.append(i * i)
    return result


def main():
     
    print(sum(values))
    multiply(scores, 10)
    print(squares(8))
main()
