#!/usr/bin/python3
"""
Module for consuming and processing data from an API using Python.
Fetches posts from JSONPlaceholder, prints titles, and saves post data to CSV.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print:
    - Status code
    - Titles of all posts (if request is successful)
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print("Status Code: {}".format(response.status_code))

    # If the request was successful, status code 200
    if response.status_code == 200:
        data = response.json()  # Parse JSON

        # Print titles of all posts
        for post in data:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch posts and save id, title, and body into posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Only continue if request succeeded
    if response.status_code == 200:
        data = response.json()

        # Create list of dictionaries
        posts_list = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in data
        ]

        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_list)
