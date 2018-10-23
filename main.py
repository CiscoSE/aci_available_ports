"""
Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""
from controllers.apic import ApicController

if __name__ == '__main__':

    apicObj = ApicController()
    # Add your APIC URL here:
    apicObj.url = ""

    # Add your username and password here:
    apicObj.token = apicObj.get_token(username="", password="")

    pods = apicObj.getPods()
    for pod in pods:
        switches = apicObj.getLeafs(pod_dn=pod["fabricPod"]["attributes"]["dn"])
        for switch in switches:
            interfaces = apicObj.getInterfaces(switch_dn=switch["fabricNode"]["attributes"]["dn"])
            for interface in interfaces:
                print(switch["fabricNode"]["attributes"]["name"] + " -> " + interface["l1PhysIf"]["attributes"]["id"] + ": " + interface["l1PhysIf"]["attributes"]["descr"])
