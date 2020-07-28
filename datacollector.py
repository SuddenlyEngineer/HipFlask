# Import a ton of features
import os
import psutil
import platform 
import subprocess
import json

def datacollector():   
    # First, let's determine our feature set and some basic information.
    basic_os = platform.system()
    #platform_info = platform.platform(terse=1)
    #full_os_info = os.uname()

    if basic_os == "Darwin":
        system_dictionary = mac_system_info()
        print(system_dictionary)
    elif basic_os == "Windows":
        system_dictionary = windows_system_info()
    return system_dictionary    

def mac_system_info(): #Pull system information.
    # First, let's build a file if one does not exist.
    if not os.path.isfile('system_info.json'):
        subprocess.run("system_profiler -detaillevel mini -json > system_info.json 2>/dev/null") #Redirect output to /dev/null to shut it up
    # Now let's load the JSON. Of course Apple's JSON is malformed.
    with open("system_info.json", encoding='utf-8', errors='ignore') as json_data:
        system_info = json.load(json_data, strict=False)
    # Schema is system_info[larger_data_set][0][secondary_item][0][tertiary_item]
    # Here is where the logic goes to build a standard python dictionary from system information
    simplified_dict = mac_dictionary_build(system_info, {})
    # Information returned: Network interfaces, 
    return simplified_dict

def mac_dictionary_build(system_info, simple_dict):
    simple_dict["AirPort MAC Address"] = system_info["SPAirPortDataType"][0]["spairport_airport_interfaces"][0]["spairport_wireless_mac_address"]
    
    return simple_dict

def mac_processes():
    pass

def windows_system_info():
    pass

def windows_processes():
    pass

def linux_system_info():
    pass

def linux_processes():
    pass

