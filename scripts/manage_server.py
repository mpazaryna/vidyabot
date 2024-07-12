# File: scripts/manage_server.py

import os
import subprocess
import sys

import psutil

PID_FILE = "server.pid"
LOG_FILE = "server.log"
SERVER_PORT = 8000


def find_server_process():
    for proc in psutil.process_iter(["pid", "name", "cmdline"]):
        if "Python" in proc.info["name"] and "start_server.py" in " ".join(
            proc.info["cmdline"]
        ):
            return proc
    return None


def start_server():
    existing_process = find_server_process()
    if existing_process:
        print(f"Server is already running with PID {existing_process.pid}.")
        return

    cmd = [sys.executable, "scripts/start_server.py"]

    process = subprocess.Popen(cmd, start_new_session=True)

    with open(PID_FILE, "w") as f:
        f.write(str(process.pid))
    print(
        f"Server started with PID {process.pid}. "
        f"Logs are being written to {LOG_FILE}"
    )


def stop_server():
    process = find_server_process()
    if not process:
        print("Server process not found. It may have already been stopped.")
        if os.path.exists(PID_FILE):
            os.remove(PID_FILE)
        return

    try:
        process.terminate()
        try:
            process.wait(timeout=10)
            print(f"Server with PID {process.pid} stopped.")
        except psutil.TimeoutExpired:
            print(
                f"Server with PID {process.pid} didn't stop gracefully. "
                "Forcing shutdown."
            )
            process.kill()
    except psutil.NoSuchProcess:
        print(f"Process with PID {process.pid} no longer exists.")
    finally:
        if os.path.exists(PID_FILE):
            os.remove(PID_FILE)
        print("PID file removed.")


def restart_server():
    stop_server()
    start_server()


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ["start", "stop", "restart"]:
        print("Usage: python manage_server.py [start|stop|restart]")
        sys.exit(1)

    action = sys.argv[1]
    if action == "start":
        start_server()
    elif action == "stop":
        stop_server()
    elif action == "restart":
        restart_server()


if __name__ == "__main__":
    main()
