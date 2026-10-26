import hashlib

FILENAME = "credentials.txt"
DELIMITER = ";"


def hashPassword(PPassword: str) -> str:
    password_bytes = PPassword.encode("utf-8")
    return hashlib.md5(password_bytes).hexdigest()


def readCredentials() -> list[str]:
    rows: list[str] = []
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip() != "":
                    rows.append(line.strip())
    except FileNotFoundError:
        pass
    return rows


def registerUser(PUsername: str, PPassword: str) -> None:
    rows = readCredentials()
    number = len(rows)
    for row in rows:
        parts = row.split(DELIMITER)
        if int(parts[0]) >= number:
            number = int(parts[0]) + 1
    password_hash = hashPassword(PPassword)
    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write("{};{};{}\n".format(number, PUsername, password_hash))
    return None


def loginUser(PUsername: str, PPassword: str) -> int:
    password_hash = hashPassword(PPassword)
    for row in readCredentials():
        parts = row.split(DELIMITER)
        if len(parts) == 3:
            if parts[1] == PUsername and parts[2] == password_hash:
                return int(parts[0])
    return -1
