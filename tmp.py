def mapDecoding(message):
    if not message: return 1
    if message[0] == '0': return 0
    ways = 1
    for i in range(len(message) - 1, 0,-1):
        print(i, message[i])
        d = message[i]
        if int(d):
            if i + 1 < len(message) and 1 <= int(d+message[i+1]) <= 26:
                ways = ways * 2 % (10^9 + 7)
        else:
            if i-1 >= 0 and 1 <= int(message[i-1] + d) <= 26:
                if message[i+1] == '0': return 0
            else:
                return 0
    return ways % (10^9 + 7)

message = '12182'
print(mapDecoding(message))

