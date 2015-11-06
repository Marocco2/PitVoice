#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance ignore

StartPV:

FileReadLine, key, HotKey.txt, 1
Hotkey, %key%, Wit
Loop {
FileReadLine, pitbutton, PitButton.txt, 1
pitbutton = %pitbutton%
if pitbutton = 1
    goto Pit
}
return

Wit:

token = DFSRHY2TSAWFHWSF6IYP5LLM2GCEMX3E
RunWait %comspec% /c "setx AUDIODRIVER waveaudio", , hide
Run %comspec% /c "sox\play on.wav", , hide; add initial alarm rec
RunWait %comspec% /c "sox\rec -c 1 sample.wav silence 1 0.1 3 1 3.0 3", , hide
RunWait %comspec% /c "sox\play off.wav", , hide; add stop alarm rec
RunWait %comspec% /c "curl -s -XPOST https://api.wit.ai/speech?v=20141022 -L -H "Authorization: Bearer %token%" -H "Content-Type: audio/wav" --data-binary "@sample.wav" -o response.json", , hide
FileDelete, sample.wav
RunWait %comspec% /c "jq-win32.exe -r ".entities.tyre | .[].value.value" response.json > PitRaw.txt", , hide
FileReadLine, tiresr, PitRaw.txt, 1
RunWait %comspec% /c "jq-win32.exe -r ".entities.number | .[].value.value" response.json > PitRaw.txt", , hide
FileReadLine, gasr, PitRaw.txt, 1
RunWait %comspec% /c "jq-win32.exe -r ".entities.FixBody | .[].value.value" response.json > PitRaw.txt", , hide
FileReadLine, bodyr, PitRaw.txt, 1
RunWait %comspec% /c "jq-win32.exe -r ".entities.FixEngine | .[].value.value" response.json > PitRaw.txt", , hide
FileReadLine, enginer, PitRaw.txt, 1
RunWait %comspec% /c "jq-win32.exe -r ".entities.FixSuspension | .[].value.value" response.json > PitRaw.txt", , hide
FileReadLine, suspensionr, PitRaw.txt, 1
FileDelete, response.json
FileDelete, PitRaw.txt

if tiresr = 
  tiresr = NoChange
if gasr = 
  gasr = 0
if bodyr = 
  bodyr = no
if enginer = 
  enginer = no
if suspensionr = 
  suspensionr = no

tiresr = %tiresr%`r`n
gasr = %gasr%`r`n
bodyr = %bodyr%`r`n
enginer = %enginer%`r`n
suspensionr = %suspensionr%`r`n

FileDelete, Pit.txt
PitFile = %A_WorkingDir%\Pit.txt
f := FileOpen(PitFile, "w")
f.Write(tiresr)
f.Write(gasr)
f.Write(bodyr)
f.Write(enginer)
f.Write(suspensionr)
f.Close() 

return

Pit:

FileReadLine, tires, Pit.txt, 1
FileReadLine, gas, Pit.txt, 2
FileReadLine, body, Pit.txt, 3
FileReadLine, engine, Pit.txt, 4
FileReadLine, suspension, Pit.txt, 5

compound = %tires%
fuel = %gas%
yes = yes

if compound = NoChange
    Click 1033, 142

if compound = SuperSoft
    Click 1183, 142

if compound = SoftSlick
    Click 1295, 142

if compound = MediumSlick
    Click 1406, 142

if compound = HardSlick
    Click 1518, 142

if compound = SuperHard
    Click 1631, 142

if fuel >= 1
    MouseClick, left, 1379, 299,fuel

if yes = %body%
    Click 1280, 467

if yes = %engine%
    Click 1523, 467

if yes = %suspension%
    Click 1053, 466

Click 1437, 623
goto StartPV