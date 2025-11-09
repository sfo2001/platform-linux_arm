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
lgpio

lgpio is a modern C library for Linux GPIO access, designed as a successor to
deprecated sysfs GPIO and the pigpio library. It uses the GPIO character device
(/dev/gpiochip*) introduced in Linux kernel 4.8.

lgpio works on all Raspberry Pi models including Pi 5, which removed support for
older GPIO interfaces.

http://abyz.me.uk/lg/lgpio.html
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

    LIBS=["lgpio"]
)
