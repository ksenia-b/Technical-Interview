from multiprocessing import Process, Queue

def f(q):
    q.put('Hello')
    q.put('Bye')
    q.put(None)

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    with open('../files/lines.txt', 'w') as fp:
        while True:
            item = q.get()
            print(item)
            if item is None:
                break
            fp.write(item)
    p.join()