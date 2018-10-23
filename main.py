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
