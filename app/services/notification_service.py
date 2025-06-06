from typing import List, Optional
from app.models import Notification
from app.repositories import NotificationRepository

class NotificationService:
    def __init__(self, repository: Optional[NotificationRepository] = None):
        self.repository = repository or NotificationRepository()
    
    @staticmethod
    def create(notification: Notification) -> Notification:
        return NotificationRepository.save(notification)
    
    @staticmethod
    def delete(notification_id: int) -> None:
        notification = NotificationService.find(notification_id)
        NotificationRepository.delete(notification)

    @staticmethod
    def find(id: int) -> Optional[Notification]:
        notification_service = NotificationRepository.find(id)
        if not notification_service:
            raise ValueError(f"Notificacion with ID {id} not found.")
        return notification_service
    
    @staticmethod
    def find_all() -> List[Notification]:
        return NotificationRepository.find_all()
    
    @staticmethod
    def find_by(**kwargs) -> List[Notification]:
        return NotificationRepository.find_by(**kwargs)

