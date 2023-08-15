from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Field, Layout, Submit
from django.forms import ModelForm

from . import models


class ArticleForm(ModelForm):
    class Meta:
        model = models.Article
        fields = [
            "name",
            "number",
            "description",
            "theme_main",
            "theme_sub",
            "prod_type",
        ]

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(HTML("<h2>Submit your session!</h2>"))

        for field in self.Meta().fields:
            helper.layout.append(Field(field))

        helper.layout.append(
            Submit("submit", "Submit your session", css_class="btn-success")
        )

        helper.field_class = "col-9"
        helper.label_class = "col-3"

        return helper
