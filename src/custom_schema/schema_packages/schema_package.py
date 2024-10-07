"""from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    ) """

from nomad.config import config
from nomad.datamodel.data import Schema
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import (
Author,
Datetime,
Quantity,
SchemaPackage,
)

configuration = config.get_plugin_entry_point(
    'custom_schema.schema_packages:schema_package_entry_point'
)

m_package = SchemaPackage()


class NewSchemaPackage(Schema):
    name = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    author = Quantity(
        type=Author, a_eln=ELNAnnotation(component=ELNComponentEnum.AuthorEditQuantity)
    ) # TODO: default current user
    date_time = Quantity(
        type=Datetime,
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateTimeEditQuantity)
    )
    rich_text = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity)
    )
    sample_id = Quantity(type=str)

    def normalize(self, archive, logger):
        super(Schema, self).normalize(archive, logger)

        if self.sample_id is None:
            self.sample_id = f'{self.added_date}--{self.formula}'


m_package.__init_metainfo__()
