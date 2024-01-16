# ------------------------------------------------------------------------------
#  Copyright 2022 Upstream Data Inc                                            -
#                                                                              -
#  Licensed under the Apache License, Version 2.0 (the "License");             -
#  you may not use this file except in compliance with the License.            -
#  You may obtain a copy of the License at                                     -
#                                                                              -
#      http://www.apache.org/licenses/LICENSE-2.0                              -
#                                                                              -
#  Unless required by applicable law or agreed to in writing, software         -
#  distributed under the License is distributed on an "AS IS" BASIS,           -
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    -
#  See the License for the specific language governing permissions and         -
#  limitations under the License.                                              -
# ------------------------------------------------------------------------------

from pyasic.rpc.cgminer import CGMinerRPCAPI


class BMMinerRPCAPI(CGMinerRPCAPI):
    """An abstraction of the BMMiner API.

    Each method corresponds to an API command in BMMiner.

    [BMMiner API documentation](https://github.com/jameshilliard/bmminer/blob/master/API-README)

    This class abstracts use of the BMMiner API, as well as the
    methods for sending commands to it.  The `self.send_command()`
    function handles sending a command to the miner asynchronously, and
    as such is the base for many of the functions in this class, which
    rely on it to send the command for them.

    Parameters:
        ip: The IP of the miner to reference the API on.
        port: The port to reference the API on.  Default is 4028.
    """
