#!/usr/bin/python3
"""
Creates personalized invitation files using a template
and a list of attendees (dictionaries).
Handles errors gracefully as required.
"""

import os


def generate_invitations(template, attendees):
    """
    Generates invitation files using a template and a list of dictionaries.

    Args:
        template (str): Template string with placeholders.
        attendees (list): List of dictionaries containing attendee data.

    Behavior:
        - Validates input types
        - Handles empty template
        - Handles empty attendee list
        - Replaces missing fields with "N/A"
        - Creates files output_X.txt (1-indexed)
    """

    # ----------- Type Validation -----------
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # ----------- Empty Template Check -----------
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # ----------- Empty Attendee List Check -----------
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # ----------- Process & Generate Files -----------
    for index, attendee in enumerate(attendees, start=1):

        # Safely fetch data, replace missing or None with "N/A"
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # Replace placeholders
        filled_template = template.replace("{name}", name)
        filled_template = filled_template.replace("{event_title}", event_title)
        filled_template = filled_template.replace("{event_date}", event_date)
        filled_template = filled_template.replace("{event_location}", event_location)

        # Create output filename
        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as output_file:
                output_file.write(filled_template)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            continue  # move to next file

