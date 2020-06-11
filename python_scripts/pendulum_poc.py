from datetime import datetime, timedelta
import pendulum

_timestamp = pendulum.instance(datetime.utcnow() - timedelta(microseconds=1)).to_rfc3339_string()
print(_timestamp)
