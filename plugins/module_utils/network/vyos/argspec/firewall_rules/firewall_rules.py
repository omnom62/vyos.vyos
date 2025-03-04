#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################
"""
The arg spec for the vyos_firewall_rules module
"""


from __future__ import absolute_import, division, print_function


__metaclass__ = type


class Firewall_rulesArgs(object):  # pylint: disable=R0903
    """The arg spec for the vyos_firewall_rules module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "afi": {
                    "choices": ["ipv4", "ipv6"],
                    "required": True,
                    "type": "str",
                },
                "rule_sets": {
                    "elements": "dict",
                    "options": {
                        "default_action": {
                            "choices": [
                                "drop",
                                "reject",
                                "accept",
                                "jump",
                            ],
                            "type": "str",
                        },
                        "default_jump_target": {"type": "str"},
                        "description": {"type": "str"},
                        "enable_default_log": {"type": "bool"},
                        "filter": {
                            "choices": [
                                "input",
                                "output",
                                "forward",
                            ],
                            "type": "str",
                        },
                        "name": {"type": "str"},
                        "rules": {
                            "elements": "dict",
                            "options": {
                                "action": {
                                    "choices": [
                                        "drop",
                                        "reject",
                                        "accept",
                                        "inspect",
                                        "continue",
                                        "return",
                                        "jump",
                                        "queue",
                                        "synproxy",
                                    ],
                                    "type": "str",
                                },
                                "description": {"type": "str"},
                                "destination": {
                                    "options": {
                                        "address": {"type": "str"},
                                        "group": {
                                            "options": {
                                                "address_group": {"type": "str"},
                                                "network_group": {"type": "str"},
                                                "port_group": {"type": "str"},
                                            },
                                            "type": "dict",
                                        },
                                        "port": {"type": "str"},
                                    },
                                    "type": "dict",
                                },
                                "disable": {
                                    "aliases": ["disabled"],
                                    "type": "bool",
                                },
                                "fragment": {
                                    "choices": [
                                        "match-frag",
                                        "match-non-frag",
                                    ],
                                    "type": "str",
                                },
                                "icmp": {
                                    "options": {
                                        "code": {"type": "int"},
                                        "type": {"type": "int"},
                                        "type_name": {
                                            "choices": [
                                                "any",
                                                "echo-reply",
                                                "destination-unreachable",
                                                "network-unreachable",
                                                "host-unreachable",
                                                "protocol-unreachable",
                                                "port-unreachable",
                                                "fragmentation-needed",
                                                "source-route-failed",
                                                "network-unknown",
                                                "host-unknown",
                                                "network-prohibited",
                                                "host-prohibited",
                                                "TOS-network-unreachable",
                                                "TOS-host-unreachable",
                                                "communication-prohibited",
                                                "host-precedence-violation",
                                                "precedence-cutoff",
                                                "source-quench",
                                                "redirect",
                                                "network-redirect",
                                                "host-redirect",
                                                "TOS-network-redirect",
                                                "TOS-host-redirect",
                                                "echo-request",
                                                "router-advertisement",
                                                "router-solicitation",
                                                "time-exceeded",
                                                "ttl-zero-during-transit",
                                                "ttl-zero-during-reassembly",
                                                "parameter-problem",
                                                "ip-header-bad",
                                                "required-option-missing",
                                                "timestamp-request",
                                                "timestamp-reply",
                                                "address-mask-request",
                                                "address-mask-reply",
                                                "ping",
                                                "pong",
                                                "ttl-exceeded",
                                            ],
                                            "type": "str",
                                        },
                                    },
                                    "type": "dict",
                                },
                                "inbound_interface": {
                                    "options": {
                                        "group": {"type": "str"},
                                        "name": {"type": "str"},
                                    },
                                    "type": "dict",
                                },
                                "ipsec": {
                                    "choices": [
                                        "match-ipsec",
                                        "match-none",
                                        "match-ipsec-in",
                                        "match-ipsec-out",
                                        "match-none-in",
                                        "match-none-out",
                                    ],
                                    "type": "str",
                                },
                                "jump_target": {"type": "str"},
                                "limit": {
                                    "options": {
                                        "burst": {"type": "int"},
                                        "rate": {
                                            "options": {
                                                "number": {"type": "int"},
                                                "unit": {"type": "str"},
                                            },
                                            "type": "dict",
                                        },
                                    },
                                    "type": "dict",
                                },
                                "log": {
                                    "choices": [
                                        "disable",
                                        "enable",
                                    ],
                                    "type": "str",
                                },
                                "number": {
                                    "required": True,
                                    "type": "int",
                                },
                                "outbound_interface": {
                                    "options": {
                                        "group": {"type": "str"},
                                        "name": {"type": "str"},
                                    },
                                    "type": "dict",
                                },
                                "packet_length": {
                                    "elements": "dict",
                                    "options": {"length": {"type": "str"}},
                                    "type": "list",
                                },
                                "packet_length_exclude": {
                                    "elements": "dict",
                                    "options": {"length": {"type": "str"}},
                                    "type": "list",
                                },
                                "packet_type": {
                                    "choices": [
                                        "broadcast",
                                        "multicast",
                                        "host",
                                        "other",
                                    ],
                                    "type": "str",
                                },
                                "protocol": {"type": "str"},
                                "queue": {"type": "str"},
                                "queue_options": {
                                    "choices": [
                                        "bypass",
                                        "fanout",
                                    ],
                                    "type": "str",
                                },
                                "recent": {
                                    "options": {
                                        "count": {"type": "int"},
                                        "time": {"type": "str"},
                                    },
                                    "type": "dict",
                                },
                                "source": {
                                    "options": {
                                        "address": {"type": "str"},
                                        "fqdn": {"type": "str"},
                                        "group": {
                                            "options": {
                                                "address_group": {"type": "str"},
                                                "network_group": {"type": "str"},
                                                "port_group": {"type": "str"},
                                            },
                                            "type": "dict",
                                        },
                                        "mac_address": {"type": "str"},
                                        "port": {"type": "str"},
                                    },
                                    "type": "dict",
                                },
                                "state": {
                                    "options": {
                                        "established": {"type": "bool"},
                                        "invalid": {"type": "bool"},
                                        "new": {"type": "bool"},
                                        "related": {"type": "bool"},
                                    },
                                    "type": "dict",
                                },
                                "synproxy": {
                                    "options": {
                                        "mss": {"type": "int"},
                                        "window_scale": {"type": "int"},
                                    },
                                    "type": "dict",
                                },
                                "tcp": {
                                    "options": {
                                        "flags": {
                                            "elements": "dict",
                                            "options": {
                                                "flag": {
                                                    "choices": [
                                                        "ack",
                                                        "cwr",
                                                        "ecn",
                                                        "fin",
                                                        "psh",
                                                        "rst",
                                                        "syn",
                                                        "urg",
                                                        "all",
                                                    ],
                                                    "type": "str",
                                                },
                                                "invert": {"type": "bool"},
                                            },
                                            "type": "list",
                                        },
                                    },
                                    "type": "dict",
                                },
                                "time": {
                                    "options": {
                                        "monthdays": {"type": "str"},
                                        "startdate": {"type": "str"},
                                        "starttime": {"type": "str"},
                                        "stopdate": {"type": "str"},
                                        "stoptime": {"type": "str"},
                                        "utc": {"type": "bool"},
                                        "weekdays": {"type": "str"},
                                    },
                                    "type": "dict",
                                },
                            },
                            "type": "list",
                        },
                    },
                    "type": "list",
                },
            },
            "type": "list",
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "gathered",
                "rendered",
                "parsed",
            ],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
