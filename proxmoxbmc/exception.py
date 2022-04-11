#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


class ProxmoxBMCError(Exception):
    message = None

    def __init__(self, message=None, **kwargs):
        if self.message and kwargs:
            self.message = self.message % kwargs
        else:
            self.message = message

        super(ProxmoxBMCError, self).__init__(self.message)


class VmIdAlreadyExists(ProxmoxBMCError):
    message = 'VMID %(vmid)s already exists'


class VmIdNotFound(ProxmoxBMCError):
    message = 'No VMID with matching ID %(vmid)s was found'


class DetachProcessError(ProxmoxBMCError):
    message = ('Error when forking (detaching) the ProxmoxBMC process '
               'from its parent and session. Error: %(error)s')
