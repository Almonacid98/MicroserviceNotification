class Route():

    def init_app(self, app):
        from app.controllers import notification_bp
        
        app.register_blueprint(notification_bp, url_prefix='/api/v1')
