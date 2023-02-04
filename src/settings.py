from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_prefix = "postgres_"
        env_file = ".env"
    driver: str = "postgresql+asyncpg"
    db: str
    user: str
    password: str
    host: str
    port: str
    
    echo: bool = False
    
    @property
    def database_uri(self):
        return f"{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"

class TestDatabseSettions(BaseSettings):
    class Config:
        env_prefix = "test_postgres_"
        env_file = ".env"
    driver: str = "postgresql+asyncpg"
    db: str
    user: str
    password: str
    host: str
    port: str
    
    echo: bool = False
    
    @property
    def database_uri(self):
        return f"{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"

settings = Settings()
test_database_settings = TestDatabseSettions()