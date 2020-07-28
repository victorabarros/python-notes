from sqlalchemy import create_engine

dsn = "mysql+pymysql://vabarros:1234@172.17.0.255:3306/ota"
engine = create_engine(dsn, echo=True)

with engine.connect() as conn:
    cursor = conn.execute("SELECT 1;")

import pdb; pdb.set_trace()
