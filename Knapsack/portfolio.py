def loadInvestments(filename):
    fp = open(filename, "r")

    lines = fp.readlines()

    investments = []
    for line in lines:
        vals = line.split(",")
        row = (vals[0], int(vals[1]), int(vals[2]))

        investments.append(row)

    fp.close()

    return investments


def optimizeInvestments(investments, limit):
    n = len(investments)

    K = [[0 for x in range(limit + 1)] for x in range(n + 1)]

    # Buiuld table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(limit + 1):            
            if i == 0 or w == 0:
                K[i][w] = 0
            else:
                wt = investments[i - 1][1]
                if wt <= w:
                    K[i][w] = max(investments[i - 1][2] + K[i - 1][w - wt], K[i - 1][w])
                else:
                    K[i][w] = K[i - 1][w]

    return K[n][w], None

investments = loadInvestments("input.txt")
value, sol = optimizeInvestments(investments, 50)

print(value)


