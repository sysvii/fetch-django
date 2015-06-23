import json

from django.db import models
from json_field import JSONField

from app.validators import json_schema_validator

class BaseProvider(models.Model):
    """
    The Base logic of a provider
    Requires a client side implementation
    No web interface to create or edit, this is admin only
    """
    name = models.CharField(max_length=160,
                            verbose_name="Base Provider's name")

    available_options = JSONField(default=json.dumps({"properties": {"id": {"type": "integer", "required": False, "title": "id"}}}),
                                  help_text="A JSON Schema of options that"
                                  " the base provider allows",
                                  validators=[json_schema_validator])

    def available_options_json(self):
        return json.dumps(self.available_options)

    def __str__(self):
        return self.name


class Provider(models.Model):
    """
    The Provider specific information to be able to fetch any series
    from the provider
    Does not needed client side implementation
    """
    base_provider = models.ForeignKey(BaseProvider)
    name = models.CharField(max_length=160,
                            verbose_name="Name of the provider")
    website = models.URLField(help_text="url to the provider's website",
                              verbose_name="Provider's website")

    regex_find_count = models.CharField(max_length=256,
                                        default="\d+",
                                        help_text="Regular expression used "
                                        "client side "
                                        "to extract the episode/chapter count "
                                        "from a file name")
    options = JSONField(help_text="JSON Object filled of BaseProvider's"
                                  " available_options with data")

    def __str__(self):
        return "{} ({})".format(self.name, self.base_provider.name)

    def base_provider_options_json(self):
        return json.dumps(self.options)
