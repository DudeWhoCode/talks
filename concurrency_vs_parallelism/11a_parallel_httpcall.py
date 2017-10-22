import multiprocessing
import time
import urllib.request

URI = 'https://api.bf4stats.com/api/onlinePlayers?output=json'
MAX_CLIENTS = 500


def fetch_sync(pid):
    print('Fetch sync process {} started'.format(pid))
    start = time.time()
    response = urllib.request.urlopen(URI)
    datetime = response.getheader('Date')
    with open(str(pid) + '.out', 'w') as f:
        f.write(datetime)
    print('Process {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start))

    return datetime


def synchronous():
    start = time.time()
    jobs = []
    for i in range(1, MAX_CLIENTS + 1):
        p = multiprocessing.Process(target=fetch_sync, args=(i,))
        jobs.append(p)
        p.start()
    print("TOTAL TIME TAKEN : {:.2f} seconds".format(time.time() - start))


print('Fetching urls parallely : \n')
synchronous()