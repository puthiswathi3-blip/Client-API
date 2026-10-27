
import requests


def fetch_post(post_id):
    """Fetch a post from a public REST API."""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        response = requests.get(url, timeout=10)

        # Check the HTTP status code
        response.raise_for_status()

        # Convert JSON response into Python data
        data = response.json()

        # Display selected information
        print("\n" + "=" * 40)
        print("           API RESPONSE")
        print("=" * 40)
        print(f"Post ID : {data['id']}")
        print(f"User ID : {data['userId']}")
        print(f"Title   : {data['title'].title()}")
        print(f"Content : {data['body']}")
        print("=" * 40)

    except requests.exceptions.Timeout:
        print("Error: The request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the server.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")

    except (ValueError, KeyError):
        print("Error: Unable to process the API response.")


def main():
    print("Welcome to the Simple API Client!")

    try:
        post_id = int(input("Enter a post ID (1-100): "))

        if not 1 <= post_id <= 100:
            print("Please enter a number between 1 and 100.")
            return

        fetch_post(post_id)

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
