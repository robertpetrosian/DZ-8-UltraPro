import time


class TimeException(Exception):
    '''
        class for raise exception
    '''


class CounterOfTime:
    '''
       counter of time
    '''

    def __init__(self):
        self._start_ = None

    def start(self):
        if self._start_ is None:
            self._start_ = time.perf_counter()
        else:
            raise TimeException('time counter was started')

    def stop(self):
        if self._start_ is not None:
            ret = time.perf_counter() - self._start_
            self._start_ = None
        else:
            raise TimeException("counter of time doesn't started")
        return ret

