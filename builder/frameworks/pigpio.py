# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
pigpio

pigpio is a C library for Raspberry Pi GPIO control, providing advanced features
including precise timing, PWM, servo control, and waveform generation. It can be
used both as a library and as a daemon (pigpiod) for remote GPIO control.

IMPORTANT: pigpio is NOT compatible with Raspberry Pi 5 due to the new RP1 I/O
controller. For Pi 5, use the lgpio framework instead.

Supported boards: Raspberry Pi 1, 2, 3, 4, Zero

http://abyz.me.uk/rpi/pigpio/
"""

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()

env.Replace(
    CPPFLAGS=[
        "-O2",
        "-Wall",
        "-Winline",
        "-pipe",
        "-fPIC"
    ]
)

env.Append(
    CPPDEFINES=[
        "_GNU_SOURCE"
    ],

    LIBS=["pigpio", "pthread"]
)
