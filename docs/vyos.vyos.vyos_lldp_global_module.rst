.. _vyos.vyos.vyos_lldp_global_module:


**************************
vyos.vyos.vyos_lldp_global
**************************

**LLDP global resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages link layer discovery protocol (LLDP) attributes on VyOS devices.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The provided link layer discovery protocol (LLDP) configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Exactly one management address (exclusive with addresses). Deprecated in favor of addresses. To be removed in 7.0.0.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>addresses</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>One or more management addresses. The management address is used to identify the management interface of the system. Only addresses connected to the system will be transmitted.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enable</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>This argument is a boolean value to enable or disable LLDP.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>legacy_protocols</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>cdp</li>
                                    <li>edp</li>
                                    <li>fdp</li>
                                    <li>sonmp</li>
                        </ul>
                </td>
                <td>
                        <div>List of the supported legacy protocols.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>snmp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This argument enable the SNMP queries to LLDP database.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>running_config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This option is used only with state <em>parsed</em>.</div>
                        <div>The value of this option should be the output received from the VyOS device by executing the command <b>show configuration commands | grep lldp</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>replaced</li>
                                    <li>deleted</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
                                    <li>parsed</li>
                        </ul>
                </td>
                <td>
                        <div>The state of the configuration after module completion.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against VyOS 1.3.8, 1.4.2, the upcoming 1.5, and the rolling release of spring 2025
   - This module works with connection ``ansible.netcommon.network_cli``. See `the VyOS OS Platform Options <../network/user_guide/platform_vyos.html>`_.



Examples
--------

.. code-block:: yaml

    # Using merged
    #
    # Before state:
    # -------------
    #
    # vyos@vyos:~$ show configuration commands|grep lldp
    #
    - name: Merge provided configuration with device configuration
      vyos.vyos.vyos_lldp_global:
        config:
          legacy_protocols:
            - fdp
            - cdp
          snmp: enable
          addresses:
            - 192.0.2.11
        state: merged
    #
    #
    # ------------------------
    # Module Execution Results
    # ------------------------
    #
    #  before": {}
    #
    #  commands": [
    #    "set service lldp legacy-protocols fdp",
    #    "set service lldp legacy-protocols cdp",
    #    "set service lldp snmp enable",
    #    "set service lldp management-address '192.0.2.11'"
    #  ]
    #
    #  after": {
    #    "snmp": "enable"
    #    "addresses": [
    #        "192.0.2.11"
    #    ]
    #    "legacy_protocols": [
    #        "cdp",
    #        "fdp"
    #    ]
    #    "enable": true
    #  }
    #
    # After state:
    # -------------
    #
    # set service lldp legacy-protocols cdp
    # set service lldp legacy-protocols fdp
    # set service lldp management-address '192.0.2.11'
    # set service lldp snmp enable


    # Using replaced
    #
    # Before state:
    # -------------
    #
    # vyos@vyos:~$ show configuration commands | grep lldp
    # set service lldp legacy-protocols cdp
    # set service lldp legacy-protocols fdp
    # set service lldp management-address '192.0.2.11'
    # set service lldp snmp enable
    #
    - name: Replace device configurations with provided configurations
      vyos.vyos.vyos_lldp_global:
        config:
          legacy_protocols:
            - edp
            - sonmp
            - cdp
          addresses:
            - 192.0.2.14
        state: replaced
    #
    #
    # ------------------------
    # Module Execution Results
    # ------------------------
    #
    #
    # "before": {
    #    "snmp": "enable"
    #    "addresses": [
    #        "192.0.2.11"
    #    ]
    #    "legacy_protocols": [
    #        "cdp",
    #        "fdp"
    #    ]
    #    "enable": true
    #  }
    #
    # "commands": [
    #        "delete service lldp snmp",
    #        "delete service lldp legacy-protocols fdp",
    #        "delete service lldp management-address '192.0.2.11'",
    #        "set service lldp management-address '192.0.2.14'",
    #        "set service lldp legacy-protocols edp",
    #        "set service lldp legacy-protocols sonmp"
    #    ]
    #
    # "after": {
    #    "addresses": [
    #        "192.0.2.14"
    #    ]
    #    "legacy_protocols": [
    #        "cdp",
    #        "edp",
    #        "sonmp"
    #    ]
    #    "enable": true
    #  }
    #
    # After state:
    # -------------
    #
    # vyos@vyos:~$ show configuration commands|grep lldp
    # set service lldp legacy-protocols cdp
    # set service lldp legacy-protocols edp
    # set service lldp legacy-protocols sonmp
    # set service lldp management-address '192.0.2.14'


    # Using deleted
    #
    # Before state
    # -------------
    # vyos@vyos:~$ show configuration commands|grep lldp
    # set service lldp legacy-protocols cdp
    # set service lldp legacy-protocols edp
    # set service lldp legacy-protocols sonmp
    # set service lldp management-address '192.0.2.14'
    #
    - name: Delete attributes of given lldp service (This won't delete the LLDP service
        itself)
      vyos.vyos.vyos_lldp_global:
        config:
        state: deleted
    #
    #
    # ------------------------
    # Module Execution Results
    # ------------------------
    #
    # "before": {
    #    "addresses": [
    #       "192.0.2.14"
    #    ]
    #    "legacy_protocols": [
    #       "cdp",
    #       "edp",
    #       "sonmp"
    #    ]
    #    "enable": true
    #  }
    #
    #  "commands": [
    #     "delete service lldp management-address",
    #     "delete service lldp legacy-protocols"
    #  ]
    #
    # "after": {
    #    "enable": true
    #  }
    #
    # After state
    # ------------
    # vyos@vyos:~$ show configuration commands | grep lldp
    # set service lldp


    # Using gathered
    #
    # Before state:
    # -------------
    #
    # vyos@192# run show configuration commands | grep lldp
    # set service lldp legacy-protocols 'cdp'
    # set service lldp management-address '192.0.2.17'
    #
    - name: Gather lldp global config with provided configurations
      vyos.vyos.vyos_lldp_global:
        config:
        state: gathered
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #    "gathered": {
    #        "config_trap": true,
    #        "group": {
    #            "address_group": [
    #                {
    #                    "description": "Sales office hosts address list",
    #                    "members": [
    #                        {
    #                            "address": "192.0.3.1"
    #                        },
    #                        {
    #                            "address": "192.0.3.2"
    #                        }
    #                    ],
    #                    "name": "ENG-HOSTS"
    #                },
    #                {
    #                    "description": "Sales office hosts address list",
    #                    "members": [
    #                        {
    #                            "address": "192.0.2.1"
    #                        },
    #                        {
    #                            "address": "192.0.2.2"
    #                        },
    #                        {
    #                            "address": "192.0.2.3"
    #                        }
    #                    ],
    #                    "name": "SALES-HOSTS"
    #                }
    #            ],
    #            "network_group": [
    #                {
    #                    "description": "This group has the Management network addresses",
    #                    "members": [
    #                        {
    #                            "address": "192.0.1.0/24"
    #                        }
    #                    ],
    #                    "name": "MGMT"
    #                }
    #            ]
    #        },
    #        "log_martians": true,
    #        "ping": {
    #            "all": true,
    #            "broadcast": true
    #        },
    #        "route_redirects": [
    #            {
    #                "afi": "ipv4",
    #                "icmp_redirects": {
    #                    "receive": false,
    #                    "send": true
    #                },
    #                "ip_src_route": true
    #            }
    #        ],
    #        "state_policy": [
    #            {
    #                "action": "accept",
    #                "connection_type": "established",
    #                "log": true
    #            },
    #            {
    #                "action": "reject",
    #                "connection_type": "invalid"
    #            }
    #        ],
    #        "syn_cookies": true,
    #        "twa_hazards_protection": true,
    #        "validation": "strict"
    #    }
    #
    # After state:
    # -------------
    #
    # vyos@192# run show configuration commands | grep lldp
    # set service lldp legacy-protocols 'cdp'
    # set service lldp management-address '192.0.2.17'


    # Using rendered
    #
    #
    - name: Render the commands for provided  configuration
      vyos.vyos.vyos_lldp_global:
        config:
          addresses:
            - 192.0.2.17
          enable: true
          legacy_protocols:
            - cdp
        state: rendered
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #
    # "rendered": [
    #    "set service lldp legacy-protocols 'cdp'",
    #    "set service lldp",
    #    "set service lldp management-address '192.0.2.17'"
    #  ]
    #


    # Using parsed
    #
    #
    - name: Parse the provided commands to provide structured configuration
      vyos.vyos.vyos_lldp_global:
        running_config:
          "set service lldp legacy-protocols 'cdp'
           set service lldp legacy-protocols 'fdp'
           set service lldp management-address '192.0.2.11'"
        state: parsed
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #
    # "parsed": {
    #    "addresses": [
    #       "192.0.2.11"
    #    ]
    #    "enable": true,
    #    "legacy_protocols": [
    #       "cdp",
    #       "fdp"
    #    ]
    #  }



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>after</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The resulting configuration after module invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format of the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration prior to the module invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format of the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>commands</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The set of commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;set service lldp legacy-protocols sonmp&#x27;, &quot;set service lldp management-address &#x27;192.0.2.14&#x27;&quot;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Rohit Thakur (@rohitthakur2590)
