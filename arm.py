import armconfig
import armconst
import armport_unix

class const:
    ARM_FSK_BROADCAST = 255
    ARM_FSK_POWER_AUTO = (-127)
    ARM_TIME_RESET = 10  # ms
    ARM_TIME_TIMEOUT = 20  # ms
    ARM_TIME_BACK_AT = 100 # ms
    ARM_TIME_BACK_SF_UPLINK_TIMEOUT = 10000  # 10sec
    ARM_TIME_BACK_SF_DOWNLINK_TIMEOUT = 45000  # 45sec
    ARM_TIME_BOOTING = 20  #ms
    ARM_NUMBER_OF_TRIALS_GO_AT = 35
    ARM_SIGFOX_PAYLOAD_MAX = 12
    ARM_SIGFOX_PAYLOAD_DOWNLINK = 8
    ARM_RF_PAYLOAD_MAX = 120
    ARM_MIN_CHANNEL = 1
    ARM_MAX_CHANNEL = 559
    ARM_MIN_RADIO_POWER = -18
    ARM_MAX_LONG_PREAMBLE_TIME = 900
    ARM_MAX_POST_TIME = 2550
    ARM_BASE_DEC = 10
    ARM_BASE_HEX = 16

    #def ARM_LW_UNCONFIRMED(self,val):
     #   return val*-1
    #def ARM_LW_IS_UNCONFIRMED(self,val):
     #   if val <= 0:
      #      return val
       # return 1


#typedef enum armError_e
#{
#	ARM_ERR_NONE,					//!< No error.
#	ARM_ERR_NO_SUPPORTED,			//!< Functionality no supported by the\b ARM.
#
#	ARM_ERR_PORT_OPEN,				//!< Port Error, at the port opening.
#	ARM_ERR_PORT_CONFIG,			//!< Port Error, at the port configuring.
#	ARM_ERR_PORT_READ,				//!< Port Error, at the port reading.
#	ARM_ERR_PORT_WRITE,				//!< Port Error, at the port writing.
#	ARM_ERR_PORT_WRITE_READ,		//!< Port Error, at the port reading/writing.
#	ARM_ERR_PORT_CLOSE,				//!< Port Error, at the port closing.
#
#	ARM_ERR_PARAM_OUT_OF_RANGE,		//!< Error, one or more of parameters is out of range.
#	ARM_ERR_PARAM_INCOMPATIBLE,		//!< Error, the parameters is incompatible between them.
#	ARM_ERR_ADDRESSING_NOT_ENABLE,	//!< Error, the addressing is not enable.
#									//!< \note To fix this error, you can enable the addressing with \ref armFskEnableAddressing() function.
#	ARM_ERR_WOR_ENABLE,				//!< Error, the WOR mode is enable.
#									//!< \note To fix this error, you can disable the WOR mode with \ref armFskSetWorMode() function.
#
#	ARM_ERR_ARM_GO_AT,				//!< \b ARM commend Error, can't switch to AT commend.
#	ARM_ERR_ARM_BACK_AT,			//!< \b ARM commend Error, can't quit AT commend.
#	ARM_ERR_ARM_CMD,				//!< \b ARM commend Error, from AT commend.
#	ARM_ERR_ARM_GET_REG,			//!< \b ARM commend Error, from get register.
#	ARM_ERR_ARM_SET_REG,			//!< \b ARM commend Error, from set register.
#}armError_t

# CONSTANT TO DEFINE BAUDRATE VALUE
class armBaudrate_t:
    ARMPORT_BAUDRATE_NONE = 0
    ARMPORT_BAUDRATE_1200 = 1200
    ARMPORT_BAUDRATE_2400 = 2400
    ARMPORT_BAUDRATE_4800 = 4800
    ARMPORT_BAUDRATE_9600 = 9600
    ARMPORT_BAUDRATE_19200 = 19200
    ARMPORT_BAUDRATE_38400 = 38400
    ARMPORT_BAUDRATE_57600 = 57600
    ARMPORT_BAUDRATE_115200 = 115200
    ARMPORT_BAUDRATE_230400 = 230400

class armFskWor_t:
    ARM_FSK_WOR_DISABLE = 0
    ARM_FSK_WOR_LP = 0
    ARM_FSK_WOR_CS = 0
    ARM_FSK_WOR_PQT = 0

class  armLed_t:
    ARM_LED_OFF = 0  # Led off all the time
    ARM_LED_OFF_RF = 0  # Led off on RF activity, on other times
    ARM_LED_ON_RF = 0  # Led on on RF activity, off other times

class armFskLbtAfa_t:
    ARM_FSK_LBTAFA_DISABLE = 0
    ARM_FSK_LBTAFA_LBT = 0 # Enable listen before talk
    ARM_FSK_LBTAFA_AFA = 0 # Enable adaptative frequenct agility
    ARM_FSK_LBTAFA_LBTAFA = 0 # Enable both

class armMode_t:
    ARM_MODE_FSK = 0  # Mode fsk
    ARM_MODE_SFX = 0  # Mode sigfox
    ARM_MODE_LORAWAN = 0  # Mode LoRaWAN

class armType_t:
    ARM_TYPE_NONE = 0x01  # No arm type
    ARM_TYPE_N8_LP = 0x02  # ARM nano in 868 MHZ low power version (sigfox also)
    ARM_TYPE_N8_LD = 0x04  # ARM nano in 868 MHz long distance version
    ARM_TYPE_N8_LW = 0x08  # ARM nano in 868 MHz LoRaWAN version

class uint128_t:  # might not be usefull
    lsb = 0
    msb = 0

class armReg_t:
    reg = 0  # Index  of register
    val = 0  # value of register
    newVal = 0  # new value of register

class armN8LpLd_t:
    regsH = [armReg_t] * armconst._ARM_N8LPLD_REGH_SIZE # diz is tricky aled
#typedef struct armN8LpLd_s
#{
#	armReg_t	regsH[_ARM_N8LPLD_REGH_SIZE];
#}armN8LpLd_t;

class armN8Lw_t:
    regsM = [armReg_t] * armconst._ARM_N8LW_REGM_SIZE
    regsO = [armReg_t] * armconst._ARM_N8LW_REGO_SIZE  # diz is tricky aled
#typedef struct armN8Lw_s
#{
#	armReg_t	regsM[_ARM_N8LW_REGM_SIZE];
#	armReg_t	regsO[_ARM_N8LW_REGO_SIZE];
#}armN8Lw_t;


##################################### begin of the class arm itself####################################################

class Arm:
    def __init__(self):
        self.port = 0
        self.type = 0

    def Init(self,port):
        self.type = armType_t.ARM_TYPE_NONE
        self.port = armport_unix.ArmPort(port)
        try:
            self.port.Open()
        except Exception as err:
            print("ERROR opening port " + err)
            return -1

        try:
            self.port.Config(armBaudrate_t.ARMPORT_BAUDRATE_19200,armport_unix.armPortDatabits_t.ARMPORT_DATA_8BITS,armport_unix.armPortParity_t.ARMPORT_PARITY_NO,armport_unix.armPortStopbit_t.ARM_STOPBIT_1)
        # default conf baudrate =19200,8bits of data, no parity, 1 bit stop
        except Exception as err:
            print("ERROR makin config " + err)
            return -1

        self.Reboot()

    def DeInit(self):
        try:
            self.port.close()
        except Exception as err:
            print("ERROR while closing port " + err)
            return -1
        self.type =armType_t.ARM_TYPE_NONE

    def Reboot(self):
        if armconfig.ARMPORT_WITH_nSLEEP:
            print("ERROR not implemented yet")
            exit(1)
        if armconfig.ARMPORT_WITH_nBOOT:
            print("ERROR not implemented yet")
            exit(1)
        if armconfig.ARMPORT_WITH_nRESET:
            print("ERROR not implemented yet")
            exit(1)
        # no need to reboot cuz inittialization ( type == ARM_TYPE_NONE)
        if self.type != armType_t.ARM_TYPE_NONE:
            if self._GoAt() == -1:
                print("ERROR GoAt")
                return -1

            # Reboot by "ATR" if ARM is already initialized/used
            if self.port.write("ATR\n"):
                print("ERROR writing on port")
                return -1
        #wait till booting
        self.port.delay(const.ARM_TIME_BOOTING)

        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(1)

        try:
            self.port.Config(armBaudrate_t.ARMPORT_BAUDRATE_19200,armport_unix.armPortDatabits_t.ARMPORT_DATA_8BITS,armport_unix.armPortParity_t.ARMPORT_PARITY_NO,armport_unix.armPortStopbit_t.ARM_STOPBIT_1)
        # default conf baudrate =19200,8bits of data, no parity, 1 bit stop
        except Exception as err:
            print("ERROR makin config " + err)
            return -1




