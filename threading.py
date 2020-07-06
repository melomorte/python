from threading import Thread
import time

def faz_algo(i):
	time.sleep(3)
print('finalizando a thread %d' %i)

for i in range(5):
	t = thread(target = faz_algo, args=(i,))
	t.start()