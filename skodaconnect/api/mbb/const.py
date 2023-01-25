"""MBB Client constants"""
BRAND = "Skoda"
COUNTRY = "CZ"
SCOPES = "sc2:fal"
SYSTEM_ID = "MBB"
XCLIENT = "fef89b3d-a6e0-4525-91eb-a9436e6e469a" # Used in Android app 5.2.7
XNAME = "cz.skodaauto.connect"
XVERSION = "5.3.0"

SHORTTERM = "shortTerm"
LONGTERM = "longTerm"
CYCLIC = "cyclic"
LIST = "list"
NEWEST = "newest"
FROM = "from"
REQUESTS = "requests"
JOBSTATUS = "jobstatus"
SETSETTINGS = "setSettings"
MAXCURRENT = "maxChargeCurrent"

APP_LOCKXML = "application/vnd.vwg.mbb.RemoteLockUnlock_v1_0_0+xml"
APP_RSJSON = "application/vnd.vwg.mbb.RemoteStandheizung_v2_0_2+json"

MBBOAUTH2 = "https://mbboauth-1d.prd.ece.vwg-connect.com/mbbcoauth/mobile/oauth2"
GARAGE_URL = "https://msg.volkswagen.de/fs-car/usermanagement/users/v1/{BRAND}/{COUNTRY}/vehicles"
HOME_URL = "https://mal-1a.prd.ece.vwg-connect.com/api/cs/vds/v1/vehicles/{VIN}/homeRegion"
BASE_URL = "https://msg.volkswagen.de/api"
OPER_LIST = "rolesrights/operationlist/v3/vehicles/{VIN}"
STATUS_URL = "fs-car/bs/vsr/v1/{BRAND}/{COUNTRY}/vehicles/{VIN}"
TRIP_URL = "fs-car/bs/tripstatistics/v1/{BRAND}/{COUNTRY}/vehicles/{VIN}/tripdata"
POS_URL = "fs-car/bs/cf/v1/{BRAND}/{COUNTRY}/vehicles/{VIN}/position"
TIMER_URL = "fs-car/bs/departuretimer/v1/{BRAND}/{COUNTRY}/vehicles/{VIN}/timer"
CLIMATE_URL = "fs-car/bs/climatisation/v1/{BRAND}/{COUNTRY}/vehicles/{VIN}/climater"
CHARGE_URL = "fs-car/bs/batterycharge/v1/{BRAND}/{COUNTRY}/vehicles/{VIN}/charger"
AUX_URL = "fs-car/bs/rs/v1/{BRAND}/{COUNTRY}/vehicles/{VIN}"
HNF_URL = "fs-car/bs/rhf/v1/{BRAND}/{COUNTRY}/vehicles/{VIN}/honkAndFlash"
LOCK_URL = "fs-car/bs/rlu/v1/{BRAND}/{COUNTRY}/vehicles/{VIN}"

# S-PIN URLs
SPIN_LOCK = '/api/rolesrights/authorization/v2/vehicles/{VIN}/services/rlu_v1/operations/LOCK/security-pin-auth-requested'
SPIN_UNLOCK =  '/api/rolesrights/authorization/v2/vehicles/{VIN}/services/rlu_v1/operations/UNLOCK/security-pin-auth-requested'
SPIN_AUX = '/api/rolesrights/authorization/v2/vehicles/{VIN}/services/rheating_v1/operations/P_QSACT/security-pin-auth-requested'
SPIN_TIMER = '/api/rolesrights/authorization/v2/vehicles/{VIN}/services/timerprogramming_v1/operations/P_SETTINGS_AU/security-pin-auth-requested'
SPIN_CLIMA = '/api/rolesrights/authorization/v2/vehicles/{VIN}/services/rclima_v1/operations/P_START_CLIMA_AU/security-pin-auth-requested'