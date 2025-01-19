import pymem
from pymem.process import module_from_name
import threading
import time

# download game here: https://github.com/assaultcube/AC/releases/tag/v1.2.0.2
# make sure to pip install pymem
# Initialize global variables
writing_enabled = False
stop_writing_event = threading.Event()

try:
    # Initialize Pymem and the game module
    pm = pymem.Pymem("ac_client.exe")
    game_module = module_from_name(pm.process_handle, "ac_client.exe").lpBaseOfDll
except pymem.exception.ProcessNotFound as e:
    print("Could not find process: Game not open or installed")
    exit()
except Exception as e:
    print(f"Unexpected error: {e}")
    exit()


# Function to get pointer address
def get_ptr_addr(base, offsets):
    addr = pm.read_int(base)  # my addr is 44439536
    for offset in offsets[:-1]:
        addr = pm.read_int(addr + offset)
    return addr + offsets[-1]


# Function to get pointers
def get_ptrs():
    health_ptr = get_ptr_addr(game_module + 0x00109B74, [0xF8])
    default_gun_ptr = get_ptr_addr(game_module + 0x0010A280, [0x08, 0x790, 0x34, 0xA4, 0x4E0])
    armor_ptr = get_ptr_addr(game_module + 0x0010A280, [0x08, 0xAD4, 0x34, 0x34, 0xA4, 0x3E4])
    grenades_ptr = get_ptr_addr(game_module + 0x00109B74, [0x158])
    pistol_ptr = get_ptr_addr(game_module + 0x0010A280, [0x08, 0xC4, 0x45C])
    dual_pistols_ptr = get_ptr_addr(game_module + 0x0010A280, [0x08, 0xA58, 0x34, 0xA4, 0x34, 0x444])
    # tuple for pointers and their descriptions
    ptrs = (
        ("Health Pointer", health_ptr),
        ("Default Gun Pointer", default_gun_ptr),
        ("Armor Pointer", armor_ptr),
        ("Grenades Pointer", grenades_ptr),
        ("Pistol Pointer", pistol_ptr),
        ("Dual_Pistols Pointer", dual_pistols_ptr)
    )
    return ptrs


# Function to write value in a loop
def infinite_write(hack_ptrs):
    while not stop_writing_event.is_set():
        if writing_enabled:
            for name, ptr in hack_ptrs:
                try:
                    pm.write_int(ptr, 100)
                except pymem.exception.MemoryWriteError as e:
                    print(f"Game closed: Error in main execution: {e}")
                    return
                except Exception as e:
                    print(f"Error in main execution: {e}")
                    return
        time.sleep(0.1)  # Prevent high CPU usage


# Function to toggle writing
def toggle_writing():
    global writing_enabled
    while True:
        input("Press Enter to toggle infinite writing...")
        writing_enabled = not writing_enabled
        print(f"Infinite writing {'enabled' if writing_enabled else 'disabled'}.")


if __name__ == '__main__':
    try:
        ptrs = get_ptrs()
        # Start the writing thread
        writing_thread = threading.Thread(target=infinite_write, args=(ptrs,))
        writing_thread.start()
        # Start the input listener thread
        toggle_thread = threading.Thread(target=toggle_writing)
        toggle_thread.start()
    except Exception as e:
        print(f"Error in main execution: {e}")
