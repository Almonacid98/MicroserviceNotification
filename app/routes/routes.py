class Route():

    def init_app(self, app):
        from app.controllers import notifications_bp
        
        app.register_blueprint(notifications_bp, url_prefix='/api/v1')
