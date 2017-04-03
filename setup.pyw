from cx_Freeze import setup, Executable

exe = Executable(
    script = "PriorityList.pyw",
    targetName = "PriorityList.exe",
    icon = "1491253525_list-alt.ico"
    )

setup(
    name = "PriorityList.exe",
    version = "1.0",
    description = "Create a prioritized list",
    executables = [exe]
    )
