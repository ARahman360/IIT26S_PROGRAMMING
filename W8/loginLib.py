"""Login and registration helpers for week 8, task 5."""
import hashlib

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def hashPassword(password: str) -> str:
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def readCredentials() -> list[str]:
    try:
        with open(CREDENTIALS_FILE, "r", encoding="utf-8") as file:
            return [row.strip() for row in file if row.strip()]
    except FileNotFoundError:
        return []


def register(username: str, password: str) -> int:
    rows = readCredentials()
    used_ids = [int(parts[0]) for row in rows
                if len(parts := row.split(DELIMITER)) == 3 and parts[0].isdigit()]
    user_id = max(used_ids, default=-1) + 1
    with open(CREDENTIALS_FILE, "a", encoding="utf-8") as file:
        file.write(f"{user_id}{DELIMITER}{username}{DELIMITER}{hashPassword(password)}\n")
    return user_id


def registerUser(username: str, password: str) -> None:
    register(username, password)


def viewProfile(username: str):
    for row in readCredentials():
        parts = row.split(DELIMITER)
        if len(parts) == 3 and parts[1] == username:
            return int(parts[0]), parts[1], parts[2]
    return None


def loginUser(username: str, password: str) -> int:
    profile = viewProfile(username)
    if profile is not None and profile[2] == hashPassword(password):
        return profile[0]
    return -1


def login(username: str, password: str) -> bool:
    return loginUser(username, password) != -1


def change_password(username: str, new_password: str) -> bool:
    rows = readCredentials()
    found = False
    for index, row in enumerate(rows):
        parts = row.split(DELIMITER)
        if len(parts) == 3 and parts[1] == username:
            rows[index] = DELIMITER.join((parts[0], parts[1], hashPassword(new_password)))
            found = True
            break
    if found:
        with open(CREDENTIALS_FILE, "w", encoding="utf-8") as file:
            for row in rows:
                file.write(row + "\n")
    return found
