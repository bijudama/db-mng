import sqlalchemy as sa
from schema import templates, versions



class AppQueries:
    _versionsAlias = {k: f"version_{k}" for k in versions.columns.keys()}

    def buildTemplatesQuery():
        return templates.select()

    def buildTemplateByNameQuery(name):
        # versionsAlias = versions.alias(**AppQueries._versionsAlias)
        query = sa.select([templates, versions]).where(sa.and_(
            templates.c.name == versions.c.templateName,
            templates.c.name == name,
            versions.c.number == templates.c.activeVersion
        ))
        return query

    def buildTemplateVersionsQuery(templateName):
        q = sa.select([versions]).where(
            versions.c.templateName == templateName
        )
        return q

    def buildVersionQuery(templateName, versionNumber):
        return versions.select().where(sa.and_(
            versions.c.number == versionNumber,
            versions.c.templateName == templateName
        ))