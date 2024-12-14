from django.apps import AppConfig
import redis


class ImagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'images'

    def ready(self):
        import images.signals
        try:
            r = redis.Redis(host='localhost', port=6379, db=0)
            r.ping()
            print("Redis is connected!")
        except redis.exceptions.RedisError as e:
            print(f"Failed to connect to Redis: {e}")

