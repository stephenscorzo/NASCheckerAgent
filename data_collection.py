import wmi
import socket
import psutil
import time
import uuid

def get_system_info():
    c = wmi.WMI()
    system_info = {}
    for os in c.Win32_OperatingSystem():
        system_info["OSName"] = os.Caption
        system_info["Version"] = os.Version
        system_info["Architecture"] = os.OSArchitecture
        # Add more system information as needed
    return system_info

def get_hard_drive_info():
    c = wmi.WMI()
    hard_drive_info = []
    for disk in c.Win32_DiskDrive():
        drive = {}
        drive["Model"] = disk.Model
        drive["Size"] = int(disk.Size) // (1024**3)  # Convert bytes to GB
        # Add more hard drive information as needed
        hard_drive_info.append(drive)
    return hard_drive_info

def get_hostname():
    return socket.gethostname()

def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

def get_uptime():
    uptime_seconds = int(time.time() - psutil.boot_time())
    return uptime_seconds

def get_mac_address():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2 * 6, 2)][::-1])
    return mac
