[![build-test](https://github.com/darkwizard242/ansible-role-containerd/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-containerd/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-containerd/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-containerd/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/56917?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/56917?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/56917?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-containerd&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-containerd) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-containerd&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-containerd) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-containerd&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-containerd) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-containerd&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-containerd) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-containerd?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-containerd?color=orange&style=flat-square)

# Ansible Role: containerd

Role to install (_by default_) [containerd](https://github.com/containerd/containerd) on **Debian/Ubuntu** and **EL** systems. **Containerd** is "An industry-standard container runtime with an emphasis on simplicity, robustness and portability".

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
containerd_app: containerd
containerd_version: 1.5.7
containerd_os: linux
containerd_arch: amd64
containerd_dl_url: "https://github.com/{{ containerd_app }}/{{ containerd_app }}/releases/download/v{{ containerd_version }}/{{ containerd_app }}-{{ containerd_version }}-{{ containerd_os }}-{{ containerd_arch }}.tar.gz"
containerd_bin_path: /usr/local/bin
containerd_files_mode: '0755'
containerd_files_owner: root
containerd_files_group: root
```

### Variables table:

Variable               | Description
---------------------- | --------------------------------------------------------------------------------------------------------------------------------
containerd_app         | Defines the app to install i.e. **containerd**
containerd_version     | Defined to dynamically fetch the desired version to install. Defaults to: **1.5.7**
containerd_os          | Defines OS type. Defaults to: **linux**
containerd_arch        | Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture. Defaults to: **amd64**
containerd_dl_url      | Defines URL to download the containerd binaries archive from.
containerd_bin_path    | Defined to dynamically set the appropriate path to store containerd binaries into.
containerd_files_mode  | Mode for the binaries file of containerd.
containerd_files_owner | Owner for the binaries file of containerd.
containerd_files_group | Group for the binaries file of containerd.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **containerd**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.containerd
```

For customizing behavior of role (i.e. specifying the desired **containerd** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.containerd
  vars:
    containerd_version: 1.5.6
```

For customizing behavior of role (i.e. setting path for extraction to **/usr/bin**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.containerd
  vars:
    containerd_bin_path: '/usr/bin'
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-containerd/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/)
