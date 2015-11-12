from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"items": [
				{
					"type": "doctype",
					"name": "Student Applicant"
				},
				{
					"type": "doctype",
					"name": "Student"
				},
				{
					"type": "doctype",
					"name": "Fees"
				},
				{
					"type": "doctype",
					"name": "Student Group"
				},
				{
					"type": "doctype",
					"name": "Course Schedule"
				},
				{
					"type": "doctype",
					"name": "Student Attendance"
				}
			]
		},
		{
			"label": _("Tools"),
			"items": [
				{
					"type": "doctype",
					"name": "Scheduling Tool"
				},
				{
					"type": "doctype",
					"name": "Student Attendance Tool"
				}
			]
		},
		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Academic Term"
				},
				{
					"type": "doctype",
					"name": "Academic Year"
				},
				{
					"type": "doctype",
					"name": "Course"
				},
				{
					"type": "doctype",
					"name": "Program"
				},
				{
					"type": "doctype",
					"name": "Instructor"
				},
				{
					"type": "doctype",
					"name": "Room"
				},
				{
					"type": "doctype",
					"name": "Fee Category"
				},
				{
					"type": "doctype",
					"name": "Fee Structure"
				}

			]
		},
	]
	