from sanic.response import json
from schema import templates as templatesTable, versions as versionsTable
from sanic.response import dumps as defaultJsonDumps

from serialization import serializeTemplate, serializeTemplates, serializeVersion, serializeVersions
from queries import AppQueries

def setup(app):
    @app.route("/templates")
    async def getTemplates(request):
        templatesRows = await request.app.db.fetch_all(AppQueries.buildTemplatesQuery())
        return json({
            'templates': serializeTemplates(templatesRows)
        })

    @app.route("/templates/<templateName>")
    async def getTemplate(request, templateName):
        query = AppQueries.buildTemplateByNameQuery(templateName)
        templateRow = await request.app.db.fetch_one(query)
        # templateRow = templateRow[0] if len(templateRow) > 0 else None
        return json({
            'template': serializeTemplate(templateRow)
        })

    @app.route("/templates/<templateName>/versions")
    async def getVersions(request, templateName):
        rows = await request.app.db.fetch_all(AppQueries.buildTemplateVersionsQuery(templateName))
        return json({
            'versions': serializeVersions(rows)
        })

    @app.route("/templates/<templateName>/versions/<versionNumber>")
    async def getVersion(request, templateName, versionNumber):
        row = await request.app.db.fetch_one(AppQueries.buildVersionQuery(templateName, int(versionNumber)))
        return json({
            'version': serializeVersion(row)
        })
