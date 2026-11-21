class ServiceDeskError(Exception):
    """Base exception for the Smart Service Desk application."""
    
class DuplicateRequestError(ServiceDeskError):
    """Raised when a request ID already exists."""
    
class RequestNotFoundError(ServiceDeskError):
    """Raised when the requested ID does not exist."""
    
class InvalidPriorityError(ServiceDeskError):
    """Raised when an unsupported priority is provided."""
    
class RequestAlreadyResolvedError(ServiceDeskError):
    """Raised when an already resolved request is resolved again."""
    
class RepositoryError(ServiceDeskError):
    """Raised when an error occurs during data storage operations."""
    
    
# ----------- Extension of the assignment given ---------------
class InvalidRequestIDError(ServiceDeskError):
    """Raised when a request ID does not follow the required format."""