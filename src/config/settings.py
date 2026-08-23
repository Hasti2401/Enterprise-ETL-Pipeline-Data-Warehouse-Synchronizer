from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    stripe_api_key: str

    salesforce_access_token: str
    salesforce_instance_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()