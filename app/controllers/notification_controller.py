from flask import Blueprint, request
from app.services import NotificationService
from app.mapping import NotificationMap, MessageMap
from app.services import MessageBuilder

notification_bp = Blueprint('notification', __name__)

@notification_bp.route('/notification/<int:id>', methods=['GET'])
def get(id: int):
    notification = NotificationService.find(id)
    notification_map = NotificationMap()
    notification_data = notification_map.dump(notification)
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Notificación encontrada').add_data({'notification': notification_data}).build()
    message_map = MessageMap()
    return message_map.dump(message_finish), 200


@notification_bp.route('/notifications', methods=['GET'])
def get_all():
    notifications = NotificationService.find_all()
    notification_map = NotificationMap()
    notifications_data = notification_map.dump(notifications, many=True)
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Se encontraron todas las notificaciones').add_data({'notifications': notifications_data}).build()
    message_map = MessageMap()
    return message_map.dump(message_finish), 200


@notification_bp.route('/notifications', methods=['POST'])
def post():
    notification_map = NotificationMap()
    notification = notification_map.load(request.json)
    NotificationService.create(notification)
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Notificación creada').build()
    message_map = MessageMap()
    return message_map.dump(message_finish), 201


@notification_bp.route('/notifications/<int:id>', methods=['DELETE'])
def delete(id: int):
    notification = NotificationService.find(id)
    NotificationService.delete(id)
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message(f'Se eliminó la notificación {id}').build()
    message_map = MessageMap()
    return message_map.dump(message_finish), 200