import re
import sys
from datetime import datetime
import os
import json

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.project_slug}}"

if not re.match(MODULE_REGEX, module_name):
    print(
        "ERROR: The project slug (%s) is not a valid Python module name. "
        "Please do not use a - and use _ instead" % module_name
    )
    # Exit to cancel project
    sys.exit(1)



def set_friendly_date():
    today = datetime.today()
    friendly_date = today.strftime("%B %-d, %Y")  # e.g., "February 2, 2025"

    context_file = "cookiecutter.json"
    with open(context_file, "r") as f:
        context = json.load(f)

    context["__friendly_date"] = friendly_date

    with open(context_file, "w") as f:
        json.dump(context, f, indent=4)

set_friendly_date()