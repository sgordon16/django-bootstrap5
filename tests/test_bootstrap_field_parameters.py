from django import forms

from tests.base import BootstrapTestCase


class CharFieldTestForm(forms.Form):
    test = forms.CharField()


class BootstrapFieldParameterTestCase(BootstrapTestCase):
    """Test `bootstrap_field` parameters`."""

    def test_wrapper_class(self):
        """Test field with default CharField widget."""
        form = CharFieldTestForm()

        self.assertHTMLEqual(
            self.render("{% bootstrap_field form.test %}", context={"form": form}),
            (
                '<div class="django_bootstrap5-req mb-3">'
                '<label for="id_test" class="form-label">Test</label>'
                '<input class="form-control" id="id_test" name="test" placeholder="Test" required type="text">'
                "</div>"
            ),
        )

        self.assertHTMLEqual(
            self.render("{% bootstrap_field form.test inline_wrapper_class='foo' %}", context={"form": form}),
            (
                '<div class="django_bootstrap5-req mb-3">'
                '<label for="id_test" class="form-label">Test</label>'
                '<input class="form-control" id="id_test" name="test" placeholder="Test" required type="text">'
                "</div>"
            ),
        )

        self.assertHTMLEqual(
            self.render("{% bootstrap_field form.test wrapper_class='foo' %}", context={"form": form}),
            (
                '<div class="django_bootstrap5-req foo">'
                '<label for="id_test" class="form-label">Test</label>'
                '<input class="form-control" id="id_test" name="test" placeholder="Test" required type="text">'
                "</div>"
            ),
        )

        self.assertHTMLEqual(
            self.render("{% bootstrap_field form.test wrapper_class=None %}", context={"form": form}),
            (
                '<div class="django_bootstrap5-req">'
                '<label for="id_test" class="form-label">Test</label>'
                '<input class="form-control" id="id_test" name="test" placeholder="Test" required type="text">'
                "</div>"
            ),
        )

    def test_inline_wrapper_class(self):
        """Test field with default CharField widget."""
        form = CharFieldTestForm()

        self.assertHTMLEqual(
            self.render("{% bootstrap_field form.test layout='inline' %}", context={"form": form}),
            (
                '<div class="col-12 django_bootstrap5-req">'
                '<label class="visually-hidden" for="id_test">Test</label>'
                '<input type="text" name="test" class="form-control" placeholder="Test" required id="id_test">'
                "</div>"
            ),
        )

        self.assertHTMLEqual(
            self.render("{% bootstrap_field form.test layout='inline' wrapper_class='foo' %}", context={"form": form}),
            (
                '<div class="col-12 django_bootstrap5-req">'
                '<label class="visually-hidden" for="id_test">Test</label>'
                '<input type="text" name="test" class="form-control" placeholder="Test" required id="id_test">'
                "</div>"
            ),
        )

        self.assertHTMLEqual(
            self.render(
                "{% bootstrap_field form.test layout='inline' inline_wrapper_class='foo' %}", context={"form": form}
            ),
            (
                '<div class="col-12 django_bootstrap5-req foo">'
                '<label class="visually-hidden" for="id_test">Test</label>'
                '<input type="text" name="test" class="form-control" placeholder="Test" required id="id_test">'
                "</div>"
            ),
        )

    def test_extra_widget_attrs(self):
        """Test that extra kwargs are passed as widget attributes."""
        form = CharFieldTestForm()

        self.assertHTMLEqual(
            self.render('{% bootstrap_field form.test autocomplete="off" %}', context={"form": form}),
            (
                '<div class="django_bootstrap5-req mb-3">'
                '<label for="id_test" class="form-label">Test</label>'
                '<input class="form-control" id="id_test" name="test" placeholder="Test" '
                'required type="text" autocomplete="off">'
                "</div>"
            ),
        )

    def test_extra_widget_attrs_underscore_conversion(self):
        """Test that underscores are converted to hyphens in attr names."""
        form = CharFieldTestForm()

        html = self.render('{% bootstrap_field form.test data_my_value="test" %}', context={"form": form})
        self.assertIn('data-my-value="test"', html)

    def test_extra_widget_attrs_override(self):
        """Test that extra attrs override widget's existing attrs."""

        class FormWithAttrs(forms.Form):
            test = forms.CharField(widget=forms.TextInput(attrs={"title": "original"}))

        form = FormWithAttrs()
        html = self.render('{% bootstrap_field form.test title="overridden" %}', context={"form": form})
        self.assertIn('title="overridden"', html)
        self.assertNotIn('title="original"', html)

    def test_extra_widget_attrs_multiple(self):
        """Test multiple extra attributes."""
        form = CharFieldTestForm()
        html = self.render(
            '{% bootstrap_field form.test data_foo="bar" aria_label="Search" autocomplete="off" %}',
            context={"form": form},
        )
        self.assertIn('data-foo="bar"', html)
        self.assertIn('aria-label="Search"', html)
        self.assertIn('autocomplete="off"', html)

    def test_extra_widget_attrs_with_hyphens(self):
        """Test that hyphenated attribute names work directly."""
        form = CharFieldTestForm()
        html = self.render('{% bootstrap_field form.test data-foo="bar" %}', context={"form": form})
        self.assertIn('data-foo="bar"', html)

    def test_extra_widget_attrs_aria_with_hyphens(self):
        """Test aria attributes with hyphens."""
        form = CharFieldTestForm()
        html = self.render('{% bootstrap_field form.test aria-label="Search field" %}', context={"form": form})
        self.assertIn('aria-label="Search field"', html)

    def test_extra_widget_attrs_vue_at_sign(self):
        """Test Vue.js @ directive syntax."""
        form = CharFieldTestForm()
        html = self.render('{% bootstrap_field form.test @click="handleClick" %}', context={"form": form})
        self.assertIn('@click="handleClick"', html)

    def test_extra_widget_attrs_vue_v_bind(self):
        """Test Vue.js v-bind: syntax."""
        form = CharFieldTestForm()
        html = self.render('{% bootstrap_field form.test v-bind:class="{active:isActive}" %}', context={"form": form})
        self.assertIn('v-bind:class="{active:isActive}"', html)

    def test_extra_widget_attrs_mixed_hyphen_and_underscore(self):
        """Test mixing hyphenated and underscore attributes."""
        form = CharFieldTestForm()
        html = self.render(
            '{% bootstrap_field form.test data-foo="bar" data_baz="qux" %}',
            context={"form": form},
        )
        self.assertIn('data-foo="bar"', html)
        self.assertIn('data-baz="qux"', html)  # underscore converted to hyphen

    def test_extra_widget_attrs_with_template_variable(self):
        """Test that template variables work as attribute values."""
        form = CharFieldTestForm()
        html = self.render(
            "{% bootstrap_field form.test data-value=my_var %}",
            context={"form": form, "my_var": "dynamic_value"},
        )
        self.assertIn('data-value="dynamic_value"', html)

    def test_extra_widget_attrs_boolean_disabled(self):
        """Test boolean attribute disabled (no value)."""
        form = CharFieldTestForm()
        html = self.render("{% bootstrap_field form.test disabled %}", context={"form": form})
        self.assertIn("disabled", html)

    def test_extra_widget_attrs_boolean_readonly(self):
        """Test boolean attribute readonly (no value)."""
        form = CharFieldTestForm()
        html = self.render("{% bootstrap_field form.test readonly %}", context={"form": form})
        self.assertIn("readonly", html)

    def test_extra_widget_attrs_alpine_x_data(self):
        """Test Alpine.js x-data attribute."""
        form = CharFieldTestForm()
        html = self.render('{% bootstrap_field form.test x-data="{ open: false }" %}', context={"form": form})
        self.assertIn('x-data="{ open: false }"', html)

    def test_extra_widget_attrs_alpine_x_bind(self):
        """Test Alpine.js x-bind attribute."""
        form = CharFieldTestForm()
        html = self.render(
            '{% bootstrap_field form.test x-bind:class="{ active: isActive }" %}', context={"form": form}
        )
        self.assertIn('x-bind:class="{ active: isActive }"', html)

    def test_extra_widget_attrs_alpine_x_on(self):
        """Test Alpine.js x-on:click attribute."""
        form = CharFieldTestForm()
        html = self.render('{% bootstrap_field form.test x-on:click="open = true" %}', context={"form": form})
        self.assertIn('x-on:click="open = true"', html)

    def test_extra_widget_attrs_htmx_get(self):
        """Test htmx hx-get attribute."""
        form = CharFieldTestForm()
        html = self.render('{% bootstrap_field form.test hx-get="/search" %}', context={"form": form})
        self.assertIn('hx-get="/search"', html)

    def test_extra_widget_attrs_htmx_post(self):
        """Test htmx hx-post attribute."""
        form = CharFieldTestForm()
        html = self.render('{% bootstrap_field form.test hx-post="/submit" %}', context={"form": form})
        self.assertIn('hx-post="/submit"', html)

    def test_extra_widget_attrs_htmx_trigger(self):
        """Test htmx hx-trigger attribute."""
        form = CharFieldTestForm()
        html = self.render(
            '{% bootstrap_field form.test hx-trigger="keyup changed delay:500ms" %}', context={"form": form}
        )
        self.assertIn('hx-trigger="keyup changed delay:500ms"', html)

    def test_extra_widget_attrs_htmx_target(self):
        """Test htmx hx-target attribute."""
        form = CharFieldTestForm()
        html = self.render('{% bootstrap_field form.test hx-target="#results" %}', context={"form": form})
        self.assertIn('hx-target="#results"', html)

    def test_extra_widget_attrs_htmx_swap(self):
        """Test htmx hx-swap attribute."""
        form = CharFieldTestForm()
        html = self.render('{% bootstrap_field form.test hx-swap="outerHTML" %}', context={"form": form})
        self.assertIn('hx-swap="outerHTML"', html)
