# File: api/src/data/user_data.py

import json
import os
from typing import Any, Dict, List


def get_user_data() -> List[Dict[str, Any]]:
    """
    Retrieve user data from a JSON file.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries, where each dictionary
        represents a user with their associated data.

    Raises:
        Exception: If there's any error in reading or parsing the data.
    """
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the JSON file
    json_file_path = os.path.join(
        current_dir, "..", "..", "static_data", "user_data.json"
    )

    try:
        # Open and read the JSON file
        with open(json_file_path, "r") as file:
            data = json.load(file)

        # Return the list of users
        return data["users"]
    except FileNotFoundError:
        raise Exception(f"Error: The file {json_file_path} was not found.")
    except json.JSONDecodeError:
        raise Exception(f"Error: The file {json_file_path} contains invalid JSON.")
    except KeyError:
        raise Exception("Error: The 'users' key is missing in the JSON data.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        users = get_user_data()
        print("Retrieved users:", users)
    except Exception as e:
        print(f"Error: {str(e)}")
