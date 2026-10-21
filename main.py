import httpx
import time

JOKE_URL = "https://official-joke-api.appspot.com/random_joke"

def tell_me_a_joke():
    # fetch a joke from the joke api
    response = httpx.get(JOKE_URL, timeout=10)
    response.raise_for_status()
    joke = response.json()

    # present the setup to stdout
    print(joke["setup"], flush=True)

    # sleep for 3
    time.sleep(3)

    # deliver the punchline to stdout
    print(joke["punchline"], flush=True)

if __name__ == "__main__":
    tell_me_a_joke()