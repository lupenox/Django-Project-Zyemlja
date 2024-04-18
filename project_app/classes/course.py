from project_app.models import Course


class CourseClass:

    def __init__(self, name, instructors, ta, sections):
        self.name = name
        self.instructors = instructors
        self.ta = ta
        self.sections = sections

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_instructors(self, instructors):
        self.instructors = instructors

    def get_instructors(self):
        return self.instructors

    """
    TODO
        AddTA()
        removeTA()
        addSection()
        removeSection()
        getTAs()
        getSections()
    """