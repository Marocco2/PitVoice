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
Run %comspec% /c "play on.wav", , hide; add initial alarm rec
RunWait %comspec% /c "rec -c 1 sample.wav silence 1 0.1 3 1 3.0 3", , hide
RunWait %comspec% /c "play off.wav", , hide; add stop alarm rec
RunWait %comspec% /c "curl -s -XPOST https://api.wit.ai/speech?v=20141022 -L -H "Authorization: Bearer %token%" -H "Content-Type: audio/wav" --data-binary "@sample.wav" -o response.json", , hide
FileDelete, sample.wav
RunWait %comspec% /c "jq-win32.exe -r ".outcomes[].entities.tyre[].value" response.json > PitRaw.txt", , hide
FileReadLine, tiresr, PitRaw.txt, 1
if (tiresr = null)
  tiresr = NoChange
RunWait %comspec% /c "jq-win32.exe -r ".outcomes[].entities.number[].value" response.json > PitRaw.txt", , hide
FileReadLine, gasr, PitRaw.txt, 1
if (gasr = null)
  gasr = 0
RunWait %comspec% /c "jq-win32.exe -r ".outcomes[].entities.FixBody[].value" response.json > PitRaw.txt", , hide
FileReadLine, bodyr, PitRaw.txt, 1
if (bodyr = null)
  bodyr = no
RunWait %comspec% /c "jq-win32.exe -r "..outcomes[].entities.FixEngine[].value" response.json > PitRaw.txt", , hide
FileReadLine, enginer, PitRaw.txt, 1
if (enginer = null)
  enginer = no
RunWait %comspec% /c "jq-win32.exe -r ".outcomes[].entities.FixSuspension[].value" response.json > PitRaw.txt", , hide
FileReadLine, suspensionr, PitRaw.txt, 1
if (suspensionr = null)
  suspensionr = no
FileDelete, response.json
FileDelete, PitRaw.txt

tiresr = %tiresr%`r`n
gasr = %gasr%`r`n
bodyr = %bodyr%`r`n
enginer = %enginer%`r`n
suspensionr = %suspensionr%`r`n

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
    Click 713, 142

if compound = SuperSoft
    Click 842, 142

if compound = SoftSlick
    Click 979, 142

if compound = MediumSlick
    Click 1087, 142

if compound = HardSlick
    Click 1198, 142

if compound = SuperHard
    Click 1323, 142

if fuel >= 1
    MouseClick, left, 1061, 299,fuel

if yes = %body%
    Click 960, 467

if yes = %engine%
    Click 1204, 467

if yes = %suspension%
    Click 734, 466

Click 1115, 623
goto StartPV