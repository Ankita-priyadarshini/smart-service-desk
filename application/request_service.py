from domain.service_request import ServiceRequest
from domain.exceptions import (
    DuplicateRequestError,
    RequestNotFoundError
)


class RequestService:
    # Handles the application-level operations of the service desk.

    def __init__(self, repository):
        self.repository = repository
        self.requests = self.repository.load_requests()

    def create_request(
        self,
        request_id,
        employee_name,
        issue,
        priority
    ):
        # Create and persist a new service request.

        if any(
            request.request_id == request_id
            for request in self.requests
        ):
            raise DuplicateRequestError(
                f"Request ID {request_id} already exists."
            )

        request = ServiceRequest(
            request_id,
            employee_name,
            issue,
            priority
        )

        self.requests.append(request)
        self.repository.save_requests(self.requests)

        return request

    def view_requests(self):
        # Return all service requests.
        return self.requests

    def search_request(self, request_id):
        # Find a request using its ID.

        for request in self.requests:
            if request.request_id == request_id:
                return request

        raise RequestNotFoundError(
            f"Request {request_id} was not found."
        )

    def resolve_request(self, request_id):
        # Resolve and persist a service request.

        request = self.search_request(request_id)
        request.resolve()

        self.repository.save_requests(self.requests)

        return request