if not defined in_subprocess (cmd /k set in_subprocess=y ^& %0 %*) & exit )
set projectLocation=C:\Users\udit\Desktop\Connector\MSFS_Connector
cd %projectLocation%
python Connector.py
