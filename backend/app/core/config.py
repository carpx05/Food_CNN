from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Samudra Suraksha"
    PROJECT_VERSION: str = "0.1.0"
    ALLOWED_ORIGINS: list = ["*"]

    class Config:
        env_file = ".env"
        from_attr = True


settings = Settings()