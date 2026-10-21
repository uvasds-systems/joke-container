[![Publish](https://github.com/uvasds-systems/joke-container/actions/workflows/publish-container.yml/badge.svg)](https://github.com/uvasds-systems/joke-container/actions/workflows/publish-container.yml)

# Joke Container

A simple demo of a containerized application. This project isn't a joke! ;^)

The image bundles a fixed Python version (3.13) and pinned dependencies (`requirements.txt`), so the app runs the same way on any machine with Docker. Nothing needs to be installed on the host.

## Build and run

```bash
docker build -t joke-container .
docker run --rm joke-container
```
The app fetches a random joke from the [Official Joke API](https://official-joke-api.appspot.com/random_joke), prints the setup, waits 3 seconds, then prints the punchline.
