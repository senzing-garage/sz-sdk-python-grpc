import os
import G2IniParams


def get_json_config():
    try:
        ini_file = os.environ['SENZING_CONFIG_FILE']
    except KeyError as ex:
        raise Exception('Cannot find SENZING_CONFIG_FILE environement variable. '\
                        ' please source senzing config senzing/setupEnv') from ex

    if not os.path.exists(ini_file):
        raise Exception(F'Senzing config file not found: {ini_file}')

    ini = G2IniParams.G2IniParams()
    return ini.getJsonINIParams(ini_file)
