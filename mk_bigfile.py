


print('reading file')
with open('oneGb.csv') as f:
    data = f.read()

print('writing data to file...')
with open('bigfile.csv', 'w') as g:
    g.write(data)

for i in range(10):  #range(n) = [0, 1, 2, n-1]
    print('writing more data to file...' + str(i))
    with open('bigfile.csv', 'a') as g:
        g.write(data)
