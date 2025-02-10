def log_message(message: str, type: str = "INFO") -> None:
    """
    Logs a message with a specified type to the terminal.

    Args:
        message (str): The message to log.
        type (str): The message type (e.g., "INFO", "WARNING", "ERROR"). Defaults to "INFO".

    Returns:
        None: The function does not return anything; it prints the log to the terminal.
    """
    prefix = f"[{type.upper()}]"
    print(f"{prefix} {message}")
