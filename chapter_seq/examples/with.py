with open('test_matrix.txt', 'r') as fin, \
     open('m.log', 'w') as fout:
    for line in fin:
        print(line, file=fout, end='')