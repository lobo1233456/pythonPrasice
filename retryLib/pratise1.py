import random

from gevent.tests.test__event import MyException
from tenacity import retry, stop_after_attempt, stop_after_delay, wait_fixed, wait_random, wait_exponential, \
    retry_if_result, retry_if_exception_type


@retry
def do_something_unreliable():
    if random.randint(0, 10) > 1:
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"

@retry
def never_give_up_never_surrender():
    print("Retry forever ignoring Exceptions, don't wait between retries")
    raise Exception
@retry(stop=stop_after_attempt(7))
def stop_after_7_attempts():
    print("Stopping after 7 attempts")
    raise Exception

@retry(stop=stop_after_delay(10))
def stop_after_10_s():
    print("Stopping after 10 seconds")
    raise Exception
@retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
def stop_after_10_s_or_5_retries():
    print("Stopping after 10 seconds or 5 retries")
    raise Exception
@retry(wait=wait_fixed(2))
def wait_2_s():
    print("Wait 2 second between retries")
    raise Exception
@retry(wait=wait_random(min=1, max=2))
def wait_random_1_to_2_s():
    print("Randomly wait 1 to 2 seconds between retries")
    raise Exception
@retry(wait=wait_exponential(multiplier=1, min=4, max=10))
def wait_exponential_1():
    print("Wait 2^x * 1 second between each retry starting with 4 seconds, then up to 10 seconds, then 10 seconds afterwards")
    raise Exception

def is_none_p(value):
    """Return True if value is None"""
    return value is None

@retry(retry=(retry_if_result(is_none_p) | retry_if_exception_type()))
def might_return_none():
    print("Retry forever ignoring Exceptions with no wait if return value is None")

def return_last_value(retry_state):
    """return the result of the last call attempt"""
    return retry_state.outcome.result()
def is_True(value):
    """Return True if value is False"""
    value = False
    if int(random.randint(0,10))==2:
        value = True
    return value

@retry(stop=stop_after_attempt(3),
    retry_error_callback=return_last_value,
       retry=retry_if_result(is_True))
def eventually_return_false():
    assert int(random.randint(0,10))==2


if __name__ == '__main__':
    list = []
    @retry(stop=stop_after_attempt(3))
    def raise_my_exception():
        assert int(random.randint(0, 10)) == 2
        # raise MyException("Fail")
    try:
        raise_my_exception()
    except Exception:
        list.append(False)
        pass
    else:
        list.append(True)
    print(list)


    # print(eventually_return_false())
