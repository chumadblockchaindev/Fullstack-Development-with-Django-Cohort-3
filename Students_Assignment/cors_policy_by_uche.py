# CORS POLICY 

# The **CORS Policy**, which stands for **Cross-Origin Resource Sharing**, is a security mechanism implemented by web browsers to regulate how a web page 
# in one "origin" can request and interact with resources from a different "origin."

# Here's a breakdown of what that means:

# 1.  **Same-Origin Policy (SOP):** By default, web browsers enforce a strict security measure called the **Same-Origin Policy**. 
# This policy dictates that a script on a web page can only request data from the same origin that served the web page. 
# An "origin" is defined by the combination of the **protocol** (e.g., `http` or `https`), **domain** (e.g., `example.com`), 
# and **port** (e.g., `80` or `443`). If any of these three are different, it is a *cross-origin* request, and the browser will typically block it 
# for security reasons.

# 2.  **Why CORS is Needed:** In modern web development, it's very common for a frontend application (e.g., running on `app.com`) 
# to need to fetch data from a backend API on a different domain (e.g., running on `api.com`). CORS is a standard mechanism that safely relaxes the 
# Same-Origin Policy to allow these valid cross-origin requests.

# 3.  **How it Works (HTTP Headers):**
#     * CORS is an **HTTP-header based mechanism**.
#     * When a browser makes a cross-origin request, it includes an `Origin` header with the domain of the requesting page.
#     * The server hosting the resource must then respond with a special CORS header, primarily **`Access-Control-Allow-Origin`**, 
#        which tells the browser whether the request is permitted.
#     * If the server's response includes the correct CORS headers authorizing the request's origin, the browser allows the request to succeed and 
#       lets the script access the data. Otherwise, the browser blocks the response, and a "CORS error" is logged in the console.

# 4.  **The "Policy":** The **CORS Policy** is essentially the configuration on the **server-side** that specifies which external origins
#  (domains, protocols, and ports), HTTP methods (GET, POST, etc.), and headers are allowed to access its resources.

# 5.  **Preflight Requests:** For complex requests (like those using HTTP methods other than `GET`, `HEAD`, or `POST`, or using custom headers), 
# the browser will automatically send an extra **"preflight"** request using the **`OPTIONS`** method *before* the actual request. 
# This check determines the server's CORS capabilities to ensure the actual request is safe to send.




# ASYNC PROGRAMMING

# Asynchronous programming (often called async programming) in Python is a way to write programs that can do multiple things at once — without blocking 
# the execution or waiting for one task to finish before starting another.

# Let’s break it down simply and clearly:

# 1. **Synchronous vs. Asynchronous:**
#    - In **synchronous programming**, tasks are performed one after the other. If one task takes a long time (like waiting for a file to download or a web request to complete),
#      the entire program waits (or "blocks") until that task is done before moving on to the next one.

# Example of synchronous code:
# The problem with this code is that it waits for `fetch_data()` to complete before moving on to the next line.

import time

def fetch_data():
    print("Fetching data...")
    time.sleep(3)  # pretend to wait for a slow network call
    print("Data fetched!")

def main():
    fetch_data()
    print("Done!")

main()

# In this example, the program waits for `fetch_data()` to complete before printing "Done!".


# The Solution: Asynchronous Code
# With async programming, you can start a slow task (like downloading or fetching data) and do something else while waiting for it to finish —
# instead of blocking the program.
# This is done using the `async` and `await` keywords in Python, along with an event loop that manages these tasks.

# Example of asynchronous code:

import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(3)  # non-blocking wait
    print("Data fetched!")

async def main():
    # Run tasks concurrently
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(fetch_data())

    await task1
    await task2
    print("Done!")

asyncio.run(main())
# In this example, `fetch_data()` is defined as an asynchronous function using the `async` keyword.
# The `await` keyword is used to pause the function until the awaited task is complete, but it doesn't block the entire program.
# Instead, the event loop can run other tasks while waiting.



# | Concept         | Description                                                                 |
# | --------------- | --------------------------------------------------------------------------- |
# | `async def`     | Declares an asynchronous function.                                          |
# | `await`         | Pauses the function until the awaited task completes.                       |
# | `asyncio`       | The built-in Python module that handles asynchronous tasks and event loops. |
# | `create_task()` | Starts a task that runs in the background.                                  |
# | `run()`         | Starts the event loop and runs the main asynchronous function.              |


# Benefits of Asynchronous Programming:
# - **Efficiency**: It allows your program to handle many tasks at once, making better use of time and resources.
# - **Responsiveness**: In applications like web servers, async programming helps keep the application responsive to user requests while performing background tasks.
# - **Concurrency**: It enables concurrent execution of tasks, which is especially useful for I/O-bound operations (like network requests or file operations).
# - **Scalability**: Async programming can help applications scale better under load, as they can handle more simultaneous operations without needing more threads or processes.
# In summary, asynchronous programming in Python allows you to write code that can perform multiple tasks at the same time without blocking, making your applications more efficient and responsive.


# Benefits of Async Programming:
# Network requests (APIs, web scraping)
# Database queries
# File I/O or slow operations
# Chat servers or bots

# Not good for:
# Heavy CPU tasks (e.g., image processing, big calculations)


# Analogy
# Think of async like a restaurant kitchen:
# The chef (your program) doesn’t wait for the soup to boil.
# While the soup simmers, they start preparing another dish.
# When the soup is ready, they finish it up.
# That’s asynchronous multitasking — efficient and fast!