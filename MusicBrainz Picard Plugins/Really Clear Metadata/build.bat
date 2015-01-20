@echo off

for %%f in (src/rcm/ui/*.ui) do call pyuic4 -o src/rcm/ui/%%~nf.py src/rcm/ui/%%f

python -m compileall src

pylupdate4 -verbose rcm.pro
