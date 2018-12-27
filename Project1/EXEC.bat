Project1.exe a.py
cd src
python GenerateFuncClass.py
cd ../
cd ./rtl/build/classes
java  -noverify -cp . std.Start
cd ../../../