import pymem
import pymem.exception
import pymem.process
import settings




def Get_Ammo():
    try:
        pm = pymem.Pymem(process_name=settings.GAME_EXECUTABLE)
        process_id = pymem.process.module_from_name(process_handle=pm.process_handle, module_name=settings.GAME_EXECUTABLE).lpBaseOfDll
        # Read the value at the memory location
        print(hex(0x00000011 * 4 + 0x00b4d6d0))
        #print(hex(pm.base_address + 0x0a99ae64 + 0x905a4d + 0x74D714 + 0x41e44))
    except pymem.exception.ProcessNotFound:
        print(f"Process not found!")

    except Exception as e:
        print(f"Error: {e}")


def Get_Score():
    try:
        pm = pymem.Pymem(process_name=process)
        process_id = pymem.process.module_from_name(process_handle=pm.process_handle, module_name=process).lpBaseOfDll

        # Read the value at the memory location
        value = pm.read_int(settings.SCORE)
        print(f"Value at {hex(settings.SCORE)}: {value}")
       
    except pymem.exception.ProcessNotFound:
        print(f"Process {process} not found!")

    except Exception as e:
        print(f"Error: {e}")



def AddAmmo(quantity):
    try:
        pm = pymem.Pymem(process_name=process)
        module = pymem.process.module_from_name(process_handle=pm.process_handle, module_name=process).lpBaseOfDll
        ammo = pm.base_address+settings.BASEOFFSET
        

        # Write the value at the memory location
        try:
            pm.write_int(ammo+settings.AMMOOFFSET, quantity)
        except Exception as e:
            print(f"Error: {e}")

    except pymem.exception.ProcessNotFound:
        print(f"Process {process} not found!")

    except Exception as e:
        print(f"Error: {e}")

def AddScore(quantity):
    try:
        pm = pymem.Pymem(process_name=process)
        process_id = pymem.process.module_from_name(process_handle=pm.process_handle, module_name=process).lpBaseOfDll

        # Write the value at the memory location
        try:
            currentScore = pm.read_int(settings.SCORE)
            pm.write_int(settings.SCORE, quantity + currentScore)
        except Exception as e:
            print(f"Error: {e}")

    except pymem.exception.ProcessNotFound:
        print(f"Process {process} not found!")

    except Exception as e:
        print(f"Error: {e}")


def Get_Health():
    try:
        pm = pymem.Pymem(process_name=process)
        process_id = pymem.process.module_from_name(process_handle=pm.process_handle, module_name=process).lpBaseOfDll

        # Read the value at the memory location
        value = pm.read_short(settings.HEALTH)
        print(f"Value at {hex(settings.HEALTH)}: {value}")

    except pymem.exception.ProcessNotFound:
        print(f"Process {process} not found!")

    except Exception as e:
        print(f"Error: {e}")

def AddHealth(quantity):
    try:
        pm = pymem.Pymem(process_name=process)
        process_id = pymem.process.module_from_name(process_handle=pm.process_handle, module_name=process).lpBaseOfDll

        # Write the value at the memory location
        try:
            currentHealth = pm.read_short(settings.HEALTH)
            pm.write_short(settings.HEALTH, quantity + currentHealth)
        except Exception as e:
            print(f"Error: {e}")

    except pymem.exception.ProcessNotFound:
        print(f"Process {process} not found!")

    except Exception as e:
        print(f"Error: {e}")