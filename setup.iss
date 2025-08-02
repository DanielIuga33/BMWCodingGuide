[Setup]
AppName=BMW Coding Guide
AppVersion=1.0
DefaultDirName={pf}\BMW Coding Guide
DefaultGroupName=BMW Coding Guide
OutputDir=output
OutputBaseFilename=BMW_Coding_Guide_Setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\BMW_Coding_Guide\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "data\icon_bmw.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "data\*"; DestDir: "{app}\data"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\BMW Coding Guide"; Filename: "{app}\BMW_Coding_Guide.exe"
Name: "{userdesktop}\BMW Coding Guide"; Filename: "{app}\BMW_Coding_Guide.exe"; IconFilename: "{app}\icon_bmw.ico"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Creează shortcut pe desktop"; GroupDescription: "Opțiuni:"
