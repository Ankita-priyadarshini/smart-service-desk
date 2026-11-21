from application.request_service import RequestService
from infrastructure.file_repository import FileRepository
from domain.exceptions import ServiceDeskError
from domain.exceptions import InvalidRequestIDError
from domain.service_request import ServiceRequest

def get_request_id(prompt):
    while True:
        request_id = input(prompt)
        
        try:
            return ServiceRequest._validate_request_id(request_id)
        except InvalidRequestIDError as error:
            print(f"Invalid input: {error}")
            print("Please try again.\n")

def display_menu():
    print("\n-_-_-_- SMART SERVICE DESK -_-_-_-")
    print("1. Create Service Request")
    print("2. View All Requests")
    print("3. Search Request")
    print("4. Resolve Request")
    print("5. Exit")


def main():
    service = RequestService(FileRepository())

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                request_id = get_request_id("Request ID (SR followed by 3 digits): ")
                employee = input("Employee Name: ")
                issue = input("Issue Description: ")
                priority = input("Priority (LOW/MEDIUM/HIGH): ")

                request = service.create_request(
                    request_id,
                    employee,
                    issue,
                    priority
                )

                print("\nRequest created successfully!")
                print(request.to_dict())

            elif choice == "2":
                requests = service.view_requests()

                if not requests:
                    print("\nNo service requests found.")
                else:
                    print("\n-_-_-_- All Service Requests -_-_-_-")

                    for request in requests:
                        print(request.to_dict())

            elif choice == "3":
                request_id = get_request_id("Enter Request ID: ")

                request = service.search_request(
                    request_id
                )

                print("\nRequest Found:")
                print(request.to_dict())

            elif choice == "4":
                request_id = get_request_id("Enter request ID to resolve: ")

                request = service.resolve_request(
                    request_id
                )

                print(
                    f"\nRequest {request.request_id} "
                    f"resolved successfully!"
                )

            elif choice == "5":
                print(
                    "Thank you for using Smart Service Desk!"
                )
                break

            else:
                print(
                    "Invalid choice. Please select 1-5."
                )

        except ServiceDeskError as error:
            print(f"\nError: {error}")

        except ValueError as error:
            print(f"\nInvalid input: {error}")


if __name__ == "__main__":
    main()