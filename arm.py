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

    def ARM_LW_UNCONFIRMED(self,val):
        return val*-1
    def ARM_LW_IS_UNCONFIRMED(self,val):
        if val <= 0:
            return 1
        return 0


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
    ARM_LED_OFF_RF = 1  # Led off on RF activity, on other times
    ARM_LED_ON_RF = 2  # Led on on RF activity, off other times

class armFskLbtAfa_t:
    ARM_FSK_LBTAFA_DISABLE = 0
    ARM_FSK_LBTAFA_LBT = 1 # Enable listen before talk
    ARM_FSK_LBTAFA_AFA = 2 # Enable adaptative frequenct agility
    ARM_FSK_LBTAFA_LBTAFA = 3 # Enable both

class armMode_t:
    ARM_MODE_FSK = 0  # Mode fsk
    ARM_MODE_SFX = 0  # Mode sigfox
    ARM_MODE_LORAWAN = 1  # Mode LoRaWAN

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
        if armconfig.ARM_WITH_N8_LPLD:
            print("Not implemented yet")
            exit(-1)
        if armconfig.ARM_WITH_N8_LW:
            self.N8LW = armN8Lw_t

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
            if self.GoAt() == -1:
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
        if self.info(self.type):
            print("ERROR info")
            return -1

        if armconfig.ARM_WITH_N8_LW:
            # we gonna init the register M, dirty, we need a function to do it
            self.N8LW.regsM[armconst._ARM_N8LW_IREGM_CONFIGURATION].reg = armconst._ARM_N8LW_REGM_CONFIGURATION
            self.N8LW.regsM[armconst._ARM_N8LW_IREGM_LOW_POWER].reg = armconst._ARM_N8LW_REGM_LOW_POWER
            self.N8LW.regsM[armconst._ARM_N8LW_IREGM_LED].reg = armconst._ARM_N8LW_REGM_LED

            # we gonna init the register O, dirty, we need a function to do it
            self.N8LW.regsO[armconst._ARM_N8LW_IREGO_TXRX2_SF].reg = armconst._ARM_N8LW_REGO_TXRX2_SF
            self.N8LW.regsO[armconst._ARM_N8LW_IREGO_POWER].reg = armconst._ARM_N8LW_REGO_POWER
            self.N8LW.regsO[armconst._ARM_N8LW_IREGO_TXRX2_CHANNEL].reg = armconst._ARM_N8LW_REGO_TXRX2_CHANNEL
            self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIRMED_FRAME].reg = armconst._ARM_N8LW_REGO_CONFIRMED_FRAME
            self.N8LW.regsO[armconst._ARM_N8LW_IREGO_PORT_FIELD].reg = armconst._ARM_N8LW_REGO_PORT_FIELD
            self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].reg = armconst._ARM_N8LW_REGO_CONFIG

            # Go to AT command for get register
        if self.GoAt() == -1:
            print("ERROR GoAt")
            return -1

        if armconfig.ARM_WITH_N8_LW:
            i = 0
            # read all M register from ARM
            while i < armconst._ARM_N8LW_REGM_SIZE:
                # kinda C++ syntax might be modified
                # TODO LATER
                if self.GetReg('M',self.N8LW.regsM[i].reg,self.N8LW.regsM[i].val):
                    print("ERROR gettin regM")
                    return -1
                self.N8LW.regsM[i].newVal = self.N8LW.regsM[i].val
                i +=1

            i = 0
            while i < armconst._ARM_N8LW_REGO_SIZE:
                if self.GetReg('M',self.N8LW.regsO[i].reg,self.N8LW.regsO[i].val):
                    print("ERROR gettin regO")
                    return -1
                self.N8LW.regsO[i].newVal = self.N8LW.regsM[i].val
                i += 1

            if armconfig.ARMPORT_WITH_nSLEEP:
                print("ERROR not implemented yet")
                exit(1)
            else:
                # disable wake up on the sleep pin
                self.N8LW.regsM[armconst._ARM_N8LW_IREGM_LOW_POWER].newVal &= ~armconst._ARM_N8LW_REGM_LOW_POWER_ENABLE

        #backAt
        if self.BackAt():
            print("ERROR back AT")
            return -1

        return self.UpdateConfig()

    # return a list with [armType,rev,sn,_rfFreq,_rfPower]
    # return -1 if error

    def info(self,rev,sn,rfFreq,rfPower):

        armType = armType_t.ARM_TYPE_NONE
        _rfFreq = -1
        _rfPower = -1
        buf = ""

        # get type, rev and sn from 'ATV' command

        if self.type == armType_t.ARM_TYPE_NONE or rev or sn:
            # go AT command
            if self.GoAt():
                print("ERROR Go AT")
                return -1
            if self.WriteRead("ATV\n", buf, const.ARM_TIME_TIMEOUT): # buf might not work should return it m8be
                print("ERROR PORT WRITE READ")
                return -1
            # quit AT command
            if self.BackAt():
                print("ERROR BACK AT")
                return -1
            #search LoRa
            if buf.find("LoRa",len(buf)):
                armType = armType_t.ARM_TYPE_N8_LW
                _rfFreq = 868
                _rfPower = armconst._ARM_N8LW_MAX_POWER
            else:
                # Is 868 Mhz
                if buf.find("868MHZ",len(buf)):
                    _rfFreq = 868
                # Is LP
                if buf.find("14DBM",len(buf)):
                    _rfPower = armconst._ARM_N8LPLD_LP_MAX_POWER
                    armType = armType_t.ARM_TYPE_N8_LP
                else: # LD
                    _rfPower = armconst._ARM_N8LPLD_LD_MAX_POWER
                    armType = armType_t.ARM_TYPE_N8_LD

            if rev:  # Get ARM firmware revision
                if armconfig.ARM_WITH_N8_LPLD:
                    print("ERROR Not implemented yet")
                    exit(-1)
                if armconfig.ARM_WITH_N8_LW:
                    if armType & armconfig.ARM_WITH_N8_LW:
                        index = buf.find("Rev:", len(buf))
                        index =+ 4
                        while buf[index] != ' ' or buf[index] != '\n' or buf[index] != '\0':
                            rev += buf[index]
                            index += 1
                        rev += '\0'

            if sn:  # Get ARM serial number
                if armconfig.ARM_WITH_N8_LPLD:
                    print("ERROR Not implemented yet")
                    exit(-1)
                if armconfig.ARM_WITH_N8_LW:
                    if armType & armconfig.ARM_WITH_N8_LW:
                        index = buf.find("S/N:", len(buf))
                        index += 4
                        while buf[index] != ' ' or buf[index] != '\n' or buf[index] != '\0':
                            sn += buf[index]
                            index +=1
                        sn += '\0'
        else:
            armType = self.type  # get type from ARM type
            if armType&(armType_t.ARM_TYPE_N8_LP|armType_t.ARM_TYPE_N8_LD|armType_t.ARM_TYPE_N8_LW):
                _rfFreq = 868

            # get power from ARM type
            if armType&(armType_t.ARM_TYPE_N8_LP|armType_t.ARM_TYPE_N8_LW):
                _rfPower = armconst._ARM_N8LPLD_LP_MAX_POWER
            elif armType&(armType_t.ARM_TYPE_N8_LD):
                _rfPower = armconst._ARM_N8LPLD_LD_MAX_POWER

        # we gonna return all settings, not sure reference work so return data aswell on a list

        config=[armType,rev,sn,_rfFreq,_rfPower]
        self.type = armType
        rfFreq = _rfFreq
        rfPower = _rfPower

        return config
    # set the mode
    # u need to call UpdateConfig to update the parameters in your ARM
    # not usefull for LoRa

    def SetMode(self,mode):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                if mode == armMode_t.ARM_MODE_LORAWAN:
                    return 0

        return -1

    # get the mode
    # return the mode FSK by default

    def GetMode(self):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                return armMode_t.ARM_MODE_LORAWAN

        return armMode_t.ARM_MODE_FSK

    # Enable disable down link, not used by LW
    def SfxEnableDownlink(self,enable):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1

    # check if sigfox downlink is enable
    # not used by LW
    def SfxIsEnableDownlink(self):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1
    # Get the maximal possible power
    # not used by LW
    def FskMaxPower(self,radiochannel,radiobaud):
        print("ERROR not implemented yet")
        return -1

    # setup fsk local radio configuration
    # not used by LW
    def FskSetRadio(self,channel,baud,power):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1

    # get the radio config
    # return a list [channel,baud,power]
    # not use by LW
    def FskGetRadio(self):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1
    # set the radio remote address
    # not used by LW
    def FskSetRemoteAdd(self,add):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1
    # Get the remote addr
    # return 255 if not supported mean nothing
    # not used by LW
    def FskGetRemoteAdd(self):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return 255

    # Set the radio local address
    # not used by LW
    def FskSetLocalAdd(self,add):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1

    # Get the radio local add
    #not used by LW
    def FskGetLocalAdd(self):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1

    # Enable local addressing
    # not used by LW
    def FskEnableAddressing(self,enable):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1

    # not used by LW
    def FskIsEnableAddressing(self):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1

    # enable disable crc
    # not used by LW
    def FskEnableCrc(self,enable):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1

    def FskIsEnableCrc(self):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1

    # enable disable infinty mode
    # not used by LW
    def FskEnableIfinityMode(self,enable):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1

    def FskIsEnableInfinityMode(self):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1
    # not used by LW
    def FskEnableWhitening(self,enable):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1

    def FskIsEnableWhitening(self):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1

    # setup serial port config
    # not used by LW
    def SetSerial(self,baud,databits,parity,stopbits):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1
    # return a list [baud,databits,parity,stopbits]
    # not used by LW
    def GetSerial(self):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1
    # enable and configure Wake On Radio mode
    # not used by LW
    def FskSetWorMode(self,mode,periodTime,postTime,rssiLevel,filterLongPreamble):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1
    # return a list [mode,periodTime,postTime,rssiLevel,filterLongPreamble]
    # not used by LW
    def FskGetWorMode(self):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1
    # enable wake up by uart/serie
    # not used by LW
    def EnableWakeUpUart(self,enable):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1

    def IsEnableWakeUpUart(self):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1

    # Enable and configure the Lbt&Afa mode
    # not used by LW
    def FskSetLbtAfaMode(self,mode,rssiLevel,nSamples,channel2):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1

    # return a list [mode,rssiLevel,nSamples,channel2]
    # not used by LW
    def FskGetLbtAfaMode(self):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        else:
            print("ERROR Not supported")
            return -1

    def SetLed(self,led):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)
        if armconfig.ARM_WITH_N8_LW:
            if self.type&armType_t.ARM_TYPE_N8_LW:
                self.N8LW.regsM[armconst._ARM_N8LW_IREGM_LED].newVal |= armconst._ARM_N8LW_REGM_LED_BOOT | armconst._ARM_N8LW_REGM_LED_WAKEUP  | armconst._ARM_N8LW_REGM_LED_RADIO_TX | armconst._ARM_N8LW_REGM_LED_RADIO_RX | armconst._ARM_N8LW_REGM_LED_DEFAULT_STATE

                if led == armLed_t.ARM_LED_OFF:
                    self.N8LW.regsM[armconst._ARM_N8LW_IREGM_LED].newVal &= ~(armconst._ARM_N8LW_REGM_LED_BOOT | armconst._ARM_N8LW_REGM_LED_WAKEUP | armconst._ARM_N8LW_REGM_LED_RADIO_TX | armconst._ARM_N8LW_REGM_LED_RADIO_RX)
                elif led == armLed_t.ARM_LED_OFF_RF:
                    self.N8LW.regsM[armconst._ARM_N8LW_IREGM_LED].newVal &= ~(armconst._ARM_N8LW_REGM_LED_DEFAULT_STATE)
                elif led == armLed_t.ARM_LED_ON_RF:
                    pass
                else:
                    print("Error wrong parameter led, 0, 1 , 2")
                    return -1
        return 0

    def GetLed(self):
        if armconfig.ARM_WITH_N8_LPLD:
            print("ERROR not implemented yet")
            exit(-1)

        if armconfig.ARM_WITH_N8_LW:
            if not self.N8LW.regsM[armconst._ARM_N8LW_IREGM_LED].newVal&armconst._ARM_N8LW_REGM_LED_DEFAULT_STATE:
                return armLed_t.ARM_LED_OFF_RF
            if self.N8LW.regsM[armconst._ARM_N8LW_IREGM_LED].newVal&(armconst._ARM_N8LW_REGM_LED_BOOT | armconst._ARM_N8LW_REGM_LED_WAKEUP | armconst._ARM_N8LW_REGM_LED_RADIO_TX | armconst._ARM_N8LW_REGM_LED_RADIO_RX):
                return armLed_t.ARM_LED_ON_RF

        return armLed_t.ARM_LED_OFF

    def LwSetRadio(self,txChannel,power,txSf,rx2Sf,rx2Channel):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                if txChannel > 9:
                    print("ERROR parameters tx channel out of range")
                    return -1
                if txSf and ((txSf < 7) or (txSf > 12)):
                    print("ERROR parameters txSf out of range")
                    return -1
                if rx2Sf and ((rx2Sf < 7) or (rx2Sf > 12)):
                    print("ERROR parameters rx2sf out of range")
                    return -1
                if rx2Channel > 9:
                    print("ERROR parameters rx2channel out of range")
                    return -1

                if power:
                    regPower = self.N8LW.regsO[armconst._ARM_N8LW_IREGO_POWER].newVal  # line 1511
                    regPower &= ~0x07

                    if power == 2:
                        regPower |= armconst._ARM_N8LW_REGO_POWER_2
                    if power == 5:
                        regPower |= armconst._ARM_N8LW_REGO_POWER_5
                    if power == 8:
                        regPower |= armconst._ARM_N8LW_REGO_POWER_8
                    if power == 11:
                        regPower |= armconst._ARM_N8LW_REGO_POWER_11
                    if power == 14:
                        regPower |= armconst._ARM_N8LW_REGO_POWER_14
                    else:
                        print("ERROR power out of range")
                        return -1
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_POWER].newVal = regPower
                    # disable Tx adaptative speed
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal &= ~armconst._ARM_N8LW_REGO_CONFIG_ADAPTIVE_SPEED
                    # set txChannel ?

                if txChannel:
                    txChannel -= 1
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_TXRX2_CHANNEL].newVal &= ~0x0f
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_TXRX2_CHANNEL].newVal |= txChannel
                    # set parameters
                    # disable adaptative channel
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal &= ~armconst._ARM_N8LW_REGO_CONFIG_ADAPTIVE_CHANNEL
                # set txSf ?
                if txSf:
                    # set parameters
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_TXRX2_SF].newVal &= ~0x07
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_TXRX2_SF].newVal |= 12-txSf
                    # disable tx adaptative speed
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal &= ~armconst._ARM_N8LW_REGO_CONFIG_ADAPTIVE_SPEED
                # set rx2sf ?
                if rx2Sf:
                    # set parameters
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_TXRX2_SF].newVal &= ~(0x07<<3)
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_TXRX2_SF].newVal |= ((12-rx2Sf)<<3)
                    #disable rx2 adaptative speed
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal &= ~armconst._ARM_N8LW_REGO_CONFIG_ADAPTIVE_RX2
                # set rx2Channel
                if rx2Channel:
                    rx2Channel -=1
                    # set parameters
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_TXRX2_CHANNEL].newVal &= ~0xf0
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_TXRX2_CHANNEL].newVal |= rx2Channel<<4
                    # disable rx2 adaptative speed
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal &= ~armconst._ARM_N8LW_REGO_CONFIG_ADAPTIVE_RX2

                return 0
        print("ERROR not supported")
        return -1

    # return a list [txChannel,power,txSf,rx2Sf,rx2Channel]
    # only for LW

    def LwGetRadio(self,txChannel,power,txSf,rx2Sf,rx2Channel):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:

                # get txChannel
                if txChannel:
                    txChannel = self.N8LW.regsO[armconst._ARM_N8LW_IREGO_TXRX2_CHANNEL].newVal&0x0f
                    txChannel += 1

                # Get power
                if power:
                    if self.N8LW.regsO[armconst._ARM_N8LW_IREGO_POWER].newVal&0x07 == armconst._ARM_N8LW_REGO_POWER_14:
                        power = 14
                    if self.N8LW.regsO[armconst._ARM_N8LW_IREGO_POWER].newVal&0x07 == armconst._ARM_N8LW_REGO_POWER_11:
                        power = 11
                    if self.N8LW.regsO[armconst._ARM_N8LW_IREGO_POWER].newVal&0x07 == armconst._ARM_N8LW_REGO_POWER_8:
                        power = 8
                    if self.N8LW.regsO[armconst._ARM_N8LW_IREGO_POWER].newVal&0x07 == armconst._ARM_N8LW_REGO_POWER_5:
                        power = 5
                    if self.N8LW.regsO[armconst._ARM_N8LW_IREGO_POWER].newVal&0x07 == armconst._ARM_N8LW_REGO_POWER_2:
                        power = 2
                    else:
                        power = 0

                # Get txSf
                if txSf:
                    txSf = self.N8LW.regsO[armconst._ARM_N8LW_IREGO_TXRX2_SF].newVal&0x07
                    txSf = 12-(txSf)
                # Get rx2sf
                if rx2Sf:
                    rx2Sf = ((self.N8LW.regsO[armconst._ARM_N8LW_IREGO_TXRX2_SF].newVal)>>3)&0x07
                    rx2Sf = 12-(rx2Sf)
                # Get rx2Channel
                if rx2Channel:
                    rx2Channel = ((self.N8LW.regsO[armconst._ARM_N8LW_IREGO_TXRX2_CHANNEL].newVal)>>4)&0x07
                    rx2Channel += 1

                radio = [txChannel, power, txSf, rx2Sf, rx2Channel]
                return radio
        return -1

    def LwSetConfirmedFrame(self,nbFrame):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                if nbFrame > 15 or nbFrame < -15:
                    print("ERROR nbframe out of range")
                    return -1

                if const.ARM_LW_IS_UNCONFIRMED(nbFrame):
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIRMED_FRAME].newVal = const.ARM_LW_UNCONFIRMED(nbFrame)
                else:
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIRMED_FRAME].newVal = nbFrame<<4
                return 0
        return -1

    def LwGetConfirmedFrame(self):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                if (self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIRMED_FRAME].newVal)&0x0f:  # is unconfirmed ?
                    return const.ARM_LW_UNCONFIRMED(self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIRMED_FRAME].newVal)
                else:
                    return (self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIRMED_FRAME].newVal)>>4

            return -1
        return  -1

    def LwSetPortField(self,port):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                self.N8LW.regsO[armconst._ARM_N8LW_IREGO_PORT_FIELD].newVal = port
            return -1
        return -1

    def LwGetPortField(self):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                return self.N8LW.regsO[armconst._ARM_N8LW_IREGO_PORT_FIELD].newVal
            return -1
        return -1

    def LwEnableOtaa(self,enable):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                if enable:
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal |= armconst._ARM_N8LW_REGO_CONFIG
                    return 0
                else:
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal &= ~armconst._ARM_N8LW_REGO_CONFIG
                    return 0
            return -1
        return -1

    def LwIsEnableOtaa(self):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                if self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal&armconst._ARM_N8LW_REGO_CONFIG_OTAA:
                    return 1
                else:
                    return 0
            return -1
        return -1

    def LwEnableRxWindows(self,enable):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                if enable:
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal |= armconst._ARM_N8LW_REGO_CONFIG_RX_ON
                else:
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal &= ~armconst._ARM_N8LW_REGO_CONFIG_RX_ON
            return -1
        return -1

    def LwIsEnableRxWindows(self):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                if self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal&armconst._ARM_N8LW_REGO_CONFIG_RX_ON:
                    return 1
                else:
                    return 0
            return -1
        return 1

    def LwEnableTxAdaptativeSpeed(self,enable):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                if enable:
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal |= armconst._ARM_N8LW_REGO_CONFIG_ADAPTIVE_SPEED
                    return 0
                else:
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal &= ~armconst._ARM_N8LW_REGO_CONFIG_ADAPTIVE_SPEED
                    return 0
            return -1
        return -1

    def LwIsEnableTxAdaptativeSpeed(self):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                if self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal&armconst._ARM_N8LW_REGO_CONFIG_ADAPTIVE_SPEED:
                    return 1
                else:
                    return 0
            return -1
        return -1

    def LwEnableDutyCycle(self,enable):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                if enable:
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal |= armconst._ARM_N8LW_REGO_CONFIG_DUTY_CYCLE
                    return 0
                else:
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal &= ~armconst._ARM_N8LW_REGO_CONFIG_DUTY_CYCLE
                    return 0
            return -1
        return-1


    def LwIsEnableDutyCycle(self):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                if self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal&armconst._ARM_N8LW_REGO_CONFIG_DUTY_CYCLE:
                    return 1
                else:
                    return 0
            return -1
        return -1

    def LwEnableTxAdaptativeChannel(self,enable):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                if enable:
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal |= armconst._ARM_N8LW_REGO_CONFIG_ADAPTIVE_CHANNEL
                    return 0
                else:
                    self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal &= ~armconst._ARM_N8LW_REGO_CONFIG_ADAPTIVE_CHANNEL
                    return 0
            return -1
        return-1

    def LwIsEnableTxAdaptativeChannel(self):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                if self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal&armconst._ARM_N8LW_REGO_CONFIG_ADAPTIVE_CHANNEL:
                    return 1
                else:
                    return 0
            return -1
        return -1


    def LwEnableRx2Adaptative(self,enable):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                if enable:
                    self.N8LW.regsO[
                        armconst._ARM_N8LW_IREGO_CONFIG].newVal |= armconst._ARM_N8LW_REGO_CONFIG_ADAPTIVE_RX2
                    return 0
                else:
                    self.N8LW.regsO[
                        armconst._ARM_N8LW_IREGO_CONFIG].newVal &= ~armconst._ARM_N8LW_REGO_CONFIG_ADAPTIVE_RX2
                    return 0
            return -1
        return -1

    def LwIsEnableRx2Adaptative(self):
        if armconfig.ARM_WITH_N8_LW:
            if self.type == armType_t.ARM_TYPE_N8_LW:
                if self.N8LW.regsO[armconst._ARM_N8LW_IREGO_CONFIG].newVal&armconst._ARM_N8LW_REGO_CONFIG_ADAPTIVE_RX2:
                    return 1
                else:
                    return 0
            return -1
        return -1

    def LwIds(self,devAddr,devEui,appEui,appKey,nwkSKey,appSKey):
























































