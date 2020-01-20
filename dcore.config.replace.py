# python script which will ask for the values and inserts them into configuration file
import yaml
import json

source_file="dcoreAnsibleVars.yaml"
destination_file="exported.data.yaml"
STATUS_WIDTH=100
questionare_satisfaction = True

def rcOutSTRING (text, width=STATUS_WIDTH, delimeter='.'):
    print("{}".format(text.ljust(width, delimeter)), end='')
def rcOutOK():
    print(' [' + '\x1b[1;33;32m' + '  OK  ' + '\x1b[0m' + ']')
def rcOutFAIL():
    print(' [' + '\x1b[1;33;31m' + ' FAIL ' + '\x1b[0m' + ']')
def rcOutWARN():
    print(' [' + '\x1b[1;33;93m' + ' WARN ' + '\x1b[0m' + ']')

def get_str(prompt, default_value=None):
    while True:
        try:
            if default_value is not None:
                rcOutSTRING(prompt + "(default: " + default_value + ") ")
                return str(input(" ")) or default_value
            else:
                rcOutSTRING(prompt)
                return str(input(" "))
        except ValueError:
           print("  Invalid input please enter an integer!")

def get_bool(prompt, default_value=None):
    while True:
        try:
            if default_value is not None:
                rcOutSTRING(prompt + "(default: " + str(default_value )+ ") ")
                return str(input(" ")) or default_value
            else:
                rcOutSTRING(prompt)
                return {"true":True,"false":False}[input(" ").lower()]
        except KeyError:
            print("  Invalid input please enter True or False!")

def get_int(prompt, default_value=None):
    while True:
        try:
            if default_value is not None:
                rcOutSTRING(prompt + "(default: " + str(default_value) + ") ")
                vstup = input(" ") or default_value
                return int(vstup)
            else:
                rcOutSTRING(prompt)
                return int(input(" "))
        except ValueError:
           print("  Invalid input please enter an integer!")

rcOutSTRING("Rading data from file \"{}\"".format(source_file))
try:
    with open(source_file) as original_config_file:
        original_config_data = yaml.load(original_config_file, Loader=yaml.FullLoader)
except: rcOutFAIL()
else: rcOutOK()

modified_config_data = original_config_data

while questionare_satisfaction:
    print()
    print("-"*STATUS_WIDTH)
    print(" Answer these questions")
    print("-"*STATUS_WIDTH)

    try: DcoreUserName
    except NameError: DcoreUserName = get_str("DcoreUserName (application_owner, application_owner_group) ")
    else: DcoreUserName = get_str("DcoreUserName (application_owner, application_owner_group) ", default_value=DcoreUserName)

    try: DcoreImageTag
    except NameError: DcoreImageTag = get_str("DcoreImageTag (image_tag) ")
    else: DcoreImageTag = get_str("DcoreImageTag (image_tag) ", default_value=DcoreImageTag)

    try: DcoreNetName
    except NameError: DcoreNetName = get_str("DcoreNetName (decent_net_name) ")
    else: DcoreNetName = get_str("DcoreNetName (decent_net_name) ", default_value=DcoreNetName)

    # # DcoreGenesisURI = str(input("DcoreGenesisURI: "))
    # # DcoreConfigURI = str(input("DcoreConfigURI: "))

    try: DcoreRPCport
    except NameError: DcoreRPCport = get_int("DcoreRPCport (exposed_port_rpc) ")
    else: DcoreRPCport = get_int("DcoreRPCport (exposed_port_rpc) ", default_value=DcoreRPCport)

    try: DcoreExposeRPCPort
    except NameError: DcoreExposeRPCPort = get_bool("DcoreExposeRPCPort (publish_rpc) ")
    else: DcoreExposeRPCPort = get_bool("DcoreExposeRPCPort (publish_rpc) ", default_value=DcoreExposeRPCPort)

    try: DcoreP2Pport
    except NameError: DcoreP2Pport = get_int("DcoreP2Pport (port_p2p) ")
    else: DcoreP2Pport = get_int("DcoreP2Pport (port_p2p) ", default_value=DcoreP2Pport)

    try: DcoreAllowNginx
    except NameError: DcoreAllowNginx = get_bool("DcoreAllowNginx (nginx_allowed) ")
    else: DcoreAllowNginx = get_bool("DcoreAllowNginx (nginx_allowed) ", default_value=DcoreAllowNginx)

    try: DcoreRoleCustom
    except NameError: DcoreRoleCustom = get_bool("DcoreRoleCustom (role_custom) ")
    else: DcoreRoleCustom = get_bool("DcoreRoleCustom (role_custom) ", default_value=DcoreRoleCustom)

    try: DcoreRoleCustomName
    except NameError: DcoreRoleCustomName = get_str("DcoreRoleCustomName (role_custom_name) ")
    else: DcoreRoleCustomName = get_str("DcoreRoleCustomName (role_custom_name) ", default_value=DcoreRoleCustomName)

    try: DcoreRoleMiner
    except NameError: DcoreRoleMiner = get_bool("DcoreRoleMiner (role_miner) ")
    else: DcoreRoleMiner = get_bool("DcoreRoleMiner (role_miner) ", default_value=DcoreRoleMiner)

    try: DcoreRoleSeeder
    except NameError: DcoreRoleSeeder = get_bool("DcoreRoleSeeder (role_seeder) ")
    else: DcoreRoleSeeder = get_bool("DcoreRoleSeeder (role_seeder) ", default_value=DcoreRoleSeeder)

    print()
    print("-"*STATUS_WIDTH)
    print("Recapitulation of your answers")
    print("-"*STATUS_WIDTH)
    rcOutSTRING("  DcoreUserName ")       ; print (" {}".format(DcoreUserName))
    rcOutSTRING("  DcoreImageTag ")       ; print (" {}".format(DcoreImageTag))
    rcOutSTRING("  DcoreRPCport ")        ; print (" {}".format(DcoreRPCport))
    rcOutSTRING("  DcoreExposeRPCPort ")  ; print (" {}".format(DcoreExposeRPCPort))
    rcOutSTRING("  DcoreP2Pport ")        ; print (" {}".format(DcoreP2Pport))
    rcOutSTRING("  DcoreAllowNginx ")     ; print (" {}".format(DcoreAllowNginx))
    rcOutSTRING("  DcoreRoleCustom ")     ; print (" {}".format(DcoreRoleCustom))
    rcOutSTRING("  DcoreRoleCustomName ") ; print (" {}".format(DcoreRoleCustomName))
    rcOutSTRING("  DcoreRoleMiner ")      ; print (" {}".format(DcoreRoleMiner))
    rcOutSTRING("  DcoreRoleSeeder ")     ; print (" {}".format(DcoreRoleSeeder))
    answer = input("\nAre these answers correct? (Y/n/q): ").lower()
    while answer not in {"y", "n", "q"}:
        answer = input("Please, respond with 'y' or 'n' or 'q' for quit: ").lower()
    if answer == "y":
        questionare_satisfaction = False
    if answer == "q":
        print("Program ended without any modification of files")
        exit(0)
    print()


# DcoreUserName
if "application_owner" in modified_config_data.keys():
    modified_config_data["application_owner"] = DcoreUserName
if "application_owner_group" in modified_config_data.keys():
    modified_config_data["application_owner_group"] = DcoreUserName
# DcoreImageTag
for dcors in modified_config_data["dcore_containers"].keys():
    if "image_tag" in modified_config_data["dcore_containers"][dcors].keys():
        modified_config_data["dcore_containers"][dcors]["image_tag"] = DcoreImageTag
# DcoreNetName
for dcors in modified_config_data["dcore_containers"].keys():
    if "decent_net_name" in modified_config_data["dcore_containers"][dcors].keys():
        modified_config_data["dcore_containers"][dcors]["decent_net_name"] = DcoreNetName
# DcoreRPCport
for dcors in modified_config_data["dcore_containers"].keys():
    if "exposed_port_rpc" in modified_config_data["dcore_containers"][dcors].keys():
        modified_config_data["dcore_containers"][dcors]["exposed_port_rpc"] = DcoreRPCport
# DcoreExposeRPCPort
for dcors in modified_config_data["dcore_containers"].keys():
    if "publish_rpc" in modified_config_data["dcore_containers"][dcors].keys():
        modified_config_data["dcore_containers"][dcors]["publish_rpc"] = DcoreExposeRPCPort
# DcoreP2Pport
for dcors in modified_config_data["dcore_containers"].keys():
    if "exposed_port_p2p" in modified_config_data["dcore_containers"][dcors].keys():
        modified_config_data["dcore_containers"][dcors]["exposed_port_p2p"] = DcoreP2Pport
# DcoreAllowNginx
for dcors in modified_config_data["dcore_containers"].keys():
    if "nginx_allowed" in modified_config_data["dcore_containers"][dcors].keys():
        modified_config_data["dcore_containers"][dcors]["nginx_allowed"] = DcoreAllowNginx
# DcoreRoleCustom
for dcors in modified_config_data["dcore_containers"].keys():
    if "role_custom" in modified_config_data["dcore_containers"][dcors].keys():
        modified_config_data["dcore_containers"][dcors]["role_custom"] = DcoreRoleCustom
# DcoreRoleCustomName
for dcors in modified_config_data["dcore_containers"].keys():
    if "role_custom_name" in modified_config_data["dcore_containers"][dcors].keys():
        modified_config_data["dcore_containers"][dcors]["role_custom_name"] = DcoreRoleCustomName
# DcoreRoleMiner
for dcors in modified_config_data["dcore_containers"].keys():
    if "role_miner" in modified_config_data["dcore_containers"][dcors].keys():
        modified_config_data["dcore_containers"][dcors]["role_miner"] = DcoreRoleMiner
# DcoreRoleSeeder
for dcors in modified_config_data["dcore_containers"].keys():
    if "role_seeder" in modified_config_data["dcore_containers"][dcors].keys():
        modified_config_data["dcore_containers"][dcors]["role_seeder"] = DcoreRoleSeeder


print("*"*STATUS_WIDTH)
# print(json.dumps(modified_config_data, indent=4))

rcOutSTRING("Writing data to file \"{}\"".format(destination_file))
try:
    with open(destination_file, 'w') as outfile:
        yaml.dump(modified_config_data, outfile, default_flow_style=False)
except: rcOutFAIL()
else: rcOutOK()
