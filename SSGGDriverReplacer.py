import os, subprocess, ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False   

def start():
    print("LilJess13's Sonar Driver Replacer")
    print("")
    location_answer = input("Is your SteelSeries GG installation in the default location? ex. (C:\\Program Files) - Y or N \n" )
    if location_answer.lower() == "n":
        install_dir = input("Please enter the file path to the folder containing the install. ex. (C:\\Users\\Desktop) \n")
        if install_dir.endswith("SteelSeries"):
            install_dir = install_dir[:-12]
        elif install_dir.endswith("SteelSeries\\"):
            install_dir = install_dir[:-13]
        install_dir += '\\SteelSeries\\GG\\apps\\sonar\\driver\\'
        if not os.path.exists(f"{install_dir}Sonar.DevInst.exe"):
            print("\n\nInvalid file path")
    elif location_answer.lower() == "y":
        install_dir = 'C:\\Program Files\\SteelSeries\\GG\\apps\\sonar\\driver\\'


    killtasks = [
    "taskkill /IM SteelSeriesGG.exe /T /F", 
    "taskkill /IM SteelSeriesGGMain.exe /T /F", 
    "taskkill /IM SteelSeriesEngine.exe /T /F", 
    "taskkill /IM SteelSeriesEngine3.exe /T /F", 
    "taskkill /IM SteelSeriesGGClient.exe /T /F", 
    "taskkill /IM SteelSeriesEngine3Client.exe /T /F", 
    "taskkill /IM SSOverlay.exe /T /F", 
    "taskkill /IM SteelSeriesEngine.exe /T /F", 
    "taskkill /IM gamesense-discord.exe /T /F", 
    "taskkill /IM gamesense-discord-x64.exe /T /F", 
    "taskkill /IM AudioSync.exe /T /F", 
    "taskkill /IM runStatsElevated.exe /T /F", 
    "taskkill /IM SteelSeriesCaptureSvc.exe /T /F", 
    "taskkill /IM moments.exe /T /F",
    "taskkill /IM SteelSeriesCVGameSense.exe /T /F",
    "taskkill /IM SteelSeriesSonar.exe /T /F",
    "taskkill /IM SteelSeriesPrismSync.exe /T /F",
    "sc stop SteelSeriesUpdateService",
    "sc delete SteelSeriesUpdateService"
    ]

    print("\n\nKilling all SteelSeries tasks")
    for task in killtasks:
        os.system(task)
    print("\n\nAll tasks killed")

    print("\n\nRemoving old driver components")
    print(f'''"{install_dir}Sonar.DevInst.exe" remove --device-hwid "ROOT\VEN_SSGG&DyEV_0001" --inf "{install_dir}vad\SteelSeries-Sonar-VAD-Extension.inf" --inf "{install_dir}vad\SteelSeries-Sonar-VAD.inf" --inf "{install_dir}apoDriverPackage\Sonar.Apo.inf" --catalog "SteelSeries.Sonar.VAD.cat" --catalog "SteelSeries.Sonar.VAD.Extension.cat''')
    subprocess.call(f'''"{install_dir}Sonar.DevInst.exe" remove --device-hwid "ROOT\VEN_SSGG&DEV_0001" --inf "{install_dir}vad\SteelSeries-Sonar-VAD-Extension.inf" --inf "{install_dir}vad\SteelSeries-Sonar-VAD.inf" --inf "{install_dir}apoDriverPackage\Sonar.Apo.inf" --catalog "SteelSeries.Sonar.VAD.cat" --catalog "SteelSeries.Sonar.VAD.Extension.cat''')
    os.system(f'rmdir "{install_dir}vad" /s /q')
    os.system(f'rmdir "{install_dir}driver" /s /q')
    print("\n\nOld driver components removed")

    print("\n\nInstalling older driver")
    subprocess.call(f'xcopy files\ "{install_dir}" /s /i')
    subprocess.call(f'''"{install_dir}Sonar.DevInst.exe" add --device-hwid "ROOT\VEN_SSGG&DEV_0001" --inf "{install_dir}driver\SteelSeries-Sonar-VAD-Extension.inf" --inf "{install_dir}driver\SteelSeries-Sonar-VAD.inf" --inf "{install_dir}apoDriverPackage\Sonar.Apo.inf"''')
    print("\n\nInstalled old driver successfully.")

    print("\n\n\n")
    input("All done! You should now be on the old driver. Press any key to exit")

if is_admin():
    start()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)