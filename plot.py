import matplotlib.pyplot as plt
import numpy as np

'''
[
    ('rafiul-bucket-0', 'EU', 'test_1_9MB.pdf', '0:00:05'),
    ('rafiul-bucket-0', 'EU', 'test_3MB.pdf', '0:00:05')
    ('rafiul-bucket-0', 'EU', 'test_4_5MB.pdf', '0:00:07')

    ('rafiul-bucket-1', 'eu-west-1', 'test_1_9MB.pdf', '0:00:03')
    ('rafiul-bucket-1', 'eu-west-1', 'test_3MB.pdf', '0:00:03')
    ('rafiul-bucket-1', 'eu-west-1', 'test_4_5MB.pdf', '0:00:05')

    ('rafiul-bucket-2', 'us-west-1', 'test_1_9MB.pdf', '0:00:13')
    ('rafiul-bucket-2', 'us-west-1', 'test_3MB.pdf', '0:00:07')
    ('rafiul-bucket-2', 'us-west-1', 'test_4_5MB.pdf', '0:00:10')


]
'''

zones = ['EU', 'eu-west-1', 'us-west-1']

# data = [[1.9, 3.0, 4.5], [.05, .03, .13]]
# data = [[.05, .03, .13], [1.9, 3.0, 4.5]]
# data = [[.05, .05, .07], [1.9, 3.0, 4.5]]
data = [[1.9, 3.0, 4.5], [.05, .05, .07]]

# data1 = [[1.9, 3.0, 4.5], [0.5, .03, .13]]
# data1 = [[0.5, .03, .13], [1.9, 3.0, 4.5]]
# data1 = [[.03, .03, .05], [1.9, 3.0, 4.5]]
data1 = [[1.9, 3.0, 4.5], [.03, .03, .05]]

# data2 = [[1.9, 3.0, 4.5], [.07, .05, .10]]
# data2 = [[.07, .05, .10], [1.9, 3.0, 4.5]]
# data2 = [[0.13, 0.07, 0.10], [1.9, 3.0, 4.5]]
data2 = [[1.9, 3.0, 4.5], [0.13, 0.07, 0.10]]

# data2 = [[1.9, 3.0, 4.5], [[.05, .05, .07], [.03, .03, .05], [0.13, 0.07, 0.10]]]

data2 = [[1.9, 3.0, 4.5], [[4.0, 3.0, 13.0], [4.0, 3.0, 8.0], [5.0, 4.0, 10.0]]]

# plt.plot(data[0], data[1], data1[0], data1[1], data2[0], data2[1], antialiased=False)

plt.plot(data2[0], data2[1], antialiased=False)

# plt.plot(data1[0], data1[1])
# plt.plot(data2[0], data2[1])
plt.axis([0, 5, 0, 0.15])
plt.show()
# x = np.linspace(0, 10)
# line, = plt.plot(x, np.sin(x), '--', linewidth=2)
