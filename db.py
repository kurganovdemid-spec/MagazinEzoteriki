import s_taper
from s_taper.consts import *

scheme = {
    "ID": INT+KEY,
    "NAME": TEXT,
    "BALANCE": INT
}
users = s_taper.Taper("users", "data.db").create_table(scheme)