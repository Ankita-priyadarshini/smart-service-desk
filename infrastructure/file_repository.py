import json
from pathlib import Path

from domain.exceptions import RepositoryError
from domain.service_request import ServiceRequest


class FileRepository:
    # Handles reading and writing service requests to a JSON file.

    def __init__(self, file_path="data/requests.json"):
        self.file_path = Path(file_path)

    def load_requests(self):
        # Load service requests from the JSON file.
        # Returns: A list of ServiceRequest objects.

        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                content = file.read()
                
            if not content.strip():
                return []
            
            data = json.loads(content)

            if not isinstance(data, list):
                raise RepositoryError(
                    "Invalid data format: expected a JSON list."
                )

            return [
                ServiceRequest.from_dict(request_data)
                for request_data in data
            ]

        except json.JSONDecodeError as error:
            raise RepositoryError(
                "The JSON storage file contains invalid data."
            ) from error

        except (OSError, KeyError, TypeError, ValueError) as error:
            raise RepositoryError(
                f"Unable to load service requests: {error}"
            ) from error

    def save_requests(self, requests):
        # Save a list of service requests to the JSON file.

        try:
            self.file_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            data = [
                request.to_dict()
                for request in requests
            ]

            with self.file_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

        except (OSError, TypeError, ValueError) as error:
            raise RepositoryError(
                f"Unable to save service requests: {error}"
            ) from error