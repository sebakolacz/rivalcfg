from .. import usbhid


profile = {

    "name": "SteelSeries Rival 500",

    "models": [{
        "name": "SteelSeries Rival 500",
        "vendor_id": 0x1038,
        "product_id": 0x170e,
        "endpoint": 0,
    }],

    "settings": {

        "sensitivity1": {
            "label": "Sensibility preset 1",
            "description": "Set sensitivity preset 1 (DPI)",
            "cli": ["-s", "--sensitivity1"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x03, 0x00, 0x01],
            "command_suffix": [0x00, 0x42],
            "value_type": "range",
            "input_range": [100, 12000, 100],
            "output_range": [0x00, 0x77, 1],
            "default": 800,
        },

        "sensitivity2": {
            "label": "Sensibility preset 2",
            "description": "Set sensitivity preset 2 (DPI)",
            "cli": ["-S", "--sensitivity2"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x03, 0x00, 0x02],
            "command_suffix": [0x00, 0x42],
            "value_type": "range",
            "input_range": [100, 12000, 100],
            "output_range": [0x00, 0x77, 1],
            "default": 1600,
        },

        "polling_rate": {
            "label": "Polling rate",
            "description": "Set polling rate (Hz)",
            "cli": ["-p", "--polling-rate"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x04, 0x00],
            "value_type": "choice",
            "choices": {
                125: 0x04,
                250: 0x03,
                500: 0x02,
                1000: 0x01,
            },
            "default": 1000,
        },

        "buttons_mapping": {
            "label": "Buttons mapping",
            "description": "Set the mapping of the buttons",
            "cli": ["-b", "--buttons"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x31, 0x00],
            "value_type": "buttons",

            "buttons": {
                "Button1":   {"id": 0x01, "offset": 0x00, "default": "button1"},    # noqa
                "Button2":   {"id": 0x02, "offset": 0x05, "default": "button2"},    # noqa
                "Button3":   {"id": 0x03, "offset": 0x0A, "default": "button3"},    # noqa
                "Button4":   {"id": 0x04, "offset": 0x0F, "default": "button4"},    # noqa
                "Button5":   {"id": 0x05, "offset": 0x14, "default": "button5"},    # noqa
                "Button6":   {"id": 0x06, "offset": 0x19, "default": "button6"},    # noqa
                "Button7":   {"id": 0x07, "offset": 0x1e, "default": "button7"},    # noqa
                "Button8":   {"id": 0x08, "offset": 0x46, "default": "button8"},    # noqa
                "Button9":   {"id": None, "offset": 0x23, "default": "disabled"},   # noqa
                "Button10":  {"id": None, "offset": 0x28, "default": "dpi"},        # noqa
                "Button11":  {"id": None, "offset": 0x2d, "default": "disabled"},   # noqa
                "Button12":  {"id": None, "offset": 0x32, "default": "disabled"},   # noqa
                "Button13":  {"id": None, "offset": 0x41, "default": "disabled"},   # noqa
                "TiltLeft":  {"id": 0x33, "offset": 0x37, "default": "tiltleft"},   # noqa
                "TiltRight": {"id": 0x34, "offset": 0x3c, "default": "tiltright"},  # noqa
            },

            "button_field_length": 5,

            "button_disable":     0x00,
            "button_keyboard":    0x51,
            "button_multimedia":  0x61,
            "button_dpi_switch":  0x30,
            "button_scroll_up":   0x31,
            "button_scroll_down": 0x32,

            "default": "default",
        },

    },

    "save_command": {
        "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
        "command": [0x09, 0x00],
    },

}