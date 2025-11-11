# KPS/vars.py

import os
from dotenv import load_dotenv
from typing import Set, Optional
from KPS.utils.logger import logger

# Load environment variables
load_dotenv("config.env")


def str_to_bool(val: str) -> bool:
    return val.lower() in ("true", "1", "t", "y", "yes")


def str_to_int_set(val: str) -> Set[int]:
    if not val:
        return set()
    result: Set[int] = set()
    for x in val.split():
        try:
            result.add(int(x))
        except (TypeError, ValueError):
            continue
    return result


class Var:
    # Required Telegram API
    API_ID: int = int(os.getenv("API_ID", "0"))
    API_HASH: str = os.getenv("API_HASH", "")
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")

    if not all([API_ID, API_HASH, BOT_TOKEN]):
        logger.critical("Missing required Telegram API configuration")
        raise ValueError("Missing required Telegram API configuration")

    # Bot info
    NAME: str = os.getenv("NAME", "vignesh-v2")
    SLEEP_THRESHOLD: int = int(os.getenv("SLEEP_THRESHOLD", "600"))
    WORKERS: int = int(os.getenv("WORKERS", "8"))

    # BIN_CHANNEL: accept numeric ID or URL
    BIN_CHANNEL_ENV = os.getenv("BIN_CHANNEL", "-1003293810900").strip()
    if not BIN_CHANNEL_ENV:
        logger.critical("BIN_CHANNEL is required")
        raise ValueError("BIN_CHANNEL is required")
    try:
        BIN_CHANNEL: int = int(BIN_CHANNEL_ENV)
    except ValueError:
        BIN_CHANNEL: str = BIN_CHANNEL_ENV  # fallback to string URL

    # FORCE_CHANNEL_ID: optional, numeric only
    FORCE_CHANNEL_ID: Optional[int] = None
    force_channel_env = os.getenv("FORCE_CHANNEL_ID", "-1003237212200").strip()
    if force_channel_env:
        try:
            FORCE_CHANNEL_ID = int(force_channel_env)
        except ValueError:
            logger.warning(
                f"Invalid FORCE_CHANNEL_ID '{force_channel_env}' in environment; must be a numeric ID like -1001234567890"
            )

    # Network / server
    PORT: int = int(os.getenv("PORT", "8080"))
    BIND_ADDRESS: str = os.getenv("BIND_ADDRESS", "0.0.0.0")
    PING_INTERVAL: int = int(os.getenv("PING_INTERVAL", "840"))
    NO_PORT: bool = str_to_bool(os.getenv("NO_PORT", "True"))

    # Owner info
    OWNER_ID: int = int(os.getenv("OWNER_ID", "0"))
    if not OWNER_ID:
        logger.warning("WARNING: OWNER_ID is not set. No user will be granted owner access.")
    OWNER_USERNAME: str = os.getenv("OWNER_USERNAME", "")

    # Public URL (use FQDN, not 0.0.0.0)
    FQDN: str = os.getenv("FQDN", "vignesh-v2.netlify.app")
    HAS_SSL: bool = str_to_bool(os.getenv("HAS_SSL", "True"))
    PROTOCOL: str = "https" if HAS_SSL else "http"
    PORT_SEGMENT: str = "" if NO_PORT else f":{PORT}"
    URL: str = f"{PROTOCOL}://{FQDN}{PORT_SEGMENT}/"

    # Bot commands
    SET_COMMANDS: bool = str_to_bool(os.getenv("SET_COMMANDS", "True"))

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    if not DATABASE_URL:
        logger.critical("DATABASE_URL is required")
        raise ValueError("DATABASE_URL is required")

    MAX_BATCH_FILES: int = int(os.getenv("MAX_BATCH_FILES", "50"))

    # Channels
    CHANNEL: bool = str_to_bool(os.getenv("CHANNEL", "False"))
    BANNED_CHANNELS: Set[int] = str_to_int_set(os.getenv("BANNED_CHANNELS", ""))

    MULTI_CLIENT: bool = False

    # Token system
    TOKEN_ENABLED: bool = str_to_bool(os.getenv("TOKEN_ENABLED", "False"))
    TOKEN_TTL_HOURS: int = int(os.getenv("TOKEN_TTL_HOURS", "24"))

    # URL shortener
    SHORTEN_ENABLED: bool = str_to_bool(os.getenv("SHORTEN_ENABLED", "False"))
    SHORTEN_MEDIA_LINKS: bool = str_to_bool(os.getenv("SHORTEN_MEDIA_LINKS", "False"))
    URL_SHORTENER_API_KEY: str = os.getenv("URL_SHORTENER_API_KEY", "")
    URL_SHORTENER_SITE: str = os.getenv("URL_SHORTENER_SITE", "")

    # Rate limiting
    GLOBAL_RATE_LIMIT: bool = str_to_bool(os.getenv("GLOBAL_RATE_LIMIT", "False"))
    MAX_GLOBAL_REQUESTS_PER_MINUTE: int = int(os.getenv("MAX_GLOBAL_REQUESTS_PER_MINUTE", "4"))
    RATE_LIMIT_ENABLED: bool = str_to_bool(os.getenv("RATE_LIMIT_ENABLED", "False"))
    MAX_FILES_PER_PERIOD: int = int(os.getenv("MAX_FILES_PER_PERIOD", "2"))
    RATE_LIMIT_PERIOD_MINUTES: int = int(os.getenv("RATE_LIMIT_PERIOD_MINUTES", "1"))
    MAX_QUEUE_SIZE: int = int(os.getenv("MAX_QUEUE_SIZE", "100"))

