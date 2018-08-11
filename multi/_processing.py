from multiprocessing.dummy import Pool


def foo(inputs):
    print(inputs[0])

threads_limit = 3
parameters = [["thread 1 inputs"], ["thread 2 inputs"]]
thread_pool = Pool(threads_limit)
results = thread_pool.map(foo, parameters)


