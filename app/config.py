from pydantic import BaseSettings


class Settings(BaseSettings):
    package_file: str = "/var/lib/dpkg/status"  # Default value for ubuntu/debian only


settings = Settings()
