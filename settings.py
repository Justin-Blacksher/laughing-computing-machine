

GAME_EXECUTABLE="DOSBox.exe"


# This will be written in C++ and Assembly later
# I will probably write this in GO and use inline assembly to make the 
# Changes. Because Assembly is life. Real Men Write Assembly

#004EF162
#EAX=0x0a914020
#EBX=0x00041e44

# List of working pointers
# This one is looking to be unstable
# "DOSBox.exe + 0x34d714" + 0x41e44 

# Currently working offsets
EDX=0x00000011 * 4 + 0x0074d6d0
AMMOOFFSETS = [EDX, 0x34d714, 0x41e44]