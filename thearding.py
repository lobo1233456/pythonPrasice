import multiprocessing
import os
import time
'''
    Process 类用来描述一个进程对象。创建子进程的时候，只需要传入一个执行函数和函数的参数即可完成 Process 示例的创建。  
    star() 方法启动进程，
    join() 方法实现进程间的同步，等待所有进程退出。
    close() 用来阻止多余的进程涌入进程池 Pool 造成进程阻塞。  
    multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)  
    target 是函数名字，需要调用的函数
    args 函数需要的参数，以 tuple 的形式传入
    pool.apply
    apply(func[, args[, kwds]])
    该方法只能允许一个进程进入池子，在一个进程结束之后，另外一个进程才可以进入池子。 
'''


def run_task(name):
    print('Task {0} pid {1} is running, parent id is {2}'.format(name, os.getpid(), os.getppid()))
    time.sleep(1)
    print('Task {0} end.'.format(name))

if __name__ == '__main__':
    print('current process {0}'.format(os.getpid()))
    p = multiprocessing.Pool(processes=3)
    for i in range(6):
        p.apply(run_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All processes done!')