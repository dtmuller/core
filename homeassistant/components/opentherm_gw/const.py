"""Constants for the opentherm_gw integration."""
import pyotgw.vars as gw_vars

from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import (
    PERCENTAGE,
    PRESSURE_BAR,
    TEMP_CELSIUS,
    TIME_HOURS,
    TIME_MINUTES,
)

ATTR_GW_ID = "gateway_id"
ATTR_LEVEL = "level"
ATTR_DHW_OVRD = "dhw_override"
ATTR_CH_OVRD = "ch_override"

CONF_CLIMATE = "climate"
CONF_FLOOR_TEMP = "floor_temperature"
CONF_PRECISION = "precision"
CONF_READ_PRECISION = "read_precision"
CONF_SET_PRECISION = "set_precision"
CONF_TEMPORARY_OVRD_MODE = "temporary_override_mode"

DATA_GATEWAYS = "gateways"
DATA_OPENTHERM_GW = "opentherm_gw"

DOMAIN = "opentherm_gw"

SERVICE_RESET_GATEWAY = "reset_gateway"
SERVICE_SET_CH_OVRD = "set_central_heating_ovrd"
SERVICE_SET_CLOCK = "set_clock"
SERVICE_SET_CONTROL_SETPOINT = "set_control_setpoint"
SERVICE_SET_HOT_WATER_SETPOINT = "set_hot_water_setpoint"
SERVICE_SET_HOT_WATER_OVRD = "set_hot_water_ovrd"
SERVICE_SET_GPIO_MODE = "set_gpio_mode"
SERVICE_SET_LED_MODE = "set_led_mode"
SERVICE_SET_MAX_MOD = "set_max_modulation"
SERVICE_SET_OAT = "set_outside_temperature"
SERVICE_SET_SB_TEMP = "set_setback_temperature"

TRANSLATE_SOURCE = {
    gw_vars.BOILER: "Boiler",
    gw_vars.OTGW: None,
    gw_vars.THERMOSTAT: "Thermostat",
}

UNIT_KW = "kW"
UNIT_L_MIN = f"L/{TIME_MINUTES}"

BINARY_SENSOR_INFO = {
    # [device_class, friendly_name format, [status source, ...]]
    gw_vars.DATA_MASTER_CH_ENABLED: [
        None,
        "Thermostat Central Heating {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_MASTER_DHW_ENABLED: [
        None,
        "Thermostat Hot Water {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_MASTER_COOLING_ENABLED: [
        None,
        "Thermostat Cooling {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_MASTER_OTC_ENABLED: [
        None,
        "Thermostat Outside Temperature Correction {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_MASTER_CH2_ENABLED: [
        None,
        "Thermostat Central Heating 2 {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_FAULT_IND: [
        BinarySensorDeviceClass.PROBLEM,
        "Boiler Fault {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_CH_ACTIVE: [
        BinarySensorDeviceClass.HEAT,
        "Boiler Central Heating {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_DHW_ACTIVE: [
        BinarySensorDeviceClass.HEAT,
        "Boiler Hot Water {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_FLAME_ON: [
        BinarySensorDeviceClass.HEAT,
        "Boiler Flame {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_COOLING_ACTIVE: [
        BinarySensorDeviceClass.COLD,
        "Boiler Cooling {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_CH2_ACTIVE: [
        BinarySensorDeviceClass.HEAT,
        "Boiler Central Heating 2 {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_DIAG_IND: [
        BinarySensorDeviceClass.PROBLEM,
        "Boiler Diagnostics {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_DHW_PRESENT: [
        None,
        "Boiler Hot Water Present {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_CONTROL_TYPE: [
        None,
        "Boiler Control Type {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_COOLING_SUPPORTED: [
        None,
        "Boiler Cooling Support {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_DHW_CONFIG: [
        None,
        "Boiler Hot Water Configuration {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_MASTER_LOW_OFF_PUMP: [
        None,
        "Boiler Pump Commands Support {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_CH2_PRESENT: [
        None,
        "Boiler Central Heating 2 Present {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_SERVICE_REQ: [
        BinarySensorDeviceClass.PROBLEM,
        "Boiler Service Required {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_REMOTE_RESET: [
        None,
        "Boiler Remote Reset Support {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_LOW_WATER_PRESS: [
        BinarySensorDeviceClass.PROBLEM,
        "Boiler Low Water Pressure {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_GAS_FAULT: [
        BinarySensorDeviceClass.PROBLEM,
        "Boiler Gas Fault {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_AIR_PRESS_FAULT: [
        BinarySensorDeviceClass.PROBLEM,
        "Boiler Air Pressure Fault {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_WATER_OVERTEMP: [
        BinarySensorDeviceClass.PROBLEM,
        "Boiler Water Overtemperature {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_REMOTE_TRANSFER_DHW: [
        None,
        "Remote Hot Water Setpoint Transfer Support {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_REMOTE_TRANSFER_MAX_CH: [
        None,
        "Remote Maximum Central Heating Setpoint Write Support {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_REMOTE_RW_DHW: [
        None,
        "Remote Hot Water Setpoint Write Support {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_REMOTE_RW_MAX_CH: [
        None,
        "Remote Central Heating Setpoint Write Support {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_ROVRD_MAN_PRIO: [
        None,
        "Remote Override Manual Change Priority {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_ROVRD_AUTO_PRIO: [
        None,
        "Remote Override Program Change Priority {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.OTGW_GPIO_A_STATE: [None, "Gateway GPIO A {}", [gw_vars.OTGW]],
    gw_vars.OTGW_GPIO_B_STATE: [None, "Gateway GPIO B {}", [gw_vars.OTGW]],
    gw_vars.OTGW_IGNORE_TRANSITIONS: [
        None,
        "Gateway Ignore Transitions {}",
        [gw_vars.OTGW],
    ],
    gw_vars.OTGW_OVRD_HB: [None, "Gateway Override High Byte {}", [gw_vars.OTGW]],
}

SENSOR_INFO = {
    # [device_class, unit, friendly_name, [status source, ...]]
    gw_vars.DATA_CONTROL_SETPOINT: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Control Setpoint {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_MASTER_MEMBERID: [
        None,
        None,
        "Thermostat Member ID {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_MEMBERID: [
        None,
        None,
        "Boiler Member ID {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_OEM_FAULT: [
        None,
        None,
        "Boiler OEM Fault Code {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_COOLING_CONTROL: [
        None,
        PERCENTAGE,
        "Cooling Control Signal {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_CONTROL_SETPOINT_2: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Control Setpoint 2 {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_ROOM_SETPOINT_OVRD: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Room Setpoint Override {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_MAX_RELATIVE_MOD: [
        None,
        PERCENTAGE,
        "Boiler Maximum Relative Modulation {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_MAX_CAPACITY: [
        None,
        UNIT_KW,
        "Boiler Maximum Capacity {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_MIN_MOD_LEVEL: [
        None,
        PERCENTAGE,
        "Boiler Minimum Modulation Level {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_ROOM_SETPOINT: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Room Setpoint {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_REL_MOD_LEVEL: [
        None,
        PERCENTAGE,
        "Relative Modulation Level {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_CH_WATER_PRESS: [
        None,
        PRESSURE_BAR,
        "Central Heating Water Pressure {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_DHW_FLOW_RATE: [
        None,
        UNIT_L_MIN,
        "Hot Water Flow Rate {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_ROOM_SETPOINT_2: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Room Setpoint 2 {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_ROOM_TEMP: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Room Temperature {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_CH_WATER_TEMP: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Central Heating Water Temperature {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_DHW_TEMP: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Hot Water Temperature {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_OUTSIDE_TEMP: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Outside Temperature {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_RETURN_WATER_TEMP: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Return Water Temperature {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SOLAR_STORAGE_TEMP: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Solar Storage Temperature {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SOLAR_COLL_TEMP: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Solar Collector Temperature {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_CH_WATER_TEMP_2: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Central Heating 2 Water Temperature {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_DHW_TEMP_2: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Hot Water 2 Temperature {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_EXHAUST_TEMP: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Exhaust Temperature {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_DHW_MAX_SETP: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Hot Water Maximum Setpoint {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_DHW_MIN_SETP: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Hot Water Minimum Setpoint {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_CH_MAX_SETP: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Boiler Maximum Central Heating Setpoint {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_CH_MIN_SETP: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Boiler Minimum Central Heating Setpoint {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_DHW_SETPOINT: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Hot Water Setpoint {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_MAX_CH_SETPOINT: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Maximum Central Heating Setpoint {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_OEM_DIAG: [
        None,
        None,
        "OEM Diagnostic Code {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_TOTAL_BURNER_STARTS: [
        None,
        None,
        "Total Burner Starts {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_CH_PUMP_STARTS: [
        None,
        None,
        "Central Heating Pump Starts {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_DHW_PUMP_STARTS: [
        None,
        None,
        "Hot Water Pump Starts {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_DHW_BURNER_STARTS: [
        None,
        None,
        "Hot Water Burner Starts {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_TOTAL_BURNER_HOURS: [
        None,
        TIME_HOURS,
        "Total Burner Hours {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_CH_PUMP_HOURS: [
        None,
        TIME_HOURS,
        "Central Heating Pump Hours {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_DHW_PUMP_HOURS: [
        None,
        TIME_HOURS,
        "Hot Water Pump Hours {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_DHW_BURNER_HOURS: [
        None,
        TIME_HOURS,
        "Hot Water Burner Hours {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_MASTER_OT_VERSION: [
        None,
        None,
        "Thermostat OpenTherm Version {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_OT_VERSION: [
        None,
        None,
        "Boiler OpenTherm Version {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_MASTER_PRODUCT_TYPE: [
        None,
        None,
        "Thermostat Product Type {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_MASTER_PRODUCT_VERSION: [
        None,
        None,
        "Thermostat Product Version {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_PRODUCT_TYPE: [
        None,
        None,
        "Boiler Product Type {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.DATA_SLAVE_PRODUCT_VERSION: [
        None,
        None,
        "Boiler Product Version {}",
        [gw_vars.BOILER, gw_vars.THERMOSTAT],
    ],
    gw_vars.OTGW_MODE: [None, None, "Gateway/Monitor Mode {}", [gw_vars.OTGW]],
    gw_vars.OTGW_DHW_OVRD: [
        None,
        None,
        "Gateway Hot Water Override Mode {}",
        [gw_vars.OTGW],
    ],
    gw_vars.OTGW_ABOUT: [None, None, "Gateway Firmware Version {}", [gw_vars.OTGW]],
    gw_vars.OTGW_BUILD: [None, None, "Gateway Firmware Build {}", [gw_vars.OTGW]],
    gw_vars.OTGW_CLOCKMHZ: [None, None, "Gateway Clock Speed {}", [gw_vars.OTGW]],
    gw_vars.OTGW_LED_A: [None, None, "Gateway LED A Mode {}", [gw_vars.OTGW]],
    gw_vars.OTGW_LED_B: [None, None, "Gateway LED B Mode {}", [gw_vars.OTGW]],
    gw_vars.OTGW_LED_C: [None, None, "Gateway LED C Mode {}", [gw_vars.OTGW]],
    gw_vars.OTGW_LED_D: [None, None, "Gateway LED D Mode {}", [gw_vars.OTGW]],
    gw_vars.OTGW_LED_E: [None, None, "Gateway LED E Mode {}", [gw_vars.OTGW]],
    gw_vars.OTGW_LED_F: [None, None, "Gateway LED F Mode {}", [gw_vars.OTGW]],
    gw_vars.OTGW_GPIO_A: [None, None, "Gateway GPIO A Mode {}", [gw_vars.OTGW]],
    gw_vars.OTGW_GPIO_B: [None, None, "Gateway GPIO B Mode {}", [gw_vars.OTGW]],
    gw_vars.OTGW_SB_TEMP: [
        SensorDeviceClass.TEMPERATURE,
        TEMP_CELSIUS,
        "Gateway Setback Temperature {}",
        [gw_vars.OTGW],
    ],
    gw_vars.OTGW_SETP_OVRD_MODE: [
        None,
        None,
        "Gateway Room Setpoint Override Mode {}",
        [gw_vars.OTGW],
    ],
    gw_vars.OTGW_SMART_PWR: [None, None, "Gateway Smart Power Mode {}", [gw_vars.OTGW]],
    gw_vars.OTGW_THRM_DETECT: [
        None,
        None,
        "Gateway Thermostat Detection {}",
        [gw_vars.OTGW],
    ],
    gw_vars.OTGW_VREF: [
        None,
        None,
        "Gateway Reference Voltage Setting {}",
        [gw_vars.OTGW],
    ],
}

DEPRECATED_BINARY_SENSOR_SOURCE_LOOKUP = {
    gw_vars.DATA_MASTER_CH_ENABLED: gw_vars.THERMOSTAT,
    gw_vars.DATA_MASTER_DHW_ENABLED: gw_vars.THERMOSTAT,
    gw_vars.DATA_MASTER_OTC_ENABLED: gw_vars.THERMOSTAT,
    gw_vars.DATA_MASTER_CH2_ENABLED: gw_vars.THERMOSTAT,
    gw_vars.DATA_SLAVE_FAULT_IND: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_CH_ACTIVE: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_DHW_ACTIVE: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_FLAME_ON: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_COOLING_ACTIVE: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_CH2_ACTIVE: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_DIAG_IND: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_DHW_PRESENT: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_CONTROL_TYPE: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_COOLING_SUPPORTED: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_DHW_CONFIG: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_MASTER_LOW_OFF_PUMP: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_CH2_PRESENT: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_SERVICE_REQ: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_REMOTE_RESET: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_LOW_WATER_PRESS: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_GAS_FAULT: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_AIR_PRESS_FAULT: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_WATER_OVERTEMP: gw_vars.BOILER,
    gw_vars.DATA_REMOTE_TRANSFER_DHW: gw_vars.BOILER,
    gw_vars.DATA_REMOTE_TRANSFER_MAX_CH: gw_vars.BOILER,
    gw_vars.DATA_REMOTE_RW_DHW: gw_vars.BOILER,
    gw_vars.DATA_REMOTE_RW_MAX_CH: gw_vars.BOILER,
    gw_vars.DATA_ROVRD_MAN_PRIO: gw_vars.THERMOSTAT,
    gw_vars.DATA_ROVRD_AUTO_PRIO: gw_vars.THERMOSTAT,
    gw_vars.OTGW_GPIO_A_STATE: gw_vars.OTGW,
    gw_vars.OTGW_GPIO_B_STATE: gw_vars.OTGW,
    gw_vars.OTGW_IGNORE_TRANSITIONS: gw_vars.OTGW,
    gw_vars.OTGW_OVRD_HB: gw_vars.OTGW,
}

DEPRECATED_SENSOR_SOURCE_LOOKUP = {
    gw_vars.DATA_CONTROL_SETPOINT: gw_vars.BOILER,
    gw_vars.DATA_MASTER_MEMBERID: gw_vars.THERMOSTAT,
    gw_vars.DATA_SLAVE_MEMBERID: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_OEM_FAULT: gw_vars.BOILER,
    gw_vars.DATA_COOLING_CONTROL: gw_vars.BOILER,
    gw_vars.DATA_CONTROL_SETPOINT_2: gw_vars.BOILER,
    gw_vars.DATA_ROOM_SETPOINT_OVRD: gw_vars.THERMOSTAT,
    gw_vars.DATA_SLAVE_MAX_RELATIVE_MOD: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_MAX_CAPACITY: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_MIN_MOD_LEVEL: gw_vars.BOILER,
    gw_vars.DATA_ROOM_SETPOINT: gw_vars.THERMOSTAT,
    gw_vars.DATA_REL_MOD_LEVEL: gw_vars.BOILER,
    gw_vars.DATA_CH_WATER_PRESS: gw_vars.BOILER,
    gw_vars.DATA_DHW_FLOW_RATE: gw_vars.BOILER,
    gw_vars.DATA_ROOM_SETPOINT_2: gw_vars.THERMOSTAT,
    gw_vars.DATA_ROOM_TEMP: gw_vars.THERMOSTAT,
    gw_vars.DATA_CH_WATER_TEMP: gw_vars.BOILER,
    gw_vars.DATA_DHW_TEMP: gw_vars.BOILER,
    gw_vars.DATA_OUTSIDE_TEMP: gw_vars.THERMOSTAT,
    gw_vars.DATA_RETURN_WATER_TEMP: gw_vars.BOILER,
    gw_vars.DATA_SOLAR_STORAGE_TEMP: gw_vars.BOILER,
    gw_vars.DATA_SOLAR_COLL_TEMP: gw_vars.BOILER,
    gw_vars.DATA_CH_WATER_TEMP_2: gw_vars.BOILER,
    gw_vars.DATA_DHW_TEMP_2: gw_vars.BOILER,
    gw_vars.DATA_EXHAUST_TEMP: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_DHW_MAX_SETP: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_DHW_MIN_SETP: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_CH_MAX_SETP: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_CH_MIN_SETP: gw_vars.BOILER,
    gw_vars.DATA_DHW_SETPOINT: gw_vars.BOILER,
    gw_vars.DATA_MAX_CH_SETPOINT: gw_vars.BOILER,
    gw_vars.DATA_OEM_DIAG: gw_vars.BOILER,
    gw_vars.DATA_TOTAL_BURNER_STARTS: gw_vars.BOILER,
    gw_vars.DATA_CH_PUMP_STARTS: gw_vars.BOILER,
    gw_vars.DATA_DHW_PUMP_STARTS: gw_vars.BOILER,
    gw_vars.DATA_DHW_BURNER_STARTS: gw_vars.BOILER,
    gw_vars.DATA_TOTAL_BURNER_HOURS: gw_vars.BOILER,
    gw_vars.DATA_CH_PUMP_HOURS: gw_vars.BOILER,
    gw_vars.DATA_DHW_PUMP_HOURS: gw_vars.BOILER,
    gw_vars.DATA_DHW_BURNER_HOURS: gw_vars.BOILER,
    gw_vars.DATA_MASTER_OT_VERSION: gw_vars.THERMOSTAT,
    gw_vars.DATA_SLAVE_OT_VERSION: gw_vars.BOILER,
    gw_vars.DATA_MASTER_PRODUCT_TYPE: gw_vars.THERMOSTAT,
    gw_vars.DATA_MASTER_PRODUCT_VERSION: gw_vars.THERMOSTAT,
    gw_vars.DATA_SLAVE_PRODUCT_TYPE: gw_vars.BOILER,
    gw_vars.DATA_SLAVE_PRODUCT_VERSION: gw_vars.BOILER,
    gw_vars.OTGW_MODE: gw_vars.OTGW,
    gw_vars.OTGW_DHW_OVRD: gw_vars.OTGW,
    gw_vars.OTGW_ABOUT: gw_vars.OTGW,
    gw_vars.OTGW_BUILD: gw_vars.OTGW,
    gw_vars.OTGW_CLOCKMHZ: gw_vars.OTGW,
    gw_vars.OTGW_LED_A: gw_vars.OTGW,
    gw_vars.OTGW_LED_B: gw_vars.OTGW,
    gw_vars.OTGW_LED_C: gw_vars.OTGW,
    gw_vars.OTGW_LED_D: gw_vars.OTGW,
    gw_vars.OTGW_LED_E: gw_vars.OTGW,
    gw_vars.OTGW_LED_F: gw_vars.OTGW,
    gw_vars.OTGW_GPIO_A: gw_vars.OTGW,
    gw_vars.OTGW_GPIO_B: gw_vars.OTGW,
    gw_vars.OTGW_SB_TEMP: gw_vars.OTGW,
    gw_vars.OTGW_SETP_OVRD_MODE: gw_vars.OTGW,
    gw_vars.OTGW_SMART_PWR: gw_vars.OTGW,
    gw_vars.OTGW_THRM_DETECT: gw_vars.OTGW,
    gw_vars.OTGW_VREF: gw_vars.OTGW,
}
