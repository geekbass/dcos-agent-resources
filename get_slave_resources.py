from requests import get
import json


def main():
    slaves = []
    slave_resources = []

    url = 'http://leader.mesos:5050/slaves'
    slaves_info = get(url).json()
    for slave in slaves_info["slaves"]:
        hostname = slave["hostname"]
        slaves.append(hostname)

    for hostname in slaves:
        slave_url = "http://" + hostname + ":5051/flags"
        slave_flag = get(slave_url).json()
        resources = slave_flag["flags"]["resources"]
        role = slave_flag["flags"]["default_role"]
        slave_resources.append({'hostname': hostname, 'role': role, 'resources': resources})

    with open('slave_resources.json', 'w') as outfile:
        json.dump(slave_resources, outfile, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
