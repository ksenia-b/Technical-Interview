# from multiprocessing import Process, Queue
#
#
#
# def f(q):
#     q.put('Hello')
#     q.put('Bye')
#     q.put(None)
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     with open('../files/lines.txt', 'w') as fp:
#         while True:
#             item = q.get()
#             print(item)
#             if item is None:
#                 break
#             fp.write(item)
#     p.join()


#=======
from multiprocessing import Pool, Process, Queue
import os, time
# from Queue import Queue

def write(q):
    for v in ['A', 'B', 'C']:
        print('Put %s to queue ' % v)
        q.put_nowait(v)
        time.sleep(0.2)


def read(q):
    while 1:
        if not q.empty():
            v = q.get(True)
            print("Get %s from queue" % v)
            time.sleep(0.2)
        else:
            break

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))
    pw.start()
    pw.join()

    pr.start()
    pr.join()

    print("all done...")