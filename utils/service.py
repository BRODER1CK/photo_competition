from django import forms
from django.db.models.functions import Lower


def order_service_object_decorator(
    *fields, default_field=None, default_sort="asc", **kwargs
):
    """
    Django forms decorator class to use to add sorting fields and ordered method in service object class
    :param default_sort: Default sorting order. If not passed then ASC will be taken as default for
        direction and pk as sorting field
    :param default_field: Default sorting field. If not passed then first field will be taken as default
    :param fields: String or Array of strings contained fields acceptable for the ordering
    """

    sort_directions = (("asc", ""), ("desc", "-"))

    sort_fields = tuple((field, field) for field in fields)

    django_orm_string_datatype_fields = [
        "CharField",
        "EmailField",
        "SlugField",
        "TextField",
    ]

    def ordered(self, queryset):
        if not (
            bool(self.cleaned_data.get("sort_direction"))
            or bool(self.cleaned_data.get("sort_field"))
        ):
            return queryset.order_by("pk")
        direction = dict(sort_directions).get(
            self.cleaned_data.get("sort_direction"),
            dict(sort_directions).get(default_sort),
        )
        field = dict(sort_fields).get(
            self.cleaned_data.get("sort_field"), default_field or fields[0]
        )
        if (
            queryset.model._meta.get_field(field).get_internal_type()
            in django_orm_string_datatype_fields
        ):
            order_attribute = Lower(field) if direction == "" else Lower(field).desc()
        else:
            order_attribute = f"{direction}{field}"
        return queryset.order_by(order_attribute)

    def inner(cls):
        cls.sort_fields_list = fields
        cls.base_fields["sort_field"] = forms.ChoiceField(
            choices=sort_fields, required=False
        )
        cls.base_fields["sort_direction"] = forms.ChoiceField(
            choices=sort_directions, required=False
        )

        cls.ordered = ordered
        return cls

    return inner
