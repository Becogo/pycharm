from pya2l import DB

db = DB()
session = db.open_existing("ASAP2_Demo_V161")   # No need to specify extension .a2ldb
