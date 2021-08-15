def mergingCities(roadRegister):
    def print_rr(r):
        for i in range(len(r)):
            for j in range(len(r)):
                if r[i][j]:
                    print('1', end=' ')
                else:
                    print('0', end=' ')
            print('')
        return
    n = len(roadRegister)
    roads_to_delete = []
    print("Original")
    print_rr(roadRegister)
    for i in range(0, n-1,2):
        if roadRegister[i][i+1]:
            roads_to_delete.append(i+1)
    for i in roads_to_delete:
        roadRegister[i-1] = list(map(lambda x: x[0] or x[1], zip(roadRegister[i-1], roadRegister[i])))
        for j in roads_to_delete:
            roadRegister[i-1][j-1] = roadRegister[i-1][j-1] or roadRegister[i-1][j]
    print(roads_to_delete)
    print('Merged')
    print_rr(roadRegister)
    res = [[val for i,val in enumerate(row) if i not in roads_to_delete] for j,row in enumerate(roadRegister) if j not in roads_to_delete]
    print('Pruned')
    print_rr(res)
    for i in range(len(res)):
        res[i][i] = False
    print('Mirrored')
    print_rr(res)
    return res

roadRegister = [[False,True,False,True,True,True,False,False,False,True],
 [True,False,False,False,False,True,False,False,False,True],
 [False,False,False,True,True,True,False,False,True,True],
 [True,False,True,False,False,True,False,True,False,True],
 [True,False,True,False,False,True,False,True,False,True],
 [True,True,True,True,True,False,False,True,False,False],
 [False,False,False,False,False,False,False,False,False,False],
 [False,False,False,True,True,True,False,False,False,True],
 [False,False,True,False,False,False,False,False,False,False],
 [True,True,True,True,True,False,False,True,False,False]]
roadRegister2 = [[False,False,True,False,False,False,False,True,False,True],
 [False,False,True,True,False,True,True,False,False,True], 
 [True,True,False,True,False,True,False,True,False,False], 
 [False,True,True,False,False,True,True,False,False,True], 
 [False,False,False,False,False,True,True,False,False,True], 
 [False,True,True,True,True,False,False,False,False,False], 
 [False,True,False,True,True,False,False,False,True,True], 
 [True,False,True,False,False,False,False,False,False,False], 
 [False,False,False,False,False,False,True,False,False,True], 
 [True,True,False,True,True,False,True,False,True,False]]
print(mergingCities(roadRegister))


