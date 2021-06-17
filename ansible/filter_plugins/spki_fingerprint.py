# Copyright © 2019 VMware Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from sys import version_info
from binascii import hexlify


class FilterModule(object):

    def filters(self):
        return {
            'spki_fingerprint': self.spki_fingerprint,
        }

    def spki_fingerprint(self, pem):
        if version_info < (3, 0):
            pem_bytes = bytes(pem)
        else:
            pem_bytes = bytes(pem, 'utf8')
        cert = x509.load_pem_x509_certificate(pem_bytes, default_backend())
        public_key = cert.public_key()
        spki = public_key.public_bytes(
            serialization.Encoding.DER,
            serialization.PublicFormat.SubjectPublicKeyInfo)
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(spki)
        hash = digest.finalize()
        return hexlify(hash).decode('ascii')
