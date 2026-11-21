from domain.exceptions import (InvalidPriorityError, RequestAlreadyResolvedError)

class ServiceRequest:
    # Represents an IT support request raised by an user/employee.
    
    # Attributes include the below:
    # request_id: Unique key identifier for the request so raised.
    # employee_name: Name of the user/employee raising the request.
    # issue: Description of the raised issue.
    # priority: Priority assigned to the request.
    # status: Current status of the request

    
    VALID_PRIORITIES = {"LOW", "MEDIUM", "HIGH"}
    VALID_STATUSES = {"OPEN", "RESOLVED"}
    
    def __init__(self, request_id, employee_name, issue, priority):
        self.request_id = self._validate_text(request_id, "Request ID")
        self.employee_name = self._validate_text(employee_name, "Employee name")
        self.issue = self._validate_text(issue, "Issue description")
        self.priority = self._validate_priority(priority)
        self._status = "OPEN"
        
    @staticmethod
    def _validate_text(value, field_name):
        # Validate that a required text field is not empty.
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} cannot be empty.")
        
        return value.strip()
    
    @classmethod
    def _validate_priority(cls, priority):
        # Validate and normalise the priority of the request
        if not isinstance(priority, str):
            raise InvalidPriorityError("Priority must be LOW, MEDIUM or HIGH")
        
        priority = priority.strip().upper()
        
        if priority not in cls.VALID_PRIORITIES:
            raise InvalidPriorityError("Priority must be LOW, MEDIUM or HIGH")
        
        return priority
    
    @property
    def status(self):
        return self._status
    
    def resolve(self):
        # Mark an open request as resolved 
        if self._status == "RESOLVED":
            raise RequestAlreadyResolvedError(f"Request {self.request_id} is already resolved.")
        
        self._status = "RESOLVED"
        
    def to_dict(self):
        # Convert the request into a dictionary format
        return {
            "request_id": self.request_id,
            "employee_name": self.employee_name,
            "issue": self.issue,
            "priority": self.priority,
            "status": self._status
        }
        
    @classmethod
    def from_dict(cls, data):
        # Create a request from a dictionary
        request = cls(
            request_id=data["request_id"],
            employee_name=data["employee_name"],
            issue=data["issue"],
            priority=data["priority"]
        )
        
        status = data["status"]
        
        if status not in cls.VALID_STATUSES:
            raise ValueError(f"Invalid request statu: {status}")
        
        request._status = status
        
        return request