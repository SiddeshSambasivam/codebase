import requests
import time


def synchronous_func():

    def download_site(url, session):
        with session.get(url) as response:
            print(f"Read {len(response.content)} from {url}")

    def download_all_sites(sites: list):
        with requests.Session() as session:
            for url in sites:
                download_site(url, session)

    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")


def threading_func(num_workers):

    import concurrent.futures
    import threading

    thread_local = threading.local()

    def get_session():
        if not hasattr(thread_local, "session"):
            thread_local.session = requests.Session()

        return thread_local.session

    def download_site(url):
        session = get_session()
        with session.get(url) as response:
            # print(f"Read {len(response.content)} from {url}")
            pass

    def download_all_sites(sites):

        with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
            executor.map(download_site, sites)

    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time

    print(
        f"With {num_workers} workers: Downloaded {len(sites)} in {duration} seconds")


if __name__ == "__main__":
    # synchronous_func() # Downloaded 160 sites in 30.00775 seconds
    for i in range(1, 10):
        threading_func(i)
    # num_workers = 1 => 30.004
    # num_workers = 2 => 15.9275
    # num_workers = 3 => 8.3080
    # num_workers = 4 =>
