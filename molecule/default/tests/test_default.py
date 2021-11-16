import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


BINARIES_DIR = '/usr/local/bin/'
BINARIES = ['containerd', 'containerd-shim', 'containerd-shim-runc-v1',
            'containerd-shim-runc-v2', 'ctr']


def test_containerd_binaries_exists(host):
    for BINARY in BINARIES:
        """
        Tests if containerd binaries exist.
        """
        assert host.file(BINARIES_DIR + BINARY).exists


def test_containerd_binaries_file(host):
    for BINARY in BINARIES:
        """
        Tests if containerd binaries are a file type.
        """
        assert host.file(BINARIES_DIR + BINARY).is_file
