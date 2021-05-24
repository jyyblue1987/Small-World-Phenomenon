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

def loadInvestments_metro(filename):
    fp = open(filename, "r")

    lines = fp.readlines()

    investments = []
    i = 0
    for line in lines:
        line = line.strip()
        if line.strip() == '':
            continue
        i = i + 1
        if i <= 2: # Continue header and total average line
            continue

        vals = line.split(",")
        latest_price = int(vals[len(vals) - 1])
        last_year_price = int(vals[len(vals) - 13])
        profit = latest_price - last_year_price
        row = (vals[1], latest_price, profit)

        investments.append(row)

    fp.close()

    return investments


def optimizeInvestments(investments, limit, step):
    n = len(investments)

    step_count = limit // step

    K = [[0 for x in range(step_count + 1)] for x in range(n + 1)]
    track = [[0 for x in range(step_count + 1)] for x in range(n + 1)] 

    # Buiuld table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(step_count + 1):            
            if i == 0 or w == 0: # the base cases, when we don’t select any investments, nomatter how much money we have to spend (top row), then we get no return on investment
                K[i][w] = 0
                track[i][w] = 0
            else:
                wt = investments[i - 1][1] // step
                if w < wt:
                    K[i][w] = K[i - 1][w]                    
                else:
                    val1 = investments[i - 1][2] // step + K[i - 1][w - wt]
                    val2 = K[i - 1][w]
                    if val1 > val2:
                        K[i][w] = val1
                        track[i][w] = 1 # select i th investment
                    else:
                        K[i][w] = val2                        
                
    # at the end to trace back through these winning options. 
    nn = n
    ww = step_count
    sols = []
    value = 0
    while nn > 1:
        if track[nn][ww] == 1:
            sols.append(nn - 1)            
            ww = ww - investments[nn - 1][1] // step
            value = value + investments[nn - 1][2]

        nn = nn - 1

    sols.reverse()

    selected = []
    for index in sols:
        selected.append(investments[index][0])

    
    return value, selected  # goal location in the table,  lower-right corner

investments = loadInvestments("input.txt")
value, sol = optimizeInvestments(investments, 50, 1)

print(value, sol)


investments = loadInvestments_metro("Metro.csv")
value, sol = optimizeInvestments(investments, 1000000, 1000)

print(value, sol)
