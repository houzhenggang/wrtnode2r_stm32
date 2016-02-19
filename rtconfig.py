import os

# toolchains options
ARCH='arm'
CPU='cortex-m3'
CROSS_TOOL='gcc'

if os.getenv('RTT_CC'):
    CROSS_TOOL = os.getenv('RTT_CC')

PLATFORM  = 'gcc'
EXEC_PATH = '/Users/schumy/arm-gcc/bin'

if os.getenv('RTT_EXEC_PATH'):
    EXEC_PATH = os.getenv('RTT_EXEC_PATH')

BUILD = ''
STM32_TYPE = 'STM32F10X_MD'
R_VERSION = 'V0.7'

# toolchains
PREFIX = 'arm-none-eabi-'
CC = PREFIX + 'gcc'
CXX = PREFIX + 'g++'
AS = PREFIX + 'gcc'
AR = PREFIX + 'ar'
LINK = PREFIX + 'g++'
TARGET_EXT = 'elf'
SIZE = PREFIX + 'size'
OBJDUMP = PREFIX + 'objdump'
OBJCPY = PREFIX + 'objcopy'

DEVICE = ' -mcpu=cortex-m3 -march=armv7-m -mthumb -DMCU_STM32F103T8 -DBOOTLOADER_wrtnode'
CFLAGS = DEVICE + ' -ffunction-sections -fdata-sections'
CXXFLAGS = DEVICE + ' -fno-exceptions -fno-rtti -DMAPLE_USE_WIRISHC'
AFLAGS = ' -c' + DEVICE + ' -x assembler-with-cpp'
LFLAGS = DEVICE + ' -nostdlib -Wl,--gc-sections,-Map=rtthread-stm32.map,-cref,-u,Reset_Handler -T stm32_rom.ld'

CPATH = ''
LPATH = ''

if BUILD == 'debug':
    CFLAGS += ' -Og -gdwarf-2'
    AFLAGS += ' -gdwarf-2'
else:
    CFLAGS += ' -Og'

    POST_ACTION = OBJCPY + ' -O binary $TARGET WRTnode_2r_STM32_rtthread_' + R_VERSION + '.bin\n' + SIZE + ' $TARGET \n'

