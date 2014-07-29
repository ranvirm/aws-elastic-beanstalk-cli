# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from ebcli.core.abstractcontroller import AbstractBaseController
from ebcli.resources.strings import strings


class LogsController(AbstractBaseController):
    class Meta:
        label = 'logs'
        description = strings['logs.info']
        arguments = [
            (['-f', '--foo'], dict(help='notorious foo option')),
        ]

    def do_command(self):
        # get environment logs
        self.app.print_to_console('There are no logs')