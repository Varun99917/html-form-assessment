
import unittest
from html.parser import HTMLParser
from pathlib import Path


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.inputs = []
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))

        if tag == "input":
            self.inputs.append(attrs)

        if tag == "button":
            self.buttons.append(attrs)


class TestHTMLForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        html_file = Path(__file__).parent / "index.html"
        cls.html = html_file.read_text(encoding="utf-8")
        cls.parser = FormParser()
        cls.parser.feed(cls.html)

    def test_form_exists(self):
        forms = [
            attrs for tag, attrs in self.parser.tags
            if tag == "form"
        ]
        self.assertTrue(forms, "Form element is missing")

    def test_name_field_exists(self):
        self.assertTrue(any(
            field.get("name") == "name"
            and field.get("type") == "text"
            for field in self.parser.inputs
        ), "Name field is missing")

    def test_email_field_exists(self):
        self.assertTrue(any(
            field.get("name") == "email"
            and field.get("type") == "email"
            for field in self.parser.inputs
        ), "Email field is missing")

    def test_contact_field_exists(self):
        self.assertTrue(any(
            field.get("name") == "contact"
            and field.get("type") == "tel"
            for field in self.parser.inputs
        ), "Contact field is missing")

    def test_submit_button_exists(self):
        self.assertTrue(
            any(button.get("type") == "submit"
                for button in self.parser.buttons)
            or any(
                field.get("type") == "submit"
                for field in self.parser.inputs
            ),
            "Submit button is missing"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
