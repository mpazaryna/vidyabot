# File: api/src/data/user_data.py

import json
import os
from typing import Any, Dict, List


def get_user_data() -> List[Dict[str, Any]]:
    """
    Retrieve user data from a JSON file.

    This function reads user data from a JSON file located in the 'static_data'
    directory. The file should contain a 'users' key with an array of user
    objects.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries, where each dictionary
        represents a user with their associated data.

    Raises:
        FileNotFoundError: If the user_data.json file is not found.
        json.JSONDecodeError: If the file contains invalid JSON.
        KeyError: If the 'users' key is missing from the JSON data.

    Note:
        If any error occurs during the process, an empty list is returned and
        an error message is printed to the console.
    """
    # Get the directory of the api folder
    api_dir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    # Construct the path to the JSON file
    json_file_path = os.path.join(api_dir, "static_data", "user_data.json")

    try:
        # Open and read the JSON file
        with open(json_file_path, "r") as file:
            data = json.load(file)

        # Return the list of users
        return data["users"]
    except FileNotFoundError:
        print(f"Error: The file {json_file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {json_file_path} contains invalid JSON.")
        return []
    except KeyError:
        print(f"Error: The file {json_file_path} is missing a 'users' key.")
        return []


# Example usage
if __name__ == "__main__":
    users = get_user_data()
    print("Retrieved users:", users)
