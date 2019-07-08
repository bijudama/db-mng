import sqlalchemy as sa
from schema import templates, versions




alltemplates = sa.select([templates.columns.name, versions.columns.templateName]).join

