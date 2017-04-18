import armconfig
import termios
import select
import time

# CONSTANT TO DEFINE BAUDRATE VALUE
class armPortBaudrate_t:
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


# const to define parity type


# const to define data bits value
class armPortDatabits_t:
    ARMPORT_DATA_7BITS = 7
    ARMPORT_DATA_8BITS = 8


# const to define the number of stop bits
class armPortStopbit_t:
    ARM_STOPBIT_1 = 1
    ARM_STOPBIT_2 = 2

class armPortParity_t:
    ARMPORT_PARITY_NO = 0
    ARMPORT_PARITY_ODD = 1
    ARMPORT_PARITY_EVEN = 2

# NOT USED TODO LATER
# if defined ARMPORT_WITH_nSLEEP || defined ARMPORT_WITH_nBOOT || defined ARMPORT_WITH_nRESET || __DOXYGEN__
# /*!	\brief Constant to define the pins.
# * \ingroup group_port
# *
# */
# typedef enum armPortPin_e
# {
# if defined ARMPORT_WITH_nSLEEP || __DOXYGEN__
#	ARMPORT_PIN_nSLEEP,		//!< nSLEEP pin.
# endif
# if defined ARMPORT_WITH_nBOOT || __DOXYGEN__
#	ARMPORT_PIN_nBOOT,		//!< nBOOT pin
# endif
# if defined ARMPORT_WITH_nRESET || __DOXYGEN__
#	ARMPORT_PIN_nRESET,		//!< nRESET pin.
# endif


# }armPortPin_t;
# endif


class ArmPort():
    def __init__(self, port):
        self._ptrport = port
        self._port = 0

    def Open(self):
        try:
            self._port = open(self._ptrport, 'a+')
        except IOError as err:
            print("ERROR" + self._ptrport + str(err))
            exit(-1)

    def Config(self, baudrate, databits, parity, stopbit):
        try:
            cfg = termios.tcgetattr(self._port)
        except Exception as err:
            print("ERROR " + str(err))
        cfg[0] = 0  # iflag
        cfg[1] = 0  # oflag
        cfg[2] = termios.CREAD | termios.CLOCAL  # setup control flag

        if databits == armPortDatabits_t.ARMPORT_DATA_7BITS:
            cfg[2] |= termios.CS7
        elif databits == armPortDatabits_t.ARMPORT_DATA_8BITS:
            cfg[2] |= termios.CS8
        else:
            print("ERROR wrong databits set 7 or 8")
            exit(-1)

        if parity == armPortParity_t.ARMPORT_PARITY_NO:
            pass
        elif parity == armPortParity_t.ARMPORT_PARITY_ODD:
            cfg[2] |= termios.PARENB | termios.PARODD
        elif parity == armPortParity_t.ARMPORT_PARITY_EVEN:
            cfg[2] |= termios.PARENB
        else:
            print("ERROR wrong parity must be 0 or 1 or 2")
            exit(-1)

        if stopbit == armPortStopbit_t.ARM_STOPBIT_1:
            pass
        elif stopbit == armPortStopbit_t.ARM_STOPBIT_2:
            cfg[2] |= termios.CSTOP
        else:
            print("ERROR wrong stop bit must be 1 or 2")

        cfg[3] = 0  # setup local flag

        # set speed

        if baudrate == armPortBaudrate_t.ARMPORT_BAUDRATE_1200:
            cfg[4] = termios.B1200  # input speed
            cfg[5] = termios.B1200  # output speed
        elif baudrate == armPortBaudrate_t.ARMPORT_BAUDRATE_2400:
            cfg[4] = termios.B2400
            cfg[5] = termios.B2400
        elif baudrate == armPortBaudrate_t.ARMPORT_BAUDRATE_4800:
            cfg[4] = termios.B4800
            cfg[5] = termios.B4800
        elif baudrate == armPortBaudrate_t.ARMPORT_BAUDRATE_9600:
            cfg[4] = termios.B9600
            cfg[5] = termios.B9600
        elif baudrate == armPortBaudrate_t.ARMPORT_BAUDRATE_19200:
            cfg[4] = termios.B19200
            cfg[5] = termios.B19200
        elif baudrate == armPortBaudrate_t.ARMPORT_BAUDRATE_38400:
            cfg[4] = termios.B38400
            cfg[5] = termios.B38400
        elif baudrate == armPortBaudrate_t.ARMPORT_BAUDRATE_57600:
            cfg[4] = termios.B57600
            cfg[5] = termios.B57600
        elif baudrate == armPortBaudrate_t.ARMPORT_BAUDRATE_115200:
            cfg[4] = termios.B115200
            cfg[5] = termios.B115200
        elif baudrate == armPortBaudrate_t.ARMPORT_BAUDRATE_230400:
            cfg[4] = termios.B230400
            cfg[5] = termios.B230400
        else:
            print("ERROR baudrate not handle by ARM")
            exit(-1)

        # Set new attributes
        termios.tcflush(self._port, termios.TCIOFLUSH)
        try:
            termios.tcsetattr(self._port, termios.TCSANOW, cfg)
        except Exception as err:
            print("ERROR set option" + str(err))
            exit(-1)
        return 0

    def close(self):
        self._port.close()  # should work gotta test TODO
        exit(0)

    def write(self, data):
        try:
            self._port.write(str(data))
        except Exception as err:
            print("ERROR writing on port " + str(err))
            return -1
        return 0

    def read(self, timeout):
        try:
            select.select(self._port, None, None, timeout)
        except OSError as err:
            print("Error might be timeout " + str(err)) # need also test TODO
            return 0
        buf = self._port.read()
        return buf

    def delay(self, time_sec):
        time.sleep(time_sec)
